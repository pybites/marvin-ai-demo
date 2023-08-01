"""Introduces MarvinAI models. For more info, see https://www.askmarvin.ai/src/docs/components/ai_application/."""
from datetime import datetime

import marvin
from marvin import AIApplication
from pydantic import BaseModel, Field

from setup import config

marvin.settings.openai.api_key = config["OPENAI_KEY"]

# create models to represent the state of our ToDo app
class ToDo(BaseModel):
    title: str
    description: str = None
    due_date: datetime = None
    done: bool = False


class ToDoState(BaseModel):
    todos: list[ToDo] = []


# create the app with an initial state and description
todo_app = AIApplication(
    state=ToDoState(),
    description=(
        "A simple todo app. Users will provide instructions for creating and updating"
        " their todo lists."
    ),
)

# invoke the application by adding a todo
response = todo_app("I need to go to the store tomorrow at 5pm")


print(
    f"Response: {response.content}\n",
)
print(f"App state: {todo_app.state.json(indent=2)}")

# complete the task
response = todo_app("I already went")


print(f"Response: {response.content}\n")
print(f"App state: {todo_app.state.json(indent=2)}")
