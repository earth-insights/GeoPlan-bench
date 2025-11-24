from pydantic import BaseModel
from typing import Literal,List,Dict,Any,Optional


class EloAnswerSchema(BaseModel):
  answer: Literal["A", "B", "Tie"]

class ComplexityChoiceSchema(BaseModel):
  complexity: Literal["Simple", "Medium", "Complex"]


class PlanStep(BaseModel):
    tool: str
    parameters: Optional[Dict[str, str]] = None

class PlanSchema(BaseModel):
    plan: List[PlanStep]

