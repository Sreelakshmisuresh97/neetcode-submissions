class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def createString(openp,closep,s,n):
            if len(s)==2*n:
                if openp == closep:
                    res.append(s)
                    return
                
            if openp>closep:
              
                createString(openp,closep+1,s+")",n)    
            if openp<n:
             
                createString(openp+1,closep,s+"(",n)
            
        
        createString(0,0,"",n)
        return res        