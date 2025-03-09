### Python api automation Framework
Hybrid Custom API automation framework include the proper folder structure.

Tech Stack
-Python 3.13
-Requests-Http requests
-pytest-testing framework
-Reporting-Allure Report, pytest Html
-test data-csv,Excel
-parallel Execution-x distribute(xdist)
-Advance Api testcase-jsonschema

How to install packages:

pip install requests pytest pytest-html faker allure-pytest jsonschema

How to run the basic test with Allure report:

pytest -s  src/tests/crud/test_create_booking.py --alluredir=allure_result
allure serve allure_result

pip install pytest-xdist

