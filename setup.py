from distutils.core import setup
setup(
  name = 'topsis-NamanJain-101803065',        
  packages = ['topsis-NamanJain-101803065'],   
  version = '1.0.0',      
  license='MIT',
  description = 'Decision Making using topsis (Python Package)',
  author = 'Naman Jain',
  author_email = 'namanjain24682468@gmail.com',
  url = 'https://github.com/namanjain323232/topsis',
  download_url = 'https://github.com/namanjain323232/topsis/archive/1.0.0.tar.gz',
  install_requires=[            
          'pandas',
          'numpy'
      ],
  classifiers=[
    'License :: OSI Approved :: MIT License', 
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.7'
  ],
)