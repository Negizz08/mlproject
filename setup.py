from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    with open(file_path, "r") as file_obj:
        requirements = [req.strip() for req in file_obj.readlines() if req.strip()]

        print("Parsed requirements:", requirements)
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="anup",
    author_email="anup2negi@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)