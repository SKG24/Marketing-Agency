"""email_create_agent: for generating professional email campaigns and outreach drafts"""

from google.adk import Agent

from . import prompt

MODEL = "gemini-2.5-pro-preview-05-06"

email_create_agent = Agent(
    model=MODEL,
    name="email_create_agent",
    instruction=prompt.EMAIL_CREATE_PROMPT,
    output_key="email_create_output",
)
