# Space Engineers Save Tools
Scripts to assist in managing Space Engineers world save files.
This repo is currently in early Alpha - most features are missing or broken.

* [Getting Started](#getting-started)
  * [Requirements](#requirements)
  * [Installation](#installation)
* [Usage](#usage)
* [Testing](#testing)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)


## Getting started


### Requirements

To install and use se_save_tools you will need:

* [Python](https://www.python.org/downloads/) 2.7+
* [Anaconda](http://continuum.io/downloads) or [Miniconda](http://conda.pydata.org/miniconda.html)


### Installation


#### Clone the repo into a new directory
Navigate to your web projects directory and use git to clone the project files
 into a new directory:

via SSH
```
git clone git@github.com:zrisher/se_save_tools.git
```

or via HTTPS
```
git clone https://github.com/zrisher/se_save_tools
```


#### Use Conda to install libraries

Conda manages a virtual environment of python libraries and sources.

* Create a conda environment and load this project's dependencies
  * `conda env create --file environment.yml`
* Tell Conda to use it for our current session
  * `activate zrisher-se-save-tools`
* If you ever need to deactivate it, you can use
  * `deactivate zrisher-se-save-tools`

##### Updating Conda Packages
Occasionally you will need to update conda's packages. Do this by activating your
environment, then `conda env update --file environment.yml`.

#### Use Pip to install more libraries

Now that Conda has set up our virtual environment and downloaded Pip, we can use
  Pip to install the packages which Conda doesn't support directly into our
  environment.

```
pip install -r requirements.txt
```

##### Updating Pip libraries
`pip install --upgrade -r requirements.txt`


## Usage

## Testing
`py.test`, add `-s` flag to view log output

Maybe eventually:
* `behave`
* https://github.com/gabrielfalcao/sure
* https://github.com/nestorsalceda/mamba
* pytest
* nose

## Roadmap

## Contributing

## License