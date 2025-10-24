from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Hotel_Reservation_MLOPS_Project",
    version="0.1",
    author="Sahishnuta",
    packages=find_packages(),
    install_requires = requirements,
)