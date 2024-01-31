
## Objectives

Project ini dibuat guna mengevaluasi konsep Computer Vision / Natural Language Processing dengan pemahaman sebagai berikut:

- Konsep Computer Vision/NLP.
- Mempersiapkan data untuk digunakan dalam model Computer Vision.
- Mampu mengimplementasikan Artificial Neural Network dengan data yang dipilih.
- Mampu menganalisis dan menjelaskan performansi dari arsitektur Artificial Neural Network yang dibuat.

---


### Data Sources

Dataset dipilih dari repository dibawah ini:

https://www.kaggle.com/datasets/pkdarabi/diagnosis-of-diabetic-retinopathy

---

## Instructions

Project dikerjakan dalam format *notebook* dan *model deployment* dengan beberapa *kriteria* di bawah ini:

1. Deep Learning framework yang digunakan adalah *TensorFlow*.

2. Ada penggunaan library visualisasi, seperti *matplotlib*, *seaborn*, atau yang lain.

3. Isi *notebook* harus mengikuti *outline* di bawah ini:
   1. Perkenalan
      > Bab pengenalan harus diisi dengan identitas, gambaran besar dataset yang digunakan, dan *objective* yang ingin dicapai.
   
   2. Import Libraries
      > *Cell* pertama pada *notebook* berisi dan hanya berisi semua *library* yang digunakan dalam *project*.
   
   3. Data Loading
      > Bagian ini berisi proses penyiapan data sebelum dilakukan eksplorasi data lebih lanjut. Proses Data Loading dapat berupa memberi nama baru untuk setiap kolom, mengecek ukuran dataset, dll.
   
   4. Exploratory Data Analysis (EDA)
      > Bagian ini berisi explorasi data pada dataset diatas dengan menggunakan query, grouping, visualisasi sederhana, dan lain sebagainya.

   5. Feature Engineering
      > Bagian ini berisi proses penyiapan data untuk proses pelatihan model, seperti pembagian data menjadi train-val-test, preprocessing, dan proses-proses lain yang dibutuhkan.   
   
   6. ANN Training (Sequential API, Functional API, dan Transfer Learning)
      
      vi.1. Model Definition
      > Bagian ini berisi cell untuk mendefinisikan model. Jelaskan alasan menggunakan suatu algoritma/model, hyperparameter yang dipakai, jenis penggunaan metrics yang dipakai, dan hal lain yang terkait dengan model.

      vi.2. Model Training
      > Cell pada bagian ini hanya berisi code untuk melatih model dan output yang dihasilkan. Lakukan beberapa kali proses training dengan hyperparameter yang berbeda untuk melihat hasil yang didapatkan. Analisis dan narasikan hasil ini pada bagian Model Evaluation.
   
      vi.3. Model Evaluation
      > Pada bagian ini, dilakukan evaluasi model yang harus menunjukkan bagaimana performa model berdasarkan metrics yang dipilih. Hal ini harus dibuktikan dengan visualisasi tren performa dan/atau tingkat kesalahan model. **Lakukan analisis secara detail terkait dengan hasil pada model dan tuliskan hasil analisisnya**.

   7. ANN Improvement (Sequential API, Functional API, dan Transfer Learning)
      
      vii.1. Model Definition
      > Bagian ini berisi cell untuk mendefinisikan model. Jelaskan alasan menggunakan suatu algoritma/model, hyperparameter yang dipakai, jenis penggunaan metrics yang dipakai, dan hal lain yang terkait dengan model.

      vii.2. Model Training
      > Cell pada bagian ini hanya berisi code untuk melatih model dan output yang dihasilkan. Lakukan beberapa kali proses training dengan hyperparameter yang berbeda untuk melihat hasil yang didapatkan. Analisis dan narasikan hasil ini pada bagian Model Evaluation.
   
      vii.3. Model Evaluation
      > Pada bagian ini, dilakukan evaluasi model yang harus menunjukkan bagaimana performa model berdasarkan metrics yang dipilih. Hal ini harus dibuktikan dengan visualisasi tren performa dan/atau tingkat kesalahan model. **Lakukan analisis secara detail terkait dengan hasil pada model dan tuliskan hasil analisisnya**.
   
   8. Model Saving
      > Pada bagian ini, dilakukan proses penyimpanan model dan file-file lain yang terkait dengan hasil proses pembuatan model. Pilihlah 1 arsitektur ANN yang terbaik berdasarkan hasil evaluasi sebelumnya. **Nyatakan secara jelas arsitektur mana yang akan dipakai sebagai model terbaik (Sequential API atau Functional API).**
   
   9. Model Inference
      > Model yang sudah dilatih akan dicoba pada data yang bukan termasuk ke dalam train-set, val-set, ataupun test-set. Data ini harus dalam format yang asli, bukan data yang sudah di-scaled. **Model Inference harus berada pada notebook yang berbeda dari notebook yang dipakai untuk pembuatan model.**
   
   10. Pengambilan Kesimpulan
       > Pada bagian terakhir ini, berisi kesimpulan yang mencerminkan hasil yang didapat dengan *objective* yang sudah ditulis di bagian pengenalan.

---