# 🎬 Media & Downloads Guide (Movies & Shows)

This guide covers how to effortlessly search, download, and stream movies and TV shows directly into your **Jellyfin** streaming server.

---

## 1. Automated Bulk Downloader Script

Included in `scripts/bulk_movie_queue.py` is the automated python script that hooks directly into qBittorrent's internal `nova2.py` search engine.

### How to Queue 50+ Movies in Seconds:
1. Open `D:\BucketMedia\Homelab\bulk_movie_queue.py` in any text editor.
2. Edit or add any franchise, film, or show to the `WANTED_MOVIES` list:
   ```python
   WANTED_MOVIES = [
       {"title": "The Matrix", "query": "The Matrix 1999 1080p"},
       {"title": "Inception", "query": "Inception 2010 1080p"},
   ]
   ```
3. Run the script:
   ```powershell
   python D:\BucketMedia\Homelab\bulk_movie_queue.py
   ```
4. The script queries PirateBay / 1337x through qBittorrent, selects the healthiest 1080p torrent with high seeders, and queues it straight into `/movies` (`D:\BucketMedia\Movies`).

---

## 2. Using qBittorrent WebUI Directly (`http://localhost:8080`)

You can also search and download directly inside your browser:

1. Open **[qBittorrent](http://localhost:8080)** (automatically logs in on your local network).
2. Go to the **Search** tab at the top.
   * If you don't see the Search tab, click **View ➔ Search Engine**.
   * Plugins installed: The Pirate Bay, 1337x, YTS, EZTV, TorrentProject.
3. Type any movie or show (e.g. `Top Gun Maverick 1080p`) and hit **Search**.
4. Right-click the result with the most seeders ➔ **Download**.
5. Set **Save Path** to `/movies` for movies, or `/shows` for TV series.
6. Click **OK**.

---

## 3. Trusted Sites for Manual Magnets

If you prefer browsing for high-bitrate releases or entire 4K box sets:

* **[YTS.mx](https://yts.mx/)**: Best for compact, lightweight 1080p & 2160p movies (instant downloads, 1.5–2.5 GB).
* **[1337x.to](https://1337x.to/)**: Best for full seasons, remuxes, and complete director filmographies.
* **[EZTV.re](https://eztv.re/)**: Best for TV shows, daily episodes, and weekly series releases.

### How to add a Magnet link:
1. Copy the magnet link from the site.
2. In qBittorrent, click the **🔗 (Add Torrent Link)** icon in the top toolbar.
3. Paste the magnet URL and ensure the category is set to `movies` (saves to `D:\BucketMedia\Movies`).

---

## 4. Jellyfin Integration & File Naming

Jellyfin automatically monitors `D:\BucketMedia\Movies` and `D:\BucketMedia\Shows`. As soon as a file finishes downloading:
* Jellyfin reads the video metadata.
* Automatically downloads 4K posters, backdrops, actor biographies, and Rotten Tomatoes/IMDb ratings.
* Grabs English and multi-language subtitles automatically.

### Ideal Folder Structures:

#### Movies:
```text
D:\BucketMedia\Movies\
├── Spider-Man (2002)\
│   └── Spider-Man (2002) [1080p].mp4
└── Dune Part Two (2024)\
    └── Dune Part Two (2024).mkv
```

#### TV Shows:
```text
D:\BucketMedia\Shows\
└── Big Time Rush (2009)\
    ├── Season 01\
    │   ├── Big Time Rush - S01E01 - Big Time Audition.mkv
    │   └── Big Time Rush - S01E02 - Big Time School of Rocque.mkv
    └── Season 02\
        └── Big Time Rush - S02E01.mkv
```

### Force a Manual Library Refresh in Jellyfin:
If you want newly downloaded files to show up immediately without waiting for the auto-scan:
1. Open **[Jellyfin](http://localhost:8096)**.
2. Click **☰ ➔ Dashboard ➔ Libraries**.
3. Click the three dots **⋮** next to **Movies** ➔ **Scan Library**.
