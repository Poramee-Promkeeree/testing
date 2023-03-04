def staircase(n,display='#'):
    text = ''
    if 0 < n <= 30:
        for i in range(1,n+1):
            text += (' ' * ( n-i ) + display * i + ('\n' if n > 1 else ''))
    return text
