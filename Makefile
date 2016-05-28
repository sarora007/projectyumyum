install:
	pip install -r requirements.txt -t lib/
test:
	dev_appserver.py .
deploy:
	appcfg.py -A project-yumyum -V v1 update .
