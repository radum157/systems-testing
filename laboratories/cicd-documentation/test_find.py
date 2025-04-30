import pytest
from tree import Tree
from node import Node

# ---------- Fixtures ----------
@pytest.fixture
def sample_tree():
    tree = Tree()
    tree.root = Node(10)
    tree.root.left = Node(5)
    tree.root.right = Node(15)
    return tree

# ---------- Tests ----------
def test_find_existing_node(sample_tree):
    node = sample_tree.find(5)
    assert node is not None
    assert node.data == 5

def test_find_nonexistent_node(sample_tree):
    node = sample_tree.find(99)
    assert node is None

def test_find_root_node(sample_tree):
    node = sample_tree.find(10)
    assert node is not None
    assert node.data == 10

def test_find_in_empty_tree():
    tree = Tree()
    assert tree.find(10) is None
