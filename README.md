# Project 3

Web Programming with Python and JavaScript

# By JonRider

# Project Overview:
This is a web app that allows users to order pizza and other food items from a virtual online store. The user can add items to their cart, select toppings for certain items and 'checkout'.

An added special feature allows an admin to access the '/fill' route to see and 'complete' orders. The user can then see that their order has been completed.

# Files:

# Templates
This folder contains all the HTML for the project. All templates inherit from base.html. Index.html is my main menu page. Order.html shows users a message after they submit their order. Fill.html is the page for admins to fill orders. Login.html is the login page and register.html is the register page.

# Models.py
This is my models file. I spent way too much time figuring out and managing models! Most of my energy was spent here so I didn't invest a lot of my time with the UI and styling. The result is a functional but ugly site!

Each Menu Item Type has its own model. Then it also has an intermediary class +Item. This allows you to create multiple instances of each item, and to associate each item with different toppings while not overwriting or adding to the base item which would mess my menu up.

Then finally there is a cart model which is separate for each user and has fields to reference each menu item type. The cart model can be marked as ordered and then as completed.

# Views.py
This file contains the main logic for my web app. It controls user login and registration. The order route processes new items when they are added to the cart and adds up the total amount for cart. In the checkout route the users cart is marked as ordered and is posted to the /fill page for admins to access. The fill route then allows admins to mark the cart as completed.

# Urls.py
This file references all the url routes that I have used in my app.

# Static
This folder includes styles.css which is my main stylesheet for this project. I used PureCSS because I wanted to try something besides bootstrap. Also included is script.js which contains all my JavaScript logic for this app. I spent quite a lot of time on the JavaScript. It allows for some cool features like the modal topping pickers for pizzas and subs.

# Admin.py
This file sets up what models can be accessed from the admin page. During development intermediary models were accessible. These were removed in the current version. Admins can however make additions and changes from here such as adding new toppings, adding new item types, or changing item names and prices. 
