import json
def f():
	old_path = input('Old url : ')
	new_path = input('New url: ')
	j=json.dumps([{"model":"redirects.redirect", "fields":{"site":1, "old_path":old_path, "new_path":new_path}}])
	return(j)

print(f())