from fastapi import APIRouter
from uuid import uuid4

from app.schemas.bid import BidRequest
from app.services.rule_engine import generate_recommendation

router = APIRouter()

bids: dict = {}


@router.post("/bids")
def create_bid(bid: BidRequest):
    bid_id = str(uuid4())

    result = generate_recommendation(
        gen_volume=bid.gen_volume,
        load_volume=bid.load_volume,
        price_band=bid.price_band,
    )

    bids[bid_id] = {
        "status": "completed",
        "input": bid.model_dump(),
        "result": result,
    }

    return {
        "bid_id": bid_id,
        "status": "completed",
        "result": result,
    }


@router.get("/bids/{bid_id}")
def get_bid(bid_id: str):
    return bids.get(bid_id, {"error": "Bid not found"})