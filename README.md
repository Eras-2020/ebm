### A simple django e-commerce project

###### Running the project
1. Clone the repository or download zip
2. A virtual Environment.
3. pip install django
4. pip install pillow
5. pip install django-ckeditor
6. pip install django-bootstrap4
7. python manage.py migrate
8. python manage.py runserver

NB: The requirements can be installed directly by running,
pip install -r requirements.txt after which you just have to run python manage.py migrate,
python manage.py runserver.

###### Home page:
1. The navbar - when user not registered it portrays home, blog, contact,
cart, signup and login.
If user is logged in, it shows home, blog, contact, change password, cart, orders,
and logout.
2. Content - Displays products together with their prices, discount, a link to a
detailed view of a product, an add to cart option and the name of the product.
There is also a side view of randomly selected products for customers.

View:
1. Gives a detailed description of a product based on its brand, size,
availability and any other special feature associated with the product.
2. There is also an option to add the product to cart and a go to cart option.

Add to cart:
1. Enables the user to add products of their interest to cart 
for purchase.
2. On clicking the button, a + and - sign are displayed, to
enable the user to adjust the quantity.

###### Blog:
1. Displays administrator articles with option to read and add
 comments.
 
######  Contact:
 1. Consist of an empty form to send a message to admin and 
 contact details of the admin.
 
######  Cart:
 1. Display items to purchase together with their prices, amount,
 and total price for the items.
 2. Gives user an option to adjust the quantity of a product.
 3. There is an option for customers to clear the cart.
 4. A button for the user to continue shopping.
 5. A payment button to make payments for the items in cart.
 
######  Orders:
 1. Displays items purchased together with the delivery status.
 



