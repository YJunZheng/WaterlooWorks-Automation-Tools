f = open("list1.txt", "r")
f2 = open("list2.txt", "r")
f3 = open("differences.txt", "w")

values1 = f.read()
values2 = f2.read()

list1 = values1.split()
list2 = values2.split()

for v1 in list1:
	match = False
	for v2 in list2:
		if v1 == v2:
			match = True

	if not match:
		f3.write(v1 + " ")
