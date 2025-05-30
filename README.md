# Puzzles
This repository contains implementations of various data structures and algorithms in Python. The implementations are organized into different modules for easy navigation and understanding.

## Directory Structure
```
python/
    ds/
    algos/
README.md
.gitignore
LICENSE
```

### Data Structures
Some data structure examples.

### Method Name Table for Common Data Structures in Python

| DS ↓ \ Operation →  | construct    | size   | copy     | add             | peek(end) | pop(end)     | pop(idx)      | del(obj/key)  |
| --------------------| ------------ | ------ | -------- | --------------- | --------- | ------------ | ------------- | ------------- |
| tuple               | (x, y, z)    | len(t) | tuple(t) | N/A*            | t[-1]     | N/A*         | N/A*          | N/A*          |
| set                 | {x, y, z}    | len(s) | set(s)   | s.add(x)        | N/A**     | s.pop()      | N/A**         | s.remove(x)   |
| list                | [x, y, z]    | len(l) | list(l)  | l.append(x)     | l[-1]     | l.pop()      | l.pop(i)      | l.remove(x)   |
| collections.deque   | deque([x,y]) | len(d) | deque(d) | d.appendleft(x) | d[-1]     | d.pop()      | N/A***        | d.remove(x)   |
| dict                | {x: a, y: b} | len(d) | dict(d)  | d[k] = v        | N/A**     | d.popitem()  | N/A**         | del d[k]      |
| heapq. (def:min)    | heapify(l)   | len(h) | h[:]     | heappush(h,x)   | h[0]****  | heappop(h)   | N/A*****      | N/A*****      |

### Time Complexity Table for Common Data Structures in Python

| DS ↓ \ Operation →  | add     | peek(end) | pop(end) | pop(idx) | del(obj/key) |
| ------------------- | ------- | --------- | -------- | -------- | ------------ |
| tuple               | N/A*    | O(1)      | N/A*     | N/A*     | N/A*         |
| set                 | O(1)    | N/A**     | O(1)     | N/A**    | O(1)         |
| list                | O(1)    | O(1)      | O(1)     | O(n)     | O(n)         |
| collections.deque   | O(1)    | O(1)      | O(1)     | N/A***   | O(n)         |
| dict                | O(1)    | N/A**     | O(1)     | N/A**    | O(1)         |
| heapq. (def:min)    | O(log n)| O(1)      | O(log n) | N/A***** | N/A*****     |

### Notes:
* *N/A for tuple: Tuples are immutable, so add/pop/del operations don't exist
* **N/A for set/dict: No concept of "last" element or index-based access since they're unordered
* ***N/A for deque: No efficient way to pop at arbitrary index (would require O(n) operation)
* ****heapq peek: h[0] peeks at minimum element (root of min-heap), not "last" element
* *****heapq limitations: No efficient way to pop/delete at arbitrary index; would require O(n) rebuild
* All size operations are O(1) because Python containers maintain length counters
* All copy operations are O(n) because they create a new container with the same elements
* heapq operates on regular Python lists but maintains heap property
* For dict: popitem() removes and returns arbitrary key-value pair in O(1)
* For set: pop() removes and returns arbitrary element in O(1)
* deque supports efficient O(1) operations at both ends: append(), appendleft(), pop(), popleft()
* deque also supports d.appendleft(x) for adding to the beginning in O(1) time


### Algorithms
Some algorithm examples.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or additions.

## Contact
For any questions or suggestions, please open an issue in this repository.
