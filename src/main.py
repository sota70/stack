from stack import Stack

stack = Stack(10)
print(stack.clone())
stack.push(2)
stack.push("wassup")
print(stack.clone())
stack.pop()
print(stack.clone())