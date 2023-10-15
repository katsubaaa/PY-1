# TODO Найдите количество книг, которое можно разместить на дискете

SizeOfDiscet = 1.44 * 1024 * 1024
AmountOfPages = 100
AmountOfLinesOnPage = 50
AmountOfSymbols = 25
SizeOfSymbol = 4


SizeOfBook = AmountOfPages * AmountOfLinesOnPage * AmountOfSymbols * SizeOfSymbol
AmountOfBooks = int(SizeOfDiscet // SizeOfBook)

print("Количество книг, помещающихся на дискету:", AmountOfBooks)
