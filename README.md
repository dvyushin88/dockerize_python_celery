# Dockerize python celery

A basic [Docker Compose](https://docs.docker.com/compose/) template for orchestrating scheduler application and [Celery](http://www.celeryproject.org/) queue with [Redis](https://redis.io/)

### Scheduler app

While app is running every 10 seconds scan `/media/input/` folder for `.txt` files and send tasks to celery queue for execution

### Worker app

Simple tasks execution app. Every task counts number of lines in file from ```input``` and write information file to `output` folder

### Installation

```bash
git clone https://github.com/dvyushin88/dockerize_python_celery
```

### Build and Launch

```bash
docker-compose up -d --build
```

This will expose a [Flower](https://github.com/mher/flower) server for monitoring workers on port `5555`


#### To shut down:

```bash
docker-compose down
```

#### Discover logs:
```bash
tail -f | docker-compose logs scheduler | docker-compose logs worker
```

### After containers run

* Put some `.txt` files into ```/media/input``` folder.
* For monitor celery worker visit [Local flower](http://0.0.0.0:5555) in browser
* Check result in ```/media/output``` folder.  