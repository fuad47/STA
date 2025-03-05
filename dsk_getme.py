import streamlit as st
import pandas as pd
from io import StringIO

def cleaner(uploaded_file,year,month):
    # data_raw=pd.read_excel(r'C:\Users\fuad.ak\Documents\getme fev 2025.xlsx', sheet_name=3,header=[1])#.rename(columns={'Unnamed: 0':'No'})
    data_raw=uploaded_file
    data_raw.drop(columns='Unnamed: 1',inplace=True)
    # data_raw.rename(columns={'Unnamed: 0':'Ölkələr',},inplace=True)
    data_raw.columns=data_raw.iloc[1]
    data_raw.rename(columns={'Cəmi':'3. Quru'},inplace=True)
    data_raw = data_raw.drop(index=[0, 1,2, 3])
    data_raw.drop(index=data_raw.index[-1]) # drop last column

    data_raw.columns.values[0]="Ölkələr"
    data_raw.columns.values[15]="Hava"
    data_raw.columns.values[16]="Su"

    data_raw.rename(columns={'Kişi': '1. Kişi','Qadın': '2. Qadın','18 yaşadək': '1. 18 yaşadək','18-35 yaş':'2. 18-35 yaş','36-65 yaş': '3. 36-65 yaş','66 yaş və yuxarı':'4. 66 yaş və yuxarı','24 saatadək':'1. 24 saatadək','1-3 sutka': '2. 1-3 sutka', '4-7 sutka': '3. 4-7 sutka','8-14 sutka':'4. 8-14 sutka','15-21 sutka':'5. 15-21 sutka','22-28 sutka':'6. 22-28 sutka','29-70 sutka':'7. 29-70 sutka','Hesabat dövründə gedən, lakin qayıtma¬yan-ların sayı':'8. Hesabat dövründə gələn, lakin ölkəni  tərk etməyənlərin sayı','Hava':'1. Hava','Su': '2. Su','Quru': '3. Quru','Ondan şəxsi avtomobil': '3.1 Ondan şəxsi avtomobil'}, inplace=True)
    arrays =[['']+2*['Cins tərkibi üzrə']+4*['Yaş qrupları üzrə']+8*['Səfərin müddəti üzrə']+4*['İstifadə edilən nəqliyyat növü üzrə'], data_raw.columns]
    data_raw.columns=pd.MultiIndex.from_arrays(arrays, names=(['indikator','subindikator']))

    st.write('Cins tərkibi üzrə:',data_raw['Cins tərkibi üzrə'].sum().sum())
    st.write('Yaş qrupları üzrə:', data_raw['Yaş qrupları üzrə'].sum().sum())
    st.write('Səfərin müddəti üzrə: ',data_raw['Səfərin müddəti üzrə'].sum().sum())

    data=data_raw.set_index(data_raw.columns[0]).melt( value_name="Göstərici",ignore_index=False) # var_name=["indikator","subindikator"],
    data['il']=int(year)
    data['month_id']=int(month)
    data['tarix']=f'{year}-0{month}-01'
    data.index.name='Ölkələr'

    return data


st.subheader('DSK fayl transformeri')
st.write('Getme melumatlari olan excel faylını bura atın və çıxan nəticəni endirin.')
uploaded_file = st.file_uploader("Hesabat sənədini yükləyin")
sheet=
date=st.date_input('Hesabat tarixini seçin')
year=date.year
month=date.month
sheet=st.number_input('Sheet no:',value=0)
if uploaded_file is not None:
    # Can be used wherever a "file-like" object is accepted:
    data_raw = pd.read_excel(uploaded_file,sheet_name=sheet,header=[1])
    st.subheader("Uploaded Table:")
    st.write(data_raw)
    st.divider()
    st.subheader("Transformed Table:")
    transformed_data=cleaner(data_raw, year, month)

    
    st.write(transformed_data.head())
    # st.dataframe(transformed_data.head())

    

# data_raw=pd.read_excel(r'C:\Users\fuad.ak\Documents\getme fev 2025.xlsx', sheet_name=3, header=[1])

    
