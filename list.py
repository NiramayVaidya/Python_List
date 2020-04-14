class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

#Doubly linked null terminated list
class Dlnl():
    def __init__(self):
        self.head = None        
    
    #appends a string element to the list
    def add(self, data):
        node = Node(data)
        if self.head == None:  
            self.head = node
        else:
            node.next = self.head
            node.next.prev = node                       
            self.head = node

    #returns the count of elements in the list
    def count(self):
        node = self.head
        count = 0
        if node != None:
            while node.next != None:
                count += 1
                node = node.next
            count += 1
        return count
    
    #returns the node of the search element
    #returns None if the search element is not present in the list
    def search(self, data):
        node = self.head
        if node != None:
            while node.next != None:
                if (node.data == data):
                    return node
                node = node.next
            if(node.data == data):
                return node
        return None

    #reverses the list in place, does not return it
    def reverse(self):
        node = self.head
        if node != None:
            while node.next != None:
                node = node.next
            self.head = node
            while node.prev != None:
                tmp = node.next
                node.next = node.prev
                node.prev = tmp
                node = node.next
            node.prev = node.next
            node.next = None
    
    #appends list1 to the list on which this method is called
    def extend(self, list1):
        node = self.head
        node1 = list1.head
        len1 = list1.count()
        if node1 != None:
            while node1.next != None:
                node1 = node1.next
            while len1:
                '''
                temp = Node(node1.data)
                node.prev = temp
                temp.next = node
                node = temp
                self.head = node
                node1 = node1.prev
                '''
                self.add(node1.data)
                node1 = node1.prev
                len1 -= 1

    #removes the element from the list specified by node
    def remove(self, node):
        if node != None:
            node.prev.next = node.next
            node.next.prev = node.prev
    
    #custom str() method to print the list as a sequence of elements in it
    #rather than printing it's object format
    def __str__(self):
        output = ""
        node = self.head
        if node != None:      
            while node.next != None:
                output += node.data + ' '
                node = node.next
            output += node.data
        return output[::-1]

def main():
    test_list = Dlnl()
    test_list.add('a')
    test_list.add('b')
    test_list.add('c')
    print(test_list)
    print(test_list.count())
    test_list.reverse()
    print(test_list)
    test_list.remove(test_list.search('b'))
    print(test_list)
    test_list.remove(test_list.search('d'))
    print(test_list)
    del test_list

    test_list = Dlnl()
    test_list.add('a')
    test_list.add('b')
    test_list.add('c')

    test_list_1 = Dlnl()
    test_list_1.add('d')
    test_list_1.add('e')
    test_list_1.add('f')
    print(test_list_1)

    test_list.extend(test_list_1)
    print(test_list)

    del test_list
    del test_list_1

if __name__ == '__main__':
    main()
