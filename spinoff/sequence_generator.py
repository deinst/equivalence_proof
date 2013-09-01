class Node(object): 
    def __init__(self, data): 
        self.data = data
        self.children = []
        
    def add_child(self, obj):
        self.children.append(obj)
        
    def print_nodes(self):
        for c in self.children:
            print c.data

    def print_nodes_atlevel(self, level):
        print self.data
        for c in self.children: 
             c.print_nodes_atlevel(level - 1)
       
    def printLevelorder(self, level):
        for i in range(1, level): 
            self.printGivenLevel(i)
    
    def printGivenLevel(self, level):
        if level == 0:
            return self.data
        else: 
            for c in self.children: 
                c.printGivenLevel(level - 1)
         
    def populate_nodes_tolevel(self, sequence, level): 
        if level == 0: 
            return 0
        else:
            new_sequences = generate_sequence(sequence)[:]
            for i in new_sequences:
                new_child = Node(i)
                self.add_child(new_child)
            for c in self.children: 
                c.populate_nodes_tolevel(c.data, level - 1)
 
    
def check_sequence(sequence): 
    # REDUCE THIS BY ZERO!
    count_list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    #print sequence
    for c in sequence:
        #print c 
        count_list[c] = count_list[c] + 1 
        if ((c == 1) and ((count_list[1] == count_list[2]) or (count_list[1] == count_list[2] + 1))):
            #print "case c=1"
            pass 
        elif ((c == 19) and ((count_list[19] == count_list[18]) or (count_list[19] == count_list[18] - 1))):
            #print "case c=9"
            pass
        elif (((count_list[c] == count_list[c+1]) or (count_list[c] == count_list[c+1] + 1)) and ((count_list[c] == count_list[c-1]) or (count_list[c] == count_list[c-1] - 1))):
            #print "case c between 2 and 8"
            pass
        else: 
            return False 
    return True
     

def generate_sequence(initial_sequence): 
        new_sequences = []
        temp = []
        #for i in range(1,10): 
        for i in range(1,15):
            temp = initial_sequence[:]
            temp.append(i)
            if (check_sequence(temp) == True):
                new_sequences.append(temp[:])
            del temp[:] 
        return new_sequences 

def test(): 
    test_sequences = [ [1,2,1,2,6] ] 
    for item in test_sequences: 
        print item
        print check_sequence(item)

def main():    
    # Allow user to input from the keyboard the initial_sequence and the level     
    #initial_sequence = []
    #initial_sequence = input("Please enter a valid initial sequence. Use the format [x,y,z], where x,y,z are integers.")
    #level = input("Please enter the level you want")
    initial_sequence = [1]
    level = 10
    n = Node(initial_sequence)
    n.populate_nodes_tolevel(initial_sequence, level)
    n.print_nodes_atlevel(level)


#    test_sequence = [1, 1]
#    print check_sequence(test_sequence)

main()
