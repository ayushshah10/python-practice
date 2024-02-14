#Q-74
def searchprop(l1,tr):
    l1 = [i[tr] for i in l1]
    return l1


l1 = [{'name': 'Theodore', 'age': 18}, {'name': 'Mathew', 'age': 22}, {'name': 'Roxanne', 'age': 20}, {'name': 'David', 'age': 18}]
res = searchprop(l1,'age')

print(res)
