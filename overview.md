### overview

---


● Here's an overview of the project's tooling:

### `bin/`

A layered set of shell scripts for managing a Python 3.13 venv-based project. They all share a common preamble (`set -o
errexit -o nounset -o pipefail`, resolve _`root` from script location).

Shared infrastructure

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

The flow is: bootstrap (human-curated) -> `dev-init` resolves and installs -> writes roots, versions, and pylock.toml (
all machine-generated). The roots vs. versions freshness comparison drives whether `dev-init` installs from the full
tree or just top-level roots on subsequent runs.

### `packages.bootstrap`

* `pipdeptree`
* `jurigged`
* `pyright`
* `pytest`
* `pyyaml`
