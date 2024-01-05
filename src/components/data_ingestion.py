# Here we will do train-test-split .

import os
import sys 
# We have to import our custom exception , therefore we have imported this .
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig
from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer

# Whenever we are performing the data ingestion component, there should be some inputs that may be probably required by this data ingestion component .The input can be like where i have to probably save the training path or train data ,where i have to probably save the test data , where i have to probably save the raw data . So, those kind of inputs we will be basically creating in another class and that class is known as DataIngestionConfig .


# The reason we are making this dataingestionconfig is in my dataingestion component any input that is required , i will probably give through this dataingestionconfig .


# input of dataingestinconfig .
@dataclass # decorator
class DataIngestionConfig:
    # we have used decorator because inside a class to define the class variable you basically use init but if you use this dataclass then you will be able to directly define your class variable .
    
    # all the output of data ingestion will be stored inside artifact folder in train.csv file . train_data_path will be str type .
    train_data_path: str = os.path.join('artifacts',"train.csv")
    test_data_path: str = os.path.join('artifacts',"test.csv")
    raw_data_path: str = os.path.join('artifacts',"data.csv")
    
    # The above mentioned paths are inputs that we are giving to Data Ingestion Component and now Data Ingestion Component knows where to save the train path, test path and data path .
    
# if we only define variable in class then we should use dataclass . But if we are defining function inside class then we should use init constructor part .   

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
        # This ingestion_config will consist of three value train_data_path, test_data_path, raw_data_path .
    
    # If our data is stored in some database , so by using this function we can read the data from that database .   
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv('notebook\data\stud.csv')
            logging.info("Read the dataset as dataframe")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            # exist_ok basically tells us if that already exist keep it as it is .
            
            # we can also save raw data path .
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            logging.info("Train test split initiated")
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)
            
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info("Ingestion of the data is completed")
            
            return(
                self.ingestion_config.train_data_path,self.ingestion_config.test_data_path
            )
            # we will return this two because our next step which is data transformation will be able to grab this information . So, data transformation which is the next step will be able to grab this information and take all these data points and start the process .
        except Exception as e:
            raise CustomException(e,sys)
        
# Now quickly initiate this and run this .
if __name__=="__main__":
    obj = DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()
    # obj = DataIngestion()
    # obj.initiate_data_ingestion() 
    
    data_transformation=DataTransformation()   
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)   
    
    modeltrainer = ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))