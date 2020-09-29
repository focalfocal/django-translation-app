# django-translation-app
# Description:
A very simple Django web app consuming a service (Google Translate) for translation from English to Spanish (source and target languages).
# NOTICE:
The equivalent to the API Key (iid and also part of the User Agent id) were eliminated on this source code for privacy reasons.

# Developer:


# Deployment and verification
# NOTICE:
These instructions were used to distribute this source code for local deployment on other machines.

...................
Follows instructions to deploy the app on a local machine running Linux (I used Ubuntu) having Python 3.8.

Unzip  so the folder structure is also created.

Open a terminal on the top folder ('django-translation-app').

Create a virtual environment:
$ python3 -m venv myvenv

Activate the virtual environment:
$ source myvenv/bin/activate

Update pip:
$ pip install --upgrade pip     //installs pip-20.2.3

Install Django 3 and dependencies using requirements.txt:
$ pip install -r requirements.txt   //installs Django 3.1.1 and dependencies

Create a Django project:
$ django-admin startproject mysite .   //mind the final dot

Unzip 'app-source-files.zip' here, with the options:
-------- "Unpack path names"
-------- "Overwrite existing files"
This will overwrite the default Django project files with the app ones, and add others.

Run the local server:
$ python manage.py runserver  
Do not care about the warning regarding 'unapplied migrations'. They are not required for this simplified demonstration app.

The success message should be:
    "Django version 3.1.1, using settings 'mysite.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CONTROL-C."

On a browser navigate to: http://127.0.0.1:8000/

The Home app page opens, and you can enter the English text to translate to Spanish.
A test text is provided on the file "source.txt", and the expected result is on the file "target.txt"

