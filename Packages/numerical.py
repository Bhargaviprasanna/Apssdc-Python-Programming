def isPrime(n):
    f=1
    if n == 2:
        return False
    else:
        for i in range(2,(n//2)+1):
            if n%i == 0:
                f=0
                return False
        if f==1:
            return True
def countOccurences(s,m):
    count=0
    for c in range(len(s)):
        if s[c] == m:
            count+=1
    return count