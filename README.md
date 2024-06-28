
<br>

## RAPIDS

This template is for developing [rapids.ai](https://rapids.ai) dependent products; [rapids.ai](https://rapids.ai) enables graphics processing unit accelerated data science.

<br>

### Remote Development

Via a remote development image.  The image depends on [.devcontainer/Dockerfile](.devcontainer/Dockerfile) & [.devcontainer/requirements.txt](.devcontainer/requirements.txt), and is built via

```shell
 docker build . --file .devcontainer/Dockerfile -t rapids
```

Run an instance of the image, i.e., a container, via

```shell
docker run --rm --gpus all -i -t -p 127.0.0.1:10000:8888 -w /app 
	--mount type=bind,src="$(pwd)",target=/app rapids
```

or

```shell
docker run --rm --gpus all -i -t -p 127.0.0.1:10000:8888 -w /app 
	--mount type=bind,src="$(pwd)",target=/app 
	-v ~/.aws:/home/rapids/.aws rapids
```

Opt for the second option if you need to interact with Amazon Web Services.  Note:

* --rm: [automatically remove container](https://docs.docker.com/engine/reference/commandline/run/#:~:text=a%20container%20exits-,%2D%2Drm,-Automatically%20remove%20the)
* -i: [interactive mode](https://docs.docker.com/engine/reference/commandline/run/#:~:text=and%20reaps%20processes-,%2D%2Dinteractive,-%2C%20%2Di)
* -t: [tag](https://docs.docker.com/get-started/02_our_app/#:~:text=Finally%2C%20the-,%2Dt,-flag%20tags%20your)
* -p: [publish](https://docs.docker.com/engine/reference/commandline/run/#:~:text=%2D%2Dpublish%20%2C-,%2Dp,-Publish%20a%20container%E2%80%99s) maps the host port 10000 to container port 8888
* `-v ~/.aws:/home/rapids/.aws` enables interactions with Amazon Web Services, if such interactions are required.  It maps the local Amazon Web Services credentials directory to a temporary `.aws` directory within the container.

<br>

Get the name of the container via:

```shell
docker ps --all
```

<br>

### Remote Development & Integrated Development Environments

In aid of productivity, use/attach an IDE (integrated development environment) to the running container.  The **IntelliJ
IDEA** set up involves connecting to a machine's Docker [daemon](https://www.jetbrains.com/help/idea/docker.html#connect_to_docker), the steps are

<br>

> * **Settings** $\rightarrow$ **Build, Execution, Deployment** $\rightarrow$ **Docker** $\rightarrow$ **WSL:** {select the linux operating system}
> * **View** $\rightarrow$ **Tool Window** $\rightarrow$ **Services** <br>Within the **Containers** section connect to the running instance of interest, or ascertain connection to the running instance of interest.

<br>

**Visual Studio Code** has its container attachment instructions; study [Attach Container](https://code.visualstudio.com/docs/devcontainers/attach-container).


<br>
<br>

## Code Analysis

The GitHub Actions script [main.yml](.github/workflows/main.yml) conducts code analysis within a Cloud GitHub Workspace.  Depending on the script, code analysis may occur `on push` to any repository branch, or `on push` to a specific branch.

The sections herein outline remote code analysis.

<br>

### pylint

The directive

```shell
pylint --generate-rcfile > .pylintrc
```

generates the dotfile `.pylintrc` of the static code analyser [pylint](https://pylint.pycqa.org/en/latest/user_guide/checkers/features.html).  Analyse a directory via the command

```shell
python -m pylint --rcfile .pylintrc {directory}
```

The `.pylintrc` file of this template project has been **amended to adhere to team norms**, including

* Maximum number of characters on a single line.
  > max-line-length=127

* Maximum number of lines in a module.
  > max-module-lines=135


<br>


### pytest

The `pytest` framework is for test writing.  This template includes a test for the program [src/algorithms/example.py](src/algorithms/example.py).  The program's corresponding test program is [tests/algorithms/test_example.py](tests/algorithms/test_example.py), which is run via

```shell
python -m pytest -p no:cacheprovider /app/tests/algorithms/test_example.py
```

The directive `no:cacheprovider` will prevent the storage of *test cache*, hence prevents the need for a *.pytest_cache* directory.

<br>

### flake8

For code & complexity analysis.  A directive of the form

```bash
python -m flake8 --count --select=E9,F63,F7,F82 --show-source 
	--statistics src/{directory.name}
```

inspects issues in relation to logic (F7), syntax (Python E9, Flake F7), mathematical formulae symbols (F63), undefined variable names (F82).  Additionally

```shell
python -m flake8 --count --exit-zero --max-complexity=10 --max-line-length=127 
	--statistics src/{directory.name}
```

inspects complexity.


<br>

<br>

### References

Images via Docker Hub Container Image Library
* [RAPIDS](https://hub.docker.com/r/rapidsai/rapidsai)
* [About Development Containers](https://github.com/rapidsai/devcontainers)
* [Development Containers](https://hub.docker.com/r/rapidsai/devcontainers)

Images via [NVIDIA GPU Cloud (NGC)](https://catalog.ngc.nvidia.com)
* [Starting](https://catalog.ngc.nvidia.com/orgs/nvidia/collections/gettingstarted)
* [Images & Containers](https://catalog.ngc.nvidia.com/containers)
* [rapids](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/rapidsai/containers/base)

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
