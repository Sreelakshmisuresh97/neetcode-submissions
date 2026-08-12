class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = ['(','{','[']
        close_brackets = [')','}',"]"]
        expr_stack = []
        for b in s:
            if b in open_brackets:
                expr_stack.append(b)
            else:
                op_brkt = open_brackets[close_brackets.index(b)]
                if len(expr_stack)==0 or expr_stack[-1]!=  op_brkt:
                    return False
                else:
                    expr_stack.pop() 

        return not len(expr_stack)            