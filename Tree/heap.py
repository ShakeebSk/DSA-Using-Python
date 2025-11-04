class Heap:
    def __init__(self):
        self.heap=[]
    def createheap(self,list1):
        for e in list1:
            self.insert(e)
    def insert(self,e):
        index=len(self.heap)
        parentIndex=(index-1)//2
        while index>0 and self.heap[parentIndex]<e:
            if index==len(self.heap):
                self.heap.append(self.heap[parentIndex])
            else:
                self.heap[index]=self.heap[parentIndex]
            index=parentIndex
            parentIndex=(index-1)//2
        if index==len(self.heap):
            self.heap.append(e)
        else:
            self.heap[index]=e
    def top(self):
        if len(self.heap)==0:
            raise EmptyHeapException()
        return self.heap[0]
    def delete(self):
        if len(self.heap)==0:
            raise EmptyHeapException()
        if len(self.heap)==1:
            return self.heap.pop()
        max_value=self.heap[0]
        temp=self.heap.pop()
        index=0
        leftchildindex=2*index+1
        rightchildindex=2*index+2
        while leftchildindex<len(self.heap):
            if rightchildindex<len(self.heap):
                if self.heap[leftchildindex]>self.heap[rightchildindex]:
                    if self.heap[leftchildindex]>temp:
                        self.heap[index]=self.heap[leftchildindex]
                        index=leftchildindex
                    else:
                        break
                else:
                    if self.heap[rightchildindex]>temp:
                        self.heap[index]=self.heap[rightchildindex]
                        index=rightchildindex
                    else:
                        break
            else: #No right child
                if self.heap[leftchildindex]>temp:
                    self.heap[index]=self.heap[leftchildindex]
                    index=leftchildindex
                else:
                    break
            leftchildindex=2*index+1
            rightchildindex=2*index+2
        self.heap[index]=temp
        return max_value
    def heapsort(self,list1):
        self.createheap(list1)
        list2=[]
        try:
            while True:
                list2.insert(0,self.delete())
        except EmptyHeapException:
            pass
        return list2
class EmptyHeapException(Exception):
    def __init__(self,msg="Empty Heap"):
        self.msg=msg
    def __str__(self):
        return self.msg
list1=[34,52,12,78,43,25,10,80,60]
h=Heap()
list1=h.heapsort(list1)
print(list1)
        
