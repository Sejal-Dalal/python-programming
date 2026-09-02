#concatenate two lists
list1=[1,2,3]
list2=[4,5,6]
result=list1+list2
print("conctenated list:",result)

#Implement following operation on list a)create list,b)access the list,c)update a list,d)delete a list
l1=[10,20,30,40]
print("List1:",l1)

print("First element:",l1[0])
print("last element:",l1[3])

l1.append(70)
print("after adding element l1 becomes:",l1)
l1.insert(2,66)
print("after insertion l1:",l1)
l1.remove(20)
print("removed item :",l1)
del l1
print("list deleted")

#implement above operation on tuple
t1=(10,20,70,80)
print("Tuple 1 :",t1)
print("firdt element:",t1[2])
temp=list(t1)
temp[2]=88
t1=tuple(temp)
print("tuple is:",t1)
del t1
print("t1 is deleted")

