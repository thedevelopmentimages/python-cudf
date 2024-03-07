

## RAPIDS

[About](https://rapids.ai)
[Install](https://docs.rapids.ai/install)

### Images

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

### In Focus

* [CUDF](https://github.com/rapidsai/cudf)


<br>

## Remote Development

```shell
docker run --rm --gpus all -i -t -p 127.0.0.1:10000:8888 -w /app \
	--mount type=bind,src="$(pwd)",target=/app \
	-v ~/.aws:/home/rapids/.aws ...
```

Note:

* `-v ~/.aws:/home/rapids/.aws:ro` maps the a directory segment of the container to the local Amazon Web Services `.aws`.  This is for credential sharing purposes.
* `ro` denotes read only.

<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>