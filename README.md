# Object Oriented Python

# Python Set up

1) Set up your environment 

           virtualenv - Tool to create isolated python environments 
           Separate Python interpreter and site-packages 
           Install virtualenv - sudo pip install virtualenv 
           Create a new virtual environment called venv :  

```
$ virtualenv venv 
```
This also installs setuptools and pip into venev 

Activate venv (add its bin directory at the front of $PATH) 

```
$ source venv/bin/activate 
```
                    
Restore : $ deactivate 

2) PIP -  Python packages 

Tool to install and manage python package 

Offers installation from Package index, source or binary distribution 

3) Get and install latest version of package "pyscaffold" from public PyPI 

```
$ pip insatll pyscaffold or 

$ pip install 'pyscffold>=0.7' 
```

4) You can install whole environment by requirements file 
```
$ pip install -r requirements.txt 
```

5) You can get packages in requirements format". 
```
$ pip freeze 
```

6) Organize the project with git. 

7) Need reasonable directory structure, unit tests, documentations 

8) Distribute your project 

Use distutils or better setuptools 

Package installation :  
```
$ python setup.py install 
```

Helpful during development 
```
$ python setup.py develop 
```
Source or Binary distribution 
```
$ python setup.py sdist 

$ python setup.py bdist 
```
9) Versioning __version__ attribute in __init__.py for distribution 

Versioneer manages version by git's identifier 

Simply use git tags to specify releases 


 

 

Misc : 

Module : a file containing python code 

Package : a folder containing an __init__.py file and Python modules 

 
