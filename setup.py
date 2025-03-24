from setuptools import find_packages,setup # type: ignore
from typing import List

def get_requirements(file_path:str)->List[str]:
    """
    this fuction will return the list of requirements
    """
    requirements=[]

    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n',"") for req in requirements]

    return requirements




setup(
    name="mlproject",
    version="0.01",
    author="Akanksha Bisht",
    author_email="akankshabisht145@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
