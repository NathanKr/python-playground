def outer():
    i_outer = 0

    def inner():
        print(f'in inner() -> i_outer : {i_outer}')
    
    while i_outer < 10:
        inner()
        i_outer += 1

    


# main
outer()        