class passengers(object):
    def __init__(self, first_name, last_name, stn_in, stn_out):
        self.first_name = first_name
        self.last_name = last_name
        self.stn_in = int(stn_in)
        self.stn_out = int(stn_out)
        self.count_stn = self.stn_out - self.stn_in
    
def main():
    fin = open('input.txt', 'r', encoding='utf-8')
    data = fin.read().split()
    fin.close()
    n = int(data[0])
    pessengers = []
    i = 1
    while i < len(data):
        pessengers.append(passengers(data[i], data[i+1], data[i+2], data[i+3]))
        i += 4
    
    transs = {}
    l = 1
    while l < n:
        transs[str(l)+ " - " +str(l+1)] = 0
        l += 1
        
    for k in range(len(pessengers)):
        for j in range(pessengers[k].stn_in, pessengers[k].stn_out):
            transs[str(j) + " - " + str(j+1)] += 1
    
    fout = open('output.txt', 'w', encoding="utf-8")
    max_count = max(transs.items(), key = lambda p : p[1])
    for k in transs:
        if transs[k] == max_count[1]:
            fout.write(str(k) + "\n")
    fout.close()
    
    
main()