venv-setup:
	python3 -m venv env && source env/bin/activate && pip install --upgrade pip -r requirements.txt
	. env/bin/activate
run:
	python3 import-mappings.py ${INSTALLER_HOST} ${WIREMOCK_PORT}
