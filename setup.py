from setuptools import setup, find_packages    # find_packages detects __init__.py

setup(
    name = "src", 
    version="0.0.1", 
    description="its a wine Q package", 
    author="abhishek",
    packages=find_packages(),
    license="MIT"
)


