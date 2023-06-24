from Book import Book

print("Library Management System")

choice = -1;

while(choice!=0):
	print("1) Admin")
	print("2) Student")

	choice = int(input("\nEnter Your Choice : "))
	if(choice == 1):
		B = Book()
		B.show_all_books()
