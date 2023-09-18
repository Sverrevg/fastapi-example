import nox

# A list of all the modules you want to scan:
sourcecode_paths = ["src"]


@nox.session(name="format")
def formatting(session):
    """Format the code and sort imports. Not needed in workflows."""
    session.install("isort", "autoflake")
    session.run("isort", *sourcecode_paths)
    session.run(
        "autoflake",
        "--recursive",
        "--in-place",
        "--remove-unused-variables",
        *sourcecode_paths,
    )


@nox.session(name="quality")
def quality(session):
    """Analyse static code for typing and code smells."""
    session.install("pylint", "mypy", "types-PyYAML")
    session.run(
        "pylint",
        *sourcecode_paths
    )
    session.run(
        "mypy",
        *sourcecode_paths
    )


@nox.session(name="complexity")
def complexity(session):
    """Assess the complexity of the code."""
    session.install("xenon")
    session.run(
        "xenon",
        "--max-absolute B",
        "--max-modules A",
        "--max-average A",
        "src"
    )


@nox.session(name="test")
def test(session):
    """Run all tests with code coverage."""
    session.install("pytest", "fastapi", "httpx", "sqlalchemy", "geoalchemy2", "psycopg2", "starlette", "coverage",
                    "uvicorn", "python-dotenv", "python-dateutil", "python-jose", "passlib[bcrypt]", "python-multipart")
    session.run(
        "coverage",
        "run",
        "-m",
        "pytest",
        "tests/unit"
    )
    session.run(
        "coverage",
        "report",
        "--fail-under=80"
    )
