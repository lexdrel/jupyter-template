.PHONY: token install lints test

# Default target
all: token install lints test

# Target to get the Jupyter Notebook token and connection URL
token:
	@echo "--- Jupyter Notebook Server Info ---"
	@jupyter server list
	@echo ""
	@echo "--- Connection URL for Host ---"
	@jupyter server list | grep -o 'token=[a-z0-9]*' | cut -d= -f2 | xargs -I{} echo "http://127.0.0.1:8888/?token={}"
	@echo "--- Toke to copy: ---"
	@jupyter server list | grep -o 'token=[a-z0-9]*' | cut -d= -f2

install:
	pip install -r requirements.txt

lints:
	@echo "--- Running Vulture (Dead Code Analysis) ---"
	vulture .
	@echo ""
	@echo "--- Running Black (Formatter) ---"
	black .
	@echo ""
	@echo "--- Running Ruff (Linter) ---"
	ruff check .

test:
	@echo "--- Running Tests ---"
	export PYTHONPATH=. && pytest tests/ -v
