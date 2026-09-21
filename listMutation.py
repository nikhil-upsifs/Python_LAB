#wap to rmove last element forom a list 
def remove_last_element(lst):
    if lst:
        lst.pop()
    return lst 

list =[]
n=int(input("Enter the number of elements in the list: "))
for i in range(n):
    element = int(input("Enter element {}: ".format(i+1)))
    list.append(element)
print("Original list:", list)
list = remove_last_element(list)
print("List after removing last element:", list)