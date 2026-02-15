## gjvc-python-bootstrap

---

### synopsis

This is a template Python 3.x project, to be used for starting a new project
from scratch. This is not intended to be a foundation on which to build and
run your next million dollar project, but it is hopefully what you need when
you want to get an idea working quickly and don't want to waste time and energy
on setting up the dull stuff.

### purpose / audience

It's intended to benefit the first 10 hours and days, not the first 10 months
or years. If you find yourself in that position and needing help, please get
in touch. :-)

### tool configuration

Where possible, use `pyproject.toml` -- doing so keeps all configuration in one
place, and does not litter the root directory of the project with configuration
files. It would be good if we could keep the project root directory pristine
clean, and refer to the location of `pyproject.toml` by environment variable,
but until that time, we will have to make do with this approach.

### workflow

* clone the repository

```bash
git clone https://github.com/gjvc/gjvc-python-bootstrap.git
```

* initialise the environment

```bash
bin/dev-init
```

* check it works!

```bash
bin/app-main --help
```

* examine the root requirement file:

```bash
$ cat etc/pip-requirement.d/3.13/root 
cmd2==3.2.0
jurigged==0.6.1
pg8000==1.31.5
pipdeptree==2.30.0
psutil==7.2.2
pyright==1.1.408
pytest==9.0.2
PyYAML==6.0.3
```

* add a top-level ("root") requirement

```bash
echo pyyaml >> etc/pip-requirement.d/3.13/root
```

* recreate the environment

```bash
bin/dev-init
```

### files

files in `bin/`

| name               | description                                                   | remarks |
|--------------------|---------------------------------------------------------------|---------|
| `.settings`        | contains `python_version`; unlikely to contain much more      |         |
| `.env`             | contains environment variables; unlikely to grow              |         |
| `bin/app-main`     | run `src/python/main/app/main/main.py` via `bin/venv-python3` |         |
| `bin/dev-clean`    |                                                               |         |
| `bin/dev-init`     |                                                               |         |
| `bin/functions`    |                                                               |         |
| `bin/run-tests`    |                                                               |         |
| `bin/settings`     |                                                               |         |
| `bin/venv-bin`     | run files from `.venv/bin/`                                   |         |
| `bin/venv-freeze`  |                                                               |         |
| `bin/venv-install` |                                                               |         |
| `bin/venv-pip3`    | run `.venv/bin/pip3` via `bin/venv-bin`                       |         |
| `bin/venv-python3` | run `.venv/bin/python3` via `bin/venv-bin`                    |         |

`bin/venv-pip3` and `bin/venv-python3` passes custom argumentsdoes so
optionally, based on the value of the environment variable `JURIGGED`. These
are two simple examples of being able to enforce uniform execution within the
context of the `.venv/` directory.

### `etc/`

| name                                     | category | remarks |
|------------------------------------------|----------|---------|
| `etc/pip/requirement.d/3.13/bootstrap`   |          |         |
| `etc/pip/requirement.d/3.13/pylock.toml` |          |         |
| `etc/pip/requirement.d/3.13/root`        |          |         |
| `etc/pip/requirement.d/3.13/versions`    |          |         |

### application entry points

* `bin/app-main` -- run `src/python/main/app/main/main.py` via `bin/venv-python3`

### examples

### assumptions

* You are using Python 3.13 (change it in `.settings`)

### cold start

bootstrap the `.venv/` directory using the contents of `etc/pip-requirement.d/3.13-bootstrap`

```bash
bin/dev-init
```

### manually install the python package `mypy`

Install via "pip" and then re-create the environment. The "root" file will get
updated with the new package and version, int this case the latest version.

```bash
bin/venv-pip3 install mypy
bin/dev-init
```

### update versioned requirements list file

update the contents of `etc/pip/requirement.d/3.13/versions`

```bash
bin/dev-init
```

---

### wrapper scripts

### development convenience scripts

