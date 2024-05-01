def main():
	top = open('./templates/top.html').read()
	bottom = open('./templates/bottom.html').read()
	#index
	index = open('./content/index.html').read()
	index_page = top + index + bottom
	open('./docs/index.html', 'w+').write(index_page)
	#projects
	projects = open('./content/projects.html').read()
	projects_page = top + projects + bottom
	open('./docs/projects.html', 'w+').write(projects_page)
	#aboutme
	aboutme = open('./content/aboutme.html').read()
	aboutme_page = top + aboutme + bottom
	open('./docs/aboutme.html', 'w+').write(aboutme_page)
main()

