import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="adformclient",
    version="0.1.dev0",
    author="Dean Kondo",
    author_email="deankondo@annalect.com",
    description="Simple wrapper for AdForm API",
    url="https://github.com/accuenmedia/adform-api-client",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6.7",
        "License :: GNU GENERAL PUBLIC LICENSE",
        "Operating System :: OS Independent",
    ],
)
