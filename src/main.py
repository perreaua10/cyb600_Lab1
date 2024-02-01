from fastapi import FastAPI

app = FastAPI()


@app.get("/api/v1/hello")
async def root():
    return {"message": "This is RunLog, The Ultimate Running Log Experience"}

#hosted simply at https://runlog-api.onrender.com/docs