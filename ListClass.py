class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class MyList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)

    def duplicate_even(self):
        current = self.head
        even_list = MyList()
        while current:
            if current.data % 2 == 0:
                even_list.append(current.data)
            current = current.next

        if not self.head:
            self.head = even_list.head
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = even_list.head

    def print(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()
