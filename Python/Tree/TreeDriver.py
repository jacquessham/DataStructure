from random import randint
import BSTree



tree = BSTree.BSTree()
tree.insert(5)
tree.insert(5)
tree.insert(4)
tree.insert(10)
tree.insert(10)
tree.insert(15)
tree.insert(6)
tree.insert(1)
tree.insert(3)
tree.printElem()
print('---------------')
tree.delete(5)
tree.printElem()

print('---------------')
# Something wrong to left leaf after deleting
tree.delete(1)
tree.printElem()
print('---------------')
"""
tree.delete(10)
tree.printElem()
"""

# Testing delete() not root
"""
tree2 = BSTree.BSTree()
size = 10
elems = []
for i in range(size):
	num = randint(0,20)
	tree2.insert(num)
	elems.append(num)
tree2.printElem()
print('---------------')
print('Deleting',elems[0])
tree2.delete(elems[0])
print('---------------')
tree2.printElem()
"""
# Testing delete() is root
"""
tree3 = BSTree.BSTree()
size = 10
elems = []
for i in range(size):
	num = randint(0,20)
	tree3.insert(num)
	elems.append(num)
tree3.printElem()
print('---------------')
root_elem = tree3.root.getElem()
print('Root is',root_elem)
print('---------------')
tree3.delete(root_elem)
tree3.printElem()
"""
"""
elems_manual = [10, 18, 17, 6, 17, 3, 4, 19, 12, 17]
tree4 = BSTree.BSTree()
for i in elems_manual:
	tree4.insert(i)
tree4.printElem()
tree4.delete(10)
print('---------------')
tree4.printElem()
"""