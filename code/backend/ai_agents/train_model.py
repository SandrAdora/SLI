import pickle 
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split  

#  load generated file 
data_dict = pickle.load(open('./data.pickle', 'rb'))



