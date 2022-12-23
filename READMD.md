# LAB - Class 4

## Project: Pythonic Garage Band

## Author: Harper Foley

## Links and Resources

* [GitHub Repo](https://github.com/hfoley2013/pythonic-garage-band)

### Setup

* Create a local repository on your machine
* Create a virtual environment on your machine
  * `python3 -m venv .venv`
  * NOTE: Replace `python3` with specific version of Python you are using
* Activate the virtual environment
  * `source .venv/bin/activate`
* Install the following packages:
  * `pip install pytest`
  * `pip install pytest-watch`
* Clone down the repo onto your local machine
  * `https://github.com/hfoley2013/pythonic-garage-band.git`

### How to initialize/run your application (where applicable)

* We use `pytest-watch` to run our tests in this program
* You can activate `pytest-watch` by running that command in the terminal
  * Any failed tests will populate as red
  * Any passed tests will populate as green

### Tests

* We conducted the tests in this program using `pytest`
* The tests for the musician classes `Guitarist`, `Bassist`, and `Drummer` were set up to verify that each instance of a musician received the appropriate attributes from the parent class `Musician` and that the appropriate instrument and instrument solo were passed to the child class
* The tests for the `Band` class ensure that the name of the band and band members are passed to the class with the appropriate attributes
* 14 tests total were conducted
