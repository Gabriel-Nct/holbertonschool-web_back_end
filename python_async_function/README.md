# Python Async Function

## Description

This project covers asynchronous programming in Python using the `asyncio` module. It focuses on writing asynchronous coroutines, executing concurrent functions, creating asyncio tasks, and understanding the fundamentals of asynchronous execution in Python.

## Learning Objectives

By the end of this project, you should be able to:

- Understand and use `async` and `await` syntax
- Execute asynchronous programs with `asyncio`
- Run concurrent coroutines efficiently
- Create and manage `asyncio` tasks
- Use the `random` module for generating random values

## Requirements

### General

- All files interpreted/compiled on Ubuntu 20.04 LTS using Python 3.9
- All files must end with a new line
- All files must be executable
- First line of all files should be exactly `#!/usr/bin/env python3`
- Code should follow pycodestyle style (version 2.5.x)
- All functions and coroutines must be type-annotated
- All modules should have documentation
- All functions should have documentation

## Tasks

### 0. The basics of async

**File**: `0-basic_async_syntax.py`

Write an asynchronous coroutine `wait_random` that:

- Takes an integer argument `max_delay` (default value: 10)
- Waits for a random delay between 0 and `max_delay` seconds (inclusive, float value)
- Returns the delay value

### 1. Concurrent coroutines

**File**: `1-concurrent_coroutines.py`

Import `wait_random` from the previous file and write an async routine `wait_n` that:

- Takes 2 integer arguments: `n` and `max_delay`
- Spawns `wait_random` `n` times with the specified `max_delay`
- Returns a list of all the delays (float values) in ascending order without using `sort()`

### 2. Measure the runtime

**File**: `2-measure_runtime.py`

Import `wait_n` from the previous file and create a function `measure_time` that:

- Takes integers `n` and `max_delay` as arguments
- Measures the total execution time for `wait_n(n, max_delay)`
- Returns `total_time / n` as a float
- Uses the `time` module to measure an approximate elapsed time

### 3. Tasks

**File**: `3-tasks.py`

Import `wait_random` from the first file and write a function `task_wait_random` that:

- Takes an integer `max_delay`
- Returns an `asyncio.Task` object
- Uses regular function syntax (not async)

### 4. Tasks (advanced)

**File**: `4-tasks.py`

Take the code from `wait_n` and alter it into a new function `task_wait_n` that:

- Has the same functionality as `wait_n`
- Uses `task_wait_random` instead of `wait_random`

## Resources

- [Async IO in Python: A Complete Walkthrough](https://realpython.com/async-io-python/)
- [asyncio - Asynchronous I/O](https://docs.python.org/3/library/asyncio.html)
- [random.uniform](https://docs.python.org/3/library/random.html#random.uniform)

## Repository Information

- GitHub repository: `holbertonschool-web_back_end`
- Directory: `python_async_function`
