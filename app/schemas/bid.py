from pydantic import BaseModel


class BidRequest(BaseModel):
    asset_id: str
    interval: str
    gen_volume: float
    load_volume: float
    price_band: float