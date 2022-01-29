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

# Show resources utilization
docker container stats [id]

# Remove container
docker container rm -f [id]

# Bind mount in a container
docker container run -t
i --mount type=bind,src=[src folder],dst=[dst folder] [image]

# Bind volume to a container
docker container run -ti --mount type=volume,src=[volume],dst=[dst folder] debian

```

Exit container without killing it: CTRL + PQ

## volume

```sh
# Create volume
# mounted in /var/lib/docker/volumes/ on linux and good look trying to find it on windows
docker volume create [volume name]

# clean unused volumes
docker volume prune
```