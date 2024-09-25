from fastapi import FastAPI

app = FastAPI(redoc_url=None)

if __name__ == "__main__":
    # Run locally
    import uvicorn

    uvicorn.run(app, port=8000)
else:
    # Run on AWS Lambda
    import mangum

    handler = mangum.Mangum(app)
