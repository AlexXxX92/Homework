from stack.stack import Stack

def validBraces(string):
    s = Stack()
    delim = {'(': ')', '[': ']', '{': '}'}
    for char in string:
        if char in delim.keys():
            s.push(char)
        elif char in delim.values():
            if not s.items or delim[s.pop()] != char:
                return 'Несбалансированно'
    return 'Сбалансированно' if s.is_empty() else 'Несбалансированно'

if __name__ == '__main__':
    pass