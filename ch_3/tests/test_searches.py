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

def test_tree_search():
    goal_state = 'STATE_1_2_1'
    init_state = 'STATE_1'
    def f(state):
        return [state+'_1', state+'_2']
    
    PATH = tree_search(init_state, goal_state, f, BFS)
    assert_equal(PATH, ['STATE_1', 'STATE_1_2', 'STATE_1_2_1']) 

    goal_state = 'STATE_2_2_2'
    PATH = tree_search(init_state, goal_state, f, DFS)
    asset_equal(PATH, ['STATE_2', 'STATE_2_2', 'STATE_2_2_2'])

if __name__ == '__main__':
    test_tree_search()
