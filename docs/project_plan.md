# CLI Thogakade Python Project Plane
## Project
### Item
#### **Save**
    - Input
      - id
      - name
      - price
      - qty
    - Output
      - Success:
        - Item Saved successfully.!
      - Error:
        - Item Fail to Save.!

#### **Find**
    - Input
      - item_name
    - Output
      - Success:
        - return Item data
      - Error:
        - return None

#### **Get All**
    - Input
      - None
    - Output
      - Success:
        - return list of all items
      - Error:
        - return None
### User
#### **Registration**
    - Input
      - email
      - password
    - Output
      - Success:
        - User successfully registered!
      - Error:
        - User alredy exist.!
        - Exception

#### **Login**
    - Input
      - email
      - password
    - Output
      - Success:
        - User successfully login.!
      - Error:
        - Error: password not matched
        - Error: email not found.!
        - Error: email can not be null

#### **View Current Session**
    - Input
      - None
    - Output
      - Current login user data

### Order

#### **Place Order**
    - Input
      - list of items
    - Output
      - Success:
        - Your order has been placed. Thank you.!
      - Error:
        - Please Try again.!

#### **View all**
    - Input
      - None (get current user session)
    - Output
      - Success:
        - List of current user orders
      - Error:
        - No Orders found

### System Init
#### **Init**
    - Input
      - None
    - Output
      - Success:
        - System initialized.!
      - Error:
        - Already initialized the System.!

