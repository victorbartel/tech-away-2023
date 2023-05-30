
# Overview

A simple example repo for running an fsharp console application in Docker.

# Tu Build

In terminal

```
DOCKER_BUILDKIT=1 BUILDKIT_PROGRESS=plain docker build  .
```

# To Run

In terminal:

```
docker run --rm -it $(docker build -q .)
```
