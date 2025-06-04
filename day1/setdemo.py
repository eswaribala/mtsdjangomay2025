javaEmployees=set()
javaEmployees.add("Alice")
javaEmployees.add("Bob")    
javaEmployees.add("Charlie")

angularEmployees=set()
angularEmployees.add("David")   
angularEmployees.add("Eve")
angularEmployees.add("Frank")
angularEmployees.add("Alice")  # Alice also works with Angular


#union of both sets
allEmployees=javaEmployees.union(angularEmployees)
#intersection of both sets
commonEmployees=javaEmployees.intersection(angularEmployees)
#difference of both sets
javaOnlyEmployees=javaEmployees.difference(angularEmployees)
#symmetric difference of both sets
angularOnlyEmployees=angularEmployees.difference(javaEmployees)
#symmetric difference of both sets
symmetricDifference=javaEmployees.symmetric_difference(angularEmployees)
#displaying the results     
print("All Employees:", allEmployees)
print("Common Employees:", commonEmployees) 
print("Java Only Employees:", javaOnlyEmployees)
print("Angular Only Employees:", angularOnlyEmployees)
print("Symmetric Difference:", symmetricDifference)
#checking if a particular employee is in the set