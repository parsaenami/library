import os
os.system('color')

wr = '\x1b[1;31;47m'
rw = '\x1b[1;37;41m'
br = '\x1b[1;31;40m'
rb = '\x1b[0;30;41m'
wg = '\x1b[0;32;47m'
gw = '\x1b[1;37;42m'
gb = '\x1b[0;30;42m'
bg = '\x1b[1;32;40m'
yb = '\x1b[0;30;43m'
by = '\x1b[2;33;40m'
bp = '\x1b[1;35;40m'
bv = '\x1b[3;35;40m'
pb = '\x1b[5;30;45m'
pw = '\x1b[1;37;45m'
lb = '\x1b[5;30;46m'
cb = '\x1b[0;30;44m'
bc = '\x1b[0;34;40m'
end = '\x1b[0m'

alphabet = tuple('0123456789abcdefghijklmnopqrstuvwxyz')


class Book:
    all_books = []
    isbn_indexing_const = 10 ** 17

    def __init__(self, isbn, name, authors, publisher, subjects, year, pages):
        self.isbn = isbn
        self.name = name
        self.authors = authors.split(',')
        self.publisher = publisher
        self.subjects = subjects.split(',')
        self.year = year
        self.pages = pages

        self.book_data()
        self.new_book()

    def book_data(self):
        self.data = {
            'isbn': self.isbn,
            'name': self.name,
            'authors': self.authors,
            'publisher': self.publisher,
            'subjects': self.subjects,
            'year': self.year,
            'pages': self.pages,
        }

    def check_publisher(self):
        return self.publisher in Publisher.all_publishers

    def new_book(self):
        if self.isbn not in self.all_books:
            self.all_books.append(self.isbn)

    def index_isbn(self, all_books):
        temp = {}
        line, val = '', ''

        for book in all_books:
            index = book.isbn
            key = (index - index % self.isbn_indexing_const, index - index % self.isbn_indexing_const + self.isbn_indexing_const - 1)

            if key in temp.keys():
                temp[key].append([book.isbn, book])

            else:
                temp[key] = [[book.isbn, book]]
            
        for k in temp.keys():
            for v in temp.get(k):
                val += f'{v[0]}-'

            line += f'{k}: {val[:-1]}\n'
            val = ''

        with open('BookISBNIndex.txt', 'w') as file1:
            file1.write(line)
            
        return temp

    def index_name(self, all_books):
        temp = {}
        line, val = '', ''

        for book in all_books:
            for key in alphabet:
                if key in book.name:
                    if key in temp.keys():
                        temp[key].append([book.name, book])

                    else:
                        temp[key] = [[book.name, book]]
        
        for k in temp.keys():
            for v in temp.get(k):
                val += f'{v[0]}-'

            line += f'{k}: {val[:-1]}\n'
            val = ''

        with open('BookTitleIndex.txt', 'w') as file2:
            file2.write(line)

        return temp

    def index_authors(self, all_books):
        temp = {}
        line, val = '', ''
        
        for book in all_books:
            for author in book.authors:
                key = author

                if key in temp.keys():
                    temp[key].append(book.isbn)

                else:
                    temp[key] = [book.isbn]

        for k in temp.keys():
            for v in temp.get(k):
                val += f'{v}-'

            line += f'{k}: {val[:-1]}\n'
            val = ''

        with open('BookAuthorIndex.txt', 'w') as file3:
            file3.write(line)
            
        return temp

    def __repr__(self):
        authors_print, subjects_print = '', ''
        for author in self.authors:
            authors_print += (author.strip() + ',')

        for subject in self.subjects:
            subjects_print += (subject.strip() + ',')

        devider = f"{br}|{end}"
        out = f'{bv}ISBN{end}{br}:{end}{self.isbn} {devider} '
        out += f'{bv}BookName{end}{br}:{end}{self.name} {devider} '
        out += f'{bv}Authors{end}{br}:{end}{authors_print[:-1]} {devider} '
        out += f'{bv}Publisher{end}{br}:{end}{self.publisher} {devider} '
        out += f'{bv}Subjects{end}{br}:{end}{subjects_print[:-1]} {devider} '
        out += f'{bv}PublishedYear{end}{br}:{end}{self.year} {devider} '
        out += f'{bv}PageNo{end}{br}:{end}{self.pages}'

        return out
    
    def simple_repr(self):
        authors_print, subjects_print = '', ''
        for author in self.authors:
            authors_print += (author.strip() + ',')

        for subject in self.subjects:
            subjects_print += (subject.strip() + ',')

        devider = f"|"
        out = f'ISBN:{self.isbn} {devider} '
        out += f'BookName:{self.name} {devider} '
        out += f'Authors:{authors_print[:-1]} {devider} '
        out += f'Publisher:{self.publisher} {devider} '
        out += f'Subjects:{subjects_print[:-1]} {devider} '
        out += f'PublishedYear:{self.year} {devider} '
        out += f'PageNo:{self.pages}'

        return out

