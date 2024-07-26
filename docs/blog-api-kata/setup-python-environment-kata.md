# Setup Python Environment Kata



## Create the Project Directory

```bash
mkdir blog-api
cd blog-api
```

## Create `README.md` File

```md
# drf-kata
Learn Django Rest Framework and Django through katas
```



## Create `LICENSE` file

```
Creative Commons Legal Code

CC0 1.0 Universal
..............
```



## Initialize a Git Repository (Optional)

```bash
git init
```

## Create `.gitignore` File

```gitignore
.venv*/
.dev*/
.vscode/

# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Packages
*.egg
*.egg-info
dist
build
eggs
parts
var
sdist
wheels
*.pip
*.tox
.coverage
.hypothesis/

# Virtual environments
.venv
env/
venv/
ENV/

# IDEs and editors
.vscode/
.idea/
```



## Create Python Virtual Environment

```bash
py -3.10 venv .venv310
```

## Activate Virtual Environment in VSCode

1. Open the project directory with VSCode.
2. Select Interpreter - select the virtual environment
3. Open a terminal - virtual environment should be automatically activated in the terminal

Further continue working in the terminal.

## Upgrade `pip`

```bash
python -m pip install --upgrade pip
```



## Install VSCode Extensions

Install following recommended extensions:

1. Even Better TOML
2. Ruff
3. Better Comments
4. REST Client
5. DotENV
6. EditorConfig for VS Code
7. GitLens
8. Live Preview or Live server
9. Python



## Create `pyproject.toml` file

Create `pyproject.toml` file in the root of your project directory

```toml
[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "drfblog"
version = "0.1.0"
description = "Blog API with Django Rest Framework"
readme = "README.md"
license = {file = "LICENSE"}

authors = [
    {name="Your Name", email="you@example.com"}
]
dependencies = [
    "python-dotenv",
]

[project.optional-dependencies]
dev = [
    "pytest",
    "pytest-cov",
]

[tool.setuptools.packages.find]
where = ["src"]

```

For more info on pyproject.toml, see [Writing your pyproject.toml](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)

We are not using `setup.cfg` in our project.

Dependencies:

* [dotenv](https://github.com/theskumar/python-dotenv)
* [pytest](https://docs.pytest.org/en/latest/)
* [pytest-cov](https://github.com/pytest-dev/pytest-cov)

## Install Dev Dependencies

Install the package and its dependencies in editable mode.

```bash
pip install -e .[dev]
```

## Create Simple Test

Create file `src/tests/simple_test.py`:

```python
def hello():
    print("Hello, world!")

def test_hello(capsys):
    hello()
    captured = capsys.readouterr()
    assert captured.out == "Hello, world!\n"
```



## Configure Tests in VSCode

Modify `.vscode/settings.json` to point to `src/tests`

```json
{
    "python.testing.pytestArgs": [
        "src/tests"
    ],
    "python.testing.unittestEnabled": false,
    "python.testing.pytestEnabled": true
}
```

## Execute the Test

```bash
pytest src/tests
```

## Code Repository

You can find completed kata in the [setup-python-environment](https://github.com/ivangeorgiev/drf-kata/tree/kata/setup-python-environment) branch of the [GitHub repository](https://github.com/ivangeorgiev/drf-kata).
