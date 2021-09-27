from Node import *

class ContactsLL:

    # singly linked list of contacts with header node

    def __init__(self):
        self._head = Node("","","",None)
        self._size = 0

    def find(self,name):
    # return contact if found else return None
        p = self._head
        found = False
        while p._next != None and not found:
            if name == p._next._name:
                found = True
            else:
                p = p._next
        if found:
            return (p._next._name,p._next._phone,p._next._address) 
        else:
            return None
            
    def insert(self,contact):
    # if contact not in list insert it and return True else return False
        if self.find(contact[0]):
            return False
        else:
            n = Node(contact[0],contact[1],contact[2],self._head._next)
            self._head._next = n
            self._size = self._size + 1
            return True
            
    def delete(self,name):
    # if contact found then delete it and return True else return False
        if self.find(name) == None:
            return False
        else:
            p = self._head
            found = False
            while p._next != None and not found:
                if name == p._next._name:
                    found = True
                else:
                    p = p._next
            p._next = p._next._next
            self._size = self._size - 1
            return True

    def update(self,contact):
        pass

    def size(self):
        return self._size

    def __str__(self):
        p = self._head
        result = "\n"
        while p._next != None:
            result = result + str(p._next)+"\n"
        p = p._next
        return result+"\n"