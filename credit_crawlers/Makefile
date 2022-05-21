create-venv:
	@if [ ! -d venv ]; then\
		python -m venv venv;\
	fi

setup: create-venv
	./venv/bin/pip install -r requirements.txt
	./venv/bin/pip install -r dev_requirements.txt

ipython:
	./venv/bin/ipython

format:
	./venv/bin/black src

lint:
	./venv/bin/flake8 src
	./venv/bin/mypy src

pre-commit: format lint