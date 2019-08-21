# :shell: Learning GraphQL by building a book query API :shell:

In this project I will be using GraphQL primarily to experiment with alternatives to RESTFUL design practices. I will also be using react and Django, both of which I have minimal experience with to further my learning in other frameworks.

This project was created using a tool I built: [`synth`](https://github.com/bennettdixon/synth)

## :running: Getting Started

- [macOS High Sierra 10.13.6](https://apple.com) - OS Used

- [Docker CE 18.09.2](https://blog.docker.com/2018/11/introducing-docker-engine-18-09/) - Version of docker used

## :warning: Prerequisites

- Must have `git` installed

- Must have `docker` installed

```
$ sudo apt-get install git
```

## :wrench: Setup

Clone the project

```
git clone https://github.com/BennettDixon/book_query_app;
cd book_query_app;
```

Run the container network, this will build them the first time so be patient while images are downloaded and containers are built

```
docker-compose up -d
```

Locate the postgres container id using

```
docker ps
```

Execute the following, substituting your postgres container id. This will setup a user and database in your postgres container. You only need to do this once unless you delete the docker-compose volume mount or the postgres data on your local machine.

```
docker exec -it <container-id> psql -U postgres -f /app/postgres_setup.sql
```

Restart the network of containers using the following to apply the migration to the new database:

```
docker-compose restart
```

Visit the GraphQL endpoint `localhost:8800/graphql` and play with GraphQL Queries!

Feel free to add objects to the `/nginx_router/backend/books.json` file for further testing! They will be loaded in each time you boot the containers.

### Shutting it down

```
docker-compose down
```

## :blue_book: Authors

- **Bennett Dixon** - [@BennettDixon](https://github.com/BennettDixon)

## :mag: License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/BennettDixon/book_query_app/LICENSE.md) file for details

## :mega: Acknowledgments

- Holberton School & Docker for the pass to DockerCon 2019!
