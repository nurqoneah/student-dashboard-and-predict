# Proyek Akhir: Mengatasi Permasalahan Dropout di Jaya Jaya Institut

## Business Understanding

Jaya Jaya Institut adalah institusi pendidikan tinggi yang telah beroperasi sejak tahun 2000 dan telah menghasilkan banyak lulusan dengan reputasi baik. Namun, institusi ini menghadapi tantangan signifikan terkait tingginya angka dropout di kalangan mahasiswa.

Tingginya angka dropout dapat berdampak negatif bagi institusi, baik dari segi finansial maupun reputasi. Oleh karena itu, Jaya Jaya Institut berupaya untuk mendeteksi mahasiswa yang berisiko tinggi mengalami dropout agar mereka bisa mendapatkan dukungan yang dibutuhkan.

### Permasalahan Bisnis

1. Tingginya angka dropout yang mengakibatkan kerugian finansial bagi institut.
2. Kesulitan dalam mengidentifikasi faktor-faktor penyebab mahasiswa meninggalkan program studi.
3. Keterbatasan dalam pengambilan keputusan berbasis data terkait manajemen akademik.

### Cakupan Proyek

Proyek ini bertujuan untuk:

- Mengembangkan model prediksi dropout menggunakan data mahasiswa yang ada.
- Menganalisis faktor-faktor yang mempengaruhi dropout melalui analisis data.
- Membangun dashboard interaktif untuk visualisasi data yang membantu pengambilan keputusan.

### Persiapan

**Sumber Data:** Data mahasiswa diambil dari [Dataset Student](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv).

**Setup Environment:**

```bash
# Install libraries
pip install -r requirements.txt
```

## Business Dashboard

Business dashboard telah dibuat menggunakan Metabase (Student Dashboard) untuk memvisualisasikan data mahasiswa dan memprediksi kemungkinan dropout. Dashboard ini mencakup informasi penting tentang status akademik, pembayaran uang kuliah, dan performa mahasiswa di berbagai unit kurikulum.

- **Email:** nurulqoniah313@gmail.com
- **Password:** dicoding12

**1. Total Mahasiswa**

- **Jumlah Total Mahasiswa:** **4,424**
  - Gambaran jumlah total mahasiswa yang terdaftar di Jaya Jaya Institut.

**2. Status Pembayaran Uang Kuliah**

- **Persentase Mahasiswa dengan Pembayaran Tepat Waktu:** **88.07%**
  - Mayoritas mahasiswa membayar uang kuliah tepat waktu, namun ada sekitar 12% yang tidak up to date, yang berpotensi menjadi faktor risiko dropout.

**3. Tingkat Kelulusan**

- **Tingkat Kelulusan:** **49.93%**
  - Persentase mahasiswa yang telah menyelesaikan studinya. Dengan hampir setengah populasi lulus, ini memberikan indikasi tentang keberhasilan akademik.

**4. Tingkat Dropout**

- **Tingkat Dropout:** **32.12%**
  - Satu dari tiga mahasiswa mengalami dropout, yang menjadi masalah serius dalam keberlangsungan akademik institut.

**5. Rata-rata Nilai di Unit Kurikulum**

- **Rata-rata Nilai:** **10.64**
  - Nilai rata-rata di seluruh unit kurikulum menunjukkan performa akademik mahasiswa yang bisa menjadi indikasi prediksi dropout. Nilai di bawah standar dapat meningkatkan risiko dropout.

**6. Rata-rata Usia Saat Pendaftaran**

- **Rata-rata Usia:** **23.27 tahun**
  - Data ini menggambarkan usia rata-rata mahasiswa saat mereka memulai program studi, yang bisa menjadi indikator penting dalam memahami karakteristik populasi mahasiswa.

**7. Rata-rata Nilai Penerimaan**

- **Rata-rata Nilai Penerimaan:** **126.98**
  - Nilai penerimaan mahasiswa menunjukkan kualitas akademik yang dimiliki saat masuk, yang bisa menjadi prediktor performa akademik di masa depan.

---

### **Visualisasi dan Insight Penting**

**8. Distribusi Program Studi**

- **Insight:** Menunjukkan distribusi mahasiswa berdasarkan program studi. Hal ini memberikan pandangan tentang program mana yang paling diminati atau memiliki risiko dropout yang lebih tinggi.
- **Analisis:** Program studi dengan mahasiswa lebih sedikit perlu mendapat perhatian untuk meningkatkan retensi, terutama jika dropout rate tinggi.

