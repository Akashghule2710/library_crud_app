# library_crud_app
################################Documentation########################################


I developed a library management system using django framework and django rest framework(DRF)
this is my repository link: https://github.com/Akashghule2710/library_crud_app
I have used VS code as a editor,mySQL as a database,xampp as a localhost
In this library crud app I created two models 
1) UserMaster: UserMaster work as a admin of library management system. only UserMaster have the access to perform crud operations
2) I have created super user to access admin panel
->Admin Registration(signup): for the admin registration you need to do login in django Administration the
for admin panal 
1)open xampp and start mysql and apache server
2)in cmd activate virtual environment <myvenv\Scripts\activate>
3)run server <python manage.py runserver
 4)copy that url and paste it in browser http://127.0.0.1:8000/
 5) go to admin panal http://127.0.0.1:8000/admin/
 6)login django administration   username = akash
                                 password = learnvern123
 #admin signup
 1)after login admin panal in go to myapp and then UserMaster click on it you will see the list registered admin  http://127.0.0.1:8000/admin/myapp/usermaster/
 from here you can add new admin,delete registered admin the all data of admin is automaticaly save on mysql table http://localhost/phpmyadmin/
 this apps mysql database name is "keywordadmin" nad the tables are stored here "myapp_usermaster" to store registerd admin details and "myapp_bookdetails" for storing book details
during registeration of new admin you cannot enter dublecate data because email id and password have unique key constraint so dublecate entries will not go into database
    
#admin login:
Admin login is performed from the index page of the system     http://127.0.0.1:8000/
for admin login I have given a login tab in menu bar after click on that you will see admin login  http://127.0.0.1:8000/loginpage/ .
server side authentication is performed in admin login except the register admin other cannot perform login because entered email and password are
varified by admin databse email and password
These are some registered admin credientials
1)email : "ghuleakash2710@gmail.com", password : "akash123"
2)email : "ramsharma33@gmail.com",password : "ramsharma123"
#crud :
after successfully login admin will land on insert page where he can enter book details.
#insert page : here admin can perform create operation he can insert new book entries http://127.0.0.1:8000/loginadmin/ . 
#Retrive page : here admin can read all available book details  http://127.0.0.1:8000/showtable/ .
#edit and #delete : edit and deleter performed on same page   http://127.0.0.1:8000/showtable/ .
#update:  when you click on edit it jumps on update here you can update existing book details  http://127.0.0.1:8000/editpage/1 .
#delete : in retrive page there is button to perform delete .
if you delete the data will gone from book details table as well as database table   http://127.0.0.1:8000/showtable/ .
#book list:
when a  visit this app there is a book list menu bar on index page by click on that student can see all book record .
http://127.0.0.1:8000/booklist/ .
                     
#rest api :
I have created the api using django rest framework here you can see  http://127.0.0.1:8000/get_book_details/ .
##End##
                     
                    
               
                   
 
            
