# 🏰 The Ultimate Self-Hosted Homelab

> A comprehensive, automated self-hosted ecosystem for high-definition media streaming, retro gaming, lossless audio, book & manga reading, photo management, paperless archiving, and live sports.

---

## 🧭 System Architecture & Services

All services run seamlessly via **Docker** on your local machine / server under `D:\BucketMedia`.

| Service | Port / URL | Category | Description |
| :--- | :--- | :--- | :--- |
| **[Jellyfin](http://localhost:8096)** | `:8096` | 🎬 Media | 4K HDR Movies, Series, & Live TV streaming (Netflix/Plex alternative). Native apps on iOS (Swiftfin), Android TV, Roku, Apple TV. |
| **[Stremio Server](http://localhost:11470)** | `:11470` | 🍿 Streaming | Local streaming server backend for on-demand community torrents & catalogs. |
| **[Navidrome](http://localhost:4533)** | `:4533` | 🎵 Music | Personal lossless audio streaming server (Spotify alternative). Supports Substreamer, Feishin, and Amperfy. |
| **[Kavita](http://localhost:5000)** | `:5000` | 📚 Books & Manga | Web-based digital library for Manga (.cbz), Comics, and E-books (.epub, .pdf). |
| **[Audiobookshelf](http://localhost:13378)** | `:13378` | 🎧 Audiobooks | Audiobooks and podcasts streaming server with playback progress sync and mobile apps. |
| **[EmulatorJS](http://localhost:4000)** | `:4000` / `:4001` | 🕹️ Gaming | In-browser retro arcade (NES, SNES, GBA, N64, Genesis, PS1). Save states & gamepads supported. |
| **[Immich](http://localhost:2283)** | `:2283` | 📸 Photos | High-performance Google Photos alternative with AI facial recognition, object detection, and mobile auto-backup. |
| **[Paperless-ngx](http://localhost:8000)** | `:8000` | 📄 Documents | Document archiving system with automatic OCR, tagging, search, and automatic login enabled. |
| **[Kiwix](http://localhost:8085)** | `:8085` | 🧠 Knowledge | 100% offline Wikipedia, WikiMed, and reference encyclopedia library. |
| **[Homarr](http://localhost:7575)** | `:7575` | 🧭 Dashboard | Customizable master dashboard linking all homelab services into one homepage. |
| **[qBittorrent](http://localhost:8080)** | `:8080` | ⚡ Downloader | Headless BitTorrent client with integrated Nova search plugins, category auto-paths, and local subnet auto-login. |
| **[Portainer](http://localhost:9000)** | `:9000` | 🐳 Docker UI | Visual web management interface for containers, volumes, networks, and images. |
| **[Dozzle](http://localhost:8888)** | `:8888` | 📋 Monitoring | Lightweight, real-time log viewer for all running Docker containers. |
| **[Uptime Kuma](http://localhost:3001)** | `:3001` | 📈 Status | Self-hosted uptime monitoring service with alerts and latency graphs. |
| **[OpenSpeedTest](http://localhost:3000)** | `:3000` | 🚀 Network | Pure HTML5 network speed test to measure local Wi-Fi and LAN throughput. |
| **[IT-Tools](http://localhost:8082)** | `:8082` | 🛠️ Utilities | Collection of handy developer, networking, token generation, and encryption tools. |

---

## 📂 Repository Contents & Documentation

* **[`guides/01-media-and-downloads.md`](guides/01-media-and-downloads.md)**: Easy methods to search, download, and automate movies, series, and 4K box sets using qBittorrent & Jellyfin.
* **[`guides/02-gaming-and-emulation.md`](guides/02-gaming-and-emulation.md)**: Retro ROMs for EmulatorJS & full Nintendo Switch emulation setup via Ryujinx (Keys, Firmware, Updates).
* **[`guides/03-books-manga-audiobooks.md`](guides/03-books-manga-audiobooks.md)**: How to acquire and organize Manga (.cbz), Books (.epub), and Audiobooks (.m4b) for Kavita and Audiobookshelf.
* **[`guides/04-music-and-streaming.md`](guides/04-music-and-streaming.md)**: Lossless FLAC/MP3 acquisition, folder structures, and connecting mobile Spotify-like apps.
* **[`guides/05-stremio-mastery.md`](guides/05-stremio-mastery.md)**: Addon management, reordering catalogs without reinstalling, and customizing Hulu, Paramount+, HBO, and Netflix rows.
* **[`guides/06-live-sports-and-tv.md`](guides/06-live-sports-and-tv.md)**: All working live sports links (VIPBox, Sportsurge, StreamEast), Stremio sports addons (PlavioLive), ISP DNS unblocking, and Jellyfin Live TV.
* **[`guides/07-homelab-maintenance.md`](guides/07-homelab-maintenance.md)**: Password-free local authentication, subnet whitelisting, daily startup scripts, and container hygiene.
* **[`TECH_WISHLIST.md`](TECH_WISHLIST.md)**: Curated personal hardware upgrades, streaming gear (Apple TV 4K), storage expansions, and Tesla accessories.

---

## ⚡ Quick Start: Running the Homelab

All containers are orchestrated through `D:\BucketMedia\Homelab`.

### Start All Services:
Double-click `D:\BucketMedia\Start_Homelab.bat` or run:
```powershell
cd D:\BucketMedia\Homelab
docker compose up -d
cd immich && docker compose up -d
cd ../paperless && docker compose up -d
```

### Stop All Services:
Double-click `D:\BucketMedia\Stop_Homelab.bat` or run:
```powershell
cd D:\BucketMedia\Homelab
docker compose down
cd immich && docker compose down
cd ../paperless && docker compose down
```

---

## 🛡️ Frictionless Authentication (Localhost / LAN)

Your homelab is configured so you don't have to keep typing passwords while on your home network:

* **qBittorrent (`:8080`)**: Local network whitelisted (`AuthSubnetWhitelistEnabled=true`). Automatically logs in without credentials. *(Fallback: `Dartdark` / `Dartdark123`)*.
* **Paperless-ngx (`:8000`)**: Set to `PAPERLESS_AUTO_LOGIN_USERNAME: admin`. Opens straight to documents.
* **Navidrome (`:4533`)**: Session timeout set to 1 year (`ND_SESSIONTIMEOUT=8760h`). Stays permanently signed in.
* **Jellyfin (`:8096`)**: Swiftfin & browser sessions persist indefinitely.
* **Dozzle, OpenSpeedTest, Kiwix**: Zero passwords required.
* **Browser Manager**: Let Chrome / Edge remember passwords once for new devices — no external password vault required.
