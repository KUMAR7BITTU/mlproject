# Any execution which happens we should log all the information or the execution in some file so, that we can track the error or the customexception error .

import logging
import os
from datetime import datetime
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# our file name will be created as per format mentioned above .
# LOG_FILE will be a text file .

# path for log file 
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)
# myfile name should have log inforward and this nameing convention . Whatever logs will be created it will be with respect to current working directory . And every file name will starts from logs and file name which is basically is being comming . 
# cwd -: current working directory .

os.makedirs(logs_path,exist_ok=True)
# It basically say us that even though there is a file, even though there is a folder keep on appending the file inside that .
LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)


logging.basicConfig(
    filename = LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s -%(message)s",
    level = logging.INFO,
)
# If we want to overwrite the functionality of this logging then we have to probably set this up in the basicconfig .
# first we will give filename where we want to save it .
# second in which we want to store it :- timestamp,line number ,name, levelname,message .

if __name__=="__main__":
    logging.info("Logging has started")
