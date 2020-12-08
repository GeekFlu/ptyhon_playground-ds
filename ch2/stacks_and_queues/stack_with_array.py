from datastructures.Stack import Stack

if __name__ == "__main__":
    stack = Stack()
    print(stack.is_empty())
    print(stack.arr)

    stack.push(1)
    assert stack.size() == 1
    print(stack.arr)

    stack.push(2)
    assert stack.size() == 2
    print(stack.arr)

    stack.push(3)
    assert stack.size() == 3
    print(stack.arr)

    for i in range(18):
        stack.push(i)
        print(stack.arr)

    for i in range(21):
        print(f"Pop value = {stack.pop()}")
    print(stack.arr)

    # if we pop one more an error should happen
    print(stack.pop())

    for i in range(18):
        stack.push(i)
        print(stack.arr)
    print(stack.pop())
    print(stack.arr)