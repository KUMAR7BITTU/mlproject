# Any functionality that we are writing in common way which will be used in entire application so that i will basically say as utils.py .

import os
import sys
import numpy as np
import pandas as pd
import dill
# dill is also another library which will also help us to create pickle file .
from src.exception import CustomException
def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,"wb")as file_obj:
            dill.dump(obj,file_obj)
    except Exception as e:
        raise CustomException(e,sys);

# Let suppose we have to read a data from dataset , i can create a mongodbclient here . If i have to save my model into the cloud , i can write the code over here . we will call the utils's code inside the component .

# Here we will write code related to evaluation method .

