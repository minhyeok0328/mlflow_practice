from pydantic import BaseModel

# FastAPI에서 REST API
class NLPDataInput(BaseModel):
    text: list[str]
    username: str


class NLPDataOutput(BaseModel):
    model_name: str
    text: list[str]
    labels: list[str]
    scores: list[float]
    prediction_time: int    