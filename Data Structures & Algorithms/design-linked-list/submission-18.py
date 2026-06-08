class DoubleLinkedList:
    def __init__(self, val=0, prev= None, next= None):
        self.val =val
        self.prev = prev
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.mll = None
        self.head = None
        self.tail = None
        self.length = 0
        

    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1

        curr= self.head
        i=0
        while i < index:
            if curr:
                curr = curr.next
            i=i+1
        return curr.val if curr else -1

    def addAtHead(self, val: int) -> None:
        ll = DoubleLinkedList(val=val)
        if not self.head:
            self.head = ll
            self.tail = ll
        else:
            ll.next = self.head
            self.head.prev = ll
            self.head = ll
        self.length+=1

        

    def addAtTail(self, val: int) -> None:
        ll = DoubleLinkedList(val=val)
        if not self.head:
            self.head = ll
            self.tail = ll
        else:
            ll.prev = self.tail
            self.tail.next = ll
            self.tail = ll
        self.length+=1

        

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return
        if index <= 0:
            self.addAtHead(val)
            return
        if index == self.length:
            self.addAtTail(val)
            return

        curr= self.head
        i=0
        while i < index:
            curr = curr.next
            i=i+1
        
        prev = curr.prev
        ll = DoubleLinkedList(val=val, prev=prev, next=curr)
        prev.next = ll
        curr.prev = ll
        self.length+=1

        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return

        curr= self.head
        i=0
        while i < index:
            curr = curr.next
            i=i+1
        
        prev = curr.prev
        nxt = curr.next

        if prev:
            prev.next = nxt
        else:
            self.head = nxt
        
        if nxt:
            nxt.prev = prev
        else:
            self.tail = prev
        
        self.length-=1