# 🛡️ Homelab Maintenance & Administration Guide

This guide details authentication management, container maintenance, and backup strategies for your homelab.

---

## 1. Frictionless Authentication Architecture

To avoid typing passwords constantly while on your home network, services are configured with zero-friction local access:

### qBittorrent (`http://localhost:8080`)
* **Subnet Whitelist Enabled:**
  In `D:\BucketMedia\Homelab\qbittorrent\config\qBittorrent\qBittorrent.conf`:
  ```ini
  WebUI\AuthSubnetWhitelistEnabled=true
  WebUI\AuthSubnetWhitelist=127.0.0.1/32, 192.168.0.0/16, 10.0.0.0/8, 172.16.0.0/12
  WebUI\BanDuration=0
  ```
  *Local devices connect directly without any login prompt.*

### Navidrome (`http://localhost:4533`)
* **1-Year Session Timeout:**
  In `D:\BucketMedia\Homelab\docker-compose.yml`:
  ```yaml
  environment:
    ND_SESSIONTIMEOUT: 8760h
  ```
  *Once logged in, credentials remain valid for an entire year.*

### Password Management: Browser Manager vs. Vaultwarden
* **Why Vaultwarden was removed:** Modern Bitwarden extensions require strict HTTPS/SSL certificates to connect to self-hosted instances. Without setting up reverse proxies and domain certificates, the extension blocked local `http://` logins.
* **The Simpler Solution:** Let your native browser (Chrome, Edge, Safari, Firefox) save your credentials. It auto-fills seamlessly across all local ports without running a separate vault container.

---

## 2. Docker Health & Container Maintenance

### Monitoring Container Logs in Real Time:
* Visit **[Dozzle](http://localhost:8888)** to view live streaming logs of any container with one click.

### Clean Up Unused Docker Images & Space:
To reclaim disk space from old versions or dangling containers, run in PowerShell:
```powershell
docker image prune -a --filter "until=168h"
```

### Checking System Resources & Uptime:
* Visit **[Uptime Kuma](http://localhost:3001)** for service heartbeats.
* Visit **[Portainer](http://localhost:9000)** for graphical CPU and RAM usage per container.

---

## 3. Backup Best Practices

The core configuration state for your homelab lives in `D:\BucketMedia\Homelab`:

### What to Back Up:
* `D:\BucketMedia\Homelab\docker-compose.yml`
* `D:\BucketMedia\Homelab\immich\docker-compose.yml`
* `D:\BucketMedia\Homelab\paperless\docker-compose.yml`
* `D:\BucketMedia\Homelab\jellyfin\config\`
* `D:\BucketMedia\Homelab\navidrome\data\`

*(Media folders like `Movies/` and `Shows/` can always be re-downloaded via the automated scripts, so focus backups on configuration files and database folders).*