* `bin/dev-init` -- create `.venv/` and install packages from `etc/pip/requirement.d/3.13`
* `bin/venv-pip3` -- run `.venv/bin/pip3`
* `bin/venv-run` -- run files from `.venv/bin/`

### venv wrapper scripts

* `bin/venv-python3` -- run `.venv/bin/python3` with environment
* `bin/venv-bin` ${1} -- run `.venv/bin/${1}` with environment

### application entry points

* `bin/run-main` -- run `src/python/app/main/main.py`

---

## CONTENTS

---

### objective / summary

### `bin/`

A layered set of shell scripts for managing a Python 3.13 venv-based project.
They all share a common preamble (`set -o errexit -o nounset -o pipefail`,
resolve `_root` from script location).

- settings -- Defines the Python version (3.13), resolves the python3 binary, and sets paths to files under
  `etc/pip-requirement.d/3.13/` (packages, packages.root, packages.deps, pylock_toml).
- functions -- Provides `banner()` and `heading()` helpers for formatted terminal output.

Core scripts

- `dev-init` -- The main setup/update script. It:
    * Creates `.venv/` if missing, installs from bootstrap.
    * Chooses the best requirement file to install from: prefers roots if newer than versions, otherwise falls back
      through `versions` -> `roots` -> `bootstrap`.
    * Installs dependencies, then freezes the environment twice via `pipdeptree --freeze` -- writing `versions` (pinned
      with full dep tree), `roots` (top-level packages only, extracted with awk), and `pylock.toml` (via pip3 lock).
    * Re-installs from `roots` to ensure consistency, then freezes again.
    * Shows `git diff` of the pip-requirement directory at each step.
- `dev-clean` -- Removes `.pyc` files, `__pycache__` dirs, and wipes `.pip/`, `.pytest/`, `.venv/` entirely.

Execution wrappers (in `bin/`)

- `venv-bin` -- Runs any binary from `.venv/bin/` with a controlled environment: `PYTHONDONTWRITEBYTECODE=1`,
  `PYTHONHASHSEED=0`,  `PYTHONNOUSERSITE=1`, PYTHONPATH pointing to `src/python/main`. Exits silently if no argument
  given.
- `venv-python3` -- Runs Python through `venv-bin`, optionally with https://github.com/breuleux/jurigged hot-reloading (
  `JURIGGED=1` by default, disable with `JURIGGED=0`).
- `venv-pip3` -- Runs pip through venv-bin with a local cache dir at `.pip/cache/`.
- `app-main` -- Runs the application (`src/python/main/app/main/main.py`) via `venv-python3` in a scrubbed environment (
  `env --ignore-environment`), passing only `COLUMNS`, `HOME`, `ROWS`.
- `run-tests` -- Runs pytest via venv-bin with `JURIGGED=0`.

`etc/pip-requirement.d/3.13/` -- Dependency files

Four files maintained by `dev-init` in `etc/pip-requirement.d/3.13/`

| file                 | generated? | contents                                                                        | 
|----------------------|------------|---------------------------------------------------------------------------------|
| `packages.bootstrap` | no         | top-level initial packages -- the set for bootstrapping via the `.venv/` setup. |
| `packages.root`      | yes        | list of top-level packages only (e.g. `jurigged==0.6.1`).                       |
| `packages.deps`      | yes        | full dependency tree with pinned versions, indented to show the hierarchy       |
| `pylock.toml`        | yes        | PEP 751-format lock file with wheel URLs and SHA-256 hashes for all packages.   |

The flow is: packages.bootstrap (human-curated) -> `dev-init` resolves and installs -> writes roots, versions, and
pylock.toml (
all machine-generated). The roots vs. versions freshness comparison drives whether `dev-init` installs from the full
tree or just top-level roots on subsequent runs.

### `packages.bootstrap`

* `pipdeptree` -- displays installed python packages in form of a dependency tree
* `jurigged` -- hot-reload
* `pyright` -- static type checker
* `pytest` -- de-facto testing framework
* `pyyaml` -- yaml format

