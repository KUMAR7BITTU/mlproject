# This file is used for exception handling purpose .

# We will write her our own custom exception .

import sys
# Any expection that will be controlled , the sys library will have that information . sys library -:  The python sys module contains methods and variables for modifying many elements of the Python Runtime Environment.

from src.logger import logging 
def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(file_name,exc_tb.tb_lineno,str(error))
    return error_message 
    
    
# whenver any error will be raised , we will push it here .
# we will give here two parameter error , error_details .  error_details will be present inside the sys .
#exc_tb will contain all the information about on which file the information have been ocurred and on which line the information have been occured . 0,1,2 are placeholder here .
# exc_tb.lineno will basically give us line number .
# When any error raises then we will call error_message_detail .

class CustomException(Exception):
    # def __init__() will be our constructor . error_details will be of sys type .
    def __init__(self,error_message,error_detail:sys):
        # since we are inheriting from exception so we have to write super.init() because we have to inherit the init() function .
        super().__init__(error_message)
        # here we are using error_message to inherit the exception class with respect to that .
        
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
        
        
    # quickly we will inherit one more functionality in CustomException which is __str__() .
    def __str__(self):
        # whenver we try to print this, it will give us error message .
        return self.error_message
    
    

# Whenever it raise exception , firstafall it will inherit from parent Exception . whatever error message will come from function error_message_detail , it will assign to error_message(class variable error_message) . error detail is basically dragged by sys .
        
if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:
        logging.info("Divide by Zero") 
        raise CustomException(e,sys)
              