# README.md

---

## synopsis

This is a template Python 3.x project, to be used for starting a new project from scratch.


---

## examples

### cold start

bootstrap the .venv/ directory use the contents of etc/pip/requirement/bootstrap

```bash
bin/dev-bootstrap
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

* bin/dev-bootstrap -- create .venv/ and install packages
* bin/dev-update -- run bin/dev-bootstrap and install latest versions of all packages
* bin/venv-pip3 -- run pip

### venv wrapper scripts

* bin/venv-bin ${1} -- run .venv/bin/${1} with environment
* bin/venv-python3 -- run .venv/bin/python3 with environment

### application entry points

* bin/run-main -- run src/python/app/main/main.py

---

