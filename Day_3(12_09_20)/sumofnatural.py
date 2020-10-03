n = eval(input('Enter the value of n :'))
sum = 0
for i in range(1, n+1):
    sum = sum + i

print(f'The sum of {n} natural number is : {sum}')


"""
      i = 0   i < 5 + 1      i < 6    0 < 6
        sum = sum + i 
            = 0 + 0 

      i = 1    1 < 6
            = 0 + 1
            sum = 1         i = i + 1
    i = 2       2 < 6
            = 1 + 2
            sum = 3         i = i + 1
    i = 3       3 < 6
            = 3 + 3
            sum = 6         i = i + 1
    i = 4       4 < 6
            = 6 + 4
            sum = 10        i = i + 1
    i = 5       5 < 6
            = 10 + 5
            sum = 15        i = i +1
    i = 6       6 < 6 
        loop terminated                      
"""

""" 5! = 5 * 4 * 3 * 2 * 1
    = 120

    1 . Read a variable n (Enter the value of n)
    2 . Not assigned 0 for any variable
    3 . Logic for factorial ( Multiplications ) 
    4 . Print the output out side the loop 
    """
