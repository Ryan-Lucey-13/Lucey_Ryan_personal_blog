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

def main():
	template = open("templates/base.html").read()
	for page in pages:
		create_page(page, template)

def create_page(page, template):
	filename = page['filename']
	output_file = page['output']
	content = open(filename).read()
	apply_template(content, template, output_file)

def apply_template(content, template, output_file):
	content_page = template.replace("{{content}}", content)
	open(output_file, 'w+').write(content_page)

main()


