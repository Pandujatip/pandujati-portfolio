# ?? GPS Truck SIG Mobile APK

> **Kategori:** Mobile Android / Field Fleet Tracking & Logistics  
> **Status:** Production Live  
> **Tech Stack:** Android Java, WebView Bridge, Gradle Portable Toolchain, ProGuard, Android Hardware Bindings  
> **Repository:** [Local Project / Pandujatip](https://github.com/Pandujatip)

---

## ?? Project Overview & STAR Case Study

### ?? Situation (Latar Belakang)
Sopir armada truk ekspedisi semen membutuhkan aplikasi mobile yang ringan, responsif, dan mudah diinstal untuk melaporkan koordinat GPS dan status perjalanan secara real-time ke sistem pemantauan pusat. Penggunaan browser biasa seringkali terkendala oleh penonaktifan akses lokasi (*geolocation permission*) oleh sistem Android saat layar redup atau saat beralih aplikasi.

### ?? Task (Tantangan & Sasaran)
Membangun aplikasi Android APK khusus yang membungkus web telemetri armada dengan integrasi izin perangkat keras native (GPS geolocation presisi tinggi, kamera untuk scan dokumen jalan, dan persistensi sesi).

### ?? Action (Arsitektur & Implementasi Teknis)
- **Native Android Wrapper & Permission Bridge:**
  - Mengonfigurasi Android WebView dengan dukungan penuh untuk JavaScript, DOM storage, cookies, HTML5 Geolocation, dan native file chooser.
  - Menyediakan handler khusus untuk meminta dan mempertahankan izin lokasi latar depan/belakang (*fine location*).
- **Zero-Dependency Portable Build Toolchain:**
  - Merancang skrip otomasi PowerShell `build-release.ps1` yang dapat mengunduh JDK portable, Gradle, dan Android SDK platform tools secara otomatis, memungkinkan kompilasi APK rilis tanpa perlu menginstal Android Studio secara penuh.
  - Penguncian tanda tangan digital rilis dengan keystore khusus (`gpstruck-release.jks`).

### ?? Result & Impact (Hasil & Metrik)
- **Ukuran APK Sangat Ringan (< 3 MB):** Beroperasi lancar bahkan pada smartphone spesifikasi rendah milik pengemudi truk.
- **Reliable Telemetry:** Mengeliminasi masalah kehilangan sinyal koordinat browser selama pengantaran logistik semen.
