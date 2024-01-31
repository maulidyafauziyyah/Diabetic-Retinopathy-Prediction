
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
      > Bab ini berisi gambaran besar dataset yang digunakan.
   
   2. Import Libraries
      > *Cell* pertama pada *notebook* berisi semua *library* yang digunakan dalam *project*.
   
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
      > Cell pada bagian ini berisi code untuk melatih model dan output yang dihasilkan.  
   
      vi.3. Model Evaluation
      > Pada bagian ini, dilakukan evaluasi model yang menunjukkan bagaimana performa model berdasarkan metrics yang dipilih. Hal ini dibuktikan dengan visualisasi tren performa dan/atau tingkat kesalahan model.

   7. ANN Improvement (Sequential API, Functional API, dan Transfer Learning)
      
      vii.1. Model Definition
      > Bagian ini berisi cell untuk mendefinisikan model. 

      vii.2. Model Training
      > Cell pada bagian ini berisi code untuk melatih model dan output yang dihasilkan. 

      vii.3. Model Evaluation
      > Pada bagian ini, dilakukan evaluasi model yang menunjukkan bagaimana performa model berdasarkan metrics yang dipilih. 
   
   8. Model Saving
      > Pada bagian ini, dilakukan proses penyimpanan model dan file-file lain yang terkait dengan hasil proses pembuatan model. 
   
   9. Model Inference
      > Model yang sudah dilatih akan dicoba pada data yang bukan termasuk ke dalam train-set, val-set, ataupun test-set. 
   
   10. Pengambilan Kesimpulan
       > Pada bagian terakhir ini, berisi kesimpulan yang mencerminkan hasil yang didapat.

---