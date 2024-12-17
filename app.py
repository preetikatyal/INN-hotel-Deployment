
import streamlit as st
import numpy as np
import pandas as pd
import pickle 

with open ('final_model_xgb.pkl','rb') as file:
    model = pickle.load(file)

with open ('transformer.pkl','rb') as file:
    pt = pickle.load(file)

def prediction(input_list):
    
    tran_data= pt.transform([[input_list[0],input_list[3]]])
    input_list[0]=tran_data[0][0]
    input_list[3]=tran_data[0][1]
    input_list = np.array(input_list,dtype=object)
    pred= model.predict_proba([input_list])[:,1][0]

    if pred>0.5:
        return f'This booking is more likely to get canceled: chances {round(pred,2)}'
    else:
        return f'This is less likely to get canceled : chances {round(pred,2)}'

def main():
    st.title('INN HOTEL GROUP')
    lt= st.text_input('Enter the lead time.')
    mst= (lambda x: 1 if x=='Online' else 0)(st.selectbox('Enter the type of booking',['Online','Offline']))
    spcl=st.selectbox('Select the no of special requests made',[1,2,3,4,5])
    price= st.text_input('Enter the price offered for the room')
    adults= st.selectbox('Select the no of adults in booking',[0,1,2,3,4])
    wkend= st.text_input('Enter the weekend nights in the booking')
    wk= st.text_input('Enter the week nights in the booking')
    park= (lambda x:1 if x=='Yes' else 0)(st.selectbox('Is parking included in the booking',['Yes','No']))
   
    

    inp_list=[lt_t,mst,spcl,price_t,adults,wkend,park,wk]

    if st.button('Predict'):
        response= prediction(inp_list)
        st.success(response)

if __name__=='__main__':
    main()
