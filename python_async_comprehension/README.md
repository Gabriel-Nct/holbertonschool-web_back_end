# Python Async Comprehension 🔄✨

## Overview 🌟

This project explores Python's asynchronous programming capabilities, focusing on asynchronous comprehensions and generators. Through practical tasks, you'll learn how to write and use asynchronous generators, implement async comprehensions, and properly type-annotate asynchronous code. Asynchronous programming is a powerful paradigm that allows your code to perform multiple operations concurrently without using threading or multiprocessing!

## Learning Objectives 🎯

By the end of this project, you will be able to:

- Write asynchronous generators 📝
- Use async comprehensions 🔄
- Apply type annotations to generators and async functions 🏷️
- Understand parallel execution in asynchronous Python code ⚡
- Implement efficient non-blocking code patterns 🚀
- Master the use of asyncio for concurrent operations 🧩
- Appreciate the performance benefits of asynchronous programming 📈

## Requirements 📋

- Python 3.9 (Ubuntu 20.04 LTS) 🐍
- PEP 8 style compliance (pycodestyle version 2.5.x) ✅
- Proper documentation for all modules and functions 📚
- Type annotations for all functions and coroutines 🏷️
- All files must end with a new line 📄
- First line of all files must be exactly `#!/usr/bin/env python3` 🔝
- A README.md file is mandatory for the project root 📑
- Code length will be tested using `wc` command 📏

## Tasks 📝

### 0. Async Generator ⏱️

**File:** `0-async_generator.py`

Implement a coroutine called `async_generator` that:

- Takes no arguments ❌
- Loops 10 times 🔄
- Asynchronously waits 1 second each iteration ⏰
- Yields a random number between 0 and 10 each time 🎲
- Uses the random module 🔀

### 1. Async Comprehensions 🧠

**File:** `1-async_comprehension.py`

Create a coroutine called `async_comprehension` that:

- Takes no arguments ❌
- Collects 10 random numbers using an async comprehension over the `async_generator` function 📊
- Returns the list of 10 random numbers 📋

### 2. Run time for four parallel comprehensions ⚡

**File:** `2-measure_runtime.py`

Write a `measure_runtime` coroutine that:

- Executes `async_comprehension` four times in parallel using `asyncio.gather` 🔄
- Measures and returns the total runtime ⏱️
- The total runtime should be approximately 10 seconds (and you should understand why) 🤔

**Think about it:** Why is the runtime around 10 seconds when we're running four tasks that each take about 10 seconds? That's the power of asynchronous programming! ✨

## Resources 📚

- [PEP 530 – Asynchronous Comprehensions](https://peps.python.org/pep-0530/) 📄
- [What's New in Python: Asynchronous Comprehensions / Generators](https://docs.python.org/3/whatsnew/3.6.html#pep-530-asynchronous-comprehensions) 🆕
- [Type-hints for generators](https://docs.python.org/3/library/typing.html#typing.Generator) 🏷️
- [Python asyncio documentation](https://docs.python.org/3/library/asyncio.html) 🔄
- [Real Python's Guide to Async/Await](https://realpython.com/async-io-python/) 🐍
- [Python's random module](https://docs.python.org/3/library/random.html) 🎲

## Key Concepts 🔑

- **Asynchronous Programming**: Allows your code to perform operations concurrently
- **Coroutines**: Functions that can pause execution and yield control back to the caller
- **async/await syntax**: Modern Python syntax for working with coroutines
- **Generators**: Functions that yield values one at a time
- **Comprehensions**: Compact syntax for creating collections

## Implementation Tips 💡

- Use `asyncio.sleep()` for simulating time-consuming I/O operations
- Remember that `async for` is used to iterate over asynchronous generators
- Use `time.perf_counter()` for accurate performance measurements
- Type annotations for async functions can use `AsyncGenerator` from typing
