#example1

#append
list1=[2,3,4,1,32,4]
list1.append(19)
print (list1)
output=[2,3,4,1,32,4,19]

#count
print(list1.count(4))
output=2
#extend
list2=[99,54]
list1.extend(list2)
print(list1)
output=[2,3,4,1,32,4,19,99,54]
#index
print(list1.index(4))
output=2

#example2

#pop
list1=[2,25,3,4,1,32,4,19,99,54]
print(list1.pop(2))
output = 3

print(list1.pop())
output = 54

#remove
list1.remove(32)
print(list1)
output=[2, 25, 4, 1, 4, 19, 99]

#reverse
list1.reverse()
print(list1)
output = [99, 19, 4, 1, 4, 25, 2]

#sort
list1.sort()
print(list1)
output = [1, 2, 4, 4, 19, 25, 99]

#example
items = "Jane John Peter Susan".split()
print(items)
output =['Jane', 'John', 'Peter', 'Susan']


'''ans10.3
Let's analyze the effects of each statement on the given list lst = [30, 1, 2, 1, 0]. Assume the statements are applied independently, meaning we start with the original lst for each line.

lst.append(40)
Adds 40 to the end of the list.
Result: [30, 1, 2, 1, 0, 40]

lst.insert(1, 43)
Inserts 43 at index 1. The existing elements are shifted to the right.
Result: [30, 43, 1, 2, 1, 0]

lst.extend([1, 43])
Extends the list by appending each element of [1, 43].
Result: [30, 1, 2, 1, 0, 1, 43]

lst.remove(1)
Removes the first occurrence of 1 from the list.
Result: [30, 2, 1, 0]

lst.pop(1)
Removes and returns the element at index 1.
Result: [30, 2, 1, 0] (after removing the element 1 at index 1).

lst.pop()
Removes and returns the last element of the list.
Result: [30, 1, 2, 1] (after removing the last element, 0).

lst.sort()
Sorts the list in ascending order.
Result: [0, 1, 1, 2, 30]

lst.reverse()
Reverses the order of the list.
Result: [0, 1, 2, 1, 30]

random.shuffle(lst)
Shuffles the list randomly. Since the order is random, the result can vary.
Example Result: [2, 30, 1, 0, 1] (this is just one possible output).'''

'''ans10.4
1.  1st.index(1)
    return value=1

2. 1st.count(1)
   return value=2

3. len(1st)
   return value=5

4.max(1st)
  return value=30

5. min(1st)
   return= 0

6. sum (1st)
   return = 34'''

'''ans10.5
1. list1+list2
   return value = [30,1,2,1,0,1,21,13]

2. 2*list2
   return value = [1,21,13,1,21,13]

3. list2*2
    return value = [1,21,13,1,21,13]

4. list1[1:3]
   return value = [1,2]

5. list1[3]
   return value= 1 
