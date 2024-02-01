#!/bin/bash
# scripts/start-web-server.py
import src.main


def start_web_server():
    import uvicorn
    uvicorn.run(src.main.app, host="127.0.0.1", port=8000, reload=False)

if __name__ == "__main__":
    start_web_server()