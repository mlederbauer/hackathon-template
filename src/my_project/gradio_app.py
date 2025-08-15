"""Simple Gradio web interface for the LLM app.

Please do customize a lot of this: colors,themes, boxes, ... !
You can also add more features, e.g. a chat history,
a way to upload files, choose different models, ...

Check out the documentation: https://www.gradio.app/docs/
Customize themes here: https://www.gradio.app/guides/theming-guide
"""

import gradio as gr

from my_project.llm_client import generate_response


def create_gradio_app():
    """Create and launch Gradio app."""
    # Simple chat interface
    with gr.Blocks(title="LLM App Template", theme=gr.themes.Soft()) as app:
        gr.Markdown("# LLM App Template")
        gr.Markdown("Enter your prompt and get a response!")

        with gr.Row():
            with gr.Column():
                input_text = gr.Textbox(
                    label="Your Prompt",
                    placeholder="Enter your question here...",
                    lines=3,
                )
                submit_btn = gr.Button("Generate Response", variant="primary")

            with gr.Column():
                output_text = gr.Textbox(
                    label="AI Response", lines=10, interactive=False
                )

        # Connect the button to the function
        submit_btn.click(fn=generate_response, inputs=input_text, outputs=output_text)

        # Example prompts
        gr.Examples(
            examples=[
                "Explain quantum computing in simple terms",
                "Write a short poem about AI",
                "What are the benefits of renewable energy?",
                "How does machine learning work?",
            ],
            inputs=input_text,
        )

    return app
