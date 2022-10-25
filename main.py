import pymysql.cursors
import sys
command=sys.argv


connection = pymysql.connect(host='localhost',
                             port=3307,
                             user='root',
                             password='123',
                             database='book',
                             cursorclass=pymysql.cursors.DictCursor)
def create_table():
     with connection.cursor() as cursor:
        sql = """create table if not exists book_info(
            id int unsigned AUTO_INCREMENT primary key,
            title VARCHAR(100) NOT NULL,
            author VARCHAR(100) NOT NULL,
            published_at DATE,
            exist BOOLEAN NOT NULL DEFAULT FALSE,
            genre VARCHAR(100),
            price dec(6,2) DEFAULT '10.00'
            )"""
        cursor.execute(sql)
     connection.commit()
def create_book():
     with connection.cursor() as cursor:
        title=input("Title: ")
        author=input("Author: ")
        published_at=input("published date: ")
        exist=int(input("is exist? "))
        genre=input("genre: ")
        price=float(input("price: "))
        sql=f"""
        insert into book_info(title,author,published_at,exist,genre,price)
        values("{title}","{author}","{published_at}","{exist}","{genre}",{price})
        
        """
        cursor.execute(sql)
     connection.commit()
def show_all():
    with connection.cursor() as cursor:
        sql="""
         select * from book_info
        
        """
        cursor.execute(sql)
        result=cursor.fetchall()
    return result
def show_book():
    id=input("write id: ")
    with connection.cursor() as cursor:
     sql=f"""
         update book_info set exist=true where id={id} and exist=false and
         set exist=false where id{id} and exist=true
        
        """
     cursor.execute(sql)
     
     result=cursor.fetchone()
    return result
def chance_status():
    id=input("write id: ")
    with connection.cursor() as cursor:
     sql=f"""
        update book_info
         set exist=case
          when exist=0 then 1
          when exist=1 then 0
        end
      where id={id}
        
        """
     cursor.execute(sql)
    connection.commit()
def chance_price():
    id=input("(write id: ")
    new_price=float(input("set new price:  "))
    with connection.cursor() as cursor:
     sql=f"""
        update book_info set price={new_price} where id={id}
        
     
        
        """
     cursor.execute(sql)  
    connection.commit()
    
def remove():
    id=input("write id: ")
    with connection.cursor() as cursor:
     sql=f"""
       delete from book_info where  id={id}
         """
     cursor.execute(sql)
    connection.commit()
def search():
    word=input("word: ")
    with connection.cursor() as cursor:
     sql=f"""
      select * from book_info where  title like "%{word}%" or author like "%{word}%"
         """
     cursor.execute(sql)
     result=cursor.fetchall()
    return result
    
        

if ("add" and "table") in command:
    create_table()
elif  len(command)==3 and command[1]=="add" and command[2]=="book":
    create_book()
elif ("show" and "all") in command:
    print(show_all())
elif len(command)==3 and command[1]=="show" and command[2]=="book":
    print(show_book())
elif len(command)==3 and command[1]=="chance" and command[2]=="status":
    chance_status()
elif len(command)==3 and command[1]=="chance" and command[2]=="price":
    chance_price()
elif len(command)==2 and command[1]=="search":
   print( search())
elif  len(command)==2 and command[1]=="remove":
    remove()

    
    

     

# import os
# import sys
# import datetime
# from tkinter import Y

# if "-" in sys.argv:
#     f=sys.argv.index("-")
#     if  len(sys.argv[1:f])!=0 and len(sys.argv[f+1:])!=0:
#         print("Book name:",*sys.argv[1:f])
#         print("Writer:",*sys.argv[f+1:])
#         print("Added in:",datetime.datetime.today().strftime("%d %b %Y"))
#     else:
#         print("wrong input")


# else:
#     print("wrong input")

# import sys,os
# from datetime import datetime
# from os.path import exists
# if not exists("book_list.txt"):
#     file=open("book_list.txt","x")
# command= sys.argv

# class Book:
#    def set_id(self):
#         with open('book_list.txt', 'r+') as f:
#             obj = f.readlines()
#             last_id = 1
#             if obj:
#                 last_id = int(obj[-5].split(':')[1]) + 1
#             ele = f'ID : {last_id}'
#             f.write(f"{ele}\n")
#         return True
#    def add_book(self):
#         title = input('Please enter book name: \n')
#         author = input('Please enter writer name: \n')
#         with open('book_list.txt', 'a+') as f:
#                 ele = f'Book name : {title}\nWriter name : {author}'
#                 f.write(f"{ele}\n")
#                 print('\nAdded successfully!')
#    def set_date(self):
#         with open('book_list.txt', 'a+') as f:
#                 obj = f.readlines()
#                 ele = f'Added in: {datetime.today().strftime("%d %B %Y")}'
#                 f.write(f"{ele}\n{'*' * 50}\n")
      
#    def show_book(self):
#         id=input("enter id : ")
#         f=open("book_list.txt", "r+")
#         obj=f.readlines()
#         for i in range(0,len(obj),5):
#           search=obj[i].split(":")[1].strip()
#           if id==search:
#             index=i
#             rangelist=[index,index+1,index+2,index+3,index+4]
#             for i in range(len(obj)):
#                 if i in rangelist:
#                  print(obj[i])
#             break
#    def show_all(self):
#           f=open("book_list.txt","r+")
#           obj=f.readlines()
#           for i in range(0,len(obj)):
#               print(obj[i])
#    def remove_book(self):
#         id=input("enter id : ")
#         f=open("book_list.txt", "r+")
#         obj=f.readlines()
#         f.seek(0)
#         for i in range(0,len(obj),5):
#           search=obj[i].split(":")[1].strip()
#           if id==search:
#             index=i
#             f.truncate()
#             rangelist=[index,index+1,index+2,index+3,index+4]
#             for i in range(len(obj)):
#                 if i not in rangelist:
#                   f.write(obj[i])
                 
                 
#             break

              
              
          
# book=Book()
# if "add" in command:
#     book.set_id()
#     book.add_book()
#     book.set_date()
# elif "show" and "all" in command:
#     book.show_book()
# elif "remove" in command:
#     book.remove_book()


    
# def addbook():
#     title=input("enter bookname: ")
#     author=input("please enter author name: ")
#     with open ("book_list.txt","r+") as f:
#         obj=f.readlines()
#         last_id=1
#         if obj:
#             last_id=int(obj[-5].split(":")[1])+1
#         ele=f'ID :{last_id}\n book name: {title}\n Writer name : {author}\n Addded in : {datetime.today().strftime("%d %B %Y")}'
#         f.write(f'{ele}\n{"*" * 50}\n')
#     return True
# def show_book():
#     id=input("enter id : ")
#     f=open("book_list.txt", "r+")
#     obj=f.readlines()
#     for i in range(0,len(obj),5):
#         search=obj[i].split(":")[1].strip()
#         if id==search:
#             index=i
#             rangelist=[index,index+1,index+2,index+3,index+4]
#             for i in range(len(obj)):
#                 if i in rangelist:
#                  print(obj[i])
#             break

# if "add" in command:
#     addbook()
# elif "show" and "book" in command:
#     show_book()
# else:
#     print("wrong input")


    
