# Programacion funcional #

## Funciones de orden superior ##

    def switch(case):
        def case_one():
            return "Case one"
        def case_two():
            return "Case two"
        def case_three():
            return "Case three"

        cases = {
            'one': case_one,
            'two': case_two,
            'three': case_three
            }

        return cases[case]



    
## Comprensión de listas y diccionarios ##

    first_list = range(1,100)
    exp_list = [n**2 for n in first_list]
    exp_list = [n**2 for n in first_list if (n % 2) == 0]

## Funciones lambda ##

    exp_if_pair = lambda n: n**2 if (n % 2) == 0 else False
    exp_if_pair(2)
    

## Generadores ##

    def list_exp_pairs(start, end):
        while(start <= end):
            if (start % 2) == 0:
                yield start**2
            start += 1
    
    for n in list_exp_pairs(1, 100):
        print n


## Decoradores ##

    def a(f):
        def c():
            return '-'+f()+'-'
        return c
    
    @a
    def b():
        return "Test"
