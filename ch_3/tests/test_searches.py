#!/user/bin/env pyton
from nose.tools import *
from searches.searches import *

def test_Node():
    N = Node('PARENT', 'STATE')
    assert_equal(N.get_parent(), 'PARENT')
    assert_equal(N.get_state(), 'STATE')
    
    def f(state):
        return [state+'_1', state+'_2']
    N.make_children(f)
    assert_equal([n.get_state() for n in N.get_children()],
                 ['STATE_1','STATE_2'])

    return

def test_get_path():
    a = Node(None, 'A')
    b = Node(a, 'B')
    c = Node(b, 'C')
    print c
    assert_equal(get_path(c), ['A', 'B', 'C'])

    return
