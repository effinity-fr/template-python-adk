from typing import Dict
import logging
import google.auth

from google.adk.agents.llm_agent import Agent

credentials, project = google.auth.default()

if hasattr(credentials, 'service_account_email'):
    print(f"✅ L'ADK tourne bien avec : {credentials.service_account_email}")
else:
    print("❌ L'ADK utilise votre compte PERSO")


def greet_user(name: str = "User") -> Dict[str, str]:
    """Greets the user."""
    print(f"Tool: greet_user called with name={name}")
    logging.info(f"-----Greeting user with name: {name}")
    return {"greeting": f"Hello, {name}!"}


root_agent = Agent(
    model="{{ cookiebutter.ai_model }}",
    name="{{ cookiecutter.project_slug }}",
    description="{{ cookiecutter.description }}",
    instruction="""
    First Ask User a Name & Start conversation by greeting user with Name by
    using 'greet_user' for greetings.
    After you can helps users with AI related queries.
    """,
    tools=[greet_user],
)
