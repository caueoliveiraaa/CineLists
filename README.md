![screenshot](system-design-overview.jpg "Application")

# DOCUMENTATION 🔎🌍⬇ 

## About the project ⚙️🗂

welcome ...

- **Programming language**: The programming language chosen for this application was ***Python*** 🐍, because it's very flexible, easy to use and it has great `libs` and `frameworks`. The application was developed in the `version 3.12.1`

## General instructions to run the application 🔎📖

### 1 - It's necessary to build and start the containers 🐋📦🐋📦

#### -- Docker commands 

**Build containers**
```
docker compose build user-api
docker compose build order-api
```

**Start containers**
```
docker compose up -d user-api
docker compose up -d order-api
```

**Restart containers**
```
docker compose down -t 0 user-api
docker compose down -t 0 order-api
```

**Check logs**
```
docker compose logs user-api
docker compose logs order-api
```

**Interact with the containers' Linux terminal**
```
docker compose exec order-api /bin/bash
docker compose exec user-api /bin/bash
```

**List active containers**
```
docker compose ps
```

**List all containers**
```
docker compose ps -a
```


#### To make the execution of the services easier, utilize the Makefile

**Targets available**
- run : Execute build for images and run services
- restart : Restart all services
- logs : Display logs of all services 
- build : Only execute the build for the images
- stop : Stop all services

**Usage**
```
make run
make restart
make logs
...
```

## 2 - Open URLs in browsers to test APIs via Swagger 🖥️🛜



### Documentações relevantes para o projeto | Relevant documentarions for the project 🔎🌐