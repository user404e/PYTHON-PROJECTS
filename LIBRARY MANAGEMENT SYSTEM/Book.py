class Book:
	def show_all_books(self):
		file = open("BookData.csv")
		books = file.readlines()
		for bookdata in books:
			book = bookdata.split(",")
			print(book[0])