###############################################################################################################


class Publisher:
    all_publishers = []

    def __init__(self, id, name, subjects, manager, address):
        self.id = id
        self.name = name
        self.subjects = subjects.split(',')
        self.manager = manager
        self.address = address

        self.publisher_data()
        self.new_publisher()

    def publisher_data(self):
        self.data = {
            'id': self.id,
            'name': self.name,
            'subjects': self.subjects,
            'manager': self.manager,
            'address': self.address,
        }

    def new_publisher(self):
        if self.name not in self.all_publishers:
            self.all_publishers.append(self.name)

    def __repr__(self):
        subjects_print = ''

        for subject in self.subjects:
            subjects_print += (subject.strip() + ',')

        devider = f"{br}|{end}"
        out = f'{bv}PubId{end}{br}:{end}{self.id} {devider} '
        out += f'{bv}PubName{end}{br}:{end}{self.name} {devider} '
        out += f'{bv}SubjectsInterest{end}{br}:{end}{subjects_print[:-1]} {devider} '
        out += f'{bv}HeadName{end}{br}:{end}{self.manager} {devider} '
        out += f'{bv}PubAddress{end}{br}:{end}{self.address}'

        return out

    def simple_repr(self):
        subjects_print = ''

        for subject in self.subjects:
            subjects_print += (subject.strip() + ',')

        devider = f"|"
        out = f'PubId:{self.id} {devider} '
        out += f'PubName:{self.name} {devider} '
        out += f'SubjectsInterest:{subjects_print[:-1]} {devider} '
        out += f'HeadName:{self.manager} {devider} '
        out += f'PubAddress:{self.address}'

        return out

###############################################################################################################

def result_list(result:list, expr, category):
    list_no = 1

    print(rw + f'\n----- Results for "{expr}" in "{category}" -----' + end)

    if len(result) == 0:
        print(f'{rw}!{end} {br}Nothing to show :({end}')

    for res in result:
        print(f'{rw}{list_no}-{end} {res}')
        list_no += 1


