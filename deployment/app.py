import streamlit as st
import eda
import prediction

PAGES = {
    "Exploration Data Analysis": eda,
    "Prediction": prediction
}

page = st.sidebar.selectbox(label='Select Page:', options=['Home Page', 'Exploration Data Analysis', 'Prediction'])

if page == 'Home Page':

    with st.columns(3)[1]:
        st.header('Welcome Page')
        st.image('https://www.drchelvinsng.com/wp-content/uploads/2021/12/Diabetic-Retinopathy1.jpg')
    st.write('')
    st.header('Diabetic Retinopathy Prediction')
    st.write('Tujuan    : Memprediksi Diabetic Retinopathy Menggunakan konsep Computer Vision')
    st.write('')

    with st.expander("Latar Belakang"):
        st.caption('Prediksi Diabetic Retinopathy dibuat untuk membantu dalam diagnosis awal dalam melihat apakah pasien menderita Diabetic Retinopathy atau tidak.')
        st.caption('Dengan menggunakan model ini, dokter dapat memprediksi pasien yang menderita Diabetic Retinopathy untuk mengurangi risiko kecenderungan yang dapat mempengaruhi diagnosis.')

    with st.expander("Kesimpulan"):
        st.caption('''
    
    - Dataset "Diagnosis of Diabetic Retinopathy" terbagi menjadi 3 set data yaitu 'train', 'valid', dan 'test'.

    - Masing-masing set data 'train', 'valid', dan 'test' memiliki 2 kelas yaitu kelas 'DR' dan 'No_DR'. Selanjutnya kelas 'DR' diganti menjadi 0 dan 'No_DR' menjadi 1.
                   
    - Ada 3 model yang dilakukan training dan evaluasi, yaitu model Sequential, model Functional, dan model Xception.
                       
    - Hasil evaluasi model pada Model Sequential menunjukkan kinerja yang paling seimbang dengan test loss yang rendah dan test precision yang tinggi, sementara Model Functional menunjukkan kinerja yang kurang dengan test loss yang tinggi dan test precision yang rendah, dan Model Xception memiliki test precision yang hampir setara dengan Sequential tetapi dengan test loss yang sedikit lebih rendah.
                   
    - Berdasarkan classification report, model Sequential memiliki nilai precision yang seimbang di kedua kelas, Model Functional unggul dalam nilai precision kelas DR tetapi lebih rendah untuk No_DR, sementara Model Xception menunjukkan nilai precision tinggi untuk DR namun dengan nilai precision yang sedikit lebih rendah untuk No_DR.
    
    - Model sequential dipilih karena menunjukkan kinerja yang stabil dan akurat dengan keseimbangan terbaik antara True Positive dan True Negative serta indikasi generalisasi yang baik dalam memprediksi Diabetic Retinopathy.''')

    st.caption('Untuk memulai, silakan pilih menu lain pada Select Box di sebelah kiri layar Anda')
    st.write('')
    st.write('')


elif page == 'Exploration Data Analysis':
    eda.app()
else:
    prediction.app()


