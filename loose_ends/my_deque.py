# a deque is a double-ended queue

def palindrome(word):
    from collections import deque
    dq = deque(word)
    while len(dq) >1:
        if dq.pop() != dq.popleft():
            return False
    return True

if __name__ == "__main__":
    print(  palindrome('racecar') ) # True
    print(  palindrome('python') )  # False
    print(  palindrome('radar') )
    print(  palindrome('anna') )
