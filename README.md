# Introduction

Exercise is from cs50ai. All provided assets except for the datasets (small + large) has been deleted, since I wanted to practice implementing the everything (data structures, algorithms etc.).<br>

The goal is to find the shortest path between any two actors by choosing a sequence of movies that connects them. For example, the shortest path between Jennifer Lawrence and Tom Hanks is 2: Jennifer Lawrence is connected to Kevin Bacon by both starring in “X-Men: First Class,” and Kevin Bacon is connected to Tom Hanks by both starring in “Apollo 13.”

# Usage

```bash
$ python3 main.py <SOURCE_ID> <DESTINATION_ID>
```

## Example

```bash
$ python3 main.py 102 129
```

prints:

```
Kevin Bacon is connected to Tom Cruise within 17 steps
Movie connection followed:
Diner
Forty Deuce
Enormous Changes at the Last Minute
Footloose
Quicksilver
End of the Line
Lemon Sky
White Water Summer
She's Having a Baby
The Big Picture
Criminal Law
Flatliners
Tremors
He Said, She Said
Pyrates
Queens Logic
A Few Good Men

```

# Setup

## Clone repository

```bash
$ git clone https://github.com/michaelbui99/cs50ai-degrees-graph-excercise.git && cd cs50ai-degrees-graph-exercise
```

## Setup venv

```bash
$ python -m venv venv
```

## Activate venv

```bash
$ source ./venv/bin/activate
```

## Install dependencies

```bash
$ source ./venv/bin/activate
```
