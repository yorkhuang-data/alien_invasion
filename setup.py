import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='alien_invasion',  
     version='0.1',
     scripts=['alien_invasion'] ,
     author="York Huang",
     author_email="yorkhuang.data@gmail.com",
     description="A Alien Invasion Game",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/yorkhuang_data/alien_invasion",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
