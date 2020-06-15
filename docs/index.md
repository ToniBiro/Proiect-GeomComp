
<img src="https://github.com/ToniBiro/Proiect-GeomComp/blob/master/docs/logo.png?raw=true" alt="Image" width="200" height="200"/>

# Polygon Intersection

- [Technical Description](TechnicalDescription.md)
- [Non-Technical Description](NonTechnicalDescription.md)

## Contributors

All students are from **group 232**:

- [Majeri Gabriel Constantin](https://github.com/GabrielMajeri)
- [Biro-Balan Antonia](https://github.com/ToniBiro)
- [Surcea Mihai-Daniel](https://github.com/Treefold)


## About the application (marketing perspective)


A picture is worth 1000 words. This is statement is especially true when it comes to learning geometry.
Teaching geometry without a visual aid is a very bad idea and unnecessary given the advancement of technology in the past 20 years.

Not being able to comprehend the visual part of geometry results most of the time in the development of a negative attitude towards the subject and frustration, and so, because of this, a lot of children and even grownups miss out on understanding a lot of things quite easy to understand and beautiful if provided with the right perspective.

The scope of this application is to help students learn and teachers teach in a more efficient and attractive way an important part of geometry, intersections.

This piece of software is designed for people of all ages but our targeted audience is mainly middle school/high school students.

## The beginning

We started working on the app as our final project for the Computational Geometry class.

Most of the concepts applied in the code of the app we learned from that class, also understanding how important visualization is for this field of study.

This can be extended to any part of geometry, so we chose to create something that eases the understanding of polygon intersection seeing what an important role it has as a building foundation to further grasp more complex concepts.


## Installation Instructions

## With Docker

### 1. Clone the GitHub repo

Download on your local machine the current repo. You can use Github Desktop if you are on Windows or download it directly from the browser version. For more instructions click [here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).

### 2. Install Docker

Before you can use the app you need to have Docker installed on your machine. If you do not have it installed yet please follow the instructions from [here](https://docs.docker.com/docker-for-windows/install/).

### 3. Run on the command line ```docker-compose up```

Assuming you have [docker-compose](https://docs.docker.com/compose/) installed open a command line and go to the place you downloaded the GitHub repo and then find the *backend* folder. Run the command ```docker-compose up```.

If you do not have docker-compose installed then please follow the instruction from [here](https://docs.docker.com/compose/install/).


## With ```npm```

Clonezi, pentru Python instalezi cu pip tot ce e în requirements.txt și apoi rulezi flask run, pentru front end instalezi cu npm install și dai npm start

### 1. Clone the GitHub repo

Download on your local machine the current repo. You can use Github Desktop if you are on Windows or download it directly from the browser version. For more instructions click [here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).

### 2. Install requirements

Because the backend of the application is written in python you will need to install using pip everything from ```requirements.txt```. If you do not have pip installed please follow the instructions [here](https://pip.pypa.io/en/stable/installing/#:~:text=Do%20I%20need%20to%20install,make%20sure%20to%20upgrade%20pip.).

### 3. Run Flask

After everything has been installed from the previous step you will need to go to the file where you cloned the repository and open a command line. There you will need to enter the following command ```run flask```. 

### 4. Install ```npm```

Go to the *frontend* folder from the repo on your local machine and open a command line there. Run ```install npm```.
Next up run ```npm run```.


## How to stop the app

### With Docker

If the app is running using Docker than all you need to do is run ```docker-compose down``` in the command line in the folder where you started the container.

### With ```npm```



