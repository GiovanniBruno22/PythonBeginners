class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return not self.stack

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return 'Underflow'
        else:
            item = self.stack.pop()
            return item

    def peek(self):
        if self.is_empty():
            return 'Underflow'
        else:
            top = len(self.stack) - 1
            return self.stack[top]

    def __repr__(self):
        if self.is_empty():
            return 'Stack is empty'
        else:
            top = len(self.stack) - 1
            stack_str = f'{self.stack[top]} <-top\n'
            for i in range(top - 1, -1, -1):
                stack_str += str(self.stack[i]) + '\n'
            return stack_str

def main():
    stack = Stack()

    while True:
        print('\n\nStack Operations:')
        print('1. Push')
        print('2. Pop')
        print('3. Peek')
        print('4. Display Stack')
        print('5. Exit')
        ch = int(input('Enter your choice:'))

        if ch == 1:
            item = int(input('Enter item:'))
            stack.push(item)
        elif ch == 2:
            item = stack.pop()
            if item == 'Underflow':
                print('Stack is empty')
            else:
                print('Popped item is:', item)
        elif ch == 3:
            item = stack.peek()
            if item == 'Underflow':
                print('Stack is empty')
            else:
                print('Topmost item is:', item)
        elif ch == 4:
            print(stack)
        elif ch == 5:
            break
        else:
            print('Invalid choice')

if __name__ == '__main__':
    main()
