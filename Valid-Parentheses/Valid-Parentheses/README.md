Valid Parentheses

Problem

Given a string s containing only the characters:

( ) { } [ ]

determine whether the input string is valid.

A string is valid when:

Every opening bracket has a corresponding closing bracket.

Brackets are closed in the correct order.

Every closing bracket matches the most recent unmatched opening bracket.

Approach

This problem can be solved using a Stack.

A stack follows the LIFO (Last In, First Out) principle.

We store opening brackets in the stack. When a closing bracket is found, we compare it with the most recently added opening bracket.

Step 1: Opening bracket

If the current character is:

(  {  [

push it into the stack.

Step 2: Closing bracket

When we encounter:

)  }  ]

we check the top element of the stack.

If the opening and closing brackets form a valid pair:

()
[]
{}

we remove the opening bracket using pop().

If they do not match, return False.

Step 3: Empty stack

After processing the complete string:

Empty stack → all brackets matched → True

Non-empty stack → some opening brackets are unmatched → False

Example

Input:  "{[()]}"
Output: True

Processing the string:

Character     Stack

{             {
[             { [
(             { [ (
)             { [
]             {
}             empty

The stack is empty at the end, so the string is valid.

Algorithm

Create an empty stack

For every character in the string:

    If it is an opening bracket:
        Push it onto the stack

    If it is a closing bracket:
        If the stack is empty:
            return False

        Check the top of the stack

        If the brackets match:
            Pop the opening bracket
        Otherwise:
            return False

After processing all characters:

    If the stack is empty:
        return True
    Otherwise:
        return False

Complexity

Time Complexity

O(n)

Each character is processed once.

Space Complexity

O(n)

In the worst case, all characters can be opening brackets and need to be stored in the stack.

Key Concept

The main data structure used in this problem is a:

Stack → LIFO (Last In, First Out)

The most recently opened bracket must be the first one to close.
