# ?? SIGXPORT Reborn - Port Logistics & Cement Dispatch System

> **Kategori:** Industrial Logistics / Fleet Management / PWA & Mobile App  
> **Status:** Production Deployment  
> **Tech Stack:** Node.js, Express, PostgreSQL, Kotlin + Jetpack Compose (Native Android), PWA, PM2, GitHub Actions CI/CD  
> **Repository:** [https://github.com/Pandujatip/sigxport-web-reborn](https://github.com/Pandujatip/sigxport-web-reborn)

---

## ?? Project Overview & STAR Case Study

### ?? Situation (Latar Belakang)
Operasional pengiriman semen ekspor melalui pelabuhan melibatkan ratusan armada truk tronton dan beberapa titik muat (*loading points*) serta dermaga kapal. Sistem legacy sebelumnya memiliki keterbatasan dalam memonitor antrean truk secara real-time, tidak memiliki aplikasi Android native modern yang efisien, dan data antrean belum terintegrasi secara modular dengan sistem pihak ketiga.

### ?? Task (Tantangan & Sasaran)
Membangun arsitektur paralel **SIGXPORT Reborn** yang terisolasi dari database legacy untuk:
1. Membangun dashboard analitik web & PWA berkinerja tinggi yang menyajikan data antrean truk, kapasitas dermaga, dan status kapal secara real-time.
2. Mengembangkan aplikasi Android Native modern menggunakan **Kotlin + Jetpack Compose** dengan pipeline build Play Store (AAB).
3. Membangun *Integration API* aman dengan autentikasi Bearer token untuk konsumsi data pihak ketiga.
4. Menerapkan sinkronisasi otomatis satu arah (*one-way cron sync*) dari database legacy ke database Reborn setiap hari pukul 08:00 WIB.

### ?? Action (Arsitektur & Implementasi Teknis)
- **Dual-Database Architecture:** Mengisolasi `sigxport_reborn_db` (PostgreSQL) pada port 5100 sehingga pengembangan dan pengujian tidak mengganggu database operasional live.
- **One-Way Cron Sync Engine:** Skrip bash otomatis yang membackup kedua basis data, melakukan pengecekan data baru (*missing rows*), dan memperbarui agregat data titik muat hanya jika data lebih mutakhir.
- **Native Android App (Kotlin + Compose):** Membangun aplikasi mobile di `android/sigxport-main` dengan UI deklaratif Jetpack Compose, konsumsi API Reborn, dan pipeline build AAB rilis Play Store.
- **Automated CI/CD Pipeline:** GitHub Actions untuk validasi backend (`npm run check`, `npm run test:security`), kompilasi native Android release bundle, serta verifikasi build APK tracking driver.

### ?? Result & Impact (Hasil & Metrik)
- **Real-Time Queue Telemetry:** Memberikan visibilitas instan atas waktu muat rata-rata (*average loading time*) dan panjang antrean per *loading point*.
- **Zero-Downtime Migration:** Integrasi data legacy berjalan mulus tanpa downtime melalui cron sync harian.
- **Enterprise-Grade Mobile Build:** Menghasilkan Android App Bundle (.aab) siap rilis dengan standar keamanan dan performa tinggi.
