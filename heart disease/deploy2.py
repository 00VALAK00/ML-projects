import pickle
import streamlit as st
from streamlit_option_menu import option_menu
#loading the saved model (change to/ directory)
loaded_model_hd=pickle.load(open("C:/Users/USER/Desktop/python/heart disease/trained_model.sav","rb"))
loaded_model_db=pickle.load(open("C:/Users/USER/Desktop/python/Diabetes/diabetes2.sav","rb"))
loaded_model_bs=pickle.load(open("C:/Users/USER/Desktop/python/Brain stroke/brain_stroke.sav","rb"))


def  heart_disease_prediction(input_data):
    
    prediction=loaded_model_hd.predict(input_data)
    if prediction[0]==1:
     return("The person has a heart disease")
    else:
     return("the person does not have heart disease")    

def brain_stroke(input_data):
    prediction=loaded_model_bs.predict(input_data)
    if prediction[0]==1:
        return("the person is at risk from having a brain stroke")
    else:
        return("the person is not at risk of having a brain stroke ")    

def diabetes(input_data):
    prediction=loaded_model_db.predict(input_data)
    if prediction[0]==1:
        return("the person is diabetic")
    else:
        return("the person is not diabetic")

def test(l):
        for e in l:
            if str(e)=="" :
                return True
        return False


def main():
    #giving a title$
    st.sidebar.write(""" # the futur is here""")
    
    with st.sidebar:
     selected = option_menu("Multiple Disease prediction system", ["Diabetes prediction", 'Brain stroke prediction',"Heart disease prediction"],icons=["","","activity"])

    if selected == "Diabetes prediction" :
        st.title("Diabetes Prediction")
        col1,col2=st.columns(2)
        with col1:
         Pregnancies=st.text_input('Pregnancies')
         Glucose=st.text_input('Glucose')
         BloodPressure=st.text_input('BloodPressure')
         SkinThickness=st.text_input('SkinThickness')
        with col2:
         Insulin=st.text_input('Insulin')
         BMI=st.text_input('Body Mass Index')
         DiabetesPedigreeFunction=st.text_input('DiabetesPedigreeFunction')
         age=st.slider("Age", value=100)
        l1=[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,age]
        if st.button("Diabetes Prediction Result"):
            if test(l1):
                st.success("try again")
            else:
             diagnosis1=diabetes([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,age]])
             st.success(diagnosis1)

    elif selected=="Brain stroke prediction":
        st.title("Brain stroke prediction")
        col12,col22=st.columns(2)
        with col12:
          st.selectbox("gender",["women","man"])
          if selected=="women":
            gender=0
          else:
            gender=1  
          

          age=st.slider("Age", value=100)
          hypertension=st.text_input('hypertension')
          heart_disease=st.text_input('heart_disease')
        with col22:
         ever_married=st.text_input('ever_married')
         Residence_type=st.text_input('Residence_type')
         avg_glucose_level=st.text_input('avg_glucose_level')
         bmi=st.text_input('Body mass index')
         smoking_status=st.text_input('smoking_status')

        l2=[gender,age,hypertension,heart_disease,ever_married,Residence_type,avg_glucose_level,bmi,smoking_status]
        if st.button("Brain stroke Prediction Result"):
            if test(l2):
                diagnosis2="try again"
                st.success(diagnosis2)
            else:
                diagnosis2=brain_stroke([[gender,age,hypertension,heart_disease,ever_married,Residence_type,avg_glucose_level,bmi,smoking_status]])
                st.success(diagnosis2)


    
        
    else :
        st.title("Heart disease prediction")
        col111,col222,col333=st.columns(3)
        with col111:
         age=st.slider("Age", value=100)
         st.selectbox("gender",["women","man"])
         if selected=="women":
            gender=0
         else:
            gender=1  
         cp=st.text_input("CP (chest pain type)")
         trestbps=st.text_input("trestbps (resting blood pressure (in mm Hg))")
        with col222:
         chol=st.text_input("chol (serum cholestoral in mg/dl)")
         st.selectbox("fps (fasting blood sugar > 120 mg/dl)",["TRUE",'False'])
         if selected=='TRUE':
            fbs=1
         else:
            fbs=0  

         restecg=st.text_input("restecg (resting electrocardiographic results)")
         thalach=st.text_input("thalach (maximum heart rate achieved)")
        with col333:
         st.selectbox("exang ( exercise induced angina)",["TRUE",'False'])
         if selected=='TRUE':
             exang=1
         else:
            exang=0
         oldpeak=st.text_input("oldpeak (ST depression induced by exercise relative to rest)")
         slope=st.text_input("slope (the slope of the peak exercise ST segment)")
         ca=st.text_input("ca (number of major vessels)")
        thal=st.text_input("thal")
        l3=[age,gender,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
        if st.button("heart disease Result"):
          if test(l3):
            diagnosis3="try again"
            st.success(diagnosis3)

          else:
           diagnosis3=heart_disease_prediction([[age,gender,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
           st.success(diagnosis3)


               


if __name__ =='__main__':
        main()





