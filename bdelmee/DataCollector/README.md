# Data Collector

- Continuously reads data from the BitMEX websocket API
- Rights the data into a PostreSQL database
- Makes the data available through a REST API

## Prerequisites

You need to install **docker** and **docker-compose** ([see documentation](https://docs.docker.com/install/)).

## Deployment

```bash
# cd to the root directory
cd dataCollector

# run the application using docker
make start

# to stop the application
# make stop
```

## Development

```bash
# cd to the root directory
cd dataCollector

# run the application using docker
make startdev

# stop the application
ctrl + c
```

## Maintenance

Each component is independent and can be shut down separately without breaking the application and without any interruption in the data collection flow.

For example, if you need to perform database maintenance operations, you can process as follow:

```bash
# shut down the database
docker-compose down db

# do your stuff...

# turn on the database
docker-compose up db
```

## Data location

The data are stored in the folder `./components/database/data`