pages = [
	{
	"filename": "content/index.html",
	"output": "docs/index.html",
	"title": "Blog",
	},
	{
	"filename": "content/projects.html",
	"output": "docs/projects.html",
	"title": "Projects",
	},
	{
	"filename": "content/aboutme.html",
	"output": "docs/aboutme.html",
	"title": "About Me",
	},
]
def main():
	template = open("templates/base.html").read()
	for page in pages:
		filename = page['filename']
		output_file = page['output']
		index = open(filename).read()
		index_page = template.replace("{{content}}", index)
		open(output_file, 'w+').write(index_page)
main()



