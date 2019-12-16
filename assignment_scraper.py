# author: vad, date: 17-dec-2019

import requests
from bs4 import BeautifulSoup
import os
import re

# replace ms.gitta exercises link here
all_pages = ["https://www.w3resource.com/python-exercises/pandas/index-dataframe.php",
			"https://www.w3resource.com/python-exercises/pandas/index-data-series.php",
			"https://www.w3resource.com/python-exercises/pandas/movies/index.php"]

for page in all_pages:
	
	root_link = re.sub("[^/]+$", "", page)
	page_req = requests.get(page)

	soup = BeautifulSoup(page_req.content, 'html.parser')
	html_code_list = soup.find_all(lambda tag:tag.name=="a" and "Click me to see the sample solution" in tag.text)


	for html_code in html_code_list:
		exercise_link = root_link + html_code.get("href")

		py_file_name = html_code.get("href").replace(".php",".py")
		ipynb_file_name = py_file_name.replace(".py", ".ipynb")

		exercise_code = BeautifulSoup(requests.get(exercise_link).content, 'html.parser').code.text

		with open(py_file_name, "w") as exercise_file:
			exercise_file.write(exercise_code)

		os.system("ipynb-py-convert " + py_file_name + " " + ipynb_file_name)

		print("Complete --- ", ipynb_file_name)

# NOTE: dont forget to run pip install ipynb-py-convert
