#!/usr/bin/python3
"""Defines a class Node"""


class Node:
    """Represents a singly linked list

    Attributes:
    __data (int): private attr
    __next_node (Node) or (None): private attr
    """
    def __init__(self, data, next_node=None):
        """Initializes the data"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """retrieves the data"""
        return self.__data

    @data.setter
    def data(self, value):
        """property setter

        Args:
        value (int):

        Raises:
        TypeError: if data is not an int
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """retrieves next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """property setter

        Args:
        value (int):

        Raises:
        TypeError: if next_node is not a Node or is not None
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


"""Defines a class SinglyLinkedList"""


class SinglyLinkedList:
    """Represents a singly linked list

    Attributes:
    __head (no setter or getter): private attr

    Public instance method: def sorted_insert(self, value):
    """
    def __init__(self):
        """Simple instantiation"""
        self.__head = None

    def sorted_insert(self, value):
        """inserts a new Node into the correct
        sorted position in the list (increasing order)
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """for the print statement in the main file"""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return '\n'.join(values)
