from ContactsLL import *

def load_contacts(fname):
    contacts = ContactsLL()
    with open(fname) as f:
      for line in f.readlines():
        line = line.strip("\n")
        c = line.split(":") 
        contacts.insert((c[0],c[1],c[2]))
    return contacts

def main():
    contacts = load_contacts("contacts.dat")
    print()
    while True:
        s = input("i n:p:a, d n, f n, u n:p:a, p, s, q for quit: ").strip()
        if s[0] == 'i':
          contact = s[1:].strip().split(":")
          if contacts.insert(contact):
            print("\n",contact[0]," INSERTED\n")
          else:
            print("\n",contact[0]," IS ALREADY PRESENT\n")
        elif s[0] == 'd':
          name = s[1:].strip()
          if contacts.delete(name):
            print("\n",name," DELETED\n")
          else:
            print("\n",name," NOT FOUND\n")
        elif s[0] == 'f':
          name = s[1:].strip()
          c = contacts.find(name)
          if c == None:
            print("\nNo entry for "+c) 
          else:
            print("\n",c,"\n")
        elif s[0] == 'u':
          contact = s[1:].strip().split(":")
          if contacts.update(contact):
            print("\n",contact[0]," UPDATED\n")
          else:
            print("\n",contact[0]," NOT FOUND\n")
        elif s[0] == 'p':
          print(contacts)
        elif s[0] == 's':
          print("\nSize = ",contacts.size(),"\n")
        elif s[0] == 'q':
          break
        else:
          print("Invalid option")

main()