#step-1
from setuptools import find_packages,setup
from typing import List

#step-4
HYPEN_E_DOT= '-e .'

#step-3
def get_requirements(file_path:str,)->List[str]:
    # this function will return requirements

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements] #once the library read there will show this \ to change as empty this code


        #step-5
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


#step-2
setup(
name='ML_Projects',
version='0.0.1',
author='Sathik',
author_email='sathikanaly@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')


)