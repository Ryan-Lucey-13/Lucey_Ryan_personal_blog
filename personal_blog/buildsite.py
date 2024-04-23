#index
top = open('./templates/top.html').read()
index = open('./content/index.html').read()
bottom = open('./templates/bottom.html').read()
index_page = top + index + bottom
open('index_page.html', 'w+').write(index.html)

#projects
top = open('./templates/top.html').read()
projects = open('./content/projects.html').read()
bottom = open('./templates/bottom.html').read()
projects_page = top + index + bottom
open('projects_page.html', 'w+').write(projects.html)

#aboutme
top = open('./templates/top.html').read()
aboutme = open('./content/aboutme.html').read()
bottom = open('./templates/bottom.html').read()
aboutme_page = top + index + bottom
open('aboutme_page.html', 'w+').write(aboutme.html)