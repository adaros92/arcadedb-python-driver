import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="pyarcade",
    version="0.0.1",
    author="Adams Rosales",
    author_email="adams.rosales.92@gmail.com",
    description="A Python driver for ArcadeDB",
    extras_require={
        "test": [
            "pytest",
            "pytest-cov",
            "pytest-clarity",
        ]
    },
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["retry", "requests"],
    url="https://github.com/adaros92/arcadedb-python-driver",
    packages=setuptools.find_packages(),
)
