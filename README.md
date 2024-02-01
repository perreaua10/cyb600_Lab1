# cyb600_Lab1
First Lab for Canisius University CYB600 Lab 1

The task was to create a web server that can be spooled up easily and is also a package that is published to pypi.
Currently I have implemented a simple restful API as my web server, it only has one endpoint at localhost:8000/time

To run the web server: uvicorn main:app --reload (This must be from inside the SRC folder)
Once running, you will find the auto-docs (feature of fastAPI) at localhost:8000/docs
The endpoint which satisfies the lab is at localhost:8000/time
