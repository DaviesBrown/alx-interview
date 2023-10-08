#!/usr/bin/python3
"""
lockboxes
"""


def canUnlockAll(boxes):
    """
    A method that determines if all the boxes can be opened.
    Args:
      boxes(list[list])
    Return:
      True if all boxes can be opened, else return False
    """
    if not boxes:
        return False
    if len(boxes) == 0:
        return False

    open_box = [0]
    for keys in open_box:
        for key in boxes[keys]:
            if key not in open_box and key < len(boxes):
                open_box.append(key)

    return len(open_box) == len(boxes)
