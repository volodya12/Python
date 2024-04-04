
"""
todo = ['wasll', 'sell']
todo[0] = 'wash'
print(todo)
-practice Slicing
"""

todos = ['1-prepare\n', '2-shower\n', '3-play\n']
new_todo = []

for todo in todos:
    new = todo.strip('\n')
    new_todo.append(new)

print(new_todo)

