class BookStore:
    isbn_indexing = {}
    name_indexing = {}
    authors_indexing = {}

    def __init__(self):
        self.table = {}
        self.pub = {}

    #############################################

    def save_all_books(self):
        list_no = 1
        line = ''
        
        if len(self.table) == 0:
            line += f'! Nothing to show :(\n'

        for key in self.table.keys():
            line += f'{list_no}- {self.table[key].simple_repr()}\n'
            list_no += 1

        with open('books.txt', 'w') as file4:
            file4.write(line)

    def view_all_books(self):
        list_no = 1
        
        if len(self.table) == 0:
            print(f'{rw}!{end} {br}Nothing to show :({end}')

        for key in self.table.keys():
            print(f'{rw}{list_no}-{end} {self.table[key]}')
            list_no += 1

    def insert_book(self, book):
        self.table[book.isbn] = book
        self.isbn_indexing = Book.index_isbn(book, self.table.values())
        self.name_indexing = Book.index_name(book, self.table.values())
        self.authors_indexing = Book.index_authors(book, self.table.values())
        
    def delete_book(self, book):
        self.table.pop(book.isbn)

    def search_book(self, expr, search_type):
        if search_type == 0:
            self.search_book_by_isbn(expr)

        elif search_type == 1:
            self.search_book_by_name(expr)

        elif search_type == 2:
            self.search_book_by_subjects(expr)

        elif search_type == 3:
            self.search_book_by_authors(expr)

    def search_book_by_name(self, name):
        result = []

        for index in name:
            if index in self.name_indexing.keys():
                for book_index in self.name_indexing[index]:
                    if name in book_index[0]:
                        if book_index[1] not in result:
                            result.append(book_index[1])

        result_list(result, name, "Book Name")

    def search_book_by_isbn(self, isbn):
        result = []

        for index in self.isbn_indexing.keys():
            if index[0] <= isbn <= index[1]:
                for book_index in self.isbn_indexing[index]:
                    if book_index[0] == isbn:
                        result.append(book_index[1])

        result_list(result, isbn, "ISBN")

    def search_book_by_authors(self, author):
        result = []

        for index in self.authors_indexing.keys():
            if author in index:
                for book_index in self.authors_indexing[index]:
                    if self.table[book_index] not in result:
                        result.append(self.table[book_index])

        result_list(result, author, "Authors")

    def search_book_by_subjects(self, subjects):
        result = []

        for book in self.table.values():
            for subject in book.subjects:
                if subjects.lower() == subject.lower() or subjects.lower() in subject.lower():
                    result.append(book)

        result_list(result, subjects, "Subjects")

    def update_book(self, book, isbn=None, name=None, authors=None, publisher=None, subjects=None, year=None, pages=None):
        if isbn is not None:
            isbn = int(isbn)
            if isbn not in Book.all_books:
                temp = book.isbn
                book.isbn = isbn
                print(f"{gb}isbn updated from {temp} to {isbn} successfully.{end}")
            else:
                print(f"{rb}there is already a book with given isbn.{end}")
        
        if name is not None:
            temp = book.name
            book.name = name
            print(f"{gb}name updated from {temp} to {name} successfully.{end}")
        
        if authors is not None:
            if authors not in book.authors:
                temp = book.authors
                book.authors = authors.split(',')
                print(f"{gb}authors updated from {temp} to {authors} successfully.{end}")
            else:
                print(f"{rb}there are already similar authors.{end}")

        if publisher is not None:
            temp = book.publisher
            book.publisher = publisher
            print(f"{gb}publisher updated from {temp} to {publisher} successfully.{end}")

            Book.check_publisher(book)
        
        if subjects is not None:
            if subjects not in book.subjects:
                temp = book.subjects
                book.subjects = subjects
                print(f"{gb}subjects updated from {temp} to {subjects} successfully.{end}")
            else:
                print(f"{rb}there are already similar subjects.{end}")
        
        if year is not None and int(year) > 0:
            year = int(year)
            temp = book.year
            book.year = year
            print(f"{gb}year updated from {temp} to {year} successfully.{end}")
        
        if pages is not None and int(pages) > 0:
            pages = int(pages)
            temp = book.pages
            book.pages = pages
            print(f"{gb}pages updated from {temp} to {pages} successfully.{end}")

        self.table[book.isbn] = book
        self.isbn_indexing = Book.index_isbn(book, self.table.values())
        self.name_indexing = Book.index_name(book, self.table.values())
        self.authors_indexing = Book.index_authors(book, self.table.values())

    #############################################

    def save_all_publishers(self):
        list_no = 1
        line = ''
        
        if len(self.pub) == 0:
            line += f'! Nothing to show :(\n'

        for key in self.pub.keys():
            line += f'{list_no}- {self.pub[key].simple_repr()}\n'
            list_no += 1

        with open('publlishers.txt', 'w') as file5:
            file5.write(line)

    def view_all_publishers(self):
        list_no = 1
        
        if len(self.pub) == 0:
            print(f'{rw}!{end} {br}Nothing to show :({end}')

        for key in self.pub.keys():
            print(f'{rw}{list_no}-{end} {self.pub[key]}')
            list_no += 1

    def insert_publisher(self, publisher):
        self.pub[publisher.id] = publisher

    def delete_publisher(self, publisher):
        self.pub.pop(publisher.id)

    def search_publisher(self, expr, search_type):
        if search_type == 0:
            self.search_publisher_by_id(expr)

        elif search_type == 1:
            self.search_publisher_by_name(expr)

    def search_publisher_by_id(self, id):
        result = []

        for publisher in self.pub.values():
            if id == publisher.id:
                result.append(publisher)

        result_list(result, id, "Publisher Id")

    def search_publisher_by_name(self, name, get_id=None):
        result = []

        if get_id:
            for publisher in self.pub.values():
                if name.lower() == publisher.name.lower():
                    return publisher.id
                    
            return None

        for publisher in self.pub.values():
            if name.lower() is publisher.name.lower() or name.lower() in publisher.name.lower():
                result.append(publisher)

        result_list(result, name, "Publisher Name")
        
    def update_publisher(self, publisher, id=None, name=None, subjects=None, manager=None, address=None):
        if id is not None:
            id = int(id)
            if id not in Publisher.all_publishers:
                temp = publisher.id
                publisher.id = id
                print(f"{gb}id updated from {temp} to {id} successfully.{end}")
            else:
                print(f"{rb}there is already a publisher with given id.{end}")
        
        if name is not None:
            temp = publisher.name
            publisher.name = name
            print(f"{gb}name updated from {temp} to {name} successfully.{end}")
        
        if subjects is not None:
            if subjects not in publisher.subjects:
                temp = publisher.subjects
                publisher.subjects = subjects
                print(f"{gb}subjects updated from {temp} to {subjects} successfully.{end}")
            else:
                print(f"{rb}there are already similar subjects.{end}")
        
        if manager is not None:
            temp = publisher.manager
            publisher.manager = manager
            print(f"{gb}manager updated from {temp} to {manager} successfully.{end}")
        
        if address is not None:
            temp = publisher.address
            publisher.address = address
            print(f"{gb}address updated from {temp} to {address} successfully.{end}")

        self.pub[publisher.id] = publisher

    def all_info(self):
        list_no = 1

        if len(self.table) == 0:
            print(f'{rw}!{end} {br}Nothing to show :({end}')
            return

        for book in self.table.values():
            authors_print, book_subjects_print, publisher_subjects_print = '', '', ''
            devider = f"{br}|{end}"

            for author in book.authors:
                authors_print += (author.strip() + ',')

            for book_subject in book.subjects:
                book_subjects_print += (book_subject.strip() + ',')

            try:
                publisher = self.pub[self.search_publisher_by_name(book.publisher, get_id=True)]

                for publisher_subject in publisher.subjects:
                    publisher_subjects_print += (publisher_subject.strip() + ',')
            
                out = f'{bv}ISBN{end}{br}:{end}{book.isbn} {devider} '
                out += f'{bv}BookName{end}{br}:{end}{book.name} {devider} '
                out += f'{bv}Authors{end}{br}:{end}{authors_print[:-1]} {devider} '
                out += f'{bv}Publisher{end}{br}:{end}{book.publisher} {devider} '
                out += f'{bv}Subjects{end}{br}:{end}{book_subjects_print[:-1]} {devider} '
                out += f'{bv}PublishedYear{end}{br}:{end}{book.year} {devider} '
                out += f'{bv}PageNo{end}{br}:{end}{book.pages} {devider} '
                out += f'{bv}PubName{end}{br}:{end}{publisher.name} {devider} '
                out += f'{bv}SubjectsInterest{end}{br}:{end}{publisher_subjects_print[:-1]} {devider} '
                out += f'{bv}HeadName{end}{br}:{end}{publisher.manager} {devider} '
                out += f'{bv}PubAddress{end}{br}:{end}{publisher.address}'
                
            except:
                out = f'{bv}ISBN{end}{br}:{end}{book.isbn} {devider} '
                out += f'{bv}BookName{end}{br}:{end}{book.name} {devider} '
                out += f'{bv}Authors{end}{br}:{end}{authors_print[:-1]} {devider} '
                out += f'{bv}Publisher{end}{br}:{end}{book.publisher} {devider} '
                out += f'{bv}Subjects{end}{br}:{end}{book_subjects_print[:-1]} {devider} '
                out += f'{bv}PublishedYear{end}{br}:{end}{book.year} {devider} '
                out += f'{bv}PageNo{end}{br}:{end}{book.pages} {devider} '
                out += f'{bv}PubName{end}{br}:{end}- {devider} '
                out += f'{bv}SubjectsInterest{end}{br}:{end}- {devider} '
                out += f'{bv}HeadName{end}{br}:{end}- {devider} '
                out += f'{bv}PubAddress{end}{br}:{end}-'

            print(f'{rw}{list_no}-{end} {out}')
            list_no += 1

    def save_all(self):
        list_no = 1
        line = ''

        if len(self.table) == 0:
            line += f'!Nothing to show :(\n'
            return

        for book in self.table.values():
            authors_print, book_subjects_print, publisher_subjects_print = '', '', ''
            devider = f"|"

            for author in book.authors:
                authors_print += (author.strip() + ',')

            for book_subject in book.subjects:
                book_subjects_print += (book_subject.strip() + ',')

            try:
                publisher = self.pub[self.search_publisher_by_name(book.publisher, get_id=True)]

                for publisher_subject in publisher.subjects:
                    publisher_subjects_print += (publisher_subject.strip() + ',')
            
                out = f'ISBN:{book.isbn} {devider} '
                out += f'BookName:{book.name} {devider} '
                out += f'Authors:{authors_print[:-1]} {devider} '
                out += f'Publisher:{book.publisher} {devider} '
                out += f'Subjects:{book_subjects_print[:-1]} {devider} '
                out += f'PublishedYear:{book.year} {devider} '
                out += f'PageNo:{book.pages} {devider} '
                out += f'PubName:{publisher.name} {devider} '
                out += f'SubjectsInterest:{publisher_subjects_print[:-1]} {devider} '
                out += f'HeadName:{publisher.manager} {devider} '
                out += f'PubAddress:{publisher.address}'
                
            except:
                out = f'ISBN:{book.isbn} {devider} '
                out += f'BookName:{book.name} {devider} '
                out += f'Authors:{authors_print[:-1]} {devider} '
                out += f'Publisher:{book.publisher} {devider} '
                out += f'Subjects:{book_subjects_print[:-1]} {devider} '
                out += f'PublishedYear:{book.year} {devider} '
                out += f'PageNo:{book.pages} {devider} '
                out += f'PubName:- {devider} '
                out += f'SubjectsInterest:- {devider} '
                out += f'HeadName:- {devider} '
                out += f'PubAddress:-'

            line += (f'{list_no}- {out}\n')
            list_no += 1

        with open('all.txt', 'w') as file6:
            file6.write(line)

