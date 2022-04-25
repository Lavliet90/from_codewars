'''
You need to return a string that looks like a diamond shape when printed on the screen, using asterisk (*) characters.
Trailing spaces should be removed, and every line must be terminated with a newline character (\n).

Return null/nil/None/... if the input is an even number or negative, as it is not possible to print a diamond of even
or negative size.
'''

def diamond(n):
    if n == 1:
        return '*\n'
    elif n>0 and n%2==1:
        diamond=''
        center = (n-1)/2+1
        for line in range(1, n+1):
            if line <= center:
                diamond += (' ' * int(((n+1)/2)-line)) + ('*' * int(line*2-1) + '\n')
            elif line > center:
                line-center
                diamond += (' ' * int(line-center)) + ('*' * int(n-(line-center)*2))  + '\n'
        return diamond
    else:
        return None