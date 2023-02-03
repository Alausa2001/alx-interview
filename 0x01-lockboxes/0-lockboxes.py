def canUnlockAll(boxes):
    if type(boxes) is not list:
        return false
    unlocked = [0]
    for n in unlocked:
        for key in boxes[n]:
            if key not in unlocked and key < len(boxes):
                unlocked.append(key)
    return (len(unlocked) == len(boxes))