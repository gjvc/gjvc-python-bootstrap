# README.md

---

## synopsis

This is a template Python 3.x project, to be used for starting a new project from scratch.


---

## examples

### assumptions

* You are using Python 3.13 (change it 


### cold start

bootstrap the .venv/ directory uting the contents of etc/pip-requirement.d/3.13-bootstrap

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
bin/dev-update
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

