import streamlit as st
import joblib
import numpy as np

st.set_page_config(page_title='Heart Testing')
st.title("Test your Heart Condition!")

@st.cache(allow_output_mutation=True)
def get_model():
    return joblib.load('heart_knn_model.joblib')
cp=st.text_input("Have you ever feel chest pain? (Enter 1 = yes; 0 = no):","")
trestbps=st.text_input("Enter resting blood pressure in beat per second. (Normal BP in adults is 120/80 mm Hg.) :","")
chol=st.text_input("Enter serum cholestoral in mg/dl. (Optimal: less than 100 mg/ dL.):","")
fbs=st.text_input("Enter fasting blood sugar &gt; 120 mg/dl. (Enter 1 = true; 0 = false):","")
restecg=st.text_input("Enter resting electrocardiographic results. (Enter 0 = bad; 1 = Normal; 2 = Good):","")
thalach=st.text_input("Enter maximum heart rate achieved:","")
exang=st.text_input("Enter exercise induced angina (Enter 1 = yes; 0 = no):","")
if st.button("Check your Heart Condition"):
    values=[cp,trestbps,chol,fbs,restecg,thalach,exang]
    num_values=[]
    for x in values:
        num_values.append(float(x))
    
    #2 dimension
    num_values=np.asarray(num_values).reshape(1,-1)
    predictions=get_model().predict(num_values)
    predictions=int(predictions)
    img_happy='minions_yay.gif'
    img_sad='sorry.gif'
    if predictions==0:
        st.write("Yahh...You have NO Heart Diseases.") 
        st.image(img_happy,caption='Happy')
    elif predictions==1:
        st.write("I am so sorry! You have got Heart Diseases!")
        st.image(img_sad,caption='Sad')
    else:
        st.write("Please Enter posible data.")
   
