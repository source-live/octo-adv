from setuptools import setup, find_packages
from codecs import open
from os import path

octo = path.abspath(path.dirname(__file__))
with open(path.join(octo, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name='octo-adv',
  version='1.0',
  
  description='An experimental image replicator based off hyperGAN.',
  long_description=long_description,
  
  url='https://github.com/source-live/octo-adv',
  
  author='Source Live',
  author_email='zack@zacklearns.com',
  
  license='MIT',
  
  classifiers=[
    'Development Status :: 1 - Pre-Alpha',
    'Intended Audience :: Developers',
    'Environment :: Console',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Multimedia :: Graphics'
  ]
  
  keywords='generate art teach computer graphics random code python experimental',
    
  packages=['octo-adv']+subpackages,
  scripts = ['bin/octo-adv']
)
