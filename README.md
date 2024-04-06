# CPMA 536 Project
This repository will be used for our class project. For this project, we will be writing a server in Python that provides access to a folder containing music albums that are themselves separated in to folders. The purpose of the server is to provide a set of endpoints that could then be used by an Alexa skill to provide a way to play these music albums via Alexa. Although I intend to use the server for this once it is completely written, we will not be focusing on that within the scope of the class. Instead, you will interact with the server via your web browser.

## Project Onboarding
The following steps explain the onboarding process for setting up your development environment.

1. Install Git and Python on your computer if they are not already installed. Optionally, install [Sourcetree](https://www.sourcetreeapp.com/) as well.
2. From a terminal, execute the following command to set your first and last name for Git:
   ```
   git config --global user.name "FIRST_NAME LAST_NAME"
   ```
   Replace `FIRST_NAME` with your actual first name and `LAST_NAME` with your actual last name.
3. From a terminal, execute the following command to set your e-mail address for Git:
   ```
   git config --global user.email "DORI_USERNAME@duq.edu"
   ```
   Replace `DORI_USERNAME` with your actual DORI username.
4. Clone this repository by using the following command:
   ```
   git clone https://github.com/Duq-CPMA-536-Spring-2024/Duq-CPMA-536-Spring-2024.git
   ```
5. From within the project's working directory, install the necessary project dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```
6. From within the project's working directory, start the server by running the following command:
   ```
   python music_server.py
   ```
7. From your web browser of choice, connect to the server by navigation to the following URL: http://localhost:5000/