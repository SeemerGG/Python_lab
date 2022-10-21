from cmath import e


class polygon(object):

    def __init__(self, xy, name):
        self.name = name
        self.xy = xy
        self.edges = []
        for i in range(len(xy)):
            if i < len(xy) - 1:
                self.edges.append([xy[i],xy[i+1]])
            else:
                self.edges.append([xy[i],xy[0]])

    def is_intersect(self, obj2):
        vertexes = [0, 0, 0, 0]
        for i in self.edges:
            for j in obj2.edges:
                vertexes[0] = ((j[1][0] - j[0][0]) * (i[0][1] - i[0][0]) - (j[1][1] - j[0][1]) * (i[0][0] - j[0][0]))
                vertexes[1] = ((j[1][0] - j[0][0]) * (i[1][1] - i[0][0]) - (j[1][1] - j[0][1]) * (i[1][0] - j[0][0]))
                vertexes[2] = ((i[1][0] - i[0][0]) * (j[0][1] - i[0][1]) - (i[1][1] - i[0][1]) * (j[0][0] - i[0][0]))
                vertexes[3] = ((i[1][0] - i[0][0]) * (j[1][1] - i[0][1]) - (i[1][1] - i[0][1]) * (j[1][0] - i[0][0]))
                if (vertexes[0] * vertexes[1] < 0) and (vertexes[2] * vertexes[3] < 0):
                    return True
        return False
    
    def is_include(self, obj2):
        if self.is_intersect(obj2):
            proj2_x = abs(max(obj2.xy)[0] - min(obj2.xy)[0])
            proj1_x = abs(max(self.xy[0]) - min(self.xy)[0])
            proj2_y = abs(max(obj2.xy, key = lambda i : i[1])[1] - min(obj2.xy,key =  lambda i:i[1])[1])
            proj1_y = abs(max(self.xy, key = lambda i : i[1])[1] - min(self.xy,key =  lambda i:i[1])[1])
            if proj1_x - proj2_x > 0 and proj1_y - proj2_y > 0:
                return True
            else:
                return False
        else:
            return False


class triangle(polygon):

    def __init__(self, xy, name):

        try:
            self.name = name
            self.xy = xy
            self.edges = []
            for i in range(len(xy)):
                if i < len(xy) - 1:
                    self.edges.append([xy[i],xy[i+1]])
                else:
                    self.edges.append([xy[i],xy[0]])
        except:
            print("Error")


class rectangle(polygon):

    def __init__(self, xy, name):

        try:
            self.name = name
            self.xy = xy
            self.edges = []
            for i in range(len(xy)):
                if i < len(xy) - 1:
                    self.edges.append([xy[i],xy[i+1]])
                else:
                    self.edges.append([xy[i],xy[0]])
        except:
            print("Error")            

        
        





def main():
    trin1 = triangle([[1,3], [2,5], [3,3]], "pol1")
    trin2 = rectangle([[0,0], [0,5], [5,5], [5,0]], "pol2")
    
    print(trin1.is_include(trin2))

main()

