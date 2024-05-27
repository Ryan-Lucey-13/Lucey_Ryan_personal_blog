pages = [
]

import glob
all_html_files = glob.glob("content/*.html")

import os

for file in all_html_files:
	file_path = file
	file_name = os.path.basename(file_path)
	name_only, extension = os.path.splitext(file_name)
	pages.append({
		"filename": file_path,
		"title": name_only,
		"output": "docs/" + file_name,
	})

from jinja2 import Template

for page in  pages:
	index_html = open(page['filename']).read()

	template_html = open("templates/base.html").read()
	template = Template(template_html)
	html_result = template.render(
		title= page['title'],
		content= index_html
	)	
	output_file = page['output']
	open(output_file, 'w+').write(html_result)





