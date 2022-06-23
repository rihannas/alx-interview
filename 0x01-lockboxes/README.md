# 0x01-lockboxes

canUnlockAll(boxes) is a function returns true or false depending if all of the boxes can be opened or no.

- boxes is a list of lists
- A key with the same number as a box opens that box
- You can assume all keys will be positive integers
- There can be keys that do not have boxes
- The first box boxes[0] is unlocked

### Case 1

boxes = [[1], [2], [3], [4], []]

You can open all of the the boxes because the keys in each matches with the boxes's numbers.

box[0] contains key 1, which means you can open box[1] (open)
box[1] contains key 2, which means you can open box[2]
box[2] contains key 3, which means you can open box[3]
box[3] contains key 4, which means you can open box[4]

Finally:
box[0]- open
box[1]- unlocked
box[2]- unlocked
box[3]- unlocked
box[4]- unlocked

### Case 2

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]

You can open all boxes because there are many keys in each box that can open other boxes.
box[0] contains key 1 & 4 & 6, which means you can open box[1] & box[4] & box[6] (open)
box[1] contains key 2, which means you can open box[2]
box[4] contains key 3, which means you can open box[3]
box[6] conatins key 6, which doesnt do much.

box[2] contains key 0 & 4 & 1, which means you can open:
box[0]: (open from the beginning )
box[4]: (unlocked by box[0] already)
box[1]: (unlocked by box[0] already)

box[3] contains key 5 & 6 & 2, which means you can open:
box[5]: contains key 4 & 1
box[6]: (unlocked by box[0] already)
box[2]: (unlocked by box[1] already)

box[5]: contains key 4 & 1, which means you can open:
box[4]: (unlocked by box[0] already)
box[1]: (unlocked by box[0] already)

Finally:
box[0]- open
box[1]- unlocked
box[2]- unlocked
box[3]- unlocked
box[4]- unlocked
box[5]- unlocked
box[6]- unlocked

### Case 3

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]

You can't open all of the boxes because you dont have the keys for it.

box[0] contains key 1 & 4, which means you can open box[1] & box[4] (open):
box[1] contains key 2
box[4] conatains no key

box[2] contains key 0 & 4 & 1, which means you can open:
box[0]: (open already)
box[4] (unlocked by box[0]) and has no keys
box[1] (unlocked by box[0]) and only unlock this box

Finally:
box[0]- open
box[1]- unlocked
box[2]- unlocked
box[3]- locked
box[4]- unlocked but empty
box[5]- locked
box[6]- locked
