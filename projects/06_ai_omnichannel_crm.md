# ?? AI Omnichannel CRM for Indonesian SMEs

> **Kategori:** AI SaaS / Customer Support CRM / Multi-Channel Integration  
> **Status:** Active Prototype  
> **Tech Stack:** Next.js 14, React, TypeScript, Supabase (PostgreSQL + RLS), AI Reply Engine, Midtrans Billing Gateway  
> **Repository:** [Local Project / Pandujatip](https://github.com/Pandujatip)

---

## ?? Project Overview & STAR Case Study

### ?? Situation (Latar Belakang)
Pelaku UMKM di Indonesia rata-rata melayani ratusan pesan masuk per hari melalui berbagai saluran yang terpisah (WhatsApp dan Instagram DM). Hal ini menyebabkan respon lambat (*slow response*), tingkat konversi penjualan rendah, dan tingginya biaya admin customer service.

### ?? Task (Tantangan & Sasaran)
Membangun aplikasi SaaS CRM Omnichannel bertenaga AI yang menggabungkan seluruh pesan percakapan ke dalam satu kotak masuk terpadu (*Unified Inbox*) serta memberikan balasan otomatis cerdas (*Smart Auto-Reply*) yang memahami konteks katalog produk dan mematuhi batasan etika bisnis (*business guardrails*).

### ?? Action (Arsitektur & Implementasi Teknis)
- **Unified Messaging Interface:** Antarmuka web modern dengan Next.js yang menampilkan obrolan lintas platform secara konsisten dan responsif.
- **AI Auto-Reply with Guardrails:**
  - Engine AI yang mengintegrasikan basis pengetahuan FAQ dan katalog produk toko.
  - Penerapan *system prompt guardrails* untuk mencegah halusinasi harga, menjaga kesopanan, dan mengalihkan pertanyaan sensitif ke agen manusia secara mulus.
- **Multi-Tenant Database Architecture:**
  - Skema database Supabase PostgreSQL dengan *Row-Level Security* (RLS) per *workspace*, memastikan data pelanggan dan percakapan antar toko terisolasi secara absolut.
  - Integrasi billing langganan otomatis dengan Midtrans.

### ?? Result & Impact (Hasil & Metrik)
- **Unified Customer View:** Riwayat interaksi pelanggan dari WhatsApp dan Instagram terkonsolidasi dalam satu profil terpadu.
- **AI Response Latency < 2s:** Menghasilkan draf atau balasan otomatis instan dengan akurasi jawaban sesuai katalog produk terdaftar.
