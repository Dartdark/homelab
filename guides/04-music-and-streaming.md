# 🎵 Lossless Music & Audio: Navidrome Guide

Navidrome is your self-hosted **Spotify alternative**. It indexes your music collection, supports bit-perfect lossless audio streaming (FLAC), and connects to modern mobile and desktop players.

---

## 1. Accessing Navidrome

* **Web Player:** `http://localhost:4533`
* **Session Lifetime:** Configured with `ND_SESSIONTIMEOUT=8760h` (1 year), so once logged in, your session never expires.

---

## 2. Directory Layout & Music Tagging

Store all music in `D:\BucketMedia\Music`:

```text
D:\BucketMedia\Music\
└── Michael Jackson\
    └── Thriller (1982)\
        ├── 01 - Wanna Be Startin' Somethin'.flac
        ├── 02 - Baby Be Mine.flac
        ├── 03 - The Girl Is Mine.flac
        ├── 04 - Thriller.flac
        └── cover.jpg
```

### Supported Formats:
* **Lossless:** `.flac`, `.alac`, `.wav`
* **Compressed:** `.mp3` (320kbps recommended), `.aac`, `.ogg`, `.opus`

### Auto-Scanning:
Navidrome automatically scans `D:\BucketMedia\Music` every 1 hour (`ND_SCANSCHEDULE=1h`). To force an instant scan:
1. Open `http://localhost:4533`.
2. Click your avatar in the top right ➔ **Activity ➔ Quick Scan**.

---

## 3. Best Spotify-like Client Apps

Navidrome implements the open **Subsonic API**, allowing you to use beautiful native clients on all your devices:

| Platform | Recommended App | Key Features |
| :--- | :--- | :--- |
| **Windows / Mac / Linux** | **[Feishin](https://github.com/jeffvli/feishin)** | Modern Spotify-like desktop interface, gapless playback, lyrics sync. |
| **iOS (iPhone / iPad)** | **[Substreamer](https://substreamerapp.com/)** or **Amperfy** | Offline caching, CarPlay support, clean UI. |
| **Android** | **[Symfonium](https://symfonium.app/)** or **Substreamer** | Material You design, Android Auto, offline downloads, equalizer. |

### How to Connect Any App:
* **Server URL:** `http://<your-local-ip>:4533` (or `http://localhost:4533` if on PC)
* **Username:** Your Navidrome username
* **Password:** Your Navidrome password

---

## 4. Acquiring High-Fidelity Music

* **[Nicotine+ (Soulseek)](https://nicotine-plus.org/)**: The premier P2P network for music enthusiasts, rare B-sides, vinyl rips, and pristine FLAC albums.
* **[Free-MP3-Download.net](https://free-mp3-download.net/)**: Direct web downloader for Qobuz/Deezer 16-bit / 24-bit FLAC and 320kbps MP3 tracks.
* **qBittorrent**: Searching `Artist Album FLAC` via the built-in PirateBay/1337x search plugins.
