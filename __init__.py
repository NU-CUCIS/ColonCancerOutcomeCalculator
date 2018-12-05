
# import flask, render_template to render the html pages, and request to be able to handle post requests between html pages
from flask import Flask, render_template, request

import numpy as np

# import RandomForestClassifier to be able to evaluate models
#from sklearn.ensemble import RandomForestClassifier

# import joblib to be able to load saved sklearn models
from sklearn.externals import joblib


from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.models import model_from_json

# create a flask object
app = Flask(__name__)

# load sklearn saved models
# note this load is only done at the webserver start and will in memory as long as the server is running


model1 = model_from_json(open('templates/models/1_year_model_architecture.json').read())
model1.load_weights('templates/models/1_year_model_weights.h5')
model1.compile(
    loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model1_cond_1 = model_from_json(open('templates/models/1_cond_on_1_year_model_architecture.json').read())
model1_cond_1.load_weights('templates/models/1_cond_on_1_year_model_weights.h5')
model1_cond_1.compile(
    loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model1_cond_2 = model_from_json(open('templates/models/1_cond_on_2_year_model_architecture.json').read())
model1_cond_2.load_weights('templates/models/1_cond_on_2_year_model_weights.h5')
model1_cond_2.compile(
    loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model1_cond_5 = model_from_json(open('templates/models/1_cond_on_5_year_model_architecture.json').read())
model1_cond_5.load_weights('templates/models/1_cond_on_5_year_model_weights.h5')
model1_cond_5.compile(
    loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model2 = model_from_json(open('templates/models/2_year_model_architecture.json').read())
model2.load_weights('templates/models/2_year_model_weights.h5')
model2.compile(
    loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model2_cond_1 = model_from_json(open('templates/models/2_cond_on_1_year_model_architecture.json').read())
model2_cond_1.load_weights('templates/models/2_cond_on_1_year_model_weights.h5')
model2_cond_1.compile(
    loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model2_cond_2 = model_from_json(open('templates/models/2_cond_on_2_year_model_architecture.json').read())
model2_cond_2.load_weights('templates/models/2_cond_on_2_year_model_weights.h5')
model2_cond_2.compile(
    loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model2_cond_5 = model_from_json(open('templates/models/2_cond_on_5_year_model_architecture.json').read())
model2_cond_5.load_weights('templates/models/2_cond_on_5_year_model_weights.h5')
model2_cond_5.compile(
    loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model5 = model_from_json(open('templates/models/5_year_model_architecture.json').read())
model5.load_weights('templates/models/5_year_model_weights.h5')
model5.compile(
    loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model5_cond_1 = model_from_json(open('templates/models/5_cond_on_1_year_model_architecture.json').read())
model5_cond_1.load_weights('templates/models/5_cond_on_1_year_model_weights.h5')
model5_cond_1.compile(
    loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model5_cond_2 = model_from_json(open('templates/models/5_cond_on_2_year_model_architecture.json').read())
model5_cond_2.load_weights('templates/models/5_cond_on_2_year_model_weights.h5')
model5_cond_2.compile(
    loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model5_cond_5 = model_from_json(open('templates/models/5_cond_on_5_year_model_architecture.json').read())
model5_cond_5.load_weights('templates/models/5_cond_on_5_year_model_weights.h5')
model5_cond_5.compile(
    loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

onehotenc = joblib.load('templates/models/onehotenc.pkl')
standardscaler = joblib.load('templates/models/standardscaler.pkl')

droplists = []
model_file = 'templates/models.csv'
category_group_names = []
category_models = []
model_types = []

with open(model_file, 'r') as f:
	header_line = f.readline()
	for line in f.read().splitlines():
		splits = line.split(',')
		category_group_names.append(splits[0])
	number_of_models = len(splits) - 1

for i in range(len(header_line.split(','))-1):
	splits = header_line.split(',')
	model_types.append(splits[i+1])

model_file_names = []
models = []

for i in range(number_of_models):
	tmp = []
	with open(model_file, 'r') as f:
		header_line = f.readline()
		for line in f.read().splitlines():
			splits = line.split(',')
			tmp.append(splits[i+1])
		model_file_names.append(tmp)

# load the models listed in models.csv into the list object models
#for i in range(len(model_file_names)):
#	tmp = []
#	tmp1 = []
#	for j in model_file_names[i]:
#		if len(j.split(':')) == 1:
#			tmp.append(joblib.load('templates/models/basic_models/'+j))
#		else:
#			print(j.split(':'))
#			for k in j.split(':'):
#				tmp1.append(joblib.load('templates/models/basic_models/'+k))
#			tmp.append(tmp1)
#		tmp1 = []
#	models.append(tmp)

# variables used in the HTML portion of index.html
# title of the html page
htmlTitle = "Colon Cancer Outcome Calculator"
title = "Colon Cancer Outcome Calculator"

# form is used for the id parameter in the html form
# this variable needs to be consistent accross html pages to pass the post parameters
form = "survivability"


# the portion of code executed when / is request from the webserver
@app.route('/', methods = ['GET', 'POST'])
def homepage():

	# start of initialization of html components
	# this section loads the values for dropdown lists to be used in the html part
	# the data is loaded from the txt files stored under templates/meta_files
	# start of initialization of html components

	# this portion is for dropdown lists
	droplists = []
	lists_file = 'templates/lists.csv'
	with open(lists_file, 'r') as f:
		for line in f.read().splitlines():
			splits = line.split(',')
			label_name = splits[0]
			file_name = splits[1].strip()
			l = []
			with open('templates/meta_files/'+file_name, 'r') as f:
				for line in f.read().splitlines():
					l.append(tuple(line.split('#')))
			droplists.append(l)

	# this portion is for text inputs
	positive_nodes = []
	positive_nodes.append(("number","3","positive_nodes","0.0","98.0","4","Number of Positive Nodes"))
	size = []
	size.append(("number","3","tumor_size","0.0","98.0","5.0","Tumor size"))
	age = []
	age.append(("number","3","age","0","120","35","Age at Diagnosis"))
	year_birth = []
	year_birth.append(("number","4","year_birth","1920","2009","1970","Year of Birth"))

	# end of initialization of html components

	# the two lists droplists and numbers are two lists passed to the html files
	# these two lists are used to dynamically create the html components
	numbers = []
	numbers.append(positive_nodes)
	numbers.append(size)
	numbers.append(age)
	numbers.append(year_birth)

	# this command returns the file and parameters that are rendered by the html file index.html
	return render_template("/index.html", htmlTitle = htmlTitle, title = title, droplists = droplists, numbers = numbers, form=form)

# the portion of code executed when coloncalc.html is request from the webserver
@app.route('/coloncalc.html', methods=['GET', 'POST'])
def colon_calc(chartID = 'survival_bar_chart', chart_type = 'column', chart_height = 250):
	droplists = []
	list_data = []
	label_names = []
	params = []
	file_names = []
	lists_file = 'templates/lists.csv'

	with open(lists_file, 'r') as f:
		for line in f.read().splitlines():
			splits = line.split(',')
			label_name = splits[0]
			file_name = splits[1].strip()
			file_names.append(file_name)
			label_names.append(label_name)

	for label in label_names:
		params.append(request.form.get(label, type=str))

	l = []
	for i in range(len(file_names)):
		with open('templates/meta_files/'+file_names[i], 'r') as f:
			for line in f.read().splitlines():
				l.append(list(line.split('#')))
		for j in l:
				if j[1] == params[i]:
					j[-1] = 1
				else:
					j[-1] = 0
		droplists.append(l)
		l = []

	# this portion is for text inputs
	positive_nodes = []
	# the request.form.get part is to get the value from the prior page
	positive_nodes.append(("number","3","positive_nodes","0.0","98.0",request.form.get('positive_nodes', type=int),"Number of Positive Nodes"))
	size = []
	size.append(("number","3","tumor_size","0.0","98.0",request.form.get('tumor_size', type=float),"Tumor size"))
	age = []
	age.append(("number","3","age","0","120",request.form.get('age', type=int),"Age at Diagnosis"))
	year_birth = []
	year_birth.append(("number","4","year_birth","1920","2009",request.form.get('year_birth', type=int),"Year of Birth"))

	# end of initialization of html components

    # the two lists droplists and numbers are two lists passed to the html files
    # these two lists are used to dynamically create the html components
	numbers = []
	numbers.append(positive_nodes)
	numbers.append(size)
	numbers.append(age)
	numbers.append(year_birth)

	# get all form parameters 'POST' and save them in variables
	request_params_file = 'templates/inputs.csv'
	request_params = []
	with open(request_params_file, 'r') as f:
		for line in f.read().splitlines():
			param_details = line.split(',')
			request_params.append(param_details)

	str_params = []
	str_inputs = []
	num_params = []
	num_inputs = []
	with open(request_params_file, 'r') as f:
		for line in f.read().splitlines():
			param_details = line.split(',')
			print(param_details)
			if param_details[1].strip() == 'str':
				str_params.append(param_details[0])
				str_inputs.append(request.form.get(param_details[0]))
			else:
				num_params.append(param_details[0])
				if param_details[1].strip() == 'int':
					num_inputs.append(int(request.form.get(param_details[0])))
				elif param_details[1].strip() == 'float':
					num_inputs.append(float(request.form.get(param_details[0])))


	#print(str_params)
	#print(str_inputs)
	X_cat = onehotenc.transform(str_inputs).toarray().tolist()
	#print(num_params)
	#print(num_inputs)
	X_num = standardscaler.transform(num_inputs)
	#print(len(X_cat))
	#print(len(X_num))
	data = np.asarray((X_cat[0] + list(X_num))).reshape(1,-1)
	#print(model1.predict(data))


	# create the list of attributes, ordered as in inputs.csv, to be evaluated against the models
	inputs = []
	for rp in request_params:
		inputs.append(request.form.get(rp[0]))


	# evaluate the list of attributes against the models listed in models.csv
	results = []
	series = []
	for i in range(len(models)):
		tmp = []
		for j in models[i]:
			if isinstance(j, list):
				calc_prob = 101
				#calc_prob = round(((float(j[0].predict_proba(np.asarray(inputs).reshape(1, -1))[0][0])*100)/(float(j[1].predict_proba(np.asarray(inputs).reshape(1, -1))[0][0])*100))*100,2)
				if calc_prob > 100:
					calc_prob = 100.00
				tmp.append(calc_prob)
			else:
				calc_prob = 91
				#calc_prob = round(float(j.predict_proba(np.asarray(inputs).reshape(1, -1))[0][0])*100,2)
				if calc_prob > 100:
					calc_prob = 100.00
				tmp.append(calc_prob)
			print(tmp)
		results.append(tmp)
		series.append({"name":model_types[i], "data":tmp})



	# this portion of the code is used to generate the chart
	chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
	# the variable series is required and its format is as the example below
	series = [{"name": 'Survival Prediction', "data": [round(model1.predict(data)[0][1]*100, 2), round(model2.predict(data)[0][1]*100, 2), round(model5.predict(data)[0][1]*100, 2)]}, 
		{"name": 'Conditional Survival Prediction of 1 Year', "data": [round(model1_cond_1.predict(data)[0][1]*100, 2), round(model1_cond_2.predict(data)[0][1]*100, 2), round(model1_cond_5.predict(data)[0][1]*100, 2)]},
		{"name": 'Conditional Survival Prediction of 2 Years', "data": [round(model2_cond_1.predict(data)[0][1]*100, 2), round(model2_cond_2.predict(data)[0][1]*100, 2), round(model2_cond_5.predict(data)[0][1]*100, 2)]},
		{"name": 'Conditional Survival Prediction of 5 Years', "data": [round(model5_cond_1.predict(data)[0][1]*100, 2), round(model5_cond_2.predict(data)[0][1]*100, 2), round(model5_cond_5.predict(data)[0][1]*100, 2)]}]
	# series = [{"name": 'Survival Prediction', "data": [first_yr_survival_pred1, second_yr_survival_pred1, fifth_yr_survival_pred1]}, {"name": 'Conditional Survival Prediction', "data": [first_yr_survival_pred2, second_yr_survival_pred2, third_yr_survival_pred2]}]

	title = {"text": 'Colon Cancer Survivability'}
	xAxis = {"categories": category_group_names}
	yAxis = {"title": {"text": 'Survivability Prediction (%)'}}
	return render_template("/coloncalc.html", htmlTitle = htmlTitle, title = title, form = form, droplists = droplists, numbers = numbers, chartID = chartID, chart = chart, series = series, xAxis = xAxis, yAxis = yAxis)

if __name__ == "__main__":
	# to turn debug mode on use the following app.run(debug=True)
	#app.run('0.0.0.0')
	from tornado.wsgi import WSGIContainer
	from tornado.httpserver import HTTPServer
	from tornado.ioloop import IOLoop
	http_server = HTTPServer(WSGIContainer(app))
	http_server.listen(5001)
	IOLoop.instance().start()
