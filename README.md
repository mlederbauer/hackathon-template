# LLM Hackathon Template

A simple template for building LLM applications quickly, for hackathons and rapid prototyping.
This template contains basic LLM client setup, environment variable management, a simple Gradio web interface, and is ready to extend with your features!

## Quick Start

1. **Install dependencies**: Download `uv` [here](https://github.com/astral-sh/uv?tab=readme-ov-file#installation) to install and manage packages (recommended).

   ```bash
   uv sync
   uv pip install -e .
   ```

   (Alternative: create a conda environment and run `pip install -e .`)

2. **Add your API key**:

   ```bash
   cp .env.example .env
   # Edit .env with your API key
   ```

3. **Run the app**:

   ```bash
   uv run main.py
   ```

   (Alternative: run with `python main.py`)

4. **Open your browser** to `http://localhost:7860` to use the web interface!

5. **Customize!** Modify the Gradio app, package structure, and add your own features!

## Adding New Features

```bash
# Add a new package
uv add package-name
```

## Project Structure

```
├── main.py              # Your main application with Gradio
├── notebooks/           # Notebooks for prototyping
├── src/
│   └── my_project/      # Your code goes here
├── .env.example         # Template for API keys
└── pyproject.toml       # Dependencies
```
