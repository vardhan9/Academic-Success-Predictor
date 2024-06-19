from setuptools import find_packages, setup
#find_packages finds all the packages installed
from typing import List

HYPEN_E_DOT='-e .'
#this function returns a list of requirements
def get_requirements(file_path:str)->List[str]:
    '''
    this function returns a list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj: 
        requirements=file_obj.readlines() #reading requirements files line by line
        requirements= [req.replace("\n","") for req in requirements] #reading next line add \n, so here we are replacing with " "
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements
   
#setup is metadata for entire package
setup(
name='academic-success-predictor',
version='0.0.1',
author='Raja Marthala',
author_email='marthalarajavardhanreddy@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)