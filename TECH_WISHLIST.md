# 🎯 Ultimate Tech & Homelab Wishlist

> Curated personal hardware upgrades, streaming gear, and homelab expansions tailored for high-performance media streaming, clean aesthetics, and seamless ecosystem integration.

---

## 📺 Living Room & Streaming (Top Priority)

### 1. 🍎 Apple TV 4K (3rd Gen, 128GB Wi-Fi + Ethernet)
* **Estimated Price:** ~$149
* **Priority:** 🔴 Immediate / Top Pick
* **Why it fits your setup:**
  * **Zero Lag:** Powered by the Apple A15 Bionic chip—the fastest, smoothest media navigation experience with 60fps/120fps fluid scrolling and instant app launches.
  * **Ad-Free UI:** Clean, minimalist interface with no intrusive banner ads or cluttered recommendation feeds.
  * **iPhone Integration:** Seamless text and password entry straight from your iPhone keyboard, AirPlay 2 screen mirroring, and hands-free Siri remote.
  * **Homelab Client (Infuse / Swiftfin / Plex):** Pairs with your local server (`D:\BucketMedia`) using the **Infuse** or **Swiftfin** app to direct-play 4K HDR, Dolby Vision, and all subtitle formats without any server transcoding.
  * **Gigabit Ethernet:** The 128GB model includes a physical gigabit LAN port for stable, high-bitrate streaming.

### 2. 🔊 Compact Dolby Atmos Soundbar (Sonos Beam Gen 2 or Bose Smart Soundbar 600)
* **Estimated Price:** ~$399 – $449
* **Priority:** 🟡 Medium
* **Why it fits your setup:**
  * **Effortless eARC Audio:** Connects via a single HDMI eARC cable to your TV/Apple TV for full Dolby Atmos spatial audio without requiring a bulky AV receiver or running speaker wires through walls.
  * **Apple Ecosystem:** Supports Apple AirPlay 2 to beam music directly from your phone or Navidrome app.

---

## 🏰 Homelab & Storage Expansion

