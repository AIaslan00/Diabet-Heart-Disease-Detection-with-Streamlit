import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# Kaydedilen modelleri yükleme

heart_model=pickle.load(open('C:/Users/Aslan/OneDrive/Masaüstü/Multiple Disease/saved model/heart_disease_model3.sav','rb'))
parkinson_model=pickle.load(open('C:/Users/Aslan/OneDrive/Masaüstü/Multiple Disease/saved model/parkinsons_model2.sav','rb'))


# Sidebar Ayarlama

with st.sidebar:
    selected = option_menu('Çoklu Hastalık Tahmin Sistemi', ['Heart Disease Prediction','Parkinson Prediction'],
                           icons=['heart','activity'],default_index=0)
    

# Heart Prediction Sayfası
if(selected == 'Heart Disease Prediction'):
    st.title(' Kalp Hastalığı Tahmin Uygulaması')
    
    col1,col2=st.columns(2)
    with col1:
        age=st.text_input('Yaş:')
    with col2:    
        sex=st.text_input('Cinsiyet:')
    with col1:
        cp=st.text_input('Göğüs Ağrısı Tipi:')
    with col2:
        trestbps=st.text_input('Dinlenme Kan Basıncı:')
    with col1:
        chol=st.text_input('Serum Kolestrolü:')
    with col2:
        fbs=st.text_input('Kan şekeri:')
    with col1:
        restecg=st.text_input('Elektrokardiyografik Sonuçları:')
    with col2:
        thalach=st.text_input('Maksimum kalp atış hızı:')
    with col1:
        exang=st.text_input('Egzersize bağlı anjina:')
    with col2:
        oldpeak=st.text_input('ST Depresyonu:')
    with col1:
        slope=st.text_input('ST Segmentinin Eğimi:')
    with col2:
        ca=st.text_input('Renklendirilen damar sayısı:')
    with col1:
        thal=st.text_input('3:Normal-6:sabit-7:Geri Dönderilebilir')
     

     
    heart_diagnosis = ''
    
    # Predict butonu
    if st.button('Heart Test Results'):
        # Girdileri doğru türe dönüştürme
        try:
            age = int(age)
            sex = int(sex)
            cp = int(cp)
            trestbps = float(trestbps)
            chol = float(chol)
            fbs = int(fbs)
            restecg = int(restecg)
            thalach = float(thalach)
            exang = int(exang)
            oldpeak = float(oldpeak)
            slope = int(slope)
            ca = int(ca)
            thal = int(thal)
            
            # Tahmin işlemi
            heart_prediction = heart_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
            
            if heart_prediction[0] == 1:
                heart_diagnosis = 'Bu kişi Kalp Hastasıdır.'
            else:
                heart_diagnosis = 'Bu kişi Kalp Hastası Değildir.'
            
        except ValueError as e:
            st.error(f'Value Error: {e}')
        except Exception as e:
            st.error(f'An error occurred: {e}')
    
    # Sonucu göster
    st.success(heart_diagnosis)

    
if(selected == 'Parkinson Prediction'):
    st.title(' Parkinson Tahmin Uygulaması')
    
    col1,col2,col3,col4=st.columns(4)
    with col1:
        fo=st.text_input("Temel frekans ölçümü (Hz)")
    with col2:
        fhi=st.text_input(" Temel frekansın yüksekliği (Hz)")
    with col3:
        flo=st.text_input(" Temel frekansın düşüklüğü (Hz)")
    with col4:
        jitter=st.text_input(" Titreme miktarı (%)")
    with col1:
        jitter_abs=st.text_input(" Titreme miktarının mutlak değeri")
    with col2:
        RAP=st.text_input("Titreme oranı")
    with col3:
        PPQ=st.text_input(" Titreme ölçümünün periyodik bileşeni ")
    with col4:
        DDP= st.text_input(" Titreme miktarının süreksizliği ")
    with col1:
        Shim= st.text_input(" Parıltı ölçümü")
    with col2:
        DB= st.text_input(" Parıltı ölçümünün desibel değeri")
    with col3:
        APQ3=st.text_input(" Parıltı ölçümünün APQ3 bileşeni")
    with col4:
        APQ5=st.text_input(" Parıltı ölçümünün APQ5 bileşeni")
    with col1:
        MDVP=st.text_input(" MDVP ölçümünün APQ bileşeni")
    with col2:
        DDA=st.text_input("Parıltı ölçümünün DDA bileşeni")
    with col3:
        NHR=st.text_input(" Gürültü oranı")
    with col4:
        HNR=st.text_input(" Harmonik-gürültü oranı")
    with col1:
        RPDE=st.text_input(" Nonlinear özellik, rekürsif birleşim oranı")
    with col2:
        DFA=st.text_input(" Nonlinear özellik, dairesel zaman değişkenliği")
    with col3:
        spread1=st.text_input(" Genlik varyansı")
    with col4:
        spread2=st.text_input(" spektral varyans")
    with col1:
        D2=st.text_input(" Kompaktlık ölçüsü")
    with col2:
        PPE=st.text_input(" Parıltı oranı değişimi")
    #Tahmin codu
    parkinson_diagnosis=''
    
    if st.button('Parkinson Test Results'):
        parkinson_prediction=parkinson_model.predict([[fo,fhi,flo,jitter,jitter_abs,RAP,PPQ,DDP,Shim,DB,APQ3,APQ5,MDVP,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])
        
        if(parkinson_prediction[0]==1):
            parkinson_diagnosis='Bu kişi Parkinson Hastasıdır.'
        else:
            parkinson_diagnosis='Bu kişi Parkinson Hastası Değildir.'
    
    st.success(parkinson_diagnosis)