**9. Kinerja Unit Kurikulum**

- **Insight:** Grafik ini menunjukkan kinerja mahasiswa di setiap unit kurikulum, dengan rata-rata nilai di berbagai semester.
- **Analisis:** Unit kurikulum dengan nilai rata-rata lebih rendah bisa menjadi indikator dimana mahasiswa berjuang, dan mungkin memerlukan intervensi tambahan seperti tutoring atau bimbingan khusus.

**10. Wawasan Demografis**

- **Insight Gender:** Menunjukkan distribusi mahasiswa berdasarkan gender.
- **Insight Usia Pendaftaran:** Menggambarkan distribusi usia saat pendaftaran.
- **Analisis:** Institusi dapat mempertimbangkan program intervensi berdasarkan usia, misalnya memberikan dukungan tambahan bagi mahasiswa yang lebih tua yang mungkin lebih berisiko mengalami dropout.

**11. Dampak Mode Aplikasi**

- **Insight:** Mode aplikasi yang digunakan untuk mendaftar ke institut mungkin mempengaruhi tingkat kelulusan dan dropout.
- **Analisis:** Beberapa mode aplikasi mungkin lebih efektif dalam memfasilitasi kesuksesan mahasiswa, dan pihak manajemen dapat menyesuaikan strategi penerimaan untuk meningkatkan kelulusan.

**12. Faktor Keuangan**

- **Insight:** Status pembayaran uang kuliah yang tidak up to date seringkali berhubungan langsung dengan risiko dropout.
- **Analisis:** Intervensi keuangan seperti beasiswa atau penundaan pembayaran bisa membantu mengurangi dropout.

**13. Distribusi Status Mahasiswa**

- **Insight:** Menunjukkan status mahasiswa apakah mereka sudah lulus, masih terdaftar, atau dropout.
- **Analisis:** Dengan dropout rate **32.1%**, fokus utama harus pada memberikan dukungan kepada mahasiswa yang masih terdaftar agar mereka tidak keluar.

**14. Tingkat Pendidikan Orang Tua**

- **Insight:** Visualisasi ini menunjukkan tingkat pendidikan orang tua mahasiswa, baik ayah maupun ibu.
- **Analisis:** Orang tua dengan pendidikan lebih tinggi mungkin lebih mampu memberikan dukungan akademik, sementara mahasiswa dengan orang tua berpendidikan lebih rendah mungkin memerlukan dukungan tambahan dari institut.

## Menjalankan Sistem Machine Learning

Jalankan app.py dengan run code ini di terminal

```bash
# run app/py
streamlit run app.py
```

atau untuk akses ke model prediksi, silakan kunjungi [link ini](https://nurqoneah-student-dashboard-and-predict-app-ilqf2i.streamlit.app/).

## Conclusion

Proyek ini berhasil mengidentifikasi faktor-faktor utama yang mempengaruhi dropout di Jaya Jaya Institut. Dengan menggunakan model Logistic Regression, RF, dan SVM, institusi dapat memprediksi mahasiswa mana yang berisiko tinggi untuk mengalami dropout. Model SVM mendapatkan validasi akurasi tertinggi 76.99%, sehingga dipilih untuk memprediksi mahasiswa berisiko.

### Faktor-Faktor yang Mempengaruhi Dropout

1. **Status Pembayaran Uang Kuliah (Tuition Fees Up to Date):**

   - Mahasiswa yang membayar uang kuliah tepat waktu cenderung memiliki peluang lebih besar untuk tetap terdaftar.

2. **Unit Kurikulum yang Disetujui pada Semester Kedua (Curricular Units 2nd Sem Approved):**
   - Persetujuan untuk unit kurikulum pada semester kedua menunjukkan kemajuan akademik yang baik.

### Rekomendasi Action Items

- **Fokus pada Mahasiswa yang Tidak Menerima Beasiswa:** Menawarkan program beasiswa yang lebih luas.
- **Tingkatkan Kesejahteraan Mahasiswa:** Program yang mendukung keseimbangan kehidupan akademik.
- **Monitor Mahasiswa Baru:** Memberikan perhatian ekstra pada mahasiswa yang baru bergabung.
