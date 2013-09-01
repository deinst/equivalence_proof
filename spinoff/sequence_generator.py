# sequence_generator.py 
# by James DeFilippo
# Generates sequences which satisfy the following three properties: 
# 1. for every two numbers i, there must be a single number i+1 between them
# 2. for every two numbers i+1, there must be a single number i between them
# 3. the number i must occur before the number i+1

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
 
# This function only works for sequences of length < 20   
def check_sequence(sequence): 
    count_list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for c in sequence:
        count_list[c] = count_list[c] + 1 
        if ((c == 1) and ((count_list[c] == count_list[c+1]) or (count_list[c] == count_list[c+1] + 1))):
            pass 
        elif ((c == 19) and ((count_list[c] == count_list[c-1]) or (count_list[c] == count_list[c-1] - 1))):
            pass
        elif (((count_list[c] == count_list[c+1]) or (count_list[c] == count_list[c+1] + 1)) and ((count_list[c] == count_list[c-1]) or (count_list[c] == count_list[c-1] - 1))):
            pass
        else: 
            return False 
    return True
     
# Using sequences of length n, this function creates potential sequences of length n+1 and runs them against the check_sequence method
def generate_sequence(initial_sequence): 
        new_sequences = []
        temp = []
        for i in range(1,20):
            temp = initial_sequence[:]
            temp.append(i)
            if (check_sequence(temp) == True):
                new_sequences.append(temp[:])
            del temp[:] 
        return new_sequences 

# Change value of test_sequences to try out your choice of sequence.
def test(): 
    test_sequences = [ [1,2,1,2,6] ] 
    for item in test_sequences: 
        print item
        print check_sequence(item)

def main():    
    max_length = input("Please enter the maximum length of the sequences you wish to generate: ")
    level = max_length - 1
    initial_sequence = [1]
    n = Node(initial_sequence)
    n.populate_nodes_tolevel(initial_sequence, level)
    n.print_nodes_atlevel(level)

main()