###############################################################################################################


class UserInterface:
    def __init__(self):
        self.store = BookStore()
        print(pw + '::::::::: Welcome to our library! :::::::::' + end)

    def menu(self):
        print(yb + '\nWhare do you want to go?' + end)
        print(by + '1. Books area' + end)
        print(by + '2. Publishers area' + end)
        print(by + '3. See all info' + end)
        print(by + '4. Exit' + end)
        
        menu_input = input('>> ')

        if menu_input == '1':
            self.books()
        
        elif menu_input == '2':
            self.publishers()

        elif menu_input == '3':
            self.store.all_info()
            self.menu()

        elif menu_input == '4':
            self.store.save_all_books()
            self.store.save_all_publishers()
            self.store.save_all()
            print(pw + '\nGoodbye!\n' + end)
            exit(1)

        else:
            print(rb + '\nWrong choice! Try again.\n')
            self.menu()

    def books(self):
        print(yb + '\nwhat do you want to do with books?' + end)
        print(by + '1. Add a book' + end)
        print(by + '2. Update a book' + end)
        print(by + '3. Delete a Book' + end)
        print(by + '4. Search for a book' + end)
        print(by + '5. View all books' + end)
        print(by + '6. Back' + end)
        print(by + '7. Exit' + end)

        book_input = input('>> ')

        if book_input == '1':
            self.add_books()
            self.books()
        
        elif book_input == '2':
            self.update_books()
            self.books()

        elif book_input == '3':
            self.delete_books()
            self.books()

        elif book_input == '4':
            self.search_books()
            self.books()

        elif book_input == '5':
            self.store.view_all_books()
            self.books()

        elif book_input == '6':
            self.menu()

        elif book_input == '7':
            self.store.save_all_books()
            self.store.save_all_publishers()
            self.store.save_all()
            print(pw + '\nGoodbye!\n' + end)
            exit(1)

        else:
            print(rb + '\nWrong choice! Try again.\n' + end)
            self.books()

    def add_books(self):
        isbn = input(bg + '\nEnter ISBN of the book: ' + end)
        while not isbn.isdigit() or len(isbn) != 20:
            if len(isbn) != 20:
                print(br + '\nISBN must have 20 carachters, try again.\n' + end)

            if not isbn.isdigit():
                print(br + '\nISBN must be a number, try again.\n' + end)
                
            isbn = input(bg + '\nEnter ISBN of the book: ' + end)

        name = input(bg + '\nEnter the name of the book: ' + end)
        while len(name) > 200:
            print(br + '\nName must have up to 200 carachters, try again.\n' + end)
            name = input(bg + '\nEnter the name of the book: ' + end)

        authors = input(bg + '\nEnter the authors\' name of the book (Separate authors with ","): ' + end)
        while len(authors) > 200:
            print(br + '\nAuthors name must have up to 200 carachters, try again.\n' + end)
            authors = input(bg + '\nEnter the authors\' name of the book (Separate authors with ","): ' + end)

        publisher = input(bg + '\nEnter the publisher of the book: ' + end)
        while len(publisher) > 200:
            print(br + '\nPublisher must have up to 200 carachters, try again.\n' + end)
            publisher = input(bg + '\nEnter the publisher of the book: ' + end)

        subjects = input(bg + '\nEnter the subjects\' name of the book (Separate subjects with ","): ' + end)
        while len(subjects) > 100:
            print(br + '\nSubjects must have up to 100 carachters, try again.\n' + end)
            subjects = input(bg + '\nEnter the subjects\' name of the book (Separate subjects with ","): ' + end)

        year = input(bg + '\nEnter publish year of the book: ' + end)
        while len(year) != 4 or not year.isdigit():
            if len(year) != 4:
                print(br + '\nPublish year must have 4 carachters, try again.\n' + end)

            if not year.isdigit():
                print(br + '\nPublish year must be a number, try again.\n' + end)
                
            year = input(bg + '\nEnter publish year of the book: ' + end)

        pages = input(bg + '\nEnter page number of the book: ' + end)
        while not pages.isdigit() or len(pages) > 4:
            if len(pages) > 4:
                print(br + '\nPage number must have up to 4 carachters, try again.\n' + end)

            if not pages.isdigit():
                print(br + '\nPage number must be a number, try again.\n' + end)
            
            pages = input(bg + '\nEnter page number of the book: ' + end)

        book = Book(int(isbn), name, authors, publisher, subjects, int(year), int(pages))
        self.store.insert_book(book)
        
        if not book.check_publisher():
            self.check_book_publisher(publisher)

    def update_books(self):
        isbn, name, authors, publisher, subjects, year, pages = None, None, None, None, None, None, None
        isbn_temp = input(bg + '\nEnter ISBN of the book you want to update: ' + end)
        book = self.store.table[int(isbn_temp)]

        print(yb + '\nWhich one do you want to update?' + end)
        print(by + '1. ISBN' + end)
        print(by + '2. Name' + end)
        print(by + '3. Authors' + end)
        print(by + '4. publisher' + end)
        print(by + '5. Subjects' + end)
        print(by + '6. Publish Year' + end)
        print(by + '7. Page number' + end)

        update_book_input = input('>> ')

        if update_book_input == '1':
            isbn = input(bg + '\nEnter ISBN of the book: ' + end)
            while not isbn.isdigit() or len(isbn) != 20:
                if len(isbn) != 20:
                    print(br + '\nISBN must have 20 carachters, try again.\n' + end)

                elif not isbn.isdigit():
                    print(br + '\nISBN must be a number, try again.\n' + end)
                
                isbn = input(bg + '\nEnter ISBN of the book: ' + end)

        elif update_book_input == '2':
            name = input(bg + '\nEnter the name of the book: ' + end)
            while len(name) > 200:
                print(br + '\nName must have up to 200 carachters, try again.\n' + end)
                name = input(bg + '\nEnter the name of the book: ' + end)
        
        elif update_book_input == '3':
            authors = input(bg + '\nEnter the authors\' name of the book (Separate authors with ","): ' + end)
            while len(authors) > 200:
                print(br + '\nAuthors name must have up to 200 carachters, try again.\n' + end)
                authors = input(bg + '\nEnter the authors\' name of the book (Separate authors with ","): ' + end)
        
        elif update_book_input == '4':
            publisher = input(bg + '\nEnter the publisher of the book: ' + end)
            while len(publisher) > 200:
                print(br + '\nPublisher must have up to 200 carachters, try again.\n' + end)
                publisher = input(bg + '\nEnter the publisher of the book: ' + end)
        
        elif update_book_input == '5':
            subjects = input(bg + '\nEnter the subjects\' name of the book (Separate subjects with ","): ' + end)
            while len(subjects) > 100:
                print(br + '\nSubjects must have up to 100 carachters, try again.\n' + end)
                subjects = input(bg + '\nEnter the subjects\' name of the book (Separate subjects with ","): ' + end)
        
        elif update_book_input == '6':
            year = input(bg + '\nEnter publish year of the book: ' + end)
            while not year.isdigit() or len(year) != 4:
                if len(year) != 4:
                    print(br + '\nPublish year must have 4 carachters, try again.\n' + end)

                elif not year.isdigit():
                    print(br + '\nPublish year must be a number, try again.\n' + end)
                
                year = input(bg + '\nEnter publish year of the book: ' + end)
        
        elif update_book_input == '7':
            pages = input(bg + '\nEnter page number of the book: ' + end)
            while not pages.isdigit() or len(pages) > 4:
                if len(pages) > 4:
                    print(br + '\nPage number must have up to 4 carachters, try again.\n' + end)

                elif not pages.isdigit():
                    print(br + '\nPage number must be a number, try again.\n' + end)
                
                pages = input(bg + '\nEnter page number of the book: ' + end)

        else:
            print(rb + '\nWrong choice, try again.\n' + end)
            self.update_books()
        
        self.store.update_book(book, isbn, name, authors, publisher, subjects, year, pages)

    def delete_books(self):
        isbn = input(bg + '\nEnter ISBN of the book you want to delete: ' + end)
        book = self.store.table[(int)]

        self.store.delete_book(book)

    def search_books(self):
        print(yb + '\nHow do you want to search?' + end)
        print(by + '1. By ISBN' + end)
        print(by + '2. By name' + end)
        print(by + '3. By subjects' + end)
        print(by + '4. By authors' + end)
        print(by + '5. Back' + end)
        print(by + '6. Exit' + end)

        search_book_input = input('>> ')

        if search_book_input == '1':
            expr = int(input(bg + '\nEnter ISBN to search: ' + end))
            self.store.search_book(expr, 0)
            self.books()

        elif search_book_input == '2':
            expr = input(bg + '\nEnter name to search: ' + end)
            self.store.search_book(expr, 1)
            self.books()

        elif search_book_input == '3':
            expr = input(bg + '\nEnter subjects to search: ' + end)
            self.store.search_book(expr, 2)
            self.books()

        elif search_book_input == '4':
            expr = input(bg + '\nEnter authors to search: ' + end)
            self.store.search_book(expr, 3)
            self.books()

        elif search_book_input == '5':
            self.books()

        elif search_book_input == '6':
            self.store.save_all_books()
            self.store.save_all_publishers()
            self.store.save_all()
            print(pw + '\nGoodBye!\n' + end)
            exit(1)

        else:
            print(rb + '\nWrong choice, try again.\n' + end)
            self.search_books()

    def check_book_publisher(self, pub_name):
        print(yb + "\nbook's publisher's name was not registered yet." + end)
        print(by + 'do you want to add this publisher?' + end)
        print(by + '1. Yes' + end)
        print(by + '2. No' + end)

        check_publisher_input = input('>> ')

        if check_publisher_input == '1':
            self.add_publishers(pub_name=pub_name)

        elif check_publisher_input == '2':
            pass

        else:
            print(rb + '\nWrong chioce, try again.\n' + end)
            self.check_book_publisher(pub_name)

    def publishers(self):
        print(yb + '\nwhat do you want to do with publishers?' + end)
        print(by + '1. Add a publisher' + end)
        print(by + '2. Update a publisher' + end)
        print(by + '3. Delete a publisher' + end)
        print(by + '4. Search for a publisher' + end)
        print(by + '5. View all publishers' + end)
        print(by + '6. Back' + end)
        print(by + '7. Exit' + end)

        publisher_input = input('>> ')

        if publisher_input == '1':
            self.add_publishers()
            self.publishers()
        
        elif publisher_input == '2':
            self.update_publishers()
            self.publishers()

        elif publisher_input == '3':
            self.delete_publishers()
            self.publishers()

        elif publisher_input == '4':
            self.search_publishers()
            self.publishers()

        elif publisher_input == '5':
            self.store.view_all_publishers()
            self.publishers()

        elif publisher_input == '6':
            self.menu()

        elif publisher_input == '7':
            self.store.save_all_books()
            self.store.save_all_publishers()
            self.store.save_all()
            print(pw + '\nGoodbye!\n' + end)
            exit(1)

        else:
            print(rb + '\nWrong choice! Try again.\n' + end)
            self.books()

    def add_publishers(self, pub_name=None):
        id = input(bg + '\nEnter id of the publisher: ' + end)
        while not id.isdigit() or len(id) != 6:
            if len(id) != 6:
                print(br + '\nId must have 6 carachters, try again.\n' + end)

            elif not id.isdigit():
                print(br + '\nId must be a number, try again.\n' + end)
            
            id = input(bg + '\nEnter id of the publisher: ' + end)

        if pub_name is None:
            name = input(bg + '\nEnter the name of the publisher: ' + end)
            while len(name) > 200:
                print(br + '\nName must have up to 200 carachters, try again.\n' + end)
                name = input(bg + '\nEnter the name of the publisher: ' + end)
        
        else:
            name = str(pub_name)

        subjects = input(bg + '\nEnter the subjects\' name of the publisher (Separate subjects with ","): ' + end)
        while len(subjects) > 200:
            print(br + '\nSubjects must have up to 200 carachters, try again.\n' + end)
            subjects = input(bg + '\nEnter the subjects\' name of the publisher (Separate subjects with ","): ' + end)

        manager = input(bg + '\nEnter the manager\'s name of the publisher: ' + end)
        while len(manager) > 200:
            print(br + '\nManager\'s name must have up to 200 carachters, try again.\n' + end)
            name = input(bg + '\nEnter the manager\'s name of the publisher: ' + end)

        address = input(bg + '\nEnter the address of the publisher: ' + end)
        while len(address) > 200:
            print(br + '\nAddress must have up to 200 carachters, try again.\n' + end)
            name = input(bg + '\nEnter the address of the publisher: ' + end)

        publisher = Publisher(int(id), name, subjects, manager, address)
        self.store.insert_publisher(publisher)
        
    def update_publishers(self):
        id, name, subjects, manager, address = None, None, None, None, None
        id_temp = input('Enter id of the publisher you want to update: ')
        publisher = self.store.pub[int(id_temp)]

        print('Which one do you want to update?')
        print('1. Id')
        print('2. Name')
        print('3. Subjects')
        print('4. Manager')
        print('5. Address')

        update_publisher_input = input('>> ')
        
        if update_publisher_input == '1':
            id = input(bg + '\nEnter id of the publisher: ' + end)
            while not id.isdigit() or len(id) != 6:
                if len(id) != 6:
                    print(br + '\nId must have 6 carachters, try again.\n' + end)

                elif not id.isdigit():
                    print(br + '\nId must be a number, try again.\n' + end)
                
                id = input(bg + '\nEnter id of the publisher: ' + end)

        elif update_publisher_input == '2':
            name = input(bg + '\nEnter the name of the publisher: ' + end)
            while len(name) > 200:
                print(br + '\nName must have up to 200 carachters, try again.\n' + end)
                name = input(bg + '\nEnter the name of the publisher: ' + end)

        elif update_publisher_input == '3':
            subjects = input(bg + '\nEnter the subjects\' name of the publisher (Separate subjects with ","): ' + end)
            while len(subjects) > 200:
                print(br + '\nSubjects must have up to 200 carachters, try again.\n' + end)
                subjects = input(bg + '\nEnter the subjects\' name of the publisher (Separate subjects with ","): ' + end)

        elif update_publisher_input == '4':
            manager = input(bg + '\nEnter the manager\'s name of the publisher: ' + end)
            while len(manager) > 200:
                print(br + '\nManager\'s name must have up to 200 carachters, try again.\n' + end)
                name = input(bg + '\nEnter the manager\'s name of the publisher: ' + end)


        elif update_publisher_input == '5':
            adderss = input(bg + '\nEnter the address of the publisher: ' + end)
            while len(adderss) > 200:
                print(br + '\nAddress must have up to 200 carachters, try again.\n' + end)
                name = input(bg + '\nEnter the address of the publisher: ' + end)

        else:
            print(rb + '\nWrong choice, try again.\n' + end)
            self.update_publishers()

        self.store.update_publisher(publisher, id, name, subjects, manager, address)

    def delete_publishers(self):
        id = input(bg + '\nEnter id of the publisher you want to delete: ' + end)
        publisher = self.store.pub[int(id)]

        self.store.delete_publisher(publisher)

    def search_publishers(self):
        print(yb + '\nHow do you want to search?' + end)
        print(by + '1. By id' + end)
        print(by + '2. By name' + end)
        print(by + '3. Back' + end)
        print(by + '4. Exit' + end)

        search_publisher_input = input('>> ')

        if search_publisher_input == '1':
            expr = int(input(bg + '\nEnter id to search: ' + end))
            self.store.search_publisher(expr, 0)
            self.publishers()

        elif search_publisher_input == '2':
            expr = input(bg + '\nEnter name to search: ' + end)
            self.store.search_publisher(expr, 1)
            self.publishers()

        elif search_publisher_input == '3':
            self.publishers()

        elif search_publisher_input == '4':
            self.store.save_all_books()
            self.store.save_all_publishers()
            self.store.save_all()
            print(pw + '\nGoodBye!\n' + end)
            exit(1)

        else:
            print(rb + '\nWrong choice, try again.\n' + end)
            self.search_publishers()

###############################################################################################################

if __name__ == "__main__":
    ui = UserInterface()
    ui.menu()
