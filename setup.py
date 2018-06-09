import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyLoRa_pkg",
    version="0.0.6",
    author="Rui Silva",
    author_email="ruisilva.real@sapo.pt",
    description="This is a python interface to the Ai-Thinker Ra-02 Modules LoRa long range, low power transceiver family. This module uses SX1278 IC and works on a 433MHz frequency.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rpsreal/pySX127x",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3.0",
        "Operating System :: Raspbian",
    ),
)
