# setup.py is responsible for creating our machine learning application as a package and deploy in pypi .We can install this package and use it .
from setuptools import find_packages,setup
# This will find all the packages that are available in entire machine learning application in the directory that we have actually created .

from typing import List


HYPEN_E_DOT = '-e .'
# get_requirements will take directory path as string and return list of strings .
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return list of requirements
    '''
    
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements 
    
    
    
    
setup(
name='ml_project',
version='0.0.1',
author='Bittu',
author_email='bittukumar30dec2002@gmail.com',
packages=find_packages(),
#install_requires=['pandas','numpy','seaborn'],
install_requires = get_requirements('requirements.txt')
)
# whenever we write any package then we have to write name of project , version. In install_require , we have to mention all the things that we require .


# How setup.py will be able to find packages ? 
# If we want src(source) to be found as package then create one file in it __init__.py . Whenever find_packages() will be running , it will see in how many folders you have __init__.py file . So, it will directory consider that folder(src in this case) as package itself. And then it will build src and then you can import this anywhere .


# We can directly run this setup.py file or whenever we are trying to install requirements mentioned in requirement.txt  so, at that time setup.py file should also run to build the packages .

