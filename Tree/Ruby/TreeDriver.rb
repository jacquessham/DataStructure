require_relative "BSTree"


tree = BSTree.new()
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
puts "---------------"
tree.delete(5)
tree.printElem()