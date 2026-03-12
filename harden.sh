#!/usr/bin/env bash
set -euo pipefail

log() { echo "[*] $*"; }

secure_vault() {
  local vault="$HOME/Vault"

  log "Securing local Vault at: $vault"
  mkdir -p "$vault"

  # Vault directory: only you can access
  chmod 700 "$vault" || true
  chown "$USER":"$USER" "$vault" 2>/dev/null || true

  # Tighten contents: directories 700, files 600
  if command -v find >/dev/null 2>&1; then
    find "$vault" -type d -exec chmod 700 {} + 2>/dev/null || true
    find "$vault" -type f -exec chmod 600 {} + 2>/dev/null || true
  fi

  log "Vault permissions now:"
  ls -ld "$vault"
}

secure_identity_files() {
  log "Audit (before):"
  ls -l /etc/shadow || true

  log "Remediating /etc/shadow -> chmod 640, chown root:shadow"
  sudo chmod 640 /etc/shadow
  sudo chown root:shadow /etc/shadow

  # Optional: gshadow is also an identity file on many Linux systems
  if [[ -f /etc/gshadow ]]; then
    log "Remediating /etc/gshadow -> chmod 640, chown root:shadow"
    sudo chmod 640 /etc/gshadow
    sudo chown root:shadow /etc/gshadow
  fi

  log "Audit (after):"
  ls -l /etc/shadow
  [[ -f /etc/gshadow ]] && ls -l /etc/gshadow
}

main() {
  secure_vault
  secure_identity_files
  log "Done."
}

main "$@"
