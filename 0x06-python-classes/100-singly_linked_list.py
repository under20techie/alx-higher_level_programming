#!/usr/bin/python3
""" Contains Node Class"""


class Node:
    """ Node Class """

    def __init__(self, data, next_node=None):
        """ Init Method """

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Gets data """

        return self.__data

    @data.setter
    def data(self, value):
        """Sets data"""

        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ Gets data """

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ Sets next_node """

        if value  is None or type(value) == Node:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """SinglyLinkedList"""

    def __init__(self):
        """ Init method"""

        self.__head = None

    def __str__(self):
        """ Makes list printable """

        rep = ''
        current = self.__head

        while current:
            if current.next_node is None:
                rep += str(current.data)
                break
            rep += str(current.data) + "\n"
            current = current.next_node
        return rep

    def sorted_insert(self, value):
        """ Inserts node in sorted list """

        if self.__head is None or self.__head.data >= value:
            self.__head = Node(value, self.__head)
            return

        current = self.__head

        while current.next_node != None and \
                current.next_node.data < value:
                    current = current.next_node

        current.next_node = Node(value, current.next_node)
