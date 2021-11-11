# CLI Thogakade Python Project
----------
## Instructions
----------
This is a sample project for gain python knowlage and it fetures. This System base on files.
### **System initialize**
#### Initialize 
This will initialize system with db folder
```cmd
main.py system init
```
### **User**

#### Registration
User need to complete registration before use system use below commend to register the it will prompt to enter details
```cmd
main.py user reg
```

#### Login
After registration user need to login to the system then automatically system create session for user
```cmd
main.py user login
```

#### Session
View current session of the login user
```cmd
main.py user session
```
### **Item**

This commend user for create update delete and view all the Items
#### add
```cmd
main.py item add
```
#### all
This commend will allows user to get all items
```cmd
main.py item all
```
#### find
This commend will allows user to find the item by name
```cmd
main.py item find
```

### **Order**
Current login user can place a order by using this section

#### Place Order
User can place order by filling the requird fields
```cmd
main.py order place
```
#### View All
User can view own all orders
```cmd
main.py order all
```