# Maoyan-Top-100

## Usage

```sh
scrapy crawl -O top100.csv top_100
```

## Global Installation

```sh
pip install Scrapy
```

## Virtual Environment Installation

The project uses [Pipenv](//github.com/pypa/pipenv) to manage its dependencies

### Install Pipenv
```sh
# Debian
sudo apt install pipenv

# Fedora
sudo dnf install pipenv

# FreeBSD
pkg install py36-pipenv

# Windows
pip install --user pipenv

# Pipx
pipx install pipenv
```

### Create a virtual environment and install dependencies

```sh
pipenv install
```

### Activate the virtual environment

```sh
pipenv shell
```

## Jupyter Notebook

### Virtual Environment Installation

```sh
# with virtual environment activated
pip install jupyterlab

jupyter lab
```
