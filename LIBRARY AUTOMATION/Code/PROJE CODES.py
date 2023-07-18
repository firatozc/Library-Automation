# -*- coding: utf-8 -*-
"""
FIRAT ÖZCAN 21050911003
BERK UYSALGİL 21050911041
MUSTAFA SELİM ATEŞMEN 21050911039
"""

import matplotlib.pyplot as plt

admin_or_user = input("Are you (1) admin or (2) user: ")

class Library():
            
    number_of_book = 0
    def user_greeting(self):
        global number_of_book
        print("==================================")
        information = int(input("Welcome the Library what do you want\n (1) will you buy a book\n (2) will you deliver a book\n (3) will you extend the time for delivering back a book\n (4) will you see which books are in the library\n (5) Exit\n "))
        
        if information == 1 and self.number_of_book >= 4:
            
            print("You can just buy less than 4 books")
            print()
            self.user_greeting()
        elif information == 1 and self.number_of_book < 4:
                
            book_name=input("Which book are you going to take? ")
            
            with open("BOOK_İNFO.txt","r",encoding="utf8") as file:
                lines=file.readlines()
                books=[]
                for line in lines:
                    line=line.rstrip()
                    splitted_books=line.split(" ")
                    
                    if len(splitted_books) != 8:
                        splitted = splitted_books[0].replace("-"," ")
                        if book_name.title() == splitted:                    
                            books.append(splitted)
            
                if len(books) == 0:
                    print("we are sorry we don't have that book maybe you should want to take another book")
                    print("Maybe you wanna take another book")
                    self.user_greeting()
                
                elif len(books) == 1:
                    print("we have already had only one book so you can take it")
                    self.number_of_book += 1
                    time=int(input("how many days after will you deliver the book: ")) 
                    while time > 30:
                        print("You cannot take the book for bigger than 30 days")
                        time=int(input("how many days after will you deliver the book: "))
                    
                    with open("BOOK_İNFO.txt","r",encoding="utf8") as file:
                        books2=[]
                        lines=file.readlines()
                        for line in lines:
                            line=line.rstrip()
                            book=line.split(" ")[0].replace("-"," ")
                            books2.append(book)
                    
                    with open("BOOK_İNFO.txt","r",encoding="utf8") as file:
                        
                        lines=file.readlines()
                        sentence = []
                        index = 0
                        count = 0
                        for line in lines:
                            line=line.rstrip()
                            sentence.append(line)
                            splitted_line = line.split(" ")
                            bookname=line.split(" ")[0].replace("-"," ")
                            if book_name.title() == bookname and len(splitted_line) == 5:
                                index = count
                            else:
                                count += 1
                    
                    
                    with open("BOOK_İNFO.txt","w",encoding="utf8") as file:   #AYNI ZAMANDA BU ALINAN KİTAPLARI TAKEN_BOOKS .TXT ÜZERİNE KAYDETMEN LAZIM
                        count2=0 
                        for i in range(len(sentence)):
                                                
                            if count2 != index:
                                file.write(sentence[count2])
                                file.write("\n")
                                count2 += 1
                            else:
                                file.write(sentence[count2])
                                file.write(" ")
                                file.write("TAKEN")
                                file.write(" ")
                                file.write(str(time)+"Day Time")
                                file.write("\n")
                                
                                count2 += 1
                    print("The process successful")
                    print()
                    self.user_greeting()
                        
                else:
                    
                    print("we have" +" "+str(len(books))+" "+ "books with different publishing")
                    self.number_of_book += 1
                    with open("BOOK_İNFO.txt","r",encoding="utf8") as file:
                        publishing=[]                    
                        lines=file.readlines()
                        
                        for line in lines:
                            line=line.rstrip()
                            splitted_line = line.split(" ")
                            splitted_published = line.split(" ")[4].replace("-"," ")
                            books_name= line.split(" ")[0].replace("-"," ")
                                                   
                            if book_name.title() == books_name and len(splitted_line) == 5:                            
                                publishing.append(splitted_published)
                                    
                    print(publishing)
                    choice=input("Which Publishing You Want: ") 
                    time=int(input("how many days after will you deliver the book: ")) 
                    while time > 30:
                        print("You cannot take the book for bigger than 30 days")
                        time=int(input("how many days after will you deliver the book: "))
                    with open("BOOK_İNFO.txt","r",encoding="utf8") as file:
                        sentences=[]
                        index=0
                        count=0
                        lines=file.readlines()
                        
                        for line in lines:
                            line=line.rstrip()
                            sentences.append(line)
                            splitted_published = line.split(" ")[4].replace("-"," ")
                            books_name= line.split(" ")[0].replace("-"," ")
                            
                            if book_name.title()==books_name and choice.title() == splitted_published:
                                    index = count
                            else:
                                count += 1
                    
                    with open("BOOK_İNFO.txt","w",encoding="utf8") as file:   #AYNI ZAMANDA BU ALINAN KİTAPLARI TAKEN_BOOKS .TXT ÜZERİNE KAYDETMEN LAZIM
                        count2=0
                        for i in range(len(sentences)):
                                                
                            if count2 != index:
                                file.write(sentences[count2])
                                file.write("\n")
                                count2 += 1
                            else:
                                file.write(sentences[count2])
                                file.write(" ")
                                file.write("TAKEN")
                                file.write(" ")
                                file.write(str(time)+"Day Time")
                                file.write("\n")
                                
                                count2 += 1    
                    print("The process successful")
                    print()    
                    self.user_greeting()                
                
        elif information == 2:
            book_name=input("which book are you going to deliver: ")
            with open("BOOK_İNFO.txt","r",encoding="utf8") as file:
                sentence = []
                lines=file.readlines()
                count=0
                for line in lines:
                    line=line.rstrip()
                    list_line = line.split(" ")
                    bookname=line.split(" ")[0].replace("-"," ")
                    
                    if book_name.title() == bookname:
                        count += 1
                
                    if book_name.title() == bookname and len(list_line) == 8:
                        liste=line.split(" ")
                        del liste[-1]
                        del liste[-1]
                        del liste[-1]
                
                        line=" ".join(liste)
                        sentence.append(line)
                        
                    else:
                        sentence.append(line)
                
                if count == 1:
                    with open("BOOK_İNFO.txt","r",encoding="utf8") as file:
                        lines =file.readlines()
                        for line in lines:
                            line=line.rstrip()
                            splitted = line.split(" ")
                            splitted_book = splitted[0].replace("-"," ")
                            if book_name.title() == splitted_book and len(splitted) != 8:
                                print("You entered wrong book name because that book isn't taken, maybe you want to try again.")
                            else:
                                pass
                    
                    with open("BOOK_İNFO.txt","w",encoding="utf8") as file:
                        for i in sentence:
                            file.write(i)        
                            file.write("\n")
                    print("The process successful")
                    print()
                    self.user_greeting()
                    
                else:
                    
                    with open("BOOK_İNFO.txt","r",encoding="utf8") as file:
                        
                        amount_of_publishing=[]                    
                        lines=file.readlines()
                        
                        for line in lines:
                            
                            line=line.rstrip()
                            splitted_line = line.split(" ")
                            splitted_published = line.split(" ")[4].replace("-"," ")
                            books_name= line.split(" ")[0].replace("-"," ")
                            if book_name.title() == books_name and len(splitted_line) == 8:
                                amount_of_publishing.append(splitted_published)
                    
                    if len(amount_of_publishing) == 0:
                        print("You entered wrong book name because that book isn't taken, maybe you want to try again.\n")
                        self.user_greeting()
                    
                    else:
                        print("there are more than one of that book so")
                        print(f"Publications of books bought related to {book_name}")            
                        print(amount_of_publishing)
                        publishing = input("What is the publishing: ")
                        
                        with open("BOOK_İNFO.txt","r",encoding="utf8") as file:
                            sentences = []
                            lines=file.readlines()
                            count=0
                            for line in lines:
                                line=line.rstrip()
                                bookname=line.split(" ")[0].replace("-"," ")
                                Publishing=line.split(" ")[4].replace("-"," ")
                                
                                if book_name.title() == bookname:
                                    count += 1
                            
                                if book_name.title() == bookname:
                                    if publishing.title() != Publishing:
                                        sentences.append(line)
                                        
                                    if publishing.title() == Publishing:
                                        
                                        liste2=line.split(" ")
                                        del liste2[-1]
                                        del liste2[-1]
                                        del liste2[-1]
                                
                                        line=" ".join(liste2)
                                        sentences.append(line)
                                        
                                else:
                                    sentences.append(line)
                        
                        with open("BOOK_İNFO.txt","w",encoding="utf8") as file:
                            for i in sentences:
                                file.write(i)
                                file.write("\n")                
                        print("The process successful")
                        print()
                        self.user_greeting()
    
        elif information == 3:
            book_name=input("For which book you wanna extend the time: ")
            day=int(input("In how many days will you deliver the book: "))
            while day>30:       
                if day > 30:
                    print("You can extend the time for a maximum of 30 days. \n")
                    day=int(input("In how many days will you deliver the book: "))
            new_day=str(day)+"Day"    
            
            books=[]
            
            with open("BOOK_İNFO.txt","r",encoding="utf8") as file:
                
                lines = file.readlines()
                for line in lines:
                    line=line.rstrip()
                    splitted_book = line.split(" ")[0].replace("-"," ")
                    if book_name.title() == splitted_book:
                        books.append(splitted_book)
            
            if len(books) == 1:
                with open("BOOK_İNFO.txt","r",encoding="utf8") as file:
                    sentences=[]
                    lines = file.readlines()
                    index=0
                    count=0
                    for line in lines:
                        line=line.rstrip()
                        splitted_book2 = line.split(" ")[0].replace("-"," ")
                        
                        if book_name.title() != splitted_book2:
                            sentences.append(line)
                            count += 1
                        else:    
                            line_list = line.split(" ")
                            line_list[6] = new_day
                            line_string = " ".join(line_list)
                            sentences.append(line_string)
                            index=count
                     
                with open("BOOK_İNFO.txt","w",encoding="utf8") as file:  
                    for i in range(len(sentences)):
                        file.write(sentences[i])
                        file.write("\n")
                print("The process successful")
                self.user_greeting()
                
            else:
                publishing = []
                with open("BOOK_İNFO.txt","r",encoding="utf8") as file:
                    lines = file.readlines()
                    for line in lines:
                        line=line.rstrip()
                        splitted_book = line.split(" ")[0].replace("-"," ")
                        splitted_publising = line.split(" ")[4].replace("-"," ")
                        if book_name.title() == splitted_book:
                            publishing.append(splitted_publising)
                print("There are more publishing for which you want to extend time")
                print(", ".join(publishing))
                which_publishing = input("What publishing do you want: ")
                
                with open("BOOK_İNFO.txt","r",encoding="utf8") as file:
                    sentences=[]
                    lines = file.readlines()
                    index=0
                    count=0
                    for line in lines:
                        line=line.rstrip()
                        splitted_book2 = line.split(" ")[0].replace("-"," ")
                        splitted_publising2 = line.split(" ")[4].replace("-"," ")
                        
                        if book_name.title() != splitted_book2:
                            sentences.append(line)
                            count += 1
                            
                        elif book_name.title() == splitted_book2 and which_publishing.title() != splitted_publising2:
                            sentences.append(line)
                        
                        elif book_name.title() == splitted_book2 and which_publishing.title() == splitted_publising2:
                            line_list = line.split(" ")
                            line_list[6] = new_day
                            line_string = " ".join(line_list)
                            sentences.append(line_string)
                            index=count
                   
                with open("BOOK_İNFO.txt","w",encoding="utf8") as file2:    
                    for i in range(len(sentences)):
                        file2.write(sentences[i])
                        file2.write("\n")
                print("The process successful")
                self.user_greeting()
        
        elif information == 4:
            
            with open("BOOK_İNFO.txt","r",encoding="utf8") as file:
                books=[]
                lines=file.readlines()
                for line in lines:
                    line = line.rstrip()
                    splitted=line.split(" ")
                    book=splitted[0].replace("-"," ")
                    if book not in books:
                        books.append(book)
                    
                print(books)
                print()
                self.user_greeting() 
        
        elif information == 5:
            print("Exiting The System")
        
    def user_registering(self):
        print()
        name,surname=input("Welcome the library can you please enter the name and surname to check if you registered or not: ").split(" ")
        full_name=str(name.capitalize())+" "+str(surname.capitalize())
        names_surnames=[]
        with open("USER_İNFO.txt","r",encoding="utf8") as info: # BURADA ENCODİNG KISMINA utf8 olmazsa ISO-8859-1 deneyin o zaman oluyor.
            file=info.readlines()
            for lines in file:
                line=lines.rstrip()
                splitted=line.split(" ")
                name_surname=splitted[0].replace("-"," ")
                names_surnames.append(name_surname)
                    
        if full_name in names_surnames:
            print("you have already registered here \n")
            self.user_greeting()
                    
        else:
            print("you have been not registered here so \nI will register here ")
            with open("USER_İNFO.txt","a",encoding="utf8") as info2:
                phone=int(input("can you give me your phone number: "))      
                email=input("can you give me your email adress: ")
                age=int(input("can you give me your age: "))
                
                info2.write("\n")            
                info2.write(full_name.replace(" ","-"))
                info2.write(" ")
                info2.write(str(phone))
                info2.write(" ")
                info2.write(email)
                info2.write(" ")
                info2.write(str(age))
                
                print()
                
            print("The process successful")
            self.user_greeting()
        
