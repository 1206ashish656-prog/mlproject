from setuptools import setup, find_packages

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str)->list:
    '''This function will return the list of requirements'''
    with open(file_path, 'r') as file:
        requirements = file.readlines()
        requirements = [req.replace("\n","").strip() for req in requirements if req.strip() and not req.startswith('#')]
    
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)
    return requirements



setup(
    name='mlproject',
    version='0.0.1',
    author='Ashish Agarwal',
    author_email='ashishagarwal656@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    description='A machine learning project setup'
)

