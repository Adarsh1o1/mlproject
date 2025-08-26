from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path:str)->List[str]:
    # this function will return the list of requirements from requirements.txt

    requirements = []

    with open('requirements.txt') as file:
        requirements = file.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements

setup(
name= 'mlproject',
version='0.0.1',
author='Adarsh',
author_email='adarshkushawha52@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)
