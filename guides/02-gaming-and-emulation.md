# 🕹️ Gaming & Emulation Guide

Your homelab supports both **in-browser retro arcade emulation** (via EmulatorJS) and **standalone 4K Nintendo Switch emulation** (via Ryujinx).

---

## 1. Browser Retro Arcade: EmulatorJS (`http://localhost:4000`)

EmulatorJS runs full retro console emulators right inside any web browser on your phone, tablet, laptop, or TV without installing any local emulator software.

### Web Addresses:
* **Player Frontend:** `http://localhost:4000`
* **Admin Management Console:** `http://localhost:4001`

### Where to Place ROM Files:
Store your game files in `D:\BucketMedia\Games\ROMs\<console_folder>`:

```text
D:\BucketMedia\Games\ROMs\
├── nes\        (Nintendo Entertainment System - .nes)
├── snes\       (Super Nintendo - .sfc, .smc)
├── gba\        (Game Boy Advance - .gba)
├── gbc\        (Game Boy Color - .gbc)
├── n64\        (Nintendo 64 - .z64, .n64)
├── genesis\    (Sega Genesis / Mega Drive - .bin, .md)
└── psx\        (PlayStation 1 - .chd, .bin/.cue)
```

### How to Index New ROMs in EmulatorJS:
1. Copy ROM files into their respective console subfolders.
2. Open the **Admin Console** at `http://localhost:4001`.
3. Click **Scan / Index**. EmulatorJS downloads box art, titles, and controller mappings automatically.
4. Open `http://localhost:4000` to play with save states and gamepad support.

---

## 2. Nintendo Switch Emulation: Ryujinx

Located at: `D:\BucketMedia\Games\Ryujinx\Ryujinx.exe`

### Required Prerequisites:
For Switch emulation to boot games, two files must exist in the Ryujinx system directory:
* **`prod.keys`** ➔ `D:\BucketMedia\Games\Ryujinx\system\prod.keys`
* **Firmware** ➔ Installed via Ryujinx UI: **Tools ➔ Install Firmware ➔ Install from XCI or ZIP**.

### ROM Formats:
* **Base Games:** `.nsp` or `.xci`
* **Updates & DLC:** `.nsp`

### Recommended Folder Structure:
```text
D:\BucketMedia\Games\Switch\
├── BaseGames\
│   ├── Super Mario Odyssey [0100000000010000].xci
│   └── The Legend of Zelda Tears of the Kingdom [0100F2C0115B6000].nsp
└── Updates\
    └── TOTK Update v1.2.1 [0100F2C0115B6800].nsp
```

### Installing Game Updates & DLC:
1. In Ryujinx, right-click the game title.
2. Click **Manage Title Updates** ➔ **Add** ➔ Select the update `.nsp` file ➔ **Save**.
3. Right-click ➔ **Manage DLC** ➔ **Add** ➔ Select DLC files ➔ **Save**.

### Controller Setup:
1. In Ryujinx, go to **Options ➔ Settings ➔ Input**.
2. Select your controller (Xbox Controller, DualSense PS5, or Nintendo Switch Pro Controller).
3. Ensure **Enable Motion Controls** is checked if your controller supports gyro.

---

## 3. Trusted Game Repositories

* **[Myrient (erista.me)](https://myrient.erista.me/)**: The most complete, verified No-Intro and Redump preservation archive for all retro systems (NES through PS2/GameCube).
* **[Vimm's Lair](https://vimm.net/)**: Legendary clean vault for US retro ROMs (NES, SNES, Genesis, N64, GameCube, Wii, PS1, PS2).
* **[CDRomance](https://cdromance.org/)**: Best for disc-based games (PS1, PS2, PSP, Dreamcast, Saturn) and English fan-translations.
* **[r/Roms Megathread](https://r-roms.github.io/)**: The Reddit community's comprehensive directory for modern and retro game archives.
