#!/usr/bin/python3
"""Contains method that determines if all the
boxes can be opened"""


def canUnlockAll(boxes):
    if not boxes or not boxes[0]:
        return False

    total_boxes = len(boxes)
    locked_boxes = [False] * total_boxes
    locked_boxes[0] = True
    keys = [0]

    while keys:
        current = keys.pop()
        for key in boxes[current]:
            if 0 <= key < total_boxes and not locked_boxes[key]:
                locked_boxes[key] = True
                keys.append(key)

    return all(locked_boxes)
