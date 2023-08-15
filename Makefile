# Define the name of your virtual environment
VENV_NAME := music_dl

# Define the Python interpreter to use
PYTHON := python3

# Create the virtual environment
venv:
	$(PYTHON) -m venv $(VENV_NAME)

# Install dependencies from requirements.txt
install:
	$(VENV_NAME)/bin/pip install -r requirements.txt

# Run your Python script inside the virtual environment
run:
	$(VENV_NAME)/bin/python main.py

execute:
	make venv
	make install
	$(VENV_NAME)/bin/ytmusicapi oauth

# Clean up the virtual environment
clean:
	rm -rf $(VENV_NAME)

# Help target to display available targets
help:
	@echo "Available targets:"
	@echo "  make venv        - Create virtual environment"
	@echo "  make install     - Install dependencies from requirements.txt"
	@echo "  make run         - Run your Python script inside the virtual environment"
	@echo "  make clean       - Clean up virtual environment"
	@echo "  make execute     - Creates the venv, install and generates the credentials"
	@echo "  make help        - Display this help message"
