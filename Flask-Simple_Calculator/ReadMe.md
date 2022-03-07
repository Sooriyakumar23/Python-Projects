#### Simple_Calculator
- Flask [Micro web framework] based simple 2 numbers arithmetic calculator written in python using HTML and CSS web page languages
# 1. static
    contains 2 CSS files to decorate 'index.html' and "results.html"
# 2. templates
    contains 'index.html' and "results.html" to provide UI to the local web page
# 3. app.py
    Backend flask based python file conducts the session
# 4. app_flask.py
    Intermediate flask based python for debug with postman
# 5. calculator.py
    Initial OOP based python file to create class for arithmetic operations
# 6. calculator_args.py
    calculator.py program but built to use it in terminal using |argpase| python library
### How to run ?
- Download this git repo as a zip file and unzip it into a folder
- Open a comfortable python IDE in that folder
    * select interpretar for PyCharm IDE
- "pip install flask" in the terminal to the environment
- run "app.py" in your IDE
- open the local host link in any of a web browser
- Now, you can see a home page
- add "calc" in the url to redirect the page
- Select 1 out of 4 operation you wish to do in this page
- Input any two numbers
- press "calculate" button to submit
- These 3 data will be passed to the backend(python) and will be unleashed the result in a page

| Technologies used |
* Flask
* PyCharm
* Postman
* HTML
* CSS
* OOP in python
* argparse python library
