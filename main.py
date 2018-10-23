################


#Prithvi Shetty
#Written in Python 3


class Problem:

    #To limit infinite negative possibilities
    def negative(self):
        return(self<0)
    
    #To limit infinite positive possibilities
    def positive(self):
        return(self>3)
    
    #To create all the possible tree branches
    def branch(self):
        np=[]
        
        
        #All the possible actionable outcomes
        #1st number in the tuple indicates number of cannibals on the left bank
        #2nd number in the tuple indicates number of missionaries on the right bank
        #3rd number in the tuple indicates position of boat
            #1 indicates left bank and 2 indicates right bank
        
        state1=(1, 0, 1)
        state2=(2, 0, 1)
        state3=(0, 1, 1)
        state4=(0, 2, 1)
        state5=(1, 1, 1)

        for i in (state1,state2,state3,state4,state5):
            #If position of boat is left bank, this lists out all the possible outcomes
            if self[2]==1:
                branch = [a - b for a, b in zip(self, i)] #Subtracts the current state with the possible state
                branch = tuple(branch)
                if any(Problem.negative(x) for x in branch): #Checks the negative limit
                    continue

                else:
                    np.append(branch)
            #If position of boat is right bank, this lists out of all the possible outcomes
            else:
                branch = [a + b for a, b in zip(self, i)] #Adds the current state with the possible state
                branch = tuple(branch)
                if any(Problem.positive(x) for x in branch): #Checks the positive limit
                    continue

                else:      
                    np.append(branch)


        return np
    
    #This function checks if the state is dead (i.e. when the number of cannibals exceeds the number of missionaries)
    def dead(self):
        return (self[1]>self[0] and self[0]!=0) or (3-self[0]< 3-self[1] and 3-self[0]!=0)
    
    #This function checks if the state has reached the goal state which is (0,0,0)
    def goal(self):
        return(self==(0, 0, 0))

    
    #This function searches the tree with Blind Depth for search
    def blind_dfs(self,queue,dictionary):

        #Checks if goal state is reached, it prints out the path and appends to a dictionary under 'all states'
        if Problem.goal(self):
            queue.append(self)
            print ("Solution:")
            for q in queue:
                print (q)
          
            dictionary['all_states'] += 1
            queue.pop()
            
        #Checks if state is dead and appends to a dictionary under dead states
        #Also appends under ' all states'
        elif Problem.dead(self):
            dictionary['dead_states'] +=1
            dictionary['all_states'] += 1

       #Checks if state is repeated again and appends to a dictionary under repeated states
        elif (self in queue):
            dictionary['repeated_states']+=1
            dictionary['all_states'] += 1
            
        #If valid, then further search deepens
        
        else :
            queue.append(self)
            dictionary['all_states']+=1
            next = Problem.branch(self)
            for i in next:
                Problem.blind_dfs(i,queue,dictionary)
            
            queue.pop()


    def run(self):
        
        #Initialize an empty dictionary to maintain a count of the three states (all states, dead states and repeated states)
        dictionary = {}
        (dictionary['dead_states'], dictionary['all_states'], dictionary['repeated_states']) = (0,0,0)
        
        #Queue to track the path
        queue = []
        
        #Initializer
        Problem.blind_dfs((3,3,1),queue,dictionary)
        print ("totals", dictionary['all_states'] - dictionary['dead_states'] - dictionary['repeated_states'], end=' ')
        print ("illegals", dictionary['dead_states'], end= ' ')
        print("repeats", dictionary['repeated_states'], end= ' ')
    
#Implementation
a=Problem()
a.run()


####################
