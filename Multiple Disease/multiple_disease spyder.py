import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# Kaydedilen modelleri yükleme

heart_model=pickle.load(open('C:/Users/Aslan/OneDrive/Masaüstü/Multiple Disease/saved model/heart_disease_model.sav','rb'))
parkinson_model=pickle.load(open('C:/Users/Aslan/OneDrive/Masaüstü/Multiple Disease/saved model/parkinsons_model.sav','rb'))


# Sidebar

with st.sidebar:
    selected = option_menu('Çoklu Hastalık Tahmin Sistemi', ['Heart Disease Prediction','Parkinson Prediction'],
                           icons=['heart','activity'],default_index=0)
    

# Heart Prediction Sayfası
if(selected == 'Heart Disease Prediction'):
    st.title(' Kalp Hastalığı Tahmin Uygulaması')
    

    age=st.text_input('Yaş:')
    sex=st.text_input('Cinsiyet:')
    cp=st.text_input('Göğüs Ağrısı Tipi:')
    tretbps=st.text_input('Dinlenme Kan Basıncı:')
    chol=st.text_input('Serum Kolestrolü:')
    fbs=st.text_input('Kan şekeri:')
    restecg=st.text_input('Elektrokardiyografik Sonuçları:')
    thalach=st.text_input('Maksimum kalp atış hızı:')
    exang=st.text_input('Egzersize bağlı anjina:')
    oldpeak=st.text_input('ST Depresyonu:')
    slope=st.text_input('ST Segmentinin Eğimi:')
    ca=st.text_input('Renklendirilen damar sayısı:')
    tal=st.text_input('3:Normal-6:sabit-7:Geri Dönderilebilir')
     
    #Tahmin codu
    heart_diagnosis=''
    
    if st.button('Heart Test Results'):
        heart_prediction=heart_model.predict([[age,sex,cp,tretbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,tal,target]])
        
        if(heart_prediction[0]==1):
            heart_diagnosis='Bu kişi Kalp Hastasıdır.'
        else:
            heart_diagnosis='Bu kişi Kalp Hastası Değildir.'
    
    st.success(heart_diagnosis)

    
    
    
if(selected == 'Parkinson Prediction'):
    st.title(' Parkinson Tahmin Uygulaması')