from pydantic import BaseModel
from typing import List


class ConverterInput(BaseModel):
    price: float
    to_currencies: List[str]


"""
Body esperado na request:
{
    "price": 5.55,
    "to_currencies": ["USD", "EUR", "GBP"]
}

"""
