# ?? EP 343EP1 Pilot - Industrial Emission Monitoring & Predictive Analytics

> **Kategori:** Industrial Environmental Compliance & Data Science (Air Pollution Control)  
> **Status:** Pilot Verified  
> **Tech Stack:** Python 3.11, DuckDB, Pandas, Scikit-learn, SQLAlchemy, PyODBC, OpenPyXL  
> **Repository:** [Local Project / Pandujatip](https://github.com/Pandujatip)

---

## ?? Project Overview & STAR Case Study

### ?? Situation (Latar Belakang)
Sistem *Electrostatic Precipitator* (EP) pada cerobong Raw Mill Tuban 3 merupakan instalasi pengendalian pencemaran udara vital untuk menangkap partikulat debu sebelum gas buang dialirkan ke atmosfer. Pengawasan emisi partikulat harus mematuhi baku mutu lingkungan hidup dan memerlukan evaluasi analitik berkelanjutan terhadap parameter kelistrikan medan tinggi (tegangan TR, arus sekunder, dan laju alir gas).

### ?? Task (Tantangan & Sasaran)
Mengembangkan pipeline analitik data emisi dan parameter operasi EP berbasis Python untuk:
1. Mengotomasi penarikan data telemetri historis dari server SQL industri secara *read-only*.
2. Melakukan *data cleaning*, agregasi performa, dan identifikasi anomali spark/arcing pada transformator penyearah (TR set).
3. Menghasilkan laporan analitik Excel terstruktur yang selaras dengan kompetensi sertifikasi **BNSP Penanggung Jawab Operasional Instalasi Pengendalian Pencemaran Udara (PPPU)**.

### ?? Action (Arsitektur & Implementasi Teknis)
- **High-Performance Data Pipeline:** Menggunakan **DuckDB** dan **Pandas** untuk memproses jutaan baris data deret waktu (*time-series*) operasional EP dengan komputasi cepat di lingkungan laptop/mini PC.
- **Feature Engineering & Modeling:**
  - Evaluasi korelasi antara temperatur gas inlet, differential pressure, dan efisiensi penangkapan debu.
  - Deteksi penurunan voltase kV mendadak yang mengindikasikan akumulasi debu pada kawat elektroda (*emitting wire*).
- **Automated Reporting:** Modul `openpyxl` otomatis untuk menyusun rekapitulasi harian/bulanan kepatuhan emisi.

### ?? Result & Impact (Hasil & Metrik)
- **Compliance Assurance:** Menjamin operasional EP selalu terpantau dalam koridor baku mutu emisi debu yang ditetapkan KLHK.
- **Predictive Maintenance Input:** Memberikan rekomendasi jadwal pembersihan rapping hopper dan alignment elektroda sebelum terjadi *derating* performa.
