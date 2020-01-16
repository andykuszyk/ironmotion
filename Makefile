shell:
	pipenv shell

init:
	pipenv --two
	pip install -r requirements.txt

listen: 
	python ironmotion.py listen sample/gestures.json
