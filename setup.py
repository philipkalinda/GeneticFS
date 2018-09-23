from distutils.core import setup
setup(
  name = 'geneticfs',
  packages = ['geneticfs'],
  version = '0.02',
  license='MIT',
  description = 'Genetic Algorithm to optimise feature selection in Machine Learning',
  author = 'Philip Kalinda',
  author_email = 'philipkalinda@gmail.com',
  url = 'https://philipkalinda.com',
  download_url = 'https://github.com/philipkalinda/GeneticFS/archive/v_002.tar.gz',
  keywords = ['Genetic Algorithm', 'Algorithm', 'Machine Learning', 'Feature Selection', 'Optimisation'],
  install_requires=[
          'numpy',
          'sklearn',
          'matplotlib'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
