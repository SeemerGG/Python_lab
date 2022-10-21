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
        flag = False
        for i in self.edges:
            for j in obj2.edges:
                #vertexes.append((j[1][0] - j[0][0]) * (i[0][1] - i[0][0]) - (j[1][1] - j[0][1]) * (i[0][0] - j[0][0]))
                #vertexes.append((j[1][0] - j[0][0]) * (i[1][1] - i[0][0]) - (j[1][1] - j[0][1]) * (i[1][0] - j[0][0]))
                #vertexes.append((i[1][0] - i[0][0]) * (j[0][1] - i[0][1]) - (i[1][1] - i[0][1]) * (j[0][0] - i[0][0]))
                #vertexes.append((i[1][0] - i[0][0]) * (j[1][1] - i[0][1]) - (i[1][1] - i[0][1]) * (j[1][0] - i[0][0]))
                vertexes[0] = ((j[1][0] - j[0][0]) * (i[0][1] - i[0][0]) - (j[1][1] - j[0][1]) * (i[0][0] - j[0][0]))
                vertexes[1] = ((j[1][0] - j[0][0]) * (i[1][1] - i[0][0]) - (j[1][1] - j[0][1]) * (i[1][0] - j[0][0]))
                vertexes[2] = ((i[1][0] - i[0][0]) * (j[0][1] - i[0][1]) - (i[1][1] - i[0][1]) * (j[0][0] - i[0][0]))
                vertexes[3] = ((i[1][0] - i[0][0]) * (j[1][1] - i[0][1]) - (i[1][1] - i[0][1]) * (j[1][0] - i[0][0]))
                flag = (vertexes[0] * vertexes[1] < 0) and (vertexes[2] * vertexes[3] < 0)
                if flag: 
                    return flag
        return flag
    
    def is_include(self, obj2):



        




def main():
    trin1 = polygon([[1,2], [3,4], [4,2]], "pol1")
    trin2 = polygon([[0,0], [1,1], [2,0]], "pol2")
    
    print(trin1.is_intersect(trin2))

main()

