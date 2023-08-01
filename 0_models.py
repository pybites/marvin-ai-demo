import marvin
from marvin import ai_model
from pydantic import BaseModel, Field

from setup import config

marvin.settings.openai.api_key = config["OPENAI_KEY"]

@ai_model
class Location(BaseModel):
    city: str
    state: str = Field(..., description="The two-letter state abbreviation")
    latitude: float
    temperature: float = Field(..., description="The mean temperature in Fahrenheit")


# print(Location("Eiffel Tower"))
print(Location("Brandenburger Tor"))
print(Location("Museo Nacion"))
