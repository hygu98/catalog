#Linux Deployment Project Readme

* IP Address: 18.217.240.195
* URL: http://18.217.240.195

List of software deployed to server:

        flask
        sqlalchemy
	psychopg2
        oauth2client
        httplib2
        json
        requests
	postgresql

This server has been configured to run a Python Flask Application utilizing the libraries listed above.  In order for the application to properly communicate with clients, port 80 is open for HTTP traffic, port 123 is open for NTP, and port 22 is open for SSH.

This application is hosted on an Amazon AWS Lightsail Server and utilizes the Google + and Facebook login API's.


Continue reading below for more information on the PantryApp



# ItemCatalogAppProject README

## What is it???

This project is a database driven web application to keep track of items in your pantry at home.

## Software Needed:

This program is being ran through a Virtual Machine environment using Vagrant. You will have to download all programs (if not have downloaded previously), depending on your operating system (windows, Linux, Apple)

    GIT: http://git-scm.com/downloads
    Virtual-Machine: https://www.virtualbox.org/wiki/Download_Old_Builds_5_1
    Vagrant: https://www.vagrantup.com/downloads.html


## Steps for Running the Application Successfully:
* Copy the code files to your local machine.
* Launch GIT Bash in your catalog directory containing all your code.
* Type *vagrant up*.  Depending on your internet speed and computer, might take up to 20 minutes.
* The Virtual Machine should be up and working.  Once it is, type *vagrant ssh* (if vagrant ssh does not work properly, you can use winpty vagrant ssh), this will log in to the Virtual Machine and get a Linux shell prompt.
* Change the directory, *cd /vagrant*, this will take the user into the vagrant folder between the Virtual Machine and the users device.
Before running the catalog application, there are a good amount of python modules that will need to be installed through the Virtual Machine.  The user will have to use either *PIP INSTALL or SUDO PIP INSTALL* while running these modules

        flask
        sqlalchemy
        oauth2client
        httplib2
        json
        requests
        
* After the python modules have been installed, type *ls* to ensure that you are in the directory that states, database_setup.py, project.py, folders named templates and static.
* Type *python database_setup.py* to initialize the database.
* Type *python project.py*.
* Go into the browser using http://localhost:8000 to view the pantry app.  

Once the user is logged into the application, they can then login through Facebook or Google+ Sign In. The user will also be able to view, add, edit and delete pantry items and create whole new pantrys.