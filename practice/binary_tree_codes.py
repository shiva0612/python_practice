class node:
    def __init__(self,data = None):
        self.data = data;
        self.left = None
        self.right = None

class tree:
    def __init__(self):
        self.head = node()

    def insert(self,data):
        temp = node(data)
        if self.head.data == None:
            self.head.data = data;

        else:

            current = self.head;
            while current:
                k = None
                parent = current;
                if data < current.data:
                    current = current.left
                    k=0;
                else:
                    current = current.right
                    k=1

            if k == 0:
                parent.left = temp
            else:
                parent.right = temp
    def level_printing(self):
        a = [[],[]]
        k = 0;

        a[0].append(self.head)


        while a[0] != [] or a[1] != []:
            if a[k][0].left:
                a[k^1].append(a[k][0].left)
            if a[k][0].right:
                a[k^1].append(a[k][0].right)
            print(a[k][0].data,end="")
            a[k].pop(0)
            if a[k] == []:
                print("")
                k = k^1

    def disp_leafnodes(self,temp):
        if temp == None:
            return
        self.disp_leafnodes(temp.left)
        self.displeafnodes(temp.right)
        if temp.left == None and temp.right == None:
            print(temp.data)
        return
    def check(self,temp): # checks if every node has left and right or none

        if temp.left:
            print("checking left,right of ",temp.data)
            if temp.right:
                a = bool(self.check(temp.left))
                b = bool(self.check(temp.right))
                return a and b

        elif temp.left == None and temp.right == None:
            return True
        else:
            pass
L = [55,6,80,9,2,1,40]
o = tree()
for i in L:
    o.insert(i)
o.disp_leafnodes(o.head)
print(o.check(o.head))
o.level_printing()
