import asyncio

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, PlainTextResponse

app = FastAPI()

@app.get("/", response_class=PlainTextResponse)
async def root():
    return "Hello world"


@app.get("/new", response_class=PlainTextResponse)
async def new():
    return "fastapi redirect target"


@app.get("/large-text", response_class=PlainTextResponse)
async def large_text():
    return "fastapi-e2e " * 2000


@app.get("/headers-source", response_class=PlainTextResponse)
async def headers_source():
    return PlainTextResponse(
        "headers source",
        headers={"X-Delete-Me": "upstream-value"},
    )


@app.get("/slow-response", response_class=PlainTextResponse)
async def slow_response(delay: float = 2.0):
    await asyncio.sleep(delay)
    return "slow response completed"


@app.post("/echo-size", response_class=JSONResponse)
async def echo_size(request: Request):
    body = await request.body()
    return {"size": len(body)}
