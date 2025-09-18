format:
	ruff format

lint:
	ruff check --fix

setup:
	uv pip install -r requirements.txt