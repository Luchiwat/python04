#Function 3 : No Parameter/Have Return
def funcA( ) :
    print('aaaaaa')
    print('vvvvv')
    return 'WoW WoW WoW'

def funcB( ) :
    return 999, True, 12+45
funcA( )
print( funcA( ) )
x=funcA( )

a, b, c =funcB( )
print(f'{a} {b} {c}')