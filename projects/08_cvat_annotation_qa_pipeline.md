# ??? Independent CVAT & Computer Vision Annotation QA Pipeline

> **Kategori:** AI Data Quality & QA / Computer Vision Annotation Engineering  
> **Status:** Production Completed  
> **Tech Stack:** CVAT (Docker Self-Hosted), YOLOv7 ONNX, Nuclio Serverless, Python, Precision/Recall/F1 Evaluation  
> **Repository:** [Independent Production Project / Pandujatip](https://github.com/Pandujatip)

---

## ?? Project Overview & STAR Case Study

### ?? Situation (Latar Belakang)
Kualitas dataset adalah penentu utama akurasi model Computer Vision di industri. Pelabelan manual rentan terhadap *label noise* (kotak terlalu longgar, label tertukar, objek terpotong/terlewat), sementara anotasi ribuan citra membutuhkan waktu lama jika dikerjakan secara manual dari nol tanpa bantuan *pre-annotation*.

### ?? Task (Tantangan & Sasaran)
Merancang dan mengoperasikan pipeline anotasi computer vision mandiri yang efisien dan terstandarisasi untuk:
1. Melakukan *self-hosting* platform anotasi CVAT menggunakan Docker container.
2. Mengintegrasikan fungsi *auto-annotation* berbasis serverless Nuclio menggunakan model YOLOv7 ONNX.
3. Melakukan kurasi data, perancangan taksonomi K3 (pekerja, helm, rompi, sepatu safety), serta penjaminan mutu (*Quality Assurance*) berbasis metrik statistik ketat.

### ?? Action (Arsitektur & Implementasi Teknis)
- **Docker CVAT & Nuclio Deployment:** Mengonfigurasi lingkungan CVAT lengkap dengan database Postgres, Redis, dan microservice Nuclio di atas Docker.
- **Automated Pre-Annotation:** Menghubungkan bobot YOLOv7 ONNX ke dalam Nuclio untuk mendeteksi *bounding box* awal secara otomatis, mempercepat kecepatan pelabelan hingga 3.5x.
- **Rigorous Taxonomy & Error Auditing:**
  - Mengklasifikasikan error ke dalam 5 kategori terstruktur: *Missing*, *Duplicate*, *Misclassified*, *Loose Bounding Box*, dan *Truncated*.
  - Mengevaluasi prediksi model dan label manusia pada ambang batas Intersection over Union ($\text{IoU} \ge 0.50$) dengan metrik Precision, Recall, dan F1-Score.

### ?? Result & Impact (Hasil & Metrik)
- **Peningkatan Throughput Anotasi:** Mengurangi waktu pelabelan per citra dari rata-rata 45 detik menjadi 12 detik berkat pipeline *Nuclio auto-annotation*.
- **High Data Fidelity:** Mencapai konsistensi taksonomi $> 98\%$ pada dataset K3 industri dengan audit sampling terukur.
