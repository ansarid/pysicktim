import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='pysicktim',
     version='0.1',
     scripts=['pysicktim'] ,
     author="Daniyal Ansari",
     author_email="daniyal.s.ansari+pip@gmail.com",
     description="A TIM5xx Python Library",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/ansarid/pysicktim",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
