.PHONY: token

# Default target
all: token

# Target to get the Jupyter Notebook token and connection URL
token:
	@echo "--- Jupyter Notebook Server Info ---"
	@jupyter server list
	@echo ""
	@echo "--- Connection URL for Host ---"
	@jupyter server list | grep -o 'token=[a-z0-9]*' | cut -d= -f2 | xargs -I{} echo "http://127.0.0.1:8888/?token={}"
	@echo "--- Toke to copy: ---"
	@jupyter server list | grep -o 'token=[a-z0-9]*' | cut -d= -f2
