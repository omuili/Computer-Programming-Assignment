class Node:

    def __init__(self, name, phone, address, next):
        self._name = name
        self._phone = phone
        self._address = address
        self._next = next

    def __str__(self):
        return "("+self._name+","+self._phone+","+self._address+")"