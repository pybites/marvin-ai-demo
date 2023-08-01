"""Introduces MarvinAI classifiers. For more info, see https://www.askmarvin.ai/src/docs/components/ai_classifier/."""
from enum import Enum

import marvin
from marvin import ai_classifier

from setup import config

marvin.settings.openai.api_key = config["OPENAI_KEY"]

@ai_classifier
class AppRoute(Enum):
    """Represents distinct routes command bar for a different application"""

    USER_PROFILE = "/user-profile"
    SEARCH = "/search"
    NOTIFICATIONS = "/notifications"
    SETTINGS = "/settings"
    HELP = "/help"
    CHAT = "/chat"
    DOCS = "/docs"
    PROJECTS = "/projects"
    WORKSPACES = "/workspaces"

print(AppRoute("update my name"))


@ai_classifier
class AppType(Enum):
    web_app = "web app"
    data_app = "data app"
