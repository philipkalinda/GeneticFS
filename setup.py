from distutils.core import setup
setup(
  name = 'GeneticFS',
  packages = ['GeneticFS'],
  version = '0.01',
  license='MIT',
  description = 'Genetic Algorithm for feature selection within Machine Learning',
  author = 'Philip Kalinda',
  author_email = 'philipkalinda@gmail.com',
  url = 'https://philipkalinda.com',
  download_url = 'https://github.com/philipkalinda/stackerpy/archive/v_001.tar.gz',
  keywords = ['Genetic Algorithm', 'Scikit-Learn', 'sklearn', 'Algorithm', 'Machine Learning', 'Optimisation'],
  install_requires=[
          'numpy',
          'sklearn',
          'matplotlib'
      ],
  classifiers=[
    'Development Status :: 1 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
