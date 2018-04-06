ATH.ENA reporting tool
======================

requirement
-----------
* python 3.6
* python3-pip
* unix-based operating system

setup
-----
cd ../path/to/repo
sudo pip3 install virtualenvwrapper
mkvirtualenv reporting
workon reporting
pip install -r requirements.txt
python manage.py runserver