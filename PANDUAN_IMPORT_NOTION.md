# ?? Panduan Lengkap Menyiapkan Portofolio di Notion
**Pandu Jati Pamungkas ? AI Trainer | Data Annotation & QA | Industrial Domain Expert | Full-Stack & Computer Vision Developer**

Dokumen ini memandu Anda membuat portofolio Notion yang profesional, modern, dan interaktif dengan 2 opsi metode:
- **Opsi A (Paling Mudah & Instan):** Import langsung file Markdown & CSV ke Notion (Tanpa token API).
- **Opsi B (Otomatisasi Script):** Menggunakan script Python `sync_to_notion.py` dengan Notion API.

---

## ?? OPSI A: Import Manual ke Notion (Rekomendasi - Cepat & Estetik)

### Langkah 1: Buat Halaman Utama Portofolio di Notion
1. Buka [Notion](https://www.notion.so) dan login ke akun Anda.
2. Di sidebar kiri, klik **`+ Add a page`**.
3. Beri judul halaman: **`? Pandu Jati Pamungkas - Portfolio`**.
4. Beri ikon **?** atau **??** dan Cover Image profesional (misal: tema *Engineering* / *Artificial Intelligence*).

### Langkah 2: Import Master Hub Markdown
1. Buka file **`NOTION_PORTFOLIO_MASTER.md`** di text editor (Notepad/VS Code).
2. Salin (*Copy*) seluruh isinya, lalu Tempel (*Paste*) langsung ke halaman Notion yang baru Anda buat.
3. Notion akan otomatis merender *Callout blocks*, *Heading*, *Tabel Ringkasan*, *Mindmap Mermaid*, dan *Tautan*.

---

### Langkah 3: Import Database Proyek (CSV)
1. Di halaman portofolio Notion Anda, ketik `/import` lalu pilih **CSV**.
2. Pilih file **`NOTION_PROJECTS_DATABASE.csv`** dari folder `c:\Users\tigal\Resume CV Pandu\`.
3. Notion akan otomatis membuat sebuah Database berisi 10 proyek dengan kolom:
   - `Project Name` (Title)
   - `Category` (Select)
   - `Domain` (Select)
   - `Status` (Select)
   - `Tech Stack` (Multi-select)
   - `Key Metric / Impact` (Text)
   - `GitHub Repo` (URL)
   - `Year` (Number)
   - `Featured` (Checkbox)
   - `Summary` (Text)

---

### Langkah 4: Ubah Tampilan Database Menjadi "Gallery View" (Sangat Menarik untuk Rekruter)
1. Di database yang baru di-import, klik tombol **`+`** di samping tab *Table* untuk menambah View baru.
2. Pilih layout **`Gallery`**.
3. Klik titik tiga (**`...`**) pada Database -> pilih **`Properties`**.
4. Aktifkan (*toggle on*) properti yang ingin ditampilkan di kartu:
   - ? `Category`
   - ? `Domain`
   - ? `Tech Stack`
   - ? `Status`
   - ? `GitHub Repo`
5. Atur *Card size* ke **Medium**.
6. Sekarang portofolio Anda memiliki galeri kartu proyek interaktif yang sangat estetik!

---

### Langkah 5: Hubungkan Halaman Detail Studi Kasus (10 Proyek)
Untuk setiap kartu proyek di dalam Database:
1. Klik salah satu proyek (misal: *AI K3 Electrical Room Monitoring*).
2. Buka file markdown terkait di folder `projects/` (misal: `projects/01_ai_electrical_room_monitor.md`).
3. Copy isinya dan paste ke dalam body halaman proyek di Notion.
4. Ulangi untuk 10 proyek yang tersedia.

---

## ? OPSI B: Otomatisasi 1-Klik Menggunakan Python Script (`sync_to_notion.py`)

Jika Anda ingin script membuat Database dan 10 halaman proyek secara otomatis lewat Notion API:

### Langkah 1: Buat Notion Integration Token
1. Kunjungi [https://www.notion.so/my-integrations](https://www.notion.so/my-integrations).
2. Klik **`+ New integration`**.
3. Beri nama (misal: `Portfolio Sync`), pilih workspace Anda, lalu klik **Submit**.
4. Salin **Internal Integration Secret** (`secret_xxxxxxxxxxxxxxxxxxxxxxxxxxxxx`).

### Langkah 2: Buat Halaman Induk & Beri Akses Integration
1. Di Notion, buat sebuah Page baru (misal: `Portfolio Hub`).
2. Klik titik tiga (**`...`**) di pojok kanan atas halaman tersebut.
3. Scroll ke bawah, pilih **`Add connections`**, lalu cari dan pilih integrasi yang baru Anda buat (`Portfolio Sync`).
4. Salin **Page ID** dari URL Notion Anda:
   - Format URL: `https://www.notion.so/workspace/Portfolio-Hub-18a7b8c9d0e14f2a8b3c4d5e6f7a8b9c`
   - Page ID adalah 32 karakter di bagian akhir: `18a7b8c9d0e14f2a8b3c4d5e6f7a8b9c`.

### Langkah 3: Jalankan Script Sync
Buka PowerShell di folder `c:\Users\tigal\Resume CV Pandu\` dan jalankan:
```powershell
python sync_to_notion.py
```
Masukkan Token dan Page ID saat diminta. Script akan otomatis:
1. Membuat Database Proyek dengan schema lengkap.
2. Mengisi seluruh 10 proyek beserta kategori, tag tech stack, metrik, link github, dan summary.

---

## ?? Tips Membagikan Portofolio ke Rekruter / Klien

1. Klik tombol **`Share`** di kanan atas halaman Notion Anda.
2. Aktifkan **`Publish to Web`**.
3. Klik **`Copy web link`**.
4. Anda sekarang memiliki tautan portofolio publik langsung (contoh: `https://pandujati.notion.site/portfolio`) yang dapat dicantumkan di:
   - CV / Resume PDF
   - Profil LinkedIn (Featured section & Contact Info)
   - GitHub Profile README (`https://github.com/Pandujatip`)
   - Lamaran kerja internasional untuk posisi AI Trainer / Data Annotation / Computer Vision / Full-Stack Engineer!
