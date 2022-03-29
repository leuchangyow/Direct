import os

import setuptools
from setuptools import setup



setup(name='REIP', version=1.0,
      description='Resolution enhancement image project',
      description_content_type='text/markdown; \
                                charset=UTF-8; variant=GFM',
      long_description=open('README.md', 'r').read(),
      long_description_content_type='text/markdown; \
                                     charset=UTF-8; variant=GFM',
      url='https://github.com/leuchangyow/REIP',
      license='MIT',
      author='Chi-Wei Lin, Ren-Mian Chin, Chang-Yow Leu, Hsuan-Yu Chen, Chia-Ying Yeh',
      python_requires=">=3.5",
      install_requires=[
          "numpy==1.21.0",
          "pandas==1.0.3",
          "keras==2.3.1",
          "tensorflow==2.7.1",
          "scikit-learn==0.23.1",
          "keras-tuner==1.0.1",
          "h5py==2.10.0",
          "plotly==4.8.1",
          "scikit-image==0.17.2",
          "opencv-python",
          "grpcio==1.24.3",
          "pyyaml==5.4",
          "scipy==1.4.1",
          "python-dateutil==2.8.1",
          "pytz==2020.1",
      ],
      packages=setuptools.find_packages())

classifiers = ("Programming Language :: Python :: 3",
               "License :: OSI Approved :: MIT License",
               "Operating System :: OS Independent")
