import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.write('Burak')

uploaded_file = st.file_uploader("Choose a file")

flag=0
if uploaded_file is not None:
    flag=1
if flag == 1:
    bytes_data = uploaded_file.getvalue()
    df = pd.read_csv(uploaded_file)
else :
    df = sns.load_dataset('iris')

if 1==1:
    #if st.button('Dataset yüklendi görselleştirmeye başlamak için tıklayın'):
        
    option = st.multiselect('Hangi kolonların görselleştirilmesini istiyorsunuz?',(df.columns.to_list()))

    
    
    #df = pd.read_csv("/home/berfin_sarioglu/files/df_frekans_app.csv")
    #a= df.columns.to_list()
    #df[a] = df[a].apply(pd.to_numeric,errors='ignore', axis=1)
    if st.button('Görselleştirmeye başlamak için tıklayın'):
        
        
        
         def grafik_cizici(i):   
            
            if df[i].dtypes == 'float64'  or df[i].dtypes == 'int64':
                st.write('-------------- SAYISAL VERİ --------------')
                fig = plt.figure(figsize=(10, 4))
                sns.histplot(data=df, x=i)
                st.pyplot(fig)
        
            if  len(df[i].unique()) < 30 and df[i].dtype == 'object':
                st.write('-------------- KATEGORİK VERİ --------------')
                #print(df[i].value_counts())
                #df.groupby([i])[i].count().plot(kind="bar")
                fig = plt.figure(figsize=(10, 4))
                #ax=plt.subplots(figsize=(10,6))
                sns.countplot(data=df, x=i,order = df[i].value_counts().index)

                #sns.barplot(data=df[i], x=i, kind="count")
                st.pyplot(fig)
            elif len(df[i].unique()) > 30 and df[i].dtype == 'object':
                st.write(i, 'adlı kolonlar çok fazla unique değere sahip olduğu için çizilmemesi önerildi.')
                


        
         for i in option:
             grafik_cizici(i)
            
        
        
        
        
