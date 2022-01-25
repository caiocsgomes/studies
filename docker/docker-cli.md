# Useful docker cli commands

## container
```sh
docker container ls
# Run a command in a container
docker container run -it container [command]

# Attach a STDIO to a running container
docker container attach [id]

# Execute a container as a deamon
docker conteiner -d [image]

# Execute a command inside a running container
docker container exec -it [id] [command]

# Stop a container but do not kill it
docker container stop [id]

# Start a stopped container
docker container start [id]

# See metadata about container
docker container inspect [id]

# Show logs
docker container logs -f [id]
```

Exit container without killing it: CTRL + PQ