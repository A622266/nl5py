import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="nl5py",
    version="3.1.5",
    description="python binding for nl5 dll",
    long_description=README,
    url="https://sidelinesoft.com/nl5/",
    author="Sidelinesoft",
    author_email="nl5@sidelinesoft.com",
    license="proprietary",
    python_requires=">=3.6",
    packages=find_packages(exclude=("test*", "testing*")),
    package_data={
    "nl5py": ["*.h", "*.dll", "*.lib", "*.so"],  
    },
    install_requires=[],
    
)
