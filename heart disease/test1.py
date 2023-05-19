import numpy as np
#pandas creating data frames =structured table
import pandas as pd
#split data into testing and training data 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
#evaluate model"s performance
from sklearn.metrics import accuracy_score
#data collection


data=pd.read_csv("Nouveau dossier\heart_disease_data.csv")

print (data)


