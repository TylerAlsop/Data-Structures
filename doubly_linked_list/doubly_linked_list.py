"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev

#####################################################################
"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def __str__(self):
        output = ''
        current_node = self.head
        while current_node is not None:
            output += f'STR METHOD: current node value: {current_node.value} ->'
            current_node = current_node.next
        return output
        # return f'STR METHOD: self.head.value: {self.head.value} ; self.tail.value: {self.tail.value} ; '

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
##### Code From Lecture Review #####
        new_list_node = ListNode(value, None, None)
        self.length += 1
        if self.head is None and self.tail is None:
            self.head = new_list_node
            self.tail = new_list_node
        else:
            new_list_node.next = self.head
            self.head.prev = new_list_node
            self.head = new_list_node
            

##### My Original Code #####
        # self.length += 1
        # new_list_node = ListNode(value)
        # if self.head is None and self.tail is None:
            # self.head = new_list_node
            # self.tail = new_list_node
        #     self.head.next = self.tail
        #     self.head.prev = None
        #     self.tail.prev = self.head
        #     self.tail.next = None
        # else:
        #     new_list_node.next = self.head
        #     self.head.prev = new_list_node
        #     self.head = new_list_node
            

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
##### Code From Lecture Review #####

        self.length -= 1
        if not self.head:
            return None
        if self.head.next is None:
            head_value = self.head.value
            self.head = None
            self.tail = None
            return head_value
        head_value = self.head.value
        self.head = self.head.next
        self.head.prev = None
        return head_value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
##### Code From Lecture Review #####

        self.length += 1
        new_list_node = ListNode(value)
        if self.head is None and self.tail is None:
            self.head = new_list_node
            self.tail = new_list_node
            self.head.next = self.tail
            self.head.prev = None
            self.tail.prev = self.head
            self.tail.next = None
        else:
            new_list_node.prev = self.tail
            self.tail.next = new_list_node
            self.tail = new_list_node

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
##### Code From Lecture Review #####

        self.length -= 1
        if not self.tail:
            return None
        if self.tail.prev is None:
            tail_value = self.tail.value
            self.head = None
            self.tail = None
            return tail_value
        tail_value = self.tail.value
        self.tail = self.tail.prev
        self.tail.next = None
        return tail_value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
##### Code From Lecture Review #####

        # self.length -= 1
        if node is self.head:
            pass
        # node_value = node.value
        # node.delete()
        # self.add_to_head(node_value)

        node.delete()
        self.head.prev = node
        node.next = self.head
        self.head = node
        node.prev = None

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
##### Code From Lecture Review #####

        # self.length -= 1
        if node is self.tail:
            pass
        # node_value = node.value
        # node.delete()
        # self.add_to_tail(node_value)

        node.delete()
        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        node.next = None

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
##### Code From Lecture Review #####
        if self.head is None and self.tail is None:
            return
        self.length -= 1
        if self.head == self.tail and node == self.head:
            self.head == None
            self.tail == None
        if self.head == node:
            self.head = node.next
            node.delete()
        if self.tail == node:
            self.tail = node.prev
            node.delete()
        else:
            node.delete()


##### My Original Code (unfinished) #####

        # # if node.next is None:
        # #     self.remove_from_tail(node)
        # # elif node.prev is None:
        # #     self.remove_from_head(node)
        # node.delete()
        
    """Returns the highest value currently in the list"""
    def get_max(self):
##### Code From Lecture Review #####

        if self.head:
            node = self.head
            current_max = node.value

            while node:
                if node.value > current_max:
                    current_max = node.value
                node = node.next
            return current_max
