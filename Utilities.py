from typing import List


class Stack:
    stack: list

    def __init__(self):
        self.stack = []

    def push(self, o: object):
        self.stack.append(o)

    def pop(self) -> object:
        return self.pop()

    def delete(self) -> bool:
        self.stack.clear()
        return True

    def is_empty(self) -> bool:
        return True if self.stack else False

    def __repr__(self) -> str:
        return self.stack.__repr__()


class Queue:
    queue: List

    def __init__(self):
        self.queue = []

    def enqueue(self, o: object):
        self.queue.append(o)

    def dequeue(self) -> object:
        return self.queue.pop(0)

    def delete(self) -> bool:
        self.queue.clear()
        return True

