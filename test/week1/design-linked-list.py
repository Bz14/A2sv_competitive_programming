class Node:

    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        idx = 0
        current = self.head
        while current:
            if idx == index:
                return current.val
            current = current.next
            idx += 1
        return -1

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode
        
    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        if not self.head:
            self.head = newNode
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode

    def addAtIndex(self, index: int, val: int) -> None:
        idx = 0
        current = self.head
        newNode = Node(val) 
        if index <= 0:
            newNode.next = self.head
            self.head = newNode
        while current:
            if idx == index - 1:
                newNode.next = current.next
                current.next = newNode
                break
            current = current.next
            idx += 1
        
    def deleteAtIndex(self, index: int) -> None:
        current = self.head
        idx = 0
        if idx < 0:
            return
        if index == 0 and self.head:
            self.head = self.head.next
            return
        while current:
            if idx == index - 1:
                if current.next is not None:
                    node = current.next
                    current.next = node.next
            current = current.next
            idx += 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

