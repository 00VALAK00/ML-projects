l=["gender","age","hypertension","heart_disease","ever_married","Residence_type","avg_glucose_level","bmi","smoking_status"]
for e in l:
  a= "{}=st.text_input('{}')"
  print (a.format(e,e))
