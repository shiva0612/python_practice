class node:
    def __init__(self,data = None):
        self.data = data
        self.next = None
        self.prev = None

class double_list:
    def __init__(self):
        self.head = node()

    def insert(self,data):
        temp = node(data)
        if self.head.data == None:
            self.head.data = temp.data;
        else:
            loop = self.head
            while loop.next != None:
                loop = loop.next
            loop.next = temp
            temp.prev = loop
    def disp(self):
        loop = self.head
        while loop:
            print(loop.data)
            loop = loop.next
l = double_list()
l.insert(1)
l.insert(2)
l.insert(3)
a = l.head.next.next.prev.prev.data
print(a)


