class node:
    def __init__(self,data = None):
        self.data = data
        self.next = None

class list():
    def __init__(self):
        self.head = node();
    def insert(self,data):
        temp = node(data)
        if self.head.data == None:
            self.head.data = temp.data;
        else:
            loop = self.head
            while loop.next != None:
                loop = loop.next
            loop.next = temp

    def disp(self):
        loop = self.head
        while loop:
            print(loop.data);
            loop = loop.next
one = list()
one.insert(1)
one.insert(2)
one.insert(3)
one.disp()