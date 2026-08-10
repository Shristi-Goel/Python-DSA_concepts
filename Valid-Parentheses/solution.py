"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']'
determine if the input string is valid."""
class Solution(object):
    def isValid(self, s):
        """
        Check whether brackets are balanced using a stack-
           Approach:
        1. Store every opening bracket in a stack.
        2. When a closing bracket is found:
           - Compare it with the most recent opening bracket.
           - If they form a valid pair, remove the opening bracket.
           - Otherwise, return False.
        3. After processing the entire string:
           - If the stack is empty, all brackets matched.
           - Otherwise, some opening brackets were left unmatched.
           """

        # Stack to store unmatched opening brackets
        result_s=[]
        for i in range(len(s)):
            # Push opening brackets into the stack
            if s[i] in "[{(":
                result_s.append(s[i])
            # Handle closing brackets
            elif s[i] in ")}]":
                # If stack is empty, there is no opening bracket to match
                if len(result_s)!=0:
                    # Create a pair using the latest opening bracket
                    # and the current closing bracket
                    if result_s[-1] in "[{(":
                        pair=result_s[-1]+s[i]
                        # Check if the pair is valid
                        if pair=="()"or pair=="[]" or pair=="{}":
                            # Remove the matched opening bracket
                            # (use pop() because stack follows LIFO)
                            result_s.pop()
                        else:
                            # Mismatched bracket pair
                            return False
                else:
                    # Closing bracket appeared before an opening bracket
                    return False
        # If stack is empty, all brackets were matched correctly
        if len(result_s)==0:
            return True
        else: return False

        
s=Solution()
print(s.isValid("{})("))
