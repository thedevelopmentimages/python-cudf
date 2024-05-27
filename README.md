
<br>

## RAPIDS

For developing products that exploit graphics processing units.  Visit

* [About](https://rapids.ai)

<br>

### Remote Development

This repository outlines using rapids for development via image containers.  The command

```shell
 docker build . --file .devcontainer/Dockerfile -t rapids-gpu
```

builds an image named `rapids-gpu`.  Run an instance of the image via

```shell
docker run --rm --gpus all -i -t -p 127.0.0.1:10000:8888 -w /app \
	--mount type=bind,src="$(pwd)",target=/app rapids-gpu
```

or

```shell
docker run --rm --gpus all -i -t -p 127.0.0.1:10000:8888 -w /app \
	--mount type=bind,src="$(pwd)",target=/app \
	-v ~/.aws:/home/rapids/.aws rapids-gpu
```

Opt for the second option if you need to interact with Amazon Web Services.  In brief:

* --rm: [remove](https://docs.docker.com/engine/reference/commandline/run/#:~:text=a%20container%20exits-,%2D%2Drm,-Automatically%20remove%20the)
* -i: [interactive](https://docs.docker.com/engine/reference/commandline/run/#:~:text=and%20reaps%20processes-,%2D%2Dinteractive,-%2C%20%2Di)
* -t: [tag](https://docs.docker.com/get-started/02_our_app/#:~:text=Finally%2C%20the-,%2Dt,-flag%20tags%20your)
* [-p](https://docs.docker.com/engine/reference/commandline/run/#:~:text=%2D%2Dpublish%20%2C-,%2Dp,-Publish%20a%20container%E2%80%99s) 10000:8888 maps the host port 10000 to container port 8888
* `-v ~/.aws:/home/rapids/.aws` enables interactions with Amazon Web Services, if such interactions are required.  It maps the local Amazon Web Services credentials directory to a temporary `.aws` directory within the container.

<br>

### References

Images via Docker Hub Container Image Library

* [RAPIDS](https://hub.docker.com/r/rapidsai/rapidsai)
* [About Development Containers](https://github.com/rapidsai/devcontainers)
* [Development Containers](https://hub.docker.com/r/rapidsai/devcontainers)
  > rapidsai/devcontainers:24.04-cpp-cuda12.2-ubuntu22.04

Images via [NVIDIA GPU Cloud (NGC)](https://catalog.ngc.nvidia.com)
* [Starting](https://catalog.ngc.nvidia.com/orgs/nvidia/collections/gettingstarted)
* [Images & Containers](https://catalog.ngc.nvidia.com/containers)
* [rapids](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/rapidsai/containers/base)
  > nvcr.io/nvidia/rapidsai/base:24.02-cuda12.0-py3.10

Additionally
* [CUDF](https://github.com/rapidsai/cudf)
* [Installing RAPIDS](https://docs.rapids.ai/install)

<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>