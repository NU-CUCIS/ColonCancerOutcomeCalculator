# ColonCancerOutcomeCalculator
Colon Cancer Conditional Survival Outcome Calculator

Required Files:
1. flask.wsgi - https://copy.com/i3GsLBsXsggjTcPW
2. colon_cancer.zip - https://copy.com/0nx8tAPanVEtGewY 

Step 1. Install python virtual environment (http://docs.python-guide.org/en/latest/dev/virtualenvs/)

	a. Install virtualenv using pip install virtualenv
	b. change directory to the apache web server and create an application directory e.g. /apache_path/colon_cancer
	c. change directory to the ColonCalc path
	d. create a virtual environment using virtualenv venv
	c. to start the virtual environment use source venv/bin/activate
	e. to stop the virtual environment use deactivate

Step 2. Install all required python packages in the virtual environment
	a. start the virtual environment use source venv/bin/activate
	b. install Flask (http://flask.pocoo.org), sklearn (http://scikit-learn.org/dev/install.html), etc. 

Notes:

1. The templates directory contains a directory called meta_files. This directory contains files for each dropdown list in the page. It follows the below convention. The post attributes used in the html code use the dropdown_list_label as the attribute name. If the label has multiple words only the first word is used. e.g Primary Site will be just Primary

dropdown_list_label#code#text_associated with the code#flag used to keep track of selection
e.g. Behavior#1#malignant potential, and uncertain malignant potential#0

2. Place the file flask.wsgi after changing the path in it in the apache web server path. i.e. the colon_cancer and flask.wsgi reside in the same directory
