from queue import Queue
from singly_linked_list import Node, LinkedList
from stack import Stack
"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # take the current value of our node (self.value)    
        # compare to the new value we want to insert
        new_node = BSTNode(value)
        
        # if new value < self.value
            # IF self.left is already taken by a node
                # make that (left) node, call insert 
            # set the left to the new node with the new value
        if value < self.value:
            if self.left is None:
                self.left = new_node
            else:
                self.left.insert(value)
        
            # if new value >= self.value
            # IF self.right is already taken by a node
                # make that (right) node call insert 
            # set the right child to the new node with new value
            
        elif value >= self.value:
            if self.right is None:
                self.right = new_node
            else:
                self.right.insert(value)
    
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        # Compare the target to current value
        # If current target < value
        found = False
        if target < self.value:
            # Check the left subtree (self.left.contains(target))
            # If you cannot go left, return False
            if self.left is None:
                return False
            found = self.left.contains(target)
            
        # If current target >= value
        if target >= self.value:
            # Check if right subtree contains target
            # If you cannot go right, return False
            if self.right is None:
                return False
            found = self.right.contains(target)
        return found

    # Return the maximum value found in the tree
    def get_max(self):
        # Check to see if self.right has a node.
            # If there is no node in self.right then return root value (self.value)
        if self.right is None:
            return self.value
            # If there is a node in self.right then run the get_max() function on self.right
        # else:
        #     return self.right.get_max()
        max_val = self.right.get_max()
        return max_val

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # The user will pass in a function to this method. That function needs to be called on for the value of each and every node.
            # Call the function on the root value.
        fn(self.value)
            # Check of a node exists in self.left.
                # If a node exists then call the for_each function on the value of self.left (the for_each functon will then treat that self.left node as if it is the root node).
        if self.left:
            self.left.for_each(fn)
            # Check of a node exists in self.right.
                # If a node exists then call the for_each function on the value of self.right (the for_each functon will then treat that self.right node as if it is the root node).
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self.left:
            self.left.in_order_print(node)

        print(self.value)

        if self.right:
            self.right.in_order_print(node)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # Create a queue for nodes
        queue = Queue()

        # Add the first node to the queue
        queue.enqueue(node)

        # While queue is not empty
        while len(queue) > 0:
            # Remove the first node from the queue
            current_node = queue.dequeue()

            # Print the removed node
            print(current_node.value)

            # Add All Children into the queue

            if current_node.left:
                queue.enqueue(current_node.left)
            if current_node.right:
                queue.enqueue(current_node.right)
            # Remove and print the first node in the queue
            # Add the children of that node.
            # Remove and print the next node in the queue
            # Add the children of that node.


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # Create a stack for nodes
        # Add the first node to the stack
        # While stack is not empty
            # Remove the first node from the top of the stack
            # Print the removed node
            # Add All Children into the stack, add first the side that you don't want printed first.
            # Remove and print the first node in the stack
            # Add All Children into the stack, add first the side that you don't want printed first.
            # Remove and print the next node in the stack
            # Add the children of that node.
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
