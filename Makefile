init:
	pip install -r requirements.txt
	
lint:
	flake8 --exclude __init__.py markdown_generator

test:
	nosetests
