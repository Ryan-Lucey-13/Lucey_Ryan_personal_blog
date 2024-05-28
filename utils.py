
from jinja2 import Template
import glob
import os

pages = []

all_html_files = glob.glob("content/*.html")

for file in all_html_files:
	file_path = file
	file_name = os.path.basename(file_path)
	name_only, extension = os.path.splitext(file_name)
	pages.append({
		"filename": file_path,
		"title": name_only,
		"output": "docs/" + file_name,
		"output_filename": file_name
	})

def generate_content():
	for page in  pages:
		content_html = open(page['filename']).read()

		template_html = open("templates/base.html").read()
		template = Template(template_html)
		html_result = template.render(
			title=page['title'],
			content=content_html,
			pages=pages,
		)
		output_file = page['output']
		open(output_file, 'w+').write(html_result)





