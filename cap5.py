class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.__last = None

    def is_empty(self):
        return self.__last is None

    def get_first(self):
        if self.is_empty():
            return None
        return self.__last.next.data

    def insert_first(self, data):
        new_node = Node(data)
        if self.is_empty():
            new_node.next = new_node
            self.__last = new_node
        else:
            new_node.next = self.__last.next
            self.__last.next = new_node

    def insert_last(self, data):
        new_node = Node(data)
        if self.is_empty():
            new_node.next = new_node
            self.__last = new_node
        else:
            new_node.next = self.__last.next
            self.__last.next = new_node
            self.__last = new_node

    def delete_first(self):
        if self.is_empty():
            return
        if self.__last.next == self.__last:
            self.__last = None
        else:
            self.__last.next = self.__last.next.next

    def search(self, target):
        if self.is_empty():
            return None
        current = self.__last.next
        while current != self.__last:
            if current.data == target:
                return current.data
            current = current.next
        if self.__last.data == target:
            return self.__last.data
        return None

    def __str__(self):
        if self.is_empty():
            return "[]"
        result = "[" + str(self.__last.next.data)
        current = self.__last.next.next
        while current != self.__last.next:
            result += ", " + str(current.data)
            current = current.next
        result += "]"
        return result

    def step(self):
        if not self.is_empty():
            self.__last = self.__last.next

    def seek(self, target):
        if self.is_empty():
            return
        current = self.__last.next
        while current != self.__last:
            if current.data == target:
                self.__last = current
                return
            current = current.next
        if self.__last.data == target:
            self.__last = current


# Ejemplo de uso
clist = CircularLinkedList()

print(clist.is_empty())  # True

clist.insert_last(10)
clist.insert_last(20)
clist.insert_first(5)

print(clist.get_first())  # 5
print(clist)  # [5, 10, 20]

clist.delete_first()

print(clist)  # [10, 20]

print(clist.search(20))  # 20

clist.step()
print(clist.get_first())  # 10

clist.seek(20)
print(clist.get_first())  # 20
