from setuptools import setup

setup(name='provdebug',
      version='0.1',
      description='Multilingual Provenance Debugger',
      url='http://github.com/jwons/MultilingualProvenanceDebugger', #currently private
      author='Joseph Wonsil',
      author_email='jwonsil@carthage.edu',
      license='GPL 3.0',
      packages=['provdebug'],
      install_requires=[
          'pandas',
          'networkx',
          'numpy',
      ],
      zip_safe=False)