#!/usr/bin/python3
"""The program aims to solve the following problem:
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1
and each box may contain keys to the other boxes.
Determine if all the boxes can be opened.
"""


def canUnlockAll(boxes: list[list[int]]) -> bool:
    """Determines if all boxes can be opened
    """
    unclockedBoxes = set([0])

    def canUnlockAllBoxesFrom(box: list[int]) -> bool:
        if len(unclockedBoxes) == len(boxes):
            return True
        elif len(box) == 0:
            return False
        else:
            if box[0] not in unclockedBoxes:
                unclockedBoxes.add(box[0])
                return (canUnlockAllBoxesFrom(boxes[box[0]]) or
                        canUnlockAllBoxesFrom(box[1:]))
            return canUnlockAllBoxesFrom(box[1:])
    return canUnlockAllBoxesFrom(boxes[0])
