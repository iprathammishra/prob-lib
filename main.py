from collection import userList, bookLust


class Library:
    def __init__(self, container: list, ulst: list) -> None:
        self.container = container
        self.ulst = ulst

    def add_book(self) -> None:
        while True:
            print('\nYou will need the Book ID to add the book to your collection.')
            action = input(
                "Do you have the ID of the book you want to add? (y/n): ")

            match action.lower():
                case 'y':
                    bID = input('Enter the book ID: ')
                    for i, value in enumerate(self.container):
                        if bID == value['id']:
                            if value in self.ulst:
                                print("Book is already added!")
                                return None
                            self.ulst.append(value)
                            print('Book added!')
                            return None
                    print("ID can't be found.")
                case 'n':
                    print("\nGo to 4: 'Book Info' to get the ID.")
                    return None
                case _:
                    print("\nInvalid response! Please choose from: [y, n]")

    def display_books(self) -> None:
        for i, value in enumerate(self.ulst):
            rtxt = f'{i+1}: Book ID {self.ulst[i]["id"]}, {self.ulst[i]["name"]} by {self.ulst[i]["author"]}'
            print("\n" + rtxt)

    def return_book(self) -> None:
        while True:
            print('\nYou will need the Book ID to return the book from your collection.')
            action = input(
                "Do you have the ID of the book you want to return? (y/n): ")

            match action.lower():
                case 'y':
                    bID = input('Enter the book ID: ')
                    for i, value in enumerate(self.container):
                        if bID == value['id']:
                            self.ulst.remove(value)
                            print('Book deleted!')
                            return None
                    print("ID can't be found.")
                case 'n':
                    print("\nGo to 2: 'Display Books' to get the ID of the book.")
                    return None
                case _:
                    print("\nInvalid response! Please choose from: [y, n]")

    def book_info(self) -> None:
        while True:
            name = input("Enter the book or author name: ")
            print('Results: \n')
            for value in self.container:
                if name.lower() in value['author'].lower() or name in value['name'].lower():
                    print(
                        f"ID: {value['id']} Book: {value['name']} Author: {value['author']}")

            if input("Want to search more? (y/n): ") == 'n':
                return None


def main() -> None:
    running = True

    pratham = Library(bookLust, userList)
    while running:
        action = input("\nWhat would you like to do: ")
        match action:
            case '1':
                (pratham.add_book())
            case '2':
                (pratham.display_books())
            case '3':
                (pratham.return_book())
            case '4':
                (pratham.book_info())
            case '5':
                jogging = True
                while jogging:
                    con = input('Do you want to quit? (y/n): ')
                    if con.lower() == 'y':
                        print('Bye!')
                        running = False
                        jogging = False
                    elif con.lower() == 'n':
                        jogging = False
                    else:
                        print("Invalid Input! Please select from [y, n]")
            case _:
                print('Invalid Input! Please select from [1, 2, 3, 4, 5]')


if __name__ == '__main__':
    print(
        """
We can do the following today:
1: Add Book
2: Display Book
3. Return Book
4: Book Info
5: Exit
"""
    )
    main()
