from fastapi import FastAPI

from app.routes.bids import router as bids_router

app = FastAPI(title="Bid Recommendation Service")


@app.get("/")
def health():
    return {"status": "healthy"}


app.include_router(bids_router)