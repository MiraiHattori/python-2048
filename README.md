# python-2048

## What is 2048?
[2048](https://play2048.co/) is a game with 4x4 tiles.

## How to build the project (tested only on ubuntu 16.04)

``` bash
sudo apt install build-essential cmake python3 python3-dev
git clone --recursive https://github.com/future731/python-2048.git
cd python-2048
mkdir build
cd build/
cmake ..
make -j4
```

## How to run the project

``` bash
cd python-2048/build
python3 ../run.py
```

## How to edit ai program
You should edit `ai.py` only.

`ai.py` must have the following functions.

move() function, which should return "up", "left", "down", "right" or "quit".
initialize\_ai() function
finalize\_ai() function
