# customer management service
Customer management system app implemented with FastAPI web framework

## Installation
Clone this repo and create a virtual environment:

```
git clone https://github.com/tabris2015/customer-management-service.git
cd customer-management-service
virtualenv -p python3 venv
```

Activate the virtual env and install dependencies:

```
source venv/bin/activate
pip install -r requirements.txt
```

## Running the development server
In order to run a development server use uvicorn:

```
uvicorn app.main:app --reload
```

and enter `http://127.0.0.1:8000` in the browser.

To check the interactive API documentation enter ` http://127.0.0.1:8000/docs`

## Running with docker
There is a simple dockerfile for running the applicacion inside a docker container. First, build the image:
```
docker build -t fastapi-todo .
```
Once built, you can run it with:
```
docker run -p "8000:8000" -t customer-management-service
```
the server will be available at `http://127.0.0.1:8000`

## Running with docker-compose
There is a still easier way to run the app in a docker container using `docker-compose`, for that, you need
to have docker-compose installed in your system, then run:
```
docker-compose up
```
as usual, the server will be available at `http://127.0.0.1:8000`

## Firestore database
This project uses google cloud firestore as database. You need to set up credentials to access your database, 
for that, the easiest way is to download a service account private key and then set up the following environment
variable:

```
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/servicekey.json"
```

**Note:** for local docker deployment you'll have to pass both the key and set the environment variable manually.
