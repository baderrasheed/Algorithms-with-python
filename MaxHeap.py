class MaxHeap:
	def __init__(self,A=[]):
		super().__init__()
		self.heap = [0]
		self.maxSize = len(A)*2
		self.size = len(A)
		
		for i in A:
			self.heap.append(i)
			self.__SwiftUp(len(self.heap)-1)
	def __Parent(self,i):
		return int(i/2)
	def __LeftChild(self,i):
		return (2*i)
	def __RightChild(self,i):
		return (2*i +1)
	def __SwiftUp(self,i):
		while i>1 and self.heap[self.__Parent(i)]<self.heap[i]:
			self.__swap(self.__Parent(i),i)
			i = self.__Parent(i)
	def __swap(self,a,b):
		self.heap[a],self.heap[b] = self.heap[b],self.heap[a]
	def __SwiftDown(self,i):
		maxIndex = i
		l = self.__LeftChild(i)
		if l <= self.size and self.heap[l]>self.heap[maxIndex]:
			maxIndex = l
		r = self.__RightChild(i)
		if r <= self.size and self.heap[r]>self.heap[maxIndex]:
			maxIndex = r
		if i != maxIndex:
			self.__swap(maxIndex,i)
			self.__SwiftDown(maxIndex)
	def Insert(self, p):
		if self.size == self.maxSize:
			return("Error")
		self.size = self.size + 1
		self.heap.append(p)
		self.__SwiftUp(self.size)
	def ExtractMax(self):
		result = self.heap[1]
		self.heap[1] = self.heap[self.size]
		self.size = self.size-1 
		self.__SwiftDown(1)
		return result
	def Remove(self,i):
		self.heap[i] = 99999999
		self.__SwiftUp(i)
		self.ExtractMax()
	def ChangePriority(self,i,p):
		oldp = self.heap[i]
		self.heap[i] = p 
		if p>oldp:
			self.__SwiftUp(i)
		else:
			self.__SwiftDown(i)
			
m = MaxHeap([1,2,3,5,4])
print(str(m.heap[1]))
m.Insert(10)
print(str(m.heap[1]))
m.Remove(1)
print(str(m.heap[1]))
m.Remove(1)
print(str(m.heap[1]))
	

	