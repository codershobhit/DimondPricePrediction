from setuptools import find_packages,setup
from typing import List

Hyphn_e_dot = '-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if Hyphn_e_dot in requirements:
            requirements.remove(Hyphn_e_dot)


        return requirements



setup(
    name='DiamondPriceprediction',
    version='0.0.1',
    author='shobhit',
    author_email='stockwiz1998@gmail.com',
    install_requires=get_requirements('requirement.txt'),
    packages=find_packages()

)