# Mini Redis – In-Memory Key Value Database

A simplified Redis-like in-memory key-value database built from scratch using Python.

## Features

- TCP socket server
- Concurrent client handling using threads
- SET, GET, DEL, TTL commands
- Key expiration with TTL
- LRU cache eviction
- Background cleanup of expired keys
- Structured logging
- Benchmarking tool
- Automated unit tests

## Architecture

Client → TCP Server → Command Parser → Store → LRU Cache

## Supported Commands

SET key value  
SET key value EX seconds  
GET key  
DEL key  
TTL key  

## Benchmark

Example performance on local machine:

10000 requests in ~0.8 seconds  
~12000 operations per second


## Tech Stack

Python

Socket Programming

Multithreading

LRU Cache

Unit Testing


## Run the Server

python server.py

## Run the client

Then open another terminal and run:

python client.py

You can now execute commands interactively:

Example session:

>> SET name Alice

OK

> GET name

Alice

> SET temp 123 EX 5

OK

> TTL temp

4

> DEL name

1

> GET name

(nil)

## Benchmark

python benchmark.py

## Run Tests

python -m unittest discover tests
