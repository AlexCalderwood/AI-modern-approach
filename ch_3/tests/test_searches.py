#!/usr/bin/env python
from nose.tools import *
from searches.searches import *

def test_Node():
    N = Node('PARENT', 'STATE',0)
    assert_equal(N.get_parent(), 'PARENT')
    assert_equal(N.get_state(), 'STATE')
    
    def f(state):
        return [state+'_1', state+'_2']
    N.make_children(f,0)
    assert_equal([n.get_state() for n in N.get_children()],
                 ['STATE_1','STATE_2'])

    return

def test_get_path():
    a = Node(None, 'A',0)
    b = Node(a, 'B', 1)
    c = Node(b, 'C', 2)
    print c
    assert_equal(get_path(c), ['A', 'B', 'C'])

    return

def test_DFS():
    a = Node(None, 'A',0)
    b = Node(a, 'B', 1)
    c = Node(b, 'C', 2)

    q = [b,c,a]
    q = DFS(q)
    assert_equal(q, [a,b,c])

def test_BFS():
    a = Node(None, 'A',0)
    b = Node(a, 'B', 1)
    c = Node(b, 'C', 2)
    q = [b,c,a]
    q = BFS(q)
    assert_equal(q, [c,b,a])

def test_greedyBestFirstSearch():
    a = Node(None, 'A',0,20)
    b = Node(a, 'B', 1,30)
    c = Node(b, 'C', 2,40)

    q = [b,c,a]
    q = greedyBestFirstSearch(q)
    assert_equal(q,[c,b,a])

def test_uniform_cost():
    a = Node(None, 'A',0,20,22)
    b = Node(a, 'B', 1,30,25)
    c = Node(b, 'C', 2,40,0)
    q = [b,c,a]
    q = uniform_cost(q)
    assert_equal(q,[b,a,c])

def test_tree_search():
    goal_state = 'STATE_1_2_1'
    init_state = 'STATE_1'
    def f(state):
        return [state+'_1', state+'_2']
    
    PATH = tree_search(init_state, goal_state, f, BFS)
    assert_equal(PATH, ['STATE_1', 'STATE_1_2', 'STATE_1_2_1']) 

    goal_state = 'STATE_1_2_2'
    PATH = tree_search(init_state, goal_state, f, DFS)
    assert_equal(PATH, ['STATE_1', 'STATE_1_2', 'STATE_1_2_2'])
   
    goal_state = 'STATE_1_2_1'
    init_state = 'STATE_1'
    PATH = tree_search(init_state, goal_state, f, greedyBestFirstSearch)
    assert_equal(PATH, ['STATE_1', 'STATE_1_2', 'STATE_1_2_1']) 
  
    return

