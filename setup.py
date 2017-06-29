
from setuptools import setup
from setuptools.extension import Extension

setup(
    author="Philip Kalinda",
    author_email="philipkalinda@gmail.com",
    name='genetic_algorithm',
    version='0.1',
    url='https://github.com/philipkalinda/genetic_algorithm',
    description='A Genetic Algorithm for feature selection in Data Science problems',
    license='MIT',
    install_requires=['matplotlib', 'numpy>=1.6.1', 'sklearn', 'numpy', 'time'],
    ext_modules=[],
    scripts=['genetic_algorithm.py'],
    packages=['genetic_algorithm'],
    package_data={'genetic_algorithm': ['stopwords', 'DroidSansMono.ttf']}
)
