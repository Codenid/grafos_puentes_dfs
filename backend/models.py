from pydantic import BaseModel
from typing import List

class GraphRequest(BaseModel):
    nodes: int
    edges: List[List[int]]

class BridgeResponse(BaseModel):
    bridges: List[List[int]]
