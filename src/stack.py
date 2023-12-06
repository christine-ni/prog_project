
class Node:
    def __int__(self, value):
        self.value = value
        self.next = None


class Stack:

    def __int__(self):
        self.head = Node
        self.size = 0

    def push(self, new_element):
        """
        add a new element to the  stack
        """
        new_node = Node()
        new_node.value = new_element
        new_node.next = self.head.next
        self.head.next = new_node
        self.size += 1


    def get_size(self) -> int:
        """
        return size of the stack
        """
        return self.size


    def check_empty(self) -> bool:
        """
        check if the stack is empty
        """
        return self.size == 0


    def pop_element(self):
        """
        delete the last element of the  stack and return it
        """
        if self.check_empty():
            node = self.head.next
            self.head.next = node.next
            node.next = None
            self.head -= 1
            return node.value
        return "Stack is empty"


    def top(self):
        """
        return last element of the stack
        """
        if self.check_empty:
            return self.head.next.value
        return "Stack is empty"



def check_parantheses(check):
    elements = {')':'(', '}': '{', ']': '['}
    in_stack = []
    for i in check:
        if i in elements.values():
            in_stack.append(i)
        else:
            if in_stack[-1] == elements.get(i):
                in_stack.pop()
            else:
                return False
    if not in_stack:
        return True

#print(check_parantheses("({[})"))


def sort_stack(stack: list):
    sort_list = []
    sort_list.append(stack.pop())
    while sort_list:
            a = sort_list.pop()
            b = stack.pop()
            if a < b:
                stack.append(a)
                sort_list.append(b)
            elif a > b and stack:
                sort_list.append(a)
                sort_list.append(b)
            else:
                stack.append(b)
                stack.append(a)
    return stack

#print(sort_stack([5, 2, 7]))

def sort_stack1(sequence: list):
    tmp_stack = []
    while sequence:
        element = sequence.pop()
        while tmp_stack and tmp_stack[-1] > element:
            sequence.append(tmp_stack.pop())
        tmp_stack.append(element)
    return tmp_stack

print(sort_stack1([5, 2, 7, 9, 4]))



def sort_n_merge(queue_first, queue_second):
    tmp_queue = []
    if not queue_first:
        return queue_second
    elif not queue_second:
        return queue_first
    while queue_first and queue_second:
        if queue_first[0] < queue_second[0]:
            tmp_queue.append(queue_first.pop(0))
        else:
            tmp_queue.append(queue_second.pop(0))
    while queue_first:
        tmp_queue.append((queue_first.pop(0)))
    while queue_second:
        tmp_queue.append((queue_second.pop(0)))
    return tmp_queue

def cards(first_q, sec_q):
    moves = 0
    while first_q and sec_q:
        if first_q[0] > sec_q[0]:
            first_q.append(first_q.pop(0))
            first_q.append(sec_q.pop(0))
            moves += 1
        elif sec_q[0] > first_q[0]:
            sec_q.append(sec_q.pop(0))
            sec_q.append(first_q.pop(0))
            moves += 1
        elif moves == 10**6:
            return 'botva'
    if not first_q:
        return 'first', moves
    else:
        return 'second', moves
print(cards([3, 5, 1, 7, 9], [2, 4, 6, 8, 0]))


