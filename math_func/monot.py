import math

input_var = 0101011

class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)

hable = Node()
print(hable)