### 3. 💾 High-Capacity Server Drive (Seagate Exos 16TB / 18TB 7200RPM Enterprise HDD)
* **Estimated Price:** ~$190 – $240
* **Priority:** 🟢 Low / Far Future Expansion
* **Why it fits your setup:**
  * **Current Status:** You currently have **1.04 TB (1,072 GB) free** out of 1.80 TB on your `D:\` drive. You have plenty of headroom for hundreds of movies and thousands of FLAC tracks.
  * **When to buy:** Only worth considering far down the line when you start filling multiple terabytes of uncompressed 4K Blu-ray remuxes.

### 4. ⚡ Dedicated 24/7 Mini PC Server (Intel N100 / Beelink S12 Pro or Minisforum)
* **Estimated Price:** ~$160 – $190
* **Priority:** 🟢 Nice to Have
* **Why it fits your setup:**
  * **Dedicated Homelab:** Moves your Docker containers (Jellyfin, Navidrome, Kavita, Stremio, qBittorrent) off your main desktop PC onto a dedicated, whisper-quiet appliance.
  * **Power Efficiency:** Draws only ~6W at idle compared to a full desktop rig running 24/7.
  * **Hardware Transcoding:** The Intel N100 features built-in Intel QuickSync with hardware AV1/HEVC decode for multi-stream remote video playback.

### 5. 🔋 Smart Uninterruptible Power Supply (CyberPower / APC 1500VA UPS)
* **Estimated Price:** ~$140 – $170
* **Priority:** 🟡 Medium
* **Why it fits your setup:**
  * **Database Protection:** Prevents SQLite database corruption (like Navidrome and Immich) and keeps your network and server online during power dips or accidental unplugging.

---

## 🤖 The Future AI & Gaming Flagship (Nvidia RTX 5090 Custom Build)

> Planned future workstation build designed to run and fine-tune private, uncensored 32B–70B AI coding models (rivaling Claude Code) and deliver flagship 4K gaming.

* **Estimated Total Build Cost:** ~$3,500 – $3,900
* **Priority:** 🟣 Long-Term Dream Build

### Complete Component Specification

| Component | Recommended Model | Est. Price | Role in the Build |
| :--- | :--- | :--- | :--- |
| **GPU** | **NVIDIA GeForce RTX 5090 (32GB GDDR7)** | ~$1,999 – $2,200 | 32GB high-speed GDDR7 VRAM runs 32B–70B abliterated coding models locally with zero cloud subscription fees. |
| **CPU** | **AMD Ryzen 7 9800X3D** (or 7800X3D) | ~$450 – $480 | Undisputed top gaming & workload processor. Low power draw (~100W), PCIe 5.0 lanes, zero GPU bottlenecks. *(Alt for massive dataset processing: Ryzen 9 9950X).* |
| **Motherboard** | **MSI MAG X870 Tomahawk** or **ASUS ROG Strix B650E-F** | ~$230 – $320 | Reinforced **PCIe 5.0 x16 slot** for full GPU throughput, heavy-duty VRM power delivery, and PCIe 5.0 M.2 lanes. |
| **RAM (Memory)** | **64GB DDR5-6000 CL30** (2x 32GB, Corsair / G.Skill) | ~$190 – $220 | **2x VRAM Rule:** 64GB system memory allows caching massive token contexts and training datasets in memory. |
| **Power Supply (PSU)**| **1200W ATX 3.1 / PCIe 5.1** (Seasonic Vertex GX-1200 / Corsair RM1200x) | ~$210 – $260 | Native **12V-2x6** (16-pin) high-current cable to safely deliver the 5090's ~600W max power draw and handle transient spikes. |
| **Primary SSD** | **2TB or 4TB NVMe M.2 (Gen 4/5)** (Samsung 990 Pro / WD SN850X) | ~$170 – $290 | Blistering 7,400 MB/s read speeds to load 20GB–40GB AI model weights in under 3 seconds. *(Your current 1.8TB drive moves over as secondary storage).* |
| **CPU Cooler** | **360mm AIO Liquid Cooler** (Arctic Liquid Freezer III 360 / Lian Li Galahad II) | ~$110 – $160 | Whispering-quiet 360mm liquid cooling keeps CPU under 70°C even under sustained compilation loads. |
| **PC Case** | **High-Airflow Chassis (400mm+ GPU Clearance)** (Lian Li O11 EVO / Fractal North XL / NZXT H9) | ~$150 – $190 | Massive internal volume to easily house a 4-slot 350mm GPU and exhaust ~750W of combined thermal dissipation. |
| **GPU Bracket** | **Heavy-Duty Metal Anti-Sag Support Column** | ~$15 | Protects the motherboard PCIe slot from cracking under the weight of a 5-pound graphics card. |

---

## 🎧 Mobile & Lifestyle Gear

### 6. 🎧 AirPods Pro (2nd Gen with USB-C)
* **Estimated Price:** ~$189 – $249
* **Priority:** 🟡 Medium
* **Why it fits your setup:**
  * **Apple TV Spatial Audio:** Watch 4K movies late at night in Dolby Atmos spatial audio with head tracking without waking anyone up.
  * **Active Noise Cancellation:** Industry-leading ANC and Transparency mode for daily listening to your `Bucketlist` playlists.

---

## 🚗 Tesla Accessories

### 7. 🧲 MagSafe Wireless Charging Mount (MagBak or Spigen for Tesla Model 3/Y)
* **Estimated Price:** ~$60 – $99
* **Priority:** 🟢 Nice to Have
* **Why it fits your setup:**
  * **Seamless Cockpit Integration:** Securely snaps your iPhone right beside the 15-inch center touchscreen for glanceable navigation and music controls.
  * **Fast Qi Charging:** Keeps your phone charged while streaming via Tailscale.

### 8. 🎮 8BitDo Ultimate 2.4G / Bluetooth Wireless Controller
* **Estimated Price:** ~$45 – $55
* **Priority:** 🟢 Nice to Have
* **Why it fits your setup:**
  * **In-Car & Arcade Gaming:** Plug the wireless USB receiver into the glovebox or center console to play Steam/Tesla Arcade games and your self-hosted EmulatorJS library.

---

*Last Updated: 2026-11-07 • Tracked in `Dartdark/homelab`*
