from setuptools import find_packages,setup
from typing import List
import os

def requirements_list(path:str)->List[str]:
 
    '''
    this functios returns the list of requirements, read from the requirements.txt file
 
    '''
    extra_line='-e .'
    requirements=[]
    with open(path) as obj:
      rquirements= obj.readlines()
    requirements=[req.replace('\n',"") for req in requirements]
    if extra_line in requirements:
       requirements.remove(hextra_line)
    return requirements
      
  



setup(
name='Insurance cost prediction',
version='0.0.1',
author='Hafedh',
author_email='benafia.hafedh1988@gmail.com',
packages=find_packages(),
install_requires=requirements_list('requirements.txt')
)