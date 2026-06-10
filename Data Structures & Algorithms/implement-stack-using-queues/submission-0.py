class DoubleLinkedList:
	def __init__(self, val=0, prev= None, next= None):
		self.val = val
		self.prev = prev
		self. next = next

class MyStack:
	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0
	
	def push(self, val):
		ll = DoubleLinkedList(val=val)
		if self.size==0:
			self.head = ll
			self.tail = ll
		elif self.size ==1:
			self.head.next = ll
			ll.prev = self.head
			self.tail = ll
		else:
			self.tail.next = ll
			ll.prev = self.tail
			self.tail = ll
		self.size+=1
		
	def top(self):
		return self.tail.val
	
	def pop(self):
		res = self.tail.val
		if self.size == 1:
			self.head = None
			self.tail = None
		else:
			prev = self.tail.prev
			prev.next = None
			self.tail.prev = None
			self.tail = prev
		self.size-=1
		return res
	
	def empty(self):
		return True if not self.size else False