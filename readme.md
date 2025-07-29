# Fast Full Stack

The fastest application in the west delivering lots of potential for hackathons or POC's.  This application leverages a 
scalable, simple, and highly googlable tech stack for your basic full stack purposes.  This sample code creates a very
basic application listing movies, so Lights, Camera, Code!

## React Requirements and Setup
React requires the following tools to get started:
* [Node.js](https://nodejs.org/en/download)
* An IDE of your choice [I used Webstorm](https://www.jetbrains.com/webstorm/download/?section=windows)

This basic application was created by using create-react-app library.

### To create your own React app from scratch use:
Install create-react-app with:
`npm install -g create-react-app` 

Create your application with:
`npx create-react-app movie-website`

Start your application with:
`npm start`

### To run this existing codebase instead use:
`npm install` and then `npm start`

### Resources:
* [React documentation](https://react.dev/learn)

## Python Requirements and Setup
The backend portion of this application utilizes Python with FastAPI.  Python should always be run in a virtual
environment, I set this up through using venv in PyCharm.
* [Python 3.12](https://www.python.org/downloads/)
* An IDE of your choice [I used Pycharm](https://www.jetbrains.com/pycharm/download/?section=windows)

To run this sample code, first install libraries with:
`pip install -r requirements.txt`

To run this FastAPI Python application use:
`fastapi dev main.py`

### Resources
* [FastAPI documentation](https://fastapi.tiangolo.com/tutorial/)
* [Pydantic documentation](https://docs.pydantic.dev/latest/)
* [PyMongo documentation](https://pymongo.readthedocs.io/en/stable/)

## MongoDB Requirements and Setup
This full stack application uses a MongoDB cluster hosted by MongoDB Atlas.  As of creating this code sample this is 
completely free to do.  In order to set up this cluster you must follow these steps:
1. Navigate to [MongoDB Atlas](https://www.mongodb.com/products/platform/atlas-database)
2. Click "Get Started"
3. Create an account/login
4. Select "Build a Cluster" and click on the free cluster option on the far right
5. Name your cluster related to your application (i.e. "MovieCluster") and click "Create Deployment"
6. To connect to your cluster, I use a username and password, since I'm running this application locally as a POC
7. Input a username and password, this will be part of your connection URN later
8. Click "Finish and Close" and wait for your cluster to provision
9. Once it is provisioned, click "Connect" then "Drivers" and select Python version 3.12 or later
10. Follow the instructions on that page, of installing pymongo and the basic code
11. Input your DB password instead of the filler in the connection string
12. Within MongoDB Atlas, create a new database in your cluster named appropriately, (i.e. "movie_db")

## Presentation Resources
* [Slides](https://docs.google.com/presentation/d/1ujdVEfQJuXHCuQd4HSCavdsayHlyjJenF2H9Eashvo4/edit?usp=sharing)
* [Presenter notes](https://docs.google.com/document/d/1c96FqZWzn7Vs8MXsOi2qt7AxDGYexiol8ifh0Kv9T8Q/edit?usp=sharing)