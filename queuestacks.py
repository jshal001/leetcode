class MyQueue(object):
    
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack1.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        if len(self.stack2) == 0 and len(self.stack1) > 0: 
            #move all items from stack1 to stack 2 and pop from stack2
            while len(self.stack1): 
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()

        else: 
            #if stack 2 isn't empty, just pop from stack 2 for now until it is empty
            return self.stack2.pop()

    def peek(self):
        """
        :rtype: int
        """
        if len(self.stack2) == 0 and len(self.stack1) > 0: 
            #move all items from stack1 to stack 2 and pop from stack2
            while len(self.stack1): 
                self.stack2.append(self.stack1.pop())
            return self.stack2[len(self.stack2) - 1]

        else: 
            #if stack 2 isn't empty, just pop from stack 2 for now until it is empty
            return self.stack2[len(self.stack2) - 1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return not(len(self.stack1) or len(self.stack2))


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

#Time Complexity: O(n) worst case but O(1) amoritized
#Space Complexity: O(n) due to stacks 