class Admin_Part():
    
    counter=0
    def indicate_admin(self):
        global counter
        passwords=[]
        
        with open("PASSWORDS.txt","r",encoding="utf8") as pasw:
            file=pasw.readlines()
            for lines in file:
                lines=lines.rstrip()
                splitted=lines.split(" ")
                passwords.append(splitted[1])
    
        while self.counter != 3:
            password = input("please enter the password: ")
            if password in passwords :
                print()
                print("Welcome the admin page\n")
                self.greeting_admin()
                break
            else:
                self.counter += 1
                print("You entered wrong password")
                
        if self.counter == 3:
            print()
            print("You entered wrong passwords 3 times.")
            print("Exiting The System")
            
    def greeting_admin(self):
        print("======================================")
        information = int(input("Welcome the admin part what do you want\n (1) will you register new admin\n (2) will you remove user\n (3) Would you like to see the visualization of which books were bought\n (4) Exit\n "))
        
        if information == 1:
            self.register_new_Admin()
            self.greeting_admin()
        
        elif information == 2:
            self.user_removing()
            print()
            self.greeting_admin()
        
        elif information == 3:
            self.visualization_taken_books()
            print()
            self.greeting_admin()
        else:
            print("Exiting The System")
    
    def register_new_Admin(self):
        
        name=input("please enter your name: ")
        surname=input("please enter your surname: ")
        password=input("please enter your password: ")
        
        with open("PASSWORDS.txt","a",encoding="utf8") as file:
            
            file.write("\n"+name+"-"+surname+" "+password)
        print("The process successful")
        print()
        
    def user_removing(self):
        users=[]
        name_surname=input("What is the name and surname you want to remove:")
        
        with open("USER_İNFO.txt","r",encoding="utf8") as info:
        
            lines=info.readlines()
            index = 0
            count = 0
            for line in lines:
                line=line.rstrip()
                split=line.split(" ")[0].replace("-"," ")
                
                if name_surname.title() == split:
                    users.append(line)
                    index = count
                    count += 1
                else:
                    users.append(line)
                    count += 1
        
        with open("USER_İNFO.txt","w",encoding="utf8") as info2:    
            
            for i in range(len(users)):
                
                if i != index:
                    info2.write(users[i])
                    info2.write("\n")
                else:
                    pass
        print("The process successful")
                
    def visualization_taken_books(self):
        taken_books = ["0"]
        days = ["0"]   #If I don't put 0, the graph doesn't look good.
        with open("BOOK_İNFO.txt","r",encoding="utf8") as file:
            lines = file.readlines()
            for line in lines:
                line=line.rstrip()
                splitted=line.split(" ")
                if len(splitted) == 8:
                    name=splitted[0].replace("-"," ")
                    day=splitted[6].replace("Day","")
                    taken_books.append(name)
                    days.append(day)
        
        plt.barh(taken_books,days,color="black",edgecolor="blue")
        plt.xlabel("day")
        plt.ylabel("books")
        plt.title("taken books")
        plt.show()
                        
LIBRARY=Library()    
ADMIN = Admin_Part()  

while True:

    if admin_or_user == "1":
        ADMIN.indicate_admin()
        print()
        break
    elif admin_or_user == "2":
        LIBRARY.user_registering()
        print()
        break
    else:
        print("You entered wrong number")
        admin_or_user = input("Are you (1) admin or (2) user: ")

