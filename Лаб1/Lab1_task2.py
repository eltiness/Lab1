# TODO Найдите количество книг, которое можно разместить на дискете
disk=1.44
pages=100
str=50
symb=25
demand=4
memory=disk*1024*1024
weight=pages*str*symb*demand
books=round(memory//weight)
print("Количество книг, помещающихся на дискету:", books)
