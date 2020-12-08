from datastructures.StackLL import Stack

if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())

    for i in range(1000):
        s.push(i)

    for i in range(999):
        s.pop()

    assert s.size() == 1
    print(s.pop())
