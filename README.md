
# fastweather
![License](https://img.shields.io/github/license/collinsuzebu/fastweather) ![Python 3.8.1](https://img.shields.io/badge/python-3.8.1-blue.svg) ![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg) ![GitHub forks](https://img.shields.io/github/forks/collinsuzebu/fastweather?style=social)

Fastweather is an asynchronous lightweight weather service application built with fastapi.

This service utilizes external API resources while respecting the rate-limit of the API.
Although, the service is built for openweathermap API, it can easily be integrated for
other external API services or any long running background task that involves I/O operation.

###  🔨  Quickstart
```
git clone https://github.com/collinsuzebu/fastweather.git
cd fastweather
```

### External dependencies
[Create a free account](https://home.openweathermap.org/users/sign_up) at Open Weather API to generate a token to call their API.
Add your API key to `.env` file in the section API_OPEN_WEATHER_MAP_KEY.

## Running Locally
**MongoDB is required to run locally.**
When running locally and you don't want to spend extra time creating a mongoDB user, simply set the environment variable flag STRICT_DEV=true.

```
pip install -r requirements.txt
```
**Setting up environment variables**
Include any environment variable like so:
```
export API_OPEN_WEATHER_MAP_KEY=your_secret_key
```

**To run the web application in debug mode:**
```uvicorn fastweather.main:app --reload```


## Running with Docker
You must have `docker` and `docker-compose` installed.
Create a mongoDB user or use an  existing user.
```
$ use admin
> db.createUser( { user: "username", pwd: "password", roles: [ { role: "root", db: "admin" } ] } )
```
Create a `.env` file in the root directory next to `.env.sample` and specify your service
configuration. Then run the command

```
docker-compose up --build
```

## Testing (Locally)
Run test using [coverage.py](https://coverage.readthedocs.io/en/coverage-5.3.1/)
In the root directory, run the command

```
pip install -r requirements-dev.txt
coverage run -m pytest
```
