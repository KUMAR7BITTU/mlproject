# To predict for new data we will basically use predict pipeline .

# Now we have to create webapplication which will be interacting with pickle files like model.pkl and preprocessor.pkl with respect to any input data that we give .

# Let say in our webapplication we will be having one form where we will be giving all our input data that is required for predicting the student performance and then we will just click on submit .Internally , the backend will capture that data and that data needs to probably interact with this preprocessor.pkl and model.pkl . Then we will try to see how or whether we are able to get the prediction or not .

import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass
    
    # This predict() is just like model pipeline and it will basically do the prediction .
    def predict(self,features):
        try:
            model_path='artifacts\model.pkl'
            # This preprocessor is responsible for handling the categorical feature and doing the feature scaling , everything.
            preprocessor_path='artifacts\preprocessor.pkl'
            # This load_object function will just import the pickle and probably it will just load the pickle file .
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            #Transforming features
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        except Exception as e:
            raise CustomException(e,sys)
        
        
   
   
# CustomData class would be responsible for mapping all the inputs that we are giving in the html to the backend with this particular values .   
class CustomData:
    # gender,race_ethnicity,parental_level_of_education,lunch,test_preparation_course,reading_score,writing_score:- These are the features that we are specifically going to use .
    def __init__(self,gender:str,race_ethnicity:str,parental_level_of_education,lunch:str,test_preparation_course:str,reading_score:int,writing_score:int):
        # Then we will be creating varaibles by using self .
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education=parental_level_of_education
        self.lunch=lunch
        self.test_preparation_course=test_preparation_course
        self.reading_score=reading_score
        self.writing_score=writing_score
    
    # This function will return all our input in the form of dataframe .Because we train our model in the form of dataframe .
    def get_data_as_data_frame(self):
        try:
            #From our website the input that we are giving there will be mapped inside this custom_data_input_dict .
            custom_data_input_dict={
                "gender":[self.gender],
                "race_ethnicity":[self.race_ethnicity],"parental_level_of_education":[self.parental_level_of_education],"lunch":[self.lunch],"test_preparation_course":[self.test_preparation_course],"reading_score":[self.reading_score],"writing_score":[self.writing_score]
            }
            return pd.DataFrame(custom_data_input_dict)
        except Exception as e:
            raise CustomException(e,sys)
       
        
