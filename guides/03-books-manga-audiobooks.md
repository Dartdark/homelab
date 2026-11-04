# 📚 Books, Manga & Audiobooks Guide

Your homelab includes dedicated servers for reading and listening to your media library across any device:

* **[Kavita](http://localhost:5000)**: Digital reading server for Manga, Comics, and E-books.
* **[Audiobookshelf](http://localhost:13378)**: Full-featured audiobook and podcast server.

---

## 1. Digital Reader: Kavita (`http://localhost:5000`)

Kavita provides an ultra-fast web reader with continuous scrolling, webtoon mode, and two-page spread reading.

### Where to Place Files:
Files are stored across three dedicated folders in `D:\BucketMedia`:

```text
D:\BucketMedia\
├── Manga\
│   └── One Piece\
│       ├── One Piece v01.cbz
│       └── One Piece v02.cbz
├── Comics\
│   └── Batman\
│       └── Batman - Year One (1987).cbr
└── Books\
    └── Brandon Sanderson\
        └── The Way of Kings (2010).epub
```

### Supported Formats:
* **Manga & Comics:** `.cbz`, `.cbr`, `.zip`, `.rar`, `.tar.gz`
* **E-Books:** `.epub`, `.pdf`

### Scanning for New Reading Material:
1. Copy your `.cbz` or `.epub` files into the appropriate folder above.
2. In Kavita, click the **⚙️ Server Settings** icon ➔ **Libraries**.
3. Click the three dots **⋮** next to your library ➔ **Scan Library**.

---

## 2. Audiobooks & Podcasts: Audiobookshelf (`http://localhost:13378`)

Audiobookshelf tracks reading progress across devices, supports embedded chapter markers, and has native iOS & Android apps.

### Where to Place Audiobooks:
Audiobookshelf strictly relies on the `Author/Title` directory layout:

```text
D:\BucketMedia\Audiobooks\
└── Frank Herbert\
    └── Dune (1965)\
        ├── cover.jpg
        └── Dune.m4b
```

### Best Formats:
* **`.m4b` (Recommended)**: Single-file audiobook containing embedded chapter markers, cover art, and author metadata.
* **Multi-file `.mp3`**: Ensure files are numbered sequentially (`01 - Chapter 1.mp3`, `02 - Chapter 2.mp3`).

---

## 3. Trusted Book & Reading Sources

* **[Anna's Archive](https://annas-archive.org/)**: The world’s largest open-source meta-search library. Indexes millions of books, papers, comics, and manga from Libgen, Sci-Hub, and Z-Library in `.epub` and `.pdf`.
* **[Library Genesis (Libgen.is)](https://libgen.is/)**: Direct mirror for non-fiction, academic textbooks, and literature.
* **[MangaDex](https://mangadex.org/)**: Premier ad-free manga scanlation hub. (Use tools like **FMD2** or **Hakuneko** to download full manga series directly into `.cbz` format for Kavita).
* **[Audiobook Bay (ABB)](https://audiobookbay.lu/)**: The primary community archive for unabridged audiobooks in `.m4b` and `.mp3`.
