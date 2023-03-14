# Introduction

AudioFy is a web app tool that uses google text to speach API to generate audio files from PDFS and make them downloadable.

![Default Home View](__screenshots/home.png?raw=true "Title")

### Main features

* Authentication Using Django Allauth

* Uploading Files

* Using Google Text To Speach API to transform PDFs to Audio Files

* User History for converted audios

* CRUD operations


# Usage

To start audiofy on your machine:

      


# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone https://github.com/ZeyadTareq224/Audio-fy.git
    $ cd Audio-fy
    
Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip install -r requirements.txt
    
    
Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver
