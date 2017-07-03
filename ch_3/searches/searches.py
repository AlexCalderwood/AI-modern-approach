#!/usr/bin/env python

class Node(object):
    ''' Node class for use in graph searching
    parent is node object
    c is node count (for use by BFS, and DFS que ordering)
    g is cost function
    h is heuristic 

    methods are make_children(), which generates child nodes bsed on action_model(<current node state>)

    get_<attributes> methods 
    
    costf defines the cost of child nodes relative to parent

    costh should return score heuristic based on state at node. 

    idea is this is a pretty general class, costf and costh should be modified for particular problem. '''


    def __init__(self, parent, state, c, g=0, h=None):
        self.parent = parent
        self.children = None
        self.state = state 
        self.g = g
        self.h = h
        self.count = c

    def __str__(self):
        s = 'state : ' + self.state + '\n'
        
        if self.parent == None:
            s += 'parent : None\n'
        else:
            s += 'parent : ' + self.parent.state + '\n' 
       
        s += 'count : ' + str(self.count) + '\n'

        s +='children : '
        if self.children == None:
            s += 'None'
        else:
            for c in self.children:
                s+= c.get_state() + ';'

        return s

    def make_children(self,action_model,count):
        child_states = action_model(self.state)
        self.children = []
        for cs in child_states:
            count += 1
            cg = self.cost_f(self.g)
            ch = self.cost_h(cs)
            c = Node(self,cs,count, cg, ch)    
            self.children.append(c)
        return count

    def cost_h(self, state):
        #problem specific function to calculate goodness heuristic from state required!
        return 0

    def cost_f(self, parent_cost):
        #should be modified to be problem specific!
        return parent_cost + 1

    def get_children(self):
        return self.children

    def get_parent(self):
        return self.parent

    def get_state(self):
        return self.state

    def get_g(self):
        return self.g

def get_path(node):
   ''' returns path which got to node, by backtracking along parents of nodes recursively '''

   if node.get_parent() == None:
        return [node.get_state()]
   else:
        p = node.get_parent()
        return get_path(node.get_parent())+[node.get_state()]

def tree_search(start_state, goal_state, action_model, q_sort_function, graph=False):
    ''' 
    Does tree or graph seach of nodes from start state, to goal state.
    Action model is function to generate child states from current node statem q_sort_function is function to sort node Q based on e.g. cost, to get next node to visit'''
    
    c = 0
    curr_N = Node(None, start_state,c, 0, None)
    q = []

    while curr_N.get_state() != goal_state:
        c = curr_N.make_children(action_model,c)
        q.extend(curr_N.get_children())
        if not q:
            return 'No way to get to goal!'
        q = q_sort_function(q)
        curr_N = q.pop()
    
    return get_path(curr_N)

def DFS(Q):
    #for DFS, go to the youngest node next
    Q = sorted(Q,key=lambda x:x.count)
    return Q

def BFS(Q):
    #for BFS, go to the oldest nose next
    Q = sorted(Q, reverse=True, key=lambda x:x.count)
    return Q

def uniformCost(Q):
    #for uniform cost, goes to the cheapest one next
    Q = sorted(Q, reverse=True, key=lambda x:x.g)
    return Q
   
def A_star(Q):
    #for A star search, goes to the cheapest cost + heuristic node
    Q = sorted(Q, reverse=True, key=lambda x: x.g+x.h)
    return Q
