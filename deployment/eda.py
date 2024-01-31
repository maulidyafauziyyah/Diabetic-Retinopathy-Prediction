import streamlit as st
from PIL import Image

def app():
    st.title('Exploration Data Analysis')

    
    st.subheader('Mengetahui Distribusi pada Data Training')
    image = Image.open('eda1.png')
    st.image(image, caption='figure 1')

    with st.expander('Notes'):
        st.caption('Distribusi pada Data Train adalah 1050 untuk DR (Diabetic Retinopathy) dan 1026 untuk No_DR (No Diabetic Retinopathy).')


    st.subheader('Mengetahui Distribusi pada Data Validasi')
    image = Image.open('eda2.png')
    st.image(image, caption='figure 2')

    with st.expander('Notes'):
        st.caption('Distribusi pada Data Validation adalah 245 untuk DR (Diabetic Retinopathy) dan 286 untuk No_DR (No Diabetic Retinopathy).')



    st.subheader('Perbandingan Diabetic Retinopathy dengan No Diabetic Retinopathy')
    image = Image.open('eda3.png')
    st.image(image, caption='figure 3')

    with st.expander('Notes'):
        st.caption('Terlihat perbedaan antara kondisi retina No Diabetic Retinopathy dan yang Diabetic Retinopathy. Pada penderita Diabetic Retinopathy menunjukkan tanda-tanda kerusakan retina seperti pendarahan, bercak, dan perubahan pembuluh darah, sedangkan 5 gambar dibawahnya tampak normal tanpa tanda-tanda tersebut.')

    