from setuptools import find_packages, setup
from typing import List

hyphen_e_dot = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements.
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

# We have added -e . in requirements.txt so that whenever we install the packages in that file, it also runs setup.py.
# But because of it -e . will also show up in the requirements variable. So to remove that we have written the below 2 lines of code.

    if hyphen_e_dot in requirements:
        requirements.remove(hyphen_e_dot)

    return requirements

setup(

    name='mlproject24.03.3025',
    version='0.0.1',
    author='Vijeta',
    author_email='vashishtha.vijeta@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    
)
