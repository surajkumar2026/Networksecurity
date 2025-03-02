'''
this setup .py file is an essential part of packaging abd 
distribution python projects. it is used by setuptools
(or distutils in order python versions) to define the configration 
of our projrct, such as metadata, dependencies, and more
'''
from setuptools import find_packages,setup
from typing import List



def get_requirements(file_path:str)->List[str]:
    '''this function will return the list of  requirements'''
    
    requirements_list:List[str]=[]
    try:

        with open(file_path) as file:
           lines=file.readlines()
           for line in lines:
               requirement=line.strip()
               if requirement and requirement != '-e .':
                       requirements_list.append(requirement)
        
    except FileNotFoundError:
         print("requirements.txt not found")
    return requirements_list
print(get_requirements("requirements.txt"))
    

setup(

    name='mlproject_networsecurity',
    version='0.0.1',
    author='suraj kumar',
    author_email='me22b1073@iiitdm.ac.in',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),

    
)