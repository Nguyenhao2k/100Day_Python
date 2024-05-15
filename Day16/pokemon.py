from prettytable import PrettyTable
mytable = PrettyTable()

mytable.field_names = ['POKEMON NAME', 'TYPE']
mytable.add_rows(
    [
                ['Pikachu', 'Electric'],
                ['Squiritle', 'Water'],
                ['Charmander', 'Fire']
                ]
    )
mytable.align = "l"
mytable.border = True
mytable.header = True
print(mytable)