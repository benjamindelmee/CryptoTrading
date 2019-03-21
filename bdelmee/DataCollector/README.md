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
```
## Development

```bash
# cd to the root directory
cd dataCollector

# run the application using docker
make startdev
```