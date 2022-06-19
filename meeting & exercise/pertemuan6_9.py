my_list = ['p','y','t','h','o','n','i','n','d','o']

#output ['y','t','h','o','n','i','n','d','o']
my_list.remove('p')
print (my_list)

#output ['p','y','t','h','o','i','n','d','o']
my_list.remove('n')
print(my_list)

#output 'y'
print(my_list.pop(1))

del my_list[2]
print (my_list)

my_list.clear()
#output []
print (my_list)