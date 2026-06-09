class DoubleLinkedList:
    def __init__(self, val= 0, next= None, prev= None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head= DoubleLinkedList(val=homepage)
        self.tail = self.head
        self.curr = self.head
        self.size =1
        

    def visit(self, url: str) -> None:
        ll = DoubleLinkedList(val=url, prev = self.curr)
        if not self.head.next:
            self.head.next= ll
        else:
            self.curr.next = ll
        self.tail = ll
        self.curr = ll
        
        
    def back(self, steps: int) -> str:
        i=0
        while i<steps and self.curr!=self.head:
            self.curr = self.curr.prev
            i+=1
        return self.curr.val
        

    def forward(self, steps: int) -> str:
        i=0
        while i<steps and self.curr!=self.tail:
            self.curr= self.curr.next
            i=i+1
        return self.curr.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)