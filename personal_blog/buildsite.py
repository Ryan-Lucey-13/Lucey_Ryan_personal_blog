#index
top = open('./templates/top.html').read()
index = open('./content/index.html').read()
bottom = open('./templates/bottom.html').read()
index_page = top + index + bottom
open('index.html', 'w+').write(index_page)

#projects
top = open('./templates/top.html').read()
projects = open('./content/projects.html').read()
bottom = open('./templates/bottom.html').read()
projects_page = top + projects + bottom
open('projects.html', 'w+').write(projects_page)

#aboutme
top = open('./templates/top.html').read()
aboutme = open('./content/aboutme.html').read()
bottom = open('./templates/bottom.html').read()
aboutme_page = top + aboutme + bottom
open('aboutme.html', 'w+').write(aboutme_page)