# 🏈 Live Sports & Live Television Guide

This guide details how to watch live sporting events (NFL, NBA, UFC / PPV, Premier League, MLB, F1) across your homelab apps, why certain free IPTV addons fail, and how to bypass ISP streaming blocks.

---

## 1. Stremio App vs. Stremio Web: The "All IPTV" Codec Difference

> 💡 **Important Discovery:** **All IPTV DOES work**, but **only in the native Stremio App** (Windows desktop, Android, Android TV, Firestick), **not in Stremio Web** (`web.stremio.com`).

### Why it failed in the browser:
* **Web Browser Codec Limitations:** Standard web browsers (Chrome, Edge, Safari) do not have native decoders for raw broadcast transport streams (MPEG-TS `.ts` files) and enforce strict CORS network restrictions. When Stremio Web tries to play raw IPTV feeds, the browser fails with `Video is not supported`.
* **Why it works in the native App:** The standalone Stremio Desktop and TV apps have **libVLC / ExoPlayer** built directly into the player engine. This enables hardware decoding for all raw IPTV streams, cable feeds, and alternate audio tracks without browser limitations.
* **Premium Prompts:** While some channels feature developer donation/premium prompts, thousands of live cable, news, and sports streams play completely fine inside the native desktop or TV app.

---

## 2. Working Stremio Sports Addon: PlavioLive

Unlike mass scrapers, **PlavioLive** provides curated, active Akamai and Cloudfront HLS streams categorized by game fixture:

* **Manifest URL:**
  ```text
  https://addon.plavio.site/manifest.json
  ```
* **How to Install:** In Stremio, click the green **`+ Add addon`** button and paste the URL.
* **Categories:** American Football (NFL & NCAA), Basketball (NBA), Fight (UFC, Boxing, WWE), Football (Soccer/EPL), Motor Sports (F1), Baseball (MLB), Hockey (NHL).
* **Fixing "Video Not Supported" in Stremio:** Go to Stremio **Settings ➔ Player ➔ Set "Play in external player" to VLC**, or run the native Stremio Desktop/TV app which has built-in decoders.

---

## 3. Verified Live Sports Web Portals (Instant 1080p Access)

If you just want to pull up a game or UFC fight in your browser with zero setup or addons:

| Portal | URL | Coverage | Notes |
| :--- | :--- | :--- | :--- |
| **VIPBox** | `https://www.vipbox.lc/` | All Sports (NFL, NBA, UFC, Soccer, MLB, F1) | Verified active 200 OK. Multiple stream quality mirrors. |
| **Sportsurge** | `https://sportsurge.club/` | Major Leagues & PPV | Aggregates 10+ live stream mirrors per matchup with bitrate info. |
| **StreamEast** | `https://thestreameast.to/` | NFL, NBA, MMA, Boxing | Clean schedule interface; very popular for American leagues. |
| **PPV.land** | `https://ppv.land/` | Combat Sports | Specifically built for UFC fight cards, Boxing PPVs, and wrestling events. |

*(Always use **uBlock Origin** on free streaming sites to block popup advertisements).*

---

## 4. How to Bypass ISP DNS Blocking (The 10-Second Fix)

If sports streaming websites say *"This site can't be reached"* or time out, your Internet Service Provider (Comcast/Xfinity, AT&T, Spectrum) is blocking the domain at the router level.

### Bypassing in Google Chrome / Microsoft Edge:
1. Open your browser **Settings** (or navigate to `chrome://settings/security`).
2. Scroll to the **Use secure DNS** section.
3. Toggle it **ON** and select **Cloudflare (1.1.1.1)** or **Google (Public DNS)** from the dropdown.
4. Refresh the page — blocked sports sites will load immediately.

---

## 5. Jellyfin Live TV (Native Cable Experience with Transcoding)

Jellyfin includes built-in **FFmpeg transcoding**, meaning it converts raw broadcast feeds into web-compatible video on the fly, eliminating "Video is not supported" errors.

### Curated Sports M3U:
A dedicated sports playlist is stored inside your Jellyfin container at `/config/sports.m3u` (`D:\BucketMedia\Homelab\jellyfin\config\sports.m3u`) featuring:
* *NFL Channel, FOX Sports, CBS Sports HQ, NBC Sports NOW, UFC, Bellator MMA, PFL MMA, DAZN Ringside, The NBA Channel, MLB, PGA Tour, UEFA Champions League, Golazo Soccer, CW WWE NXT.*

### How to Enable in Jellyfin:
1. Open **[Jellyfin](http://localhost:8096)** ➔ Click **☰ ➔ Dashboard ➔ Live TV**.
2. Under **Tuner Devices**, click **`+` (Add)**:
   * **Tuner Type:** Select `M3U Tuner`
   * **File or URL:** `/config/sports.m3u`
   * Click **Save**.
3. Under **TV Guide Data Providers**, click **`+` (Add)**:
   * **Guide Type:** Select `XMLTV`
   * **File or URL:** `https://sulthanpamenan.github.io/pluto-playlist/epg.xml`
   * Click **Save**.
4. The **Live TV** icon will now appear on your Jellyfin home screen and mobile Swiftfin app!
