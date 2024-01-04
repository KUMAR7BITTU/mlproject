# The main purpose of data transformation is to do feature engineering and data cleaning .

import sys
from dataclasses import dataclass
import numpy as np 
import pandas as pd 
from sklearn.compose import ColumnTransformer
# If we have some missing values then we will use imputer and we will import it from sklearn.imputer .
from sklearn.impute import SimpleImputer 
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

from src.exception import CustomException
from src.logger import logging
import os
from src.utils import save_object

# Data transformation config will provide all the inputs that are required for data transformation components .
@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts',"preprocessor.pkl")
    # Suppose we want to create any model and we want to save it in any pickle file , so for that we require any one kind of path .

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()
    
    # we are creating below mentioned function to create all our pickle files which wiil be basically responsible into converting our categorical features into numerical features or we want to perform standardscaller and all .
    def get_data_transformer_object(self):
        '''
        This function is responsible for data transformation based on different types of data .
        '''
        try:
            numerical_columns=["writing_score","reading_score"]
            categorical_columns=["gender","race_ethnicity","parental_level_of_education","lunch","test_preparation_course"]
            
            # Then we will create pipeline . Imputer responsible for handling missing values .
            num_pipeline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="median")),("scaler",StandardScaler(with_mean=False))]
                  
                # Here in strategy we use median because there are some outliers that we saw in EDA .
            )
            # So, inshort we have create a pipeline which is doing two things:- 1, handling missing values    2, doing StandardScaler. This pipeline is to run on training dataset . Like fit_transform on training dataset and we just do transform on test dataset .
            
            #cat_pipeline will handle missing values and will also be responsible for converting categorical features into numerical features .
            cat_pipeline=Pipeline(
                steps=[("imputer",SimpleImputer(strategy="most_frequent")),("one_hot_encoder",OneHotEncoder()),("scaler",StandardScaler(with_mean=False))]
                # strategy = most frequent means we are going to replace our missing with mode .
            )
            logging.info(f"Categorical columns: {categorical_columns}")
            logging.info(f"Numerical columns: {numerical_columns}")
            
            # Next combine numerical pipeline and categorical pipeline . And for that only we will use column transformer .
            
            preprocessor = ColumnTransformer([
                ("num_pipeline",num_pipeline,numerical_columns),("cat_pipeline",cat_pipeline,categorical_columns)
            ])
            # first give pipeline name then give what pipeline it is then on which column you want to give that pipeline .
            
            return preprocessor
        except Exception as e:
            raise CustomException(e,sys)
        
    # Now below mentioned function will start data transformation .
    def initiate_data_transformation(self,train_path,test_path):
        # we are getting train_path and test_path from data ingestion .
        try:
           train_df=pd.read_csv(train_path)
           test_df=pd.read_csv(test_path)

           logging.info("Read train and test data completed")

           logging.info("Obtaining preprocessing object")

           preprocessing_obj=self.get_data_transformer_object()

           target_column_name="math_score"
           numerical_columns = ["writing_score", "reading_score"]

           input_feature_train_df=train_df.drop(columns=[target_column_name],axis=1)
           target_feature_train_df=train_df[target_column_name]

           input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)
           target_feature_test_df=test_df[target_column_name]

           logging.info(
                f"Applying preprocessing object on training dataframe and testing dataframe."
            )

           input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
           input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)

           train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
           test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

           logging.info(f"Saved preprocessing object.")
            
            # This is just used for saving the pickle file .
           save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )
            # We are saving the pickle name in the hard disk.
            
           return(
                train_arr,test_arr,self.data_transformation_config.preprocessor_obj_file_path
            )
        except Exception as e:
            raise CustomException(e,sys)     
