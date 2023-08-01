"""Introduces MarvinAI functions. For more info, see https://www.askmarvin.ai/src/docs/components/ai_function/."""
import marvin
from marvin import ai_fn

from setup import config

marvin.settings.openai.api_key = config["OPENAI_KEY"]

@ai_fn
def sentiment_list(texts: list[str]) -> list[float]:
    """
    Given a list of `texts`, returns a list of numbers between 1 (positive) and
    -1 (negative) indicating their respective sentiment scores.
    """

@ai_fn
def return_fruits(number: int) -> list[str]:
    """Returns a list of `number` fruits. Use a temperature of 0."""

print(sentiment_list(
    [
        "That was surprisingly easy!",
        "Oh no, not again.",
    ]
))


print(return_fruits(4), return_fruits(2
                                      ))
