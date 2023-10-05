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
    for key in open_box:
        for box in boxes[key]:
            if box not in open_box and key < len(boxes):
                open_box.append(box)
     
    return len(open_box) == len(boxes)