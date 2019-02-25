from setuptools import setup, find_packages


setup(
    name='restapi',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'connexion[swagger-ui]',
        'numpy==1.14.3',
        'scipy==1.1.0',
        'scikit-learn==0.19.1'
    ]
)
