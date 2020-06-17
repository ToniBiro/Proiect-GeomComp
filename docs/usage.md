# Usage Instructions

## With Docker

### 1. Clone the GitHub repo

Download on your local machine the current repo. You can use Github Desktop if you are on Windows or download it directly from the browser version. For more instructions click [here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).

### 2. Install Docker

Before you can use the app you need to have Docker installed on your machine. If you do not have it installed yet please follow the instructions from [here](https://docs.docker.com/docker-for-windows/install/).

### 3. Run on the command line `docker-compose up`

Assuming you have [docker-compose](https://docs.docker.com/compose/) installed open a command line and go to the place you downloaded the GitHub repo and then find the _backend_ folder. Run the command `docker-compose up`.

If you do not have docker-compose installed then please follow the instruction from [here](https://docs.docker.com/compose/install/).

## With package managers

### 1. Clone the GitHub repo

Download on your local machine the current repo. You can use Github Desktop if you are on Windows or download it directly from the browser version. For more instructions click [here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).

### 2. Install requirements

Because the backend of the application is written in python you will need to install using pip everything from `requirements.txt`. If you do not have pip installed please follow the instructions [here](https://pip.pypa.io/en/stable/installing/#:~:text=Do%20I%20need%20to%20install,make%20sure%20to%20upgrade%20pip.).

### 3. Run Flask

After everything has been installed from the previous step you will need to go to the file where you cloned the repository and open a command line. There you will need to enter the following command `flask run`.

### 4. Install `npm`

Go to the _frontend_ folder from the repo on your local machine and open a command line there. Run `npm install`.
Next up run `npm start`.
This should start the application.

# How to stop the app

## With Docker

If the app is running using Docker than all you need to do is run `docker-compose down` in the command line in the folder where you started the container.

## With package managers

Using `Ctrl + C` you should:

- In the `backend` folder stop the `flask run` command.
- In the `frontend` folder stop the `npm start` command.
