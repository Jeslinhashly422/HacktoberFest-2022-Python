def solution(n=None):
    if n == None:
        return 0
    if isinstance(n, str):
        try:
            n = int(n)
        except:
            return 0
    if n > 0 and isinstance(n, int):
        try:
            n = int(n)
            return (2**int(n)) - 1
        except:
            return 0 
    else:
        return 0
