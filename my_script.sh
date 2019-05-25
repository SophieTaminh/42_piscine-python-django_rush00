pip3 install virtualenv
virtualenv django_venv; source django_venv/bin/activate
pip3 install -r requirements.txt
cd RUSH00
echo To start Django, type: ./manage.py runserver
PS1='(django_venv) \w> ' sh

# django-admin.py startproject RUSH00
# cd RUSH00
# django-admin.py startapp ex00
