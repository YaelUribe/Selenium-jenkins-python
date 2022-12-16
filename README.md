# DVORA AUTOMATION TESTS

This project is made on python3.8 with selenium and pytest for testing dvora web app and mobile app.

## Usage

First activate the virtual environment with
``source venv/bin/activate `` 

### Web tests

to run the tests on web on the root folder run the command

``pytest -v --alluredir=./reports/web  tests_web/ ``

the `--alluredir ` is for adding the reports 
after the tests finish to see the reports type `allure serve` and it will create a server and show the results

to run specific tests add the files you want to specifically test
`` pytest -v --alluredir=./reports/mobile  tests_mobile/test_log_in.py tests_mobile/test_events_tenant.py``

### Mobile Test

The mobile app is development on ionic to run the mobile ui tests first you need to install mobile app and install all the requirements with ```npm install``` 
