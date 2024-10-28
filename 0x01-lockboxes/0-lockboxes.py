#!/usr/bin/python3
"""
The program aims to solve the following problem:
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1
and each box may contain keys to the other boxes.
Determine if all the boxes can be opened.
"""


class QueueFrontier():
    def __init__(self) -> None:
        self.queue = []

    def add(self, key):
        self.queue.append(key)

    def remove(self):
        key = self.queue[0]
        self.queue = self.queue[1:]
        return key

    def empty(self):
        return len(self.queue) == 0

    def contains(self, key):
        return key in self.queue


def unlock(boxes, key):
    return [box for box in boxes[key] if box >= 0 and box < len(boxes)]


def canUnlockAll(boxes):
    """Determines if all boxes can be opened
    """
    unclockedBoxes = set()
    frontier = QueueFrontier()
    frontier.add(0)

    while True:
        if frontier.empty():
            return False

        box = frontier.remove()
        unclockedBoxes.add(box)

        if len(unclockedBoxes) == len(boxes):
            return True

        for b in unlock(boxes, box):
            if not (frontier.contains(b) or b in unclockedBoxes):
                frontier.add(b)
