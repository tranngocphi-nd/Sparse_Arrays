# Technical test : Maison du Monde

## Requirements to run code
- Docker

# Part 1 : Python

## Problem 
Solve this problem : [Sparse Arrays](https://www.hackerrank.com/challenges/sparse-arrays/problem)
##### Argument :
- strings : environment varaible which is define in Dockerfile. Values format : ab,ac,bc,abc,ac
- queries : variable define by user when running the code. Values format : ab,ac,bc,d

## Files
* Dockerfile : to build docker image
* main.py : main file to run python code, the result is presented with an Flask api using Swagger UI
* SparseArray.py : define SparseArray class
* requirements.txt : all the requirement to set up an environment where python code can run

## How to run
1. Open CLI and move to the folder containing all the files.
2. ```docker build . -t test_mdm```
3. ```docker run -p 5000:5000 -t test_mdm```
4. Use your browser to open : http://localhost:5000/
5. Follow the steps in the following images :
![Alt text](image/step_1.png?raw=true)
![Alt text](image/step_2.png?raw=true)

## Expected result
1. If the format of queries is OK
```
{
  "string": [
    "tran",
    "ngoc",
    "phi",
    "tran",
    "ngoc"
  ],
  "queries": [
    "tran",
    "ngoc",
    "phi"
  ],
  "result": {
    "ngoc": 2,
    "tran": 2,
    "phi": 1
  }
}
```

2. Otherwise
```
{
  "string": [
    "tran",
    "ngoc",
    "phi",
    "tran",
    "ngoc"
  ],
  "queries": [
    "tran",
    "ngoc",
    "phiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii"
  ],
  "result": {
    "error": "('size of elements in array must be in [1, 20]',)",
    "traceback": "Traceback (most recent call last):\n  File \"/sparse_array/SparseArray.py\", line 25, in matching_strings\n    raise Exception (\"size of elements in array must be in [1, 20]\")\nException: size of elements in array must be in [1, 20]\n"
  }
}
```

# Part 2 : SQL

## Files

1. SQL.sql

