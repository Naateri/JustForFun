class Coord: #coordinates

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Objct:

    def __init__(self, data, lower, upper):
        self.data = data
        self.ll = lower
        self.ur = upper
        self.type = 1

class BBox: #bounding box

    def __init__(self, lower, upper):
        self.ll = lower
        self.ur = upper
        self.data = list()

    def add_data(self, data):
        self.data.append(data)

    def print_data(self):
        print ('Bounding box')
        for dat in self.data:
            print('nombre del dato: ' + str(dat.data)
                  + '\nLower left corner (' + str(dat.ll.x) + ','
                  + str(dat.ll.y) + ')\nUpper right corner ('
            + str(dat.ur.x) + ',' + str(dat.ur.y) + ')')
        print()

class RNode:
    #type 0 = internal node, type 1 = leaf node
    def __init__(self, obj_bb, n_type = 1):
        self.type = n_type
        self.ll = [None] * 4
        self.ur = [None] * 4
        self.obj_ptr = [None] * 4
        self.boundbox = [None] * 4

        self.ll[0] = obj_bb.ll
        self.ur[0] = obj_bb.ur
        self.obj_ptr[0] = obj_bb
            
        """if (n_type == 1):
            self.obj_ptr[0] = obj_bb #Object pointer
        else: #type = 0, pointer to child
            self.boundbox[0] = obj_bb #bounding box"""

#4 minimum bounding boxes (mbb) per leaf node

class RTree:

    def __init__(self):
        #self.root = [None] * 4
        self.root = None

    def real_lookup(self, x, y, n, result):
        if n.type == 0:
            return
        else:
            obj = n
            if (obj.ll.x <= x and x <= obj.ur.x
                    and obj.ll.y <= y and y <= obj.ur.y):
                    #if the object is in the point
                result.append(obj)
            """for obj in n.obj_ptr:
                if obj is None:
                    continue
                if (obj.ll.x <= x and x <= obj.ur.x
                    and obj.ll.y <= y and y <= obj.ur.y):
                    #if the object is in the point
                    result.append(obj)"""
        return result

    def lookup(self, x, y, n, result = list()):
        for node in n.obj_ptr:
            #print('node data: ' + node.data)
            if node is not None:
                print ('n: ' + str(n))                
                self.real_lookup(x,y,node,result)
        return result

    def insert(self, obj, n):
        if self.root is None:
            self.root = RNode(obj, 1)
        else:
            if n.type == 0:
                for i in range(4):
                    if (n[i].ll.x <= obj.ll.x and obj.ur.x <= n[i].ur.x
                        and n[i].ll.y <= obj.ll.y and
                        obj.ur.y <= n[i].ur.y):
                        self.insert(obj, n[i].obj_ptr)
                        return
            else:
                return
            """
                #split leaf node into 2 nodes

                #find bounding box for new nodes

                #and the stuff found at
                #http://www.mathcs.emory.edu/~cheung/Courses/554/Syllabus/3-index/R-tree.html
            """


bb1 = BBox(Coord(0,0),Coord(60,50))
house1 = Objct('house1',Coord(25,25), Coord(50,40))
bb1.add_data(Objct('house1',Coord(25,25), Coord(50,40)))
bb1.add_data(Objct('road1', Coord(0,45), Coord(60,50)))
bb1.add_data(Objct('road2', Coord(55,0), Coord(60,50)))
bb2 = BBox(Coord(20,20),Coord(100,80))
bb2.add_data(Objct('school', Coord(20,60), Coord(50,80)))
bb2.add_data(Objct('pop', Coord(70,60), Coord(80,75)))
bb2.add_data(Objct('house2', Coord(70,40), Coord(90,60)))
bb2.add_data(Objct('pipeline', Coord(50,35), Coord(100,40)))

bb1.print_data()
bb2.print_data()
#print ('Upper corner y: ' + str(bb1.ur.y) ) 
    
gg = RTree()
gg.insert(house1, gg.root)

temp = gg.lookup(35,40,gg.root)
print ('Value found: ' + str(temp[0].data))
