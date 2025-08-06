"""LLM App Template - A simple template for building LLM applications."""

from .gradio_app import create_gradio_app
from .llm_client import generate_response

__all__ = ["generate_response", "create_gradio_app"]
