# PsychoTests
![Preview](polls_preview.png)
This is learning Django project. It can create any social polls (including questions and answers) at web interface of administrator.
## System
- Ubuntu 23.10 Mantic
- Conda 24.1.2
## Packages
- python 3.11.8
- django 4.1
- django-bootstrap5
- pillow 10.2.0
## Install
- ``` git clone git@github.com:barabashka25219/PsychoTests.git ```
- ``` cd PsychoTests ```
- ``` conda env create -f environment.yml ```
## Prepare to launch
- conda activate Psycho
- ./manage.py migrate
- ./manage.py createsuperuser
- ./manage.py runserver