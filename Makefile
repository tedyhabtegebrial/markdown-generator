init:
	pip install -r requirements.txt
	
lint:
	flake8

test:
	python -m pytest
	coverage run -m pytest -v

clean:
	rm -rf dist/*

package: init lint test clean
	python setup.py sdist

publish: package
	twine upload dist/*
