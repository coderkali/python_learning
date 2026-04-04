'''
set -> Hasable 
tuple -> Hashbale 
'''


d = {(10,20):"Item1"}
print(d)

d1 = {(10,20):"Item1",[10,20]:"Items2"} # TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
