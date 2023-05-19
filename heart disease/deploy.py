import numpy as np
import pickle

#loading the saved model (change to/ directory)
loaded_model=pickle.load(open("C:/Users/USER/Desktop/python/Nouveau dossier/trained_model.sav","rb"))
loaded_model_db=pickle.load(open("C:/Users/USER/Desktop/python/Diabetes/diabetes2.sav","rb"))





input_data=[[8,1,0,100,234,0,1,156,0,0.1,2,1,3]]

#build a predicition 
prediction=loaded_model.predict(input_data)
print(prediction)
if prediction[0]==1:
    print("the person has heart disease")
else:
    print("the person does not have heart disease")    
