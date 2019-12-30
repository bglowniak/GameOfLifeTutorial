# Cellular Automata and Game of Life

This 3-part tutorial examines the use of cellular automata as a simple yet powerful modeling technique for discrete systems. We utilize John Conway's Game of Life, a well-known example of this approach, as a vehicle to first explore the basic concepts, then to investigate methods of analyzing and expanding upon it.

The tutorial entrance point can be found in [notebooks/part0--navigator.ipynb](notebooks/part0--navigator.ipynb)

## Tutorial Contents
* [Part 1 - Introduction to CA and Game of Life](notebooks/part1--ca_intro.ipynb): This first tutorial explores the basic methodologies and terminologies of cellular automation as well as introducing Game of Life via a Python implementation.


* [Part 2 - Expansions to Cellular Automata](notebooks/part2--Expansions_to_CA.ipynb) - This tutorial experiments with extensions to the Game of Life, showing ways to explore and improve upon cellular automata.


* [Part 3 - Exploring Patterns in Game of Life](notebooks/part3--patterns.ipynb) - In this final tutorial, we investigate how complex behavior and patterns can emerge in even a simple CA. We use [Golly](http://golly.sourceforge.net/), an open-source program for visualizing Game of Life, to assist in investigating the more complicated patterns.

## Scripts
Throughout this tutorial, we will occasionally make reference to auxiliary files.

* *[conway_basic.py](scripts/conway_basic.py)* - a barebones implementation of Conway's Game of Life. The functions in this file provide ways to generate, update, and visualize a progression of Game of Life from a random initial state and are used as boilerplate functions in other files.


* *[pattern_worlds.py](scripts/pattern_worlds.py)* - provides hardcoded initialization functions for various patterns (fixed, oscillator, pulsar, glider, and glider gun).


* *[conway_patterns.py](scripts/conway_patterns.py)* - uses the initialization functions from pattern_worlds to generate a limited number of timesteps for each pattern to demonstrate behavior.


* *[interactive_timeseries.py](scripts/interactive_timeseries.py)* - uses helper functions from other files to generate an initial state and a series of timesteps for Game of Life. It allows for parameter modification and for interactive exploration using the arrow keys.


* *glider_guns.rle* - a save file for Golly containing two glider guns.

The interested reader is invited to explore these files to gain further insight into CA and Game of Life.

## Informal References

* *Introduction to the Modeling and Analysis of Complex Systems* - Hiroki Sayama, Chapters 11-12. https://textbooks.opensuny.org/introduction-to-the-modeling-and-analysis-of-complex-systems/
* *A New Kind of Science* - Stephen Wolfram. https://www.wolframscience.com/nks/
* *Cellular Automata* - Stephen Wolfram. https://www.stephenwolfram.com/publications/cellular-automata-complexity/pdfs/cellular-automata.pdf
* *Implementation of logical functions in the Game of Life* - Jean-Philippe Rennard. https://www.rennard.org/alife/CollisionBasedRennard.pdf

## Contributors

This project was developed by Brian Glowniak and Joel Katz, two CS undergraduate students at Georgia Tech, for CX 4230/CSE 6730 Computer Simulation during Spring 2019.
