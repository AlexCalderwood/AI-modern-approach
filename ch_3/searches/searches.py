#!/usr/bin/env python

class Node:
    def __init__(self, parent, state, c, g=None, h=None):
        self.parent = parent
        self.children = None
        self.state = state 
        self.g = g
        self.h = h
        self.count = c

    def __str__(self):
        s = 'state : ' + self.state + '\n'
        
        if self.parent == None:
            s += 'None\n'
        else:
            s += 'parent : ' + self.parent.state + '\n' 
        
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
            c = Node(self,cs,count, None, None)    
            self.children.append(c)
        return count

    def get_children(self):
        return self.children

    def get_parent(self):
        return self.parent

    def get_state(self):
        return self.state

def get_path(node):
    if node.get_parent() == None:
        return [node.get_state()]
    else:
        p = node.get_parent()
        return get_path(node.get_parent())+[node.get_state()]

def tree_search(start_state, goal_state, action_model, q_sort_function):
    c = 0
    curr_N = Node(None, start_state,c, None, None)
    q = []
    while curr_N.get_state() != goal_state:
        print curr_N.get_state()
        c = curr_N.make_children(action_model,c)
        q.extend(curr_N.get_children())
        q = q_sort_function(q)
        curr_N = q.pop()
    
    return get_path(curr_N)

def DFS(Q):
    #for DFS, go to the youngest node next
    Q = sorted(Q,key=lambda x:x.count)

def BFS(Q):
    #for BFS, go to the oldest nose next
    Q = sorted(Q,reverse=True, key=lambda x:x.count)
    return Q

    
