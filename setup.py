from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

setup(
    name='pysicktim',
    version='0.1.0',
    description='TIM561 Python Library',
    license='GNU General Public License v3.0',
    packages=['pysicktim'],
    install_requires=['pyusb'],
    author='Daniyal Ansari',
    author_email='daniyal.s.ansari+pypi@gmail.com',
    keywords=['tim561','sick','lidar','sicktim','tim5xx','sicktim5xx','sicktim561'],
    url='https://github.com/ansarid/pysicktim',
    long_description=long_description,
    long_description_content_type='text/markdown'
)
