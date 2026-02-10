# README.md

---

## synopsis

This is a template Python 3.x project, to be used for starting a new project
from scratch.  This is not intended to be a foundation on which to build and
run your next million dollar project, but it is hopefully what you need when
you want to get an idea working quickly and don't want to waste time and energy
on setting up the dull stuff.


## purpose / audience

It's intended to benefit the first 10 hours and days, not the first 10 months
or years.  If you find yourself in that position and needing help, please get
in touch. :-)


## tool configuration

Where possible, use `pyproject.toml` -- doing so keeps all configuration in one
place, and does not litter the root directory of the project with configuration
files.  It would be good if we could keep the project root directory pristine
clean, and refer to the location of `pyproject.toml` by environment variable,
but until that time, we will have to make do with this approach.



## workflow

* clone the repository
```bash
git clone some/where/repository.git
```

* install the basics
```bash
bin/dev-setup
```

* check it works!
```bash
bin/app-main --help
```

* examine the root requirement file:
```bash
$ cat etc/pip-requirement.d/3.13/roots 
jurigged==0.6.1
pipdeptree==2.30.0
pyright==1.1.408
pytest==9.0.2
```

* add a top-level ("root") requirement
```bash
echo pyyaml >> etc/pip-requirement.d/3.13/roots
```

* update
```bash
bin/dev-init
```


## files

files in `bin/`

| name               | remarks                                                       |
|--------------------|---------------------------------------------------------------|
| `.settings`        | contains `python_version`; unlikely to grow                   |
| `.env`             | contains environment variables; unlikely to grow              |
| `bin/app-main`     | run `src/python/main/app/main/main.py` via `bin/venv-python3` |
| `bin/dev-setup`    | create .venv/ and install packages from                       |
| `bin/dev-update`   | run bin/dev-setup and install latest versions of all packages |
| `bin/venv-pip3`    | run `.venv/bin/pip3` via `bin/venv-run`                       |
| `bin/venv-python3` | run `.venv/bin/python3` via `bin/venv-run`                    |
| `bin/venv-run`     | run files from `.venv/bin/`                                   |

bin/venv-pip3 and bin/venv-python3 pass custom arguments to their executables

files in `etc/pip-requirement.d/`

| name                                   | category | remarks |
|----------------------------------------|----------|---------|
| `etc/pip-requirement.d/3.13-bootstrap` |          |         |
| `etc/pip-requirement.d/3.13-roots`     |          |         |
| `etc/pip-requirement.d/3.13-version`   |          |         |


### venv wrapper scripts

* `bin/venv-python3` -- run `.venv/bin/python3` with environment
* `bin/venv-run` `{basename}` -- run `.venv/bin/{basename}` with environment

### application entry points

* bin/app-main -- run src/python/app/main/main.py

## examples

### assumptions

* You are using Python 3.13 (change it in .settings)

### cold start

bootstrap the `.venv/` directory using the contents of `etc/pip-requirement.d/3.13-bootstrap`

```bash
bin/dev-setup
```

### install python package

```bash
bin/venv-pip3 install mypy
```

### update versioned requirements list file

update the contents of etc/pip/requirement/{version}/version

```bash
bin/dev-init
```

---

## wrapper scripts

### development convenience scripts

* bin/dev-setup -- create .venv/ and install packages from etc/pip-requirement.d/3.13-*
* bin/dev-update -- run bin/dev-setup and install latest versions of all packages
* bin/venv-pip3 -- run pip3 from .venv/bin/
* bin/venv-run -- run files from .venv/bin/

### venv wrapper scripts

* bin/venv-python3 -- run .venv/bin/python3 with environment
* bin/venv-run ${1} -- run .venv/bin/${1} with environment

### application entry points

* bin/run-main -- run src/python/app/main/main.py

---

