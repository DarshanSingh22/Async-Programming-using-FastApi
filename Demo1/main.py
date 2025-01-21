import os
from fastapi import FastAPI
import requests  # Synchronous HTTP library
import sqlite3   # Synchronous SQLite library
import time      # For Synchronous delay
import httpx     # Asynchronous HTTP library
import aiosqlite # Asynchronous SQLite library
import asyncio   # For Asynchronous delay
import threading

from db_connection import execute_query

app = FastAPI()

THIRD_PARTY_URL = "http://127.0.0.1:8001/third-party-endpoint/sleep"  # Example third-party API
DATABASE_PATH = "sqlite.db"


@app.get('/hello-world')
def hello():
    thread_id = threading.get_ident()  

    print(f"\nThread id: {thread_id}")
    print("Sync Hello world")


@app.get('/async-hello-world')
async def hello():
    thread_id = threading.get_ident()  
    print(f"\nThread id: {thread_id}")
    print("Async Hello world")




@app.get("/non-async")
def correct_sync():
    worker_pid = os.getpid()  
    thread_id = threading.get_ident()  
    print(f"\nWorker PID: {worker_pid}, Thread id: {thread_id}")

    response = requests.get(THIRD_PARTY_URL)  # Blocking call

    return {"data": response.json()}


# Incorrect Implementation: Using a blocking call (requests) in an async endpoint
@app.get("/incorrect-async-blocking-request")
async def incorrect_async():
    worker_pid = os.getpid()  
    thread_id = threading.get_ident()  
    print(f"\nWorker PID: {worker_pid}, Thread id: {thread_id}")

    response = requests.get(THIRD_PARTY_URL)  # Blocking call

    return {"data": response.json()}


# Correct Implementation: Using an asynchronous HTTP client (httpx) in an async endpoint
@app.get("/truely-async")
async def correct_async():
    worker_pid = os.getpid()
    thread_id = threading.get_ident()  
    print(f"\nWorker PID: {worker_pid}, Thread id: {thread_id}")

    async with httpx.AsyncClient() as client:
        response = await client.get(THIRD_PARTY_URL, timeout=50.0)  # Non-blocking call
    
    return {"data": response.json()}


@app.get('/cpu-bound-with-async')
async def incorrect_async_cpu_bound():
    worker_pid = os.getpid()
    thread_id = threading.get_ident()  
    print(f"\nWorker PID: {worker_pid}, Thread id: {thread_id}")

    fibonacci(37)   #blocks the event loop
    
    return {"data": "completed"}


@app.get('/cpu-bound-without-async')
def correct_async_cpu_bound():
    worker_pid = os.getpid()
    thread_id = threading.get_ident()  
    print(f"\nWorker PID: {worker_pid}, Thread id: {thread_id}")
    fibonacci(37)
    return {"data": "completed"}


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)




