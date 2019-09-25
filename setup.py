from distutils.core import setup
setup(
  name = 'StackerPy',
  packages = ['stackerpy'],
  version = '0.01',
  license='MIT',
  description = 'Machine Learning model stacking with blending capabilities (Compatible with Scikit-Learn)',
  author = 'Philip Kalinda',
  author_email = 'philipkalinda@gmail.com',
  url = 'https://philipkalinda.com',
  download_url = 'https://github.com/philipkalinda/stackerpy/archive/v_001.tar.gz',
  keywords = ['Stacking', 'Scikit-Learn', 'sklearn', 'Algorithm', 'Machine Learning', 'Blending', 'Optimisation'],
  install_requires=[
          'numpy',
          'sklearn',
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
