# 🍿 Stremio Mastery & Addon Organization Guide

Stremio connects community scrapers and media catalogs into an on-demand streaming hub. Your homelab runs the local **Stremio Streaming Server** on port `11470` (`http://localhost:11470`).

---

## 1. How Stremio Organizes Your Home Screen

Stremio displays rows (catalogs) on your **Board / Home** page in the exact order that addons are installed in your account.

> ⚠️ **The "Disappearing Tabs" Trap:** When you install addons that provide dozens of categories (such as sports or global TV scrapers), Stremio runs out of space on the main screen and pushes your favorite rows (like Hulu, Paramount+, and HBO Max) all the way down to the bottom or off the screen.

---

## 2. Reordering Addons Without Reinstalling

Instead of manually deleting and reinstalling addons to fix your row order, use the community **Stremio Addon Manager**:

1. Open **[Stremio Addon Manager](https://stremio-addon-manager.vercel.app/)** in your browser.
2. Log in with your Stremio email and password ➔ Click **Load Addons**.
3. You will see a visual list of every addon installed on your account.
4. **Drag and drop** your primary catalog addon (**CyberFlix / Streaming Catalogs**) to the **very top** of the list.
5. Move secondary or utility addons below it.
6. Click **Sync to Stremio**.
7. In the Stremio app, press `Ctrl + Shift + R` (or restart the app) to pull the new layout.

---

## 3. Streaming Catalogs Setup (Hulu, Paramount, HBO, Netflix)

To display clean streaming service rows on your Home screen:

1. Visit the **[CyberFlix Catalog Configurator](https://cyberflix.elfhosted.com/)**.
2. Under **Select Providers**, check only the services you actually watch:
   * ✅ **Netflix**
   * ✅ **HBO Max / Max**
   * ✅ **Hulu**
   * ✅ **Paramount+**
   * ✅ **Disney+**
   * ✅ **Apple TV+**
   * *(Uncheck foreign or unused networks to prevent Home screen bloat)*.
3. Click **Install Addon** to link it directly to your Stremio account.

---

## 4. The Essential On-Demand Scraper: Torrentio

Torrentio is the gold standard scraper for on-demand 4K movies and TV shows:

* **Configurator URL:** `https://torrentio.strem.fun/configure`
* **Features:** Scrapes 1337x, YTS, ThePirateBay, TorrentGalaxy, EZTV, and RARBG mirrors.
* **Resolution Filters:** You can prioritize 1080p and 4K HDR streams, filter out CAM rips, and configure Real-Debrid / AllDebrid caching if desired.

---

## 5. Adding Addons via Custom Manifest URLs

Third-party community addons (like live sports or niche metadata) are often delisted from Stremio's default search bar to avoid DMCA issues.

### To Install Any Addon via URL:
1. Copy the addon's `https://.../manifest.json` URL.
2. In Stremio, go to **Addons** (the puzzle piece icon).
3. Click the green **`+ Add addon`** button (or paste the manifest URL directly into the search box).
4. Click **Install**.
