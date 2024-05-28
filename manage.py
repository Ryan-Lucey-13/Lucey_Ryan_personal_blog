
import utils
import sys

print("This is argv:", sys.argv)
command = sys.argv[1]
print(command)
if command == "build":
	print("Build was specified")
	utils.generate_content()
elif command == "new":
	print("New page was specified")
	new_file= open("content/new_content_page.html", 'w+')
	html_template = """
	<h1>New Content!</h1>

	<p>New Content...</p>
	"""
	new_file.write(html_template)
else:
	print("Please specify 'build' or 'new'")
