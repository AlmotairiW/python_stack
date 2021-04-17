class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None


class SList:
    def __init__(self):
        self.head = None

    def add_to_front(self, val):
        new_node = SLNode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self

    def remove_from_front(self):
        current_head = self.head
        val = self.head.value
        self.head = self.head.next
        current_head.next = None

        return val

    def remove_from_back(self):
        runner = self.head
        while(runner.next.next != None):
            runner = runner.next
        val = runner.next.value
        runner.next = None
        return val

    def print_values(self):
        runner = self.head
        while(runner != None):
            print(runner.value)
            runner = runner.next
        return self

    def add_to_back(self, val):
        if self.head == None:
            self.add_to_front(val)
            return self
        runner = self.head
        while(runner.next != None):
            runner = runner.next
        new_node = SLNode(val)
        runner.next = new_node

        return self

    def remove_val(self, val):
        if(self.head.value == val):
            self.head = self.head.next
            return self

        runner = self.head
        while(runner.next != None):
            if(runner.next.value == val):
                if(runner.next.next != None):
                    runner.next = runner.next.next
                else:
                    runner.next = None
                    return self
            runner = runner.next

        return self
    def insert_at(self, val, n):
        if(n == 0):
            self.add_to_front(val)
            return self
        
        counter = 1
        runner = self.head
        while(runner != None):
            if(counter == n):
                if runner.next == None:
                    self.add_to_back(val)
                    return self
                else:
                    new_node = SLNode(val)
                    new_node.next = runner.next
                    runner.next = new_node

                    return self
            counter += 1
            runner = runner.next
        print("N out of list length")
        return self
my_list = SList()
my_list.add_to_front("are").add_to_front(
    "Linked lists").add_to_back("fun!").print_values()
# print(f"{my_list.remove_from_back()}, removed")
# my_list.remove_val('fun!').print_values()
print('----')
my_list.insert_at('NEW', 4).print_values()
