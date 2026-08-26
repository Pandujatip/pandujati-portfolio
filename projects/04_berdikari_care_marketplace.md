# ?? Berdikari Care (Saling Bantu) - Hyperlocal Services Marketplace

> **Kategori:** Full-Stack Web SaaS / On-Demand Services Marketplace  
> **Status:** Live MVP  
> **Tech Stack:** React 18, TypeScript, Vite, Node.js, Express, Prisma ORM, SQLite (Dev) / PostgreSQL (Prod), DOKU Payment Gateway, WhatsApp OTP  
> **Repository:** [https://github.com/Pandujatip/saling-bantu](https://github.com/Pandujatip/saling-bantu)

---

## ?? Project Overview & STAR Case Study

### ?? Situation (Latar Belakang)
Kabupaten Tuban membutuhkan platform digital terpercaya untuk memberdayakan penyedia jasa lokal (reparasi AC/elektronik, renovasi rumah, montir panggilan, kebersihan, dan laundry) dan menghubungkan mereka langsung dengan masyarakat tanpa risiko penipuan atau pemotongan harga yang tidak transparan.

### ?? Task (Tantangan & Sasaran)
Membangun MVP marketplace on-demand terpadu yang memfasilitasi 3 jenis pengguna (Konsumen, Rekanan/Mitra, dan Aplikator/Admin) dengan sistem pembayaran terjamin (*escrow*), verifikasi dokumen mitra, serta proteksi transaksi di luar platform (*anti-bypass protection*).

### ?? Action (Arsitektur & Implementasi Teknis)
- **Unified 3-Mode Architecture:**
  - **Portal Konsumen:** Pencarian jasa terfilter, pemesanan, integrasi payment gateway DOKU, dan rating review setelah pekerjaan selesai.
  - **Portal Rekanan:** Pendaftaran mandiri, katalog jasa fleksibel multi-kategori, penerimaan order, dan ledger pencairan saldo (*escrow balance*).
  - **Portal Aplikator (Admin):** Dashboard GMV, verifikasi berkas legal mitra (PDF/JPG), monitoring margin komisi, dan persetujuan pencairan dana (*payout ledger*).
- **Anti-Bypass Protection System:**
  - Masking nomor kontak pada chat in-app sebelum pesanan berstatus aktif.
  - Filter otomatis kata kunci nomor handphone / tautan WhatsApp eksternal di ruang obrolan.
- **Database & Migration Strategy:**
  - Prisma ORM dengan dual-schema (`schema.prisma` untuk SQLite dev dan `schema.postgres.prisma` untuk PostgreSQL produksi).

### ?? Result & Impact (Hasil & Metrik)
- **End-to-End Transaction Flow:** Transaksi terselesaikan dengan sistem escrow aman, mulai dari booking, pembayaran via DOKU, hingga dana masuk ke ledger saldo mitra.
- **Mitra Verification:** Mencegah pendaftaran fiktif melalui sistem upload dan kurasi dokumen KTP/surat usaha di portal admin.
