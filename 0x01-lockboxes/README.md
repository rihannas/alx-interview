# 0x01. Lockboxes
## Requirements

### General

-   Allowed editors:  `vi`,  `vim`,  `emacs`
-   All your files will be interpreted/compiled on Ubuntu 14.04 LTS using  `python3`  (version 3.4.3)
-   All your files should end with a new line
-   The first line of all your files should be exactly  `#!/usr/bin/python3`
-   A  `README.md`  file, at the root of the folder of the project, is mandatory
-   Your code should be documented
-   Your code should use the  `PEP 8`  style (version 1.7.x)
-   All your files must be executable

## Tasks

### 0. Lockboxes

You have  `n`  number of locked boxes in front of you. Each box is numbered sequentially from  `0`  to  `n - 1`  and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

-   Prototype:  `def canUnlockAll(boxes)`
-   `boxes`  is a list of lists
-   A key with the same number as a box opens that box
-   You can assume all keys will be positive integers
    -   There can be keys that do not have boxes
-   The first box  `boxes[0]`  is unlocked
-   Return  `True`  if all boxes can be opened, else return  `False`

```
carrie@ubuntu:~/0x01-lockboxes$ cat main_0.py
#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))

carrie@ubuntu:~/0x01-lockboxes$

```

```
carrie@ubuntu:~/0x01-lockboxes$ ./main_0.py
True
True
False
carrie@ubuntu:~/0x01-lockboxes$
```
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
