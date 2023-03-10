from pydantic import BaseModel, Field, validator
from typing import List
import re


class ConverterInput(BaseModel):
    price: float = Field(gt=0)
    to_currencies: List[str]

    @validator('to_currencies')
    def validate_to_currencies(cls, value):
        for currency in value:
            if not re.match('^[A-Z]{3}$', currency):
                raise ValueError(f'Formato de moeda {currency} inválido')
        return value


class ConverterOutput(BaseModel):
    message: str
    data: List[dict]


"""
Body esperado na request:
{
    "price": 5.55,
    "to_currencies": ["USD", "EUR", "GBP"]
}

"""
