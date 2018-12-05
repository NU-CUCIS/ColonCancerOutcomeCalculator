# Colon Cancer Outcome Calculator

This calculator is published at (http://info.eecs.northwestern.edu/ColonCancerOutcomeCalculator)

## Run instructions:
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
	
Step 3. Run the backend code by executing the <code>\_\_init\_\_.py</code> file

## Notes:

1. The templates directory contains a directory called meta_files. This directory contains files for each dropdown list in the page. It follows the below convention. The post attributes used in the html code use the dropdown_list_label as the attribute name. If the label has multiple words only the first word is used. e.g Primary Site will be just Primary

	dropdown_list_label#code#text_associated with the code#flag used to keep track of selection.
	<code>e.g. Behavior#1#malignant potential, and uncertain malignant potential#0</code>

2. If a flask.wsgi is needed, place the file flask.wsgi after changing the path in it in the apache web server path. i.e. the colon_cancer and flask.wsgi reside in the same directory
