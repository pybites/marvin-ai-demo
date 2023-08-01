"""Implements a simplistic streamlit app that leverages MarvinAI to handle birthday wishes."""

import datetime

import marvin
from dotenv import dotenv_values
from marvin import ai_fn, ai_model
from pydantic import BaseModel, Field

config = dotenv_values("../.env") 

marvin.settings.openai.api_key = config["OPENAI_KEY"]


@ai_model
class BirthdayContact(BaseModel):
    first_name: str
    last_name: str
    birthday_date: datetime.date = None
    origin: str  = Field(..., description="Where do I know this person from?")
    humor: str = Field(..., description="The kind of humor the person likes.")
    misc: str = Field(..., description="Any additional information given in the text.")
    telephone_number: str = Field(..., description="The telephone number of the contact.")

@ai_fn
def generate_wish(birthday_contact: BirthdayContact) -> str:
    """Based on the `birthday_contact` generate a birthday wish, 
    adjusted based on the `birthday_contact.humor`. 
    Then, kindly ask a question based on `birthday_contact.misc`."""


