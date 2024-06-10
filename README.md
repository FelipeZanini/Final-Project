# _Zanfe_

This e-commerce platform is a haven for fashion enthusiasts and home decor aficionados alike, with a primary focus on clothing, particularly jeans and t-shirts, it provides a diverse array of styles, fits, and designs to suit every taste and occasion, from classic denim staples to trendy graphic tees, customers can explore an extensive selection of apparel that combines comfort, quality, and style.

  ![Mock Up](/readme//MOCKUP.png)
  - The live link can be found here: [Zanfe](https://zanfe-009510b2eec0.herokuapp.com/)

# UX
Welcome to Zanfe e-commerce, a site made for all needs, clothing and home goods! Our user experience (UX) design offers customers a smooth purchasing experience for apparel and home decoration. Our platform is made to fit your demands, whether you're renovating your living area or changing your wardrobe.

## Target Audience
The target audience for our e-commerce that offers home goods. Convenience, quality, and style are important to our customers when it comes to personal style and home decoration. Usually young to middle-aged adults who enjoy the comfort of online shopping. This market seeks products that effortlessly combine fashionable design with useful and fashionable clothing's homeware items.

## Goals
<details>
<summary>Goals Details</summary>
  
**Customer Goals:**
- Desired Products: Customers want to find the goods or services they are looking to buy easily, this entails effective category navigation, filters, and sorting choices.

- Products Description: Customers can easily find product details, such as specifications, photos, other customers testimonial and full descriptions. Making planned purchasing 
  decisions having access to complete and accurate information.
  
- Secure Checkout Process: A smooth and safe checkout experience is our priority for customers. This entails safe payment methods, and personal data security.
  Order tracking: In order to keep track of their purchases, customers want to have access to order tracking information's. Keeping them informed and in control by providing updates on order processing, shipping, and delivery.

**Business Goals:**
- ⁤Customer Satisfaction: Offering professional styling guidance demonstrates our dedication to making sure customers are happy with the clothes we choose, making them feel and look 
  their best. ⁤

- ⁤Loyal Customers: We are compromised with customer loyalty, always offering the best user experience making our customer wish to buy again. ⁤

- ⁤Safety: We place a high priority on protecting the financial and personal data of our clients. ⁤⁤The following safety precautions are in place to guarantee a secure purchasing  
  experience: ⁤

**User Experience:**

- Design a user-friendly, aesthetically pleasing website that makes it simple for customers to browse and locate the products. ⁤
   
- Create a user-friendly search and filtering system that makes it easy for customers to find particular supplements depending on their dietary preferences and fitness objectives. ⁤

- Optimise the website for quick loading times and flawless cross-platform operation to boost user happiness and promote return visits. ⁤

**Segure Checkout Process:**

- Put security measures in place to safeguard consumer information, guarantee a secure online shopping environment, and encourage customers to make transactions.

- Simplify the checkout process with quick order processing and user-friendly payment options to deliver a flawless shopping experience.
</details>
<hr>

## User Stories
<details>
<summary>User Stories Details</summary>

- As a User I want to easily login and logout so I can better manage my personal information.
- As a Guest I want to easily create an account using my email or social media credentials.
- As a Guest I want to browse products without creating an account.
- As a Shopper I want to select the product quantity so I can easily choose how many items I want to buy.
- As a Shopper I want to browse products by name or description.
- As a Guest I want to add products to my bag and wish list without creating an account.
- As a Guest I want to add products to my bag and wish list without creating an account.
- As a User I want to view my order history to see my previous purchases.
- As a User I want to update my personal information like shipping address and password(future feature).
- As a User I want to receive email notifications about my orders and personal information update(future feature).
- As a Shopper I want to select product size so I can easily get the correct size(future feature).
</details>
<hr>

## Scope
<details>
<summary>Scope Details</summary>

1. **Products Page:** Well-structured product page, allowing users to see each product rating category and price, and functions to add to card or wishlist.
2. **User Accounts:** This application provides account registration, to secure a checkout and visualize order history.
3. **Shopping Bag & Wishlist:** Shoppers will be able to add and see bags and wishlists, this feature is implemented using cookies via JavaScript.
4. **Product Reviews:** A review page will be implemented, enabling customers to provide feedback and ratings for products they have purchased and full CRUD operations for their testimonials.
5. **User-Friendly & Responsive Design:** The website will be optimized for various devices, ensuring a consistent and user-friendly experience for both desktop and mobile users.
</details>

## Design Choices
<details>
<summary>Design Choices Details</summary>
  
### Colors

![image](/readme/colors.png)

- The color palette chosen for Zanfe e-commerce is to have a visually appealing and unified brand identity, simple and minimalistic. 
- **(Black):** This color is presented in the main nav and buttons.
- **(White):** White is used as a background color for all the pages of the application.
- **#b64545(Red):** This colour is just presented in the secondary nav bar.

### Images
- **Hero image:** Leaving the boutique with her purchase in hand, the happiness of the woman expressions as she navigates the shopping experience. Here's why each element contributes to imprinting a sense of joy.

![image](/readme/hero-image.png)

</details>

<hr>

### Frameworks
- I decided to utilise Bootstrap for my website because it made it simple and quick for me to construct a responsive design that functions well across a range of devices. 

### Custom Javascript
- Cookies are used in this project to store wishlist and bag items, storing product id and quantity values in a dictionary.
- Decrement and increment buttons are presented on the bag page.
- Remove product button is also presented, deleting the desired product from the dictionary.
  
</details>

## Information Architecture
<details>
<summary>Information Architecture Details</summary>
  
1. **Order:**
   - User(Foreingkey to AUTH_USER): The user associated with the order.
   - Date Ordered(DateTimeField): The date and time when the order was made.
   - Email(EmailField): The email address of the user.
   - Order Number(IntegerField): Indicates unique indentifier for the order.
   - Complete(BooleanField): Indicates whether the order has been approved.
   - Delivery Cost(DecimalField): Indicates the delivery cost.
   - Order total(DecimalField): Indicates the order total.
   - Grand Total(DecimalField): Indicates the grand total.
   - Stripe Pid(CharField): Indicates the stripe pid.

2. **Order Item:**
   - User(Foreingkey to AUTH_USER): The user associated with the order item.
   - Product(Foreingkey to Product Model): The product associated with the order item.
   - Order(Foreingkey to Product Model): The order associated with the order item.
   - Quantity(IntergerField): Indicates the product quantity.
   - Date added(DateTimeField): The date and time when the order item was added.

3. **Shipping Address:**
   - User(Foreingkey to AUTH_USER): The user associated with the order.
   - Order(Foreingkey to Product Model): The order associated with the order item.
   - Address(CharField): Indicates the address line one.
   - City(CharField): Indicates the city of shipping.
   - County(CharField): Indicates the county of shipping.
   - Eircode(CharField): Indicates the eircode of shipping.
   - Date added(DateTimeField): The date and time when the order item was added.

4. **Contact Us:**
   - Name(CharField): Indicates the name for the newsletters sign up.
   - Email(CharField): Indicates the email for the newsletters sign up.
   - Message(CharField): Indicates the message for the newsletters sign up.
   - Date added(DateTimeField): The date and time when the order item was added.

5. **Category:**
   - name(CharField): Indicates the name of the category.
   - Friendly Name(CharField): Indicates the friendly name of the category.

6. **Product:**
   - SKU(CharField): Indicates the SKU of the product.
   - Name(CharField): Indicates the name of the product.
   - Description(TextField): Indicates the description of the product.
   - Price(DecimalField): Indicates the price of the product.
   - Category(Foreingkey to Category Model): The category associated with the product.
   - Rating(DecimalField): Indicates the rating of the product, and its evaluated after each user review by update rating function.
   - Image Url(CharField): Indicates the image url of the product.
  
7. **User Rate:**
   - User(Foreingkey to AUTH_USER): The user associated with the order.
   - Rating(DecimalField): Indicates the rating of the product, and its evaluated after each user review by update rating function.
   - Product(Foreingkey to Product Model): The product associated with the order item.
   - Date added(DateTimeField): The date and time when the order item was added.

  
8. **Testimonial**
   - User(Foreingkey to AUTH_USER): The user associated with the order.
   - Testimonial Text(TextField): Indicates the testimonial text of the product associeted with the user.
   - Rating(DecimalField): Indicates the rating of the product, and its evaluated after each user review by update rating function.
   - Product(Foreingkey to Product Model): The product associated with the order item.
   - Date added(DateTimeField): The date and time when the order item was added.

9. **Address Profile:**
   - User(Foreingkey to AUTH_USER): The user associated with the order.
   - Address_line(CharField): Indicates the address line one.
   - City(CharField): Indicates the city of shipping.
   - Eircode(CharField): Indicates the eircode of shipping.
   - County(CharField): Indicates the county of shipping.
   - Phone(CharField): Indicates the eircode of shipping.
   - Date added(DateTimeField): The date and time when the order item was added.


</details>
<hr>

## Wireframes
<details>
<summary>Wireframes Details</summary>
  
- Home Page:
 ![image](/readme/HOME-PAGE-WIREFRAME.png)

- Product Page:
 ![image](/readme/Product_Page_Wireframe.png) 

- Product Detail Page:
 ![image](/readme/PRODUCT_DETAIL_WIREFRAME.png)

- Profile Page:
 ![image](/readme/Profile_update_wireframe.png)

 - Product Review Page:
 ![image](/readme/review_page_WIREFRAME_NEW.png)

- Wishlist Page:
 ![image](/readme/WISHLIST_WIREFRAME.png)

 - Newsletter Page:
 ![image](/readme/news-WIREFRAME.png)

- Contact Us Page:
 ![image](/readme/contact_us_wireframe_update.png)

- Reviews Page:
 ![image](/readme/ADD_REVIEW_WIREFRAME.png)

- Edit Your Product Rating Page:
 ![image](/readme/EDIT_YOUR_RATING_WIREFRAME.png)

- Edit Your Product Testimonial Page:
 ![image](/readme/EDIT_TESTIMONIAL_WIREFRAME.png)

- Reviews Page (Mobile View):

 ![image](/readme/IPHONE_WIREFRAME_VIEW.png)

- Product List (Tablet View):

 ![image](/readme/TABLET_WIREFRAME_VIEW.png)

</details>
<hr>

## Entity–Relationship Model
<details>

 ![image](/readme/new_diagram.png)
</details>

## Database Choice
I used PostgreSQL as the database for this project. Hosting the application on Heroku allows for easy deployment and scalability, and PostgreSQL is one of the supported and recommemdede databases on the Heroku platform.


<hr>

### CRUD
<details>
<summary>CRUD Details</summary>

- **Bag:**
  
- Increase item quantity
![image](/readme/in-bag.png)

- Decrease item quantity
![image](/readme/ds-bag.png)

- Remove item from bag
![image](/readme/ex-bag.png)


- **Wishlist:**
  
- Remove item from wishlist
![image](/readme/ex-wishlist.png)

- **Testimonial:**
  
- Edit testimonial
![image](/readme/EDIT_TESTIMONIAL_NEW.png)

- Remove text testimonial 
![image](/readme/DELETE_REVIEW_NEW.png)

- **Rating:**
  
- Edit product rating
![image](/readme/EDIT_RATING_NEW.png)

</details>
<hr>

# Agile Process
## User Story Templates

![image](/readme/user-stories.png)


- [**LINK TO THE TEMPLATE**](https://github.com/users/FelipeZanini/projects/10/views/1)
  
## Implemented Features 
### Features
**Navigation:**
<details>
<summary>Navigation Details</summary>

- **Desktop**
  
  ![image](/readme/nav-desktop.png)

<hr>
  
- **Tablet**
  
  ![image](/readme/nav-tablet.png)

<hr> 

- **Mobile**

![image](/readme/nav-mob.png)

<hr>

- To improve browsing and provide quick access to key features and material, our website has an intuitive navigation system.
- Fixed Navigation: When visitors scroll down the page, the navigation bar stays visible at the top.

</details>
<hr>

**Sign in/ Sign up:**
<details>
<summary>Sign in/ Sign up Details</summary>
  
![image](/readme/sign-up.png)

<hr>

![image](/readme/singin-page.png)

<hr>

- Users can sign in using their email address or name. The sign-in page offers a clear link to the registration process for new users who haven't signed up yet.
- Sign-up: If the user's name or email address is already in the system, a clear error message will appear; otherwise, the sign-up page contains a link to the 
  sign-in page, the user's username and email address are unique to the system.
  
</details>
<hr>

**Products Page:**
<details>
<summary>Products Page Details</summary>

![image](/readme/produc-page.png)

<hr>

![image](/readme/product-detail-page.png)

<hr>

- Simplify the checkout process with quick order processing and user-friendly payment options to deliver a flawless shopping experience.
- Our Products Page makes shopping easier for visitors by improving their experience from browsing to buying.
- Product Information: By providing users with concise, vital information on each product, they can make well-informed decisions and ensure they have all the 
  information they need at a glance.
- Quantities & Descriptions: The product's name, price, rating, and category are all clearly stated on the product detail page. The quantity area allows users 
  to easily select how many things they want.

</details>
<hr>

**Bag, Wishlist and Checkout:**
<details>
<summary>Bag, Wishlist and Checkout details</summary>

![image](/readme/shoping-bag.png)

<hr>

![image](/readme/wishlist-page.png)

![image](/readme/checkout-page.png)

<hr>

- Simplify the checkout process with quick order processing and user-friendly payment options to deliver a flawless shopping experience.
- By streamlining the purchasing process, our Bag & Checkout feature guarantees a quick and easy transaction for customers.
- Bag Page: Users may conveniently manage the products they have chosen on the bag page. Every product has its name, price, SKU, and image displayed. To  
  provide complete control over the order, the user can easily modify the quantity of things or remove products from the bag using the quantity button.
- Checkout Page: Security and ease of use are the design features of our checkout page. Important data, such as shipping and credit card information, is 
  gathered via an intuitive checkout form. Users can review their order on the order summary page located on the checkout page. By assisting customers in verifying their choice prior to finalising their transaction, this synopsis promotes transparency.

</details>
<hr>

**Profile:**
<details>
<summary>Profile Details</summary>

![image](/readme/PROFILE_PAGE_NEW.png)

<hr>

- Simplify the checkout process with quick order processing and user-friendly payment options to deliver a flawless shopping experience.
  With the help of our profile function, users can track their order history and manage account details in a personalised hub.
- Order History: Customers have easy access to a thorough record of their previous orders arranged by order number. The user may easily monitor or place  
  another order by just clicking on the order number to view the specifics of their past purchases.

</details>
<hr>

**Order Detail:**
<details>
<summary>Order Detail</summary>

![image](/readme/order-detail-page.png)


<hr>

</details>
<hr>

**Product Review:**
<details>
<summary>Product Review</summary>

![image](/readme/PRODUCT_REVIEW_NEW.png)


<hr>

</details>
<hr>

**News Letters SignUp:**
<details>
<summary>News Letters SignUp</summary>

![image](/readme/newsl-singup-page.png)


<hr>

- Subscribers often receive exclusive discounts, promotions, and special offers that are not available to non-subscribers. This can include early access to 
  sales, limited-time discounts, and subscriber-only promotions, helping customers save money on their clothing purchases.

</details>

<hr>

**Reviews:**
<details>
<summary>Reviews Details</summary>

![image](/readme/reviews-page.png)

<hr>

- **(Authorized User - Update)**

![image](/readme/ed-testimonal.png)
![image](/readme/ed-review.png)

<hr>

- **(Authorized User - Delete)**

![image](/readme/ex-testimonal.png)

<hr>

- Users can interact with our products and services by providing feedback through the reviews page feature. Users can utilise this tool to voice their opinions 
  regarding our company, goods, and overall experience.
- User-generated Reviews: This feature allows users who are signed in and have already bought the spefic product to post reviews. Users can offer thorough 
  feedback to help us improve and support other.
- Editing and Deleteing Reviews: We respect authenticity, thus we provide people the option to alter or remove their reviews so they may maintain control over 
  their input. Users are empowered to edit their reviews if their thoughts alter over time thanks to this strategy that is easy to utilise.


</details>
<hr>

**Messages Notifications:**
<details>
<summary>Messages Notifications Details</summary>

<hr>

- There's a succes message if the user logged in. 
![image](/readme/signin-msg.png)

- There's a succes message if the user logged out. 
![image](/readme/signout-msg.png)

<hr>

- There's a info message when a testimonial is submitted. 
![image](/readme/test-sub-msg.png)

<hr>

- There's a info message if the user edit a product rating.
![image](/readme/edt-rating-msg.png) 

<hr>

- There's a danger message if the user remove a testimonial.
![image](/readme/ex-testimonial-msg.png)


<hr>

- There's a success message if the user submit a newsletters forms. 
![image](/readme/form-sub-msg.png)

<hr>

</details>
<hr>


### Error 404
<details>
<summary>Error Page Details</summary>

- **404 Error Page:**
  
  ![image](/readme/page404.png)


</details>
<hr>

## Future Features

- As a user of our e-commerce platform, you will have the ability to update your personal information, including your shipping address and password, conveniently within your user profile. This feature aims to provide you with greater control over your account settings and enhance your overall user experience.

- As a shopper on our e-commerce platform, we understand the importance of getting the correct size when purchasing clothing items. To enhance your shopping experience and ensure that you find the perfect fit, we will introduce a size selection feature for all applicable products.

- Customer Wishlist and Alerts: Allow customers to create wishlists of their favorite products and set up alerts for price drops or when items come back in stock, improving customer engagement and retention.

## Testing
<details>
<summary>Testing</summary>

## Compatibility and Responsive Testing
I ensured my site was worked well, and looked nice on a variety of devices & browsers as noted in the table below:

| **TOOL / Device**           | **BROWSER** | **OS**                        | **SCREEN WIDTH** |
|-----------------------------|-------------|-------------------------------|------------------|
| iPhone 14 Plus v16.0        | Safari      | iOS, v16.0                    | 1284x2778 px     |
| iPhone 6S v12.1             | Safari      | iOS, v12.1                    | 375 x 559 px     |
| Samsung Galaxy A52 v11.0    | Chrome      | Android, v11.0                | 412 x 777 px     |
| Moto G9 Play v10.0          | Firefox     | Android, v10.0                | 412 x 804 px     |
| OnePlus 6T v9.0             | Edge        | Android, v9.0                 | 412 x 757 px     |
| Samsung Galaxy A10 v9.0     | Samsung     | Android, v9.0                 | 412 x 734 px     |
| Samsung Galaxy Tab S7 v11.0 | Chrome      | Android, v11.0                | 753 x 1037 px    |
| iPad Mini 4 v11.4           | Safari      | iOS, v11.4                    | 768 x 954 px     |
| windows 11                  | Firefox     | Browser Version 115.0         | 1920 x 955 px    |
| Mac Ventura                 | Safari      | Safari 15.6 on macOS Monterey | 1920 x 955 px    |
| windows 11                  | Yandex      | Yandex & Browser Version=14.12 | 1920 x 955 px   |

## Automated Testing
- Manual Testing was conducted due to time constrains.
- The examination of each app's views will be carried out using Django unittest module in the upcoming iteration.

## Manual Testing
In the Testing section of the README, I extensively conducted manual testing to ensure the functionality and usability of Zanfe Website [CLICK HERE](https://github.com/users/FelipeZanini/projects/13).

## Hacker Proof Testing
 I carefully tested the Zanfe website myself to make sure it works well and is not hackable. [CLICK HERE](https://github.com/users/FelipeZanini/projects/14).


## Defects
**DEFECTS** were documented in github using a custom issue template. 
- Here is my [DEFECT Template](https://github.com/FelipeZanini/Zanfe/issues/33)

### Defects of Note

**Add Product from Product Detail Page**
- DESCRIBE A BUG

- [Issue Link](https://github.com/FelipeZanini/Zanfe/issues/25)

### Outstanding Defects
- No Outstading Defects

# HTML Validator

<details>

- Home
![image](/readme/HOME_HTML_VALIDATOR.png)

- Product Page
![image](/readme/PRODUCTS_HTML_VALIDATOR.png)

- Product Detail Page
![image](/readme/PRODUCT_DETAIL_HTML_VALIDATOR.png)

- News Letter Page
![image](/readme/NEWS_LETTER_HTML_VALIDATOR.png)

- Cart
![image](/readme/CART_HTML_VALIDATOR.png)

- Wishlist
![image](/readme/WISHLIST_HTML_VALIDATOR.png)

- Profile
![image](/readme/PROFILE_HTML_VALIDATOR.png)


- Product Review Page
![image](/readme/HTML_VALIDATOR_PRODUCT_REVIEW.png)


</details>

# CSS Validator

<details>
  - Css validator
  
  ![image](/readme/css-test-validator.png)


</details>

# JavaScript Validator

<details>
- JavaScript Validator 

![image](/readme/JS_HINT_VALIDATOR.png)

- JavaScript Validator, Base Template

![image](/readme/BASE_HTML_JS_VALIDATOR.png)

</details>

# PEP8 Validator

<details>

- __Cart APP__

- PEP8 Views
![image](/readme/PEP_VIEWS_CART.png)

- PEP8 Models
![image](/readme/PEP_MODELS_CART.png)

- PEP8 Urls
![image](/readme/PEP_URLS_CART.png)

- PEP8 Forms
![image](/readme/PEP_FORM_CART.png)

- PEP8 Admin
![image](/readme/PEP_ADMIN_CART.png)

- PEP8 Webhook Handler
![image](/readme/PEP_WEBH_CART.png)

- PEP8 Webhooks
![image](/readme/PEP_WEB_CART.png)

- __Contact Us APP__

- PEP8 Views
![image](/readme/PEP_VIWS_CONTACT_US.png)

- PEP8 Models
![image](/readme/PEP_MODELS_CONTACT_US.png)

- PEP8 Urls
![image](/readme/PEP_URLS_CONTACT_US.png)

- PEP8 Admin
![image](/readme/PEP_ADMIN__CONTACT_US.png)

- __Products APP__

- PEP8 Views
![image](/readme/PEP_PRODUCTS_VIEWS.png)

- PEP8 Models
![image](/readme/PEP_%20MODELS_PRODUCT.png)

- PEP8 Urls
![image](/readme/PEP_URLS_PRODUCT.png)

- PEP8 Admin
![image](/readme/PEP_ADMIN_PRODUCTS.png)

- __Testimonials APP__

- PEP8 Views
![image](/readme/PEP_VIEWS_TESTIMONIALS.png)

- PEP8 Models
![image](/readme/PEP_MODELS_TESTIMONIALS.png)

- PEP8 Urls
![image](/readme/PEP_URLS_TESTIMONIALS.png)

- PEP8 Admin
![image](/readme/PEP_ADMIN_TESTIMONIALS.png)

- __User Rate APP__

- PEP8 Views
![image](/readme/PEP_VIEWES_USERRATE.png)

- PEP8 Models
![image](/readme/PEP_MODELS_USERRATE.png)

- PEP8 Urls
![image](/readme/PEP_URLS_USERRATE.png)

- PEP8 Admin
![image](/readme/PEP_USERRATE_ADMIN.png)

- __My Profile APP__

- PEP8 Views
![image](/readme/PEP_VIEWS_MY_PROFILE.png)


- PEP8 Urls
![image](/readme/PEP_URLS_MY_PROFILE.png)


- __Home APP__

- PEP8 Views
![image](/readme/PEP_VIEWS_HOME.png)


- PEP8 Urls
![image](/readme/PEP_URLS_HOME.png)



</details>

# Wave Test

<details>

- Home Page
![image](/readme/HOME_WAVE.png)

- Product Page
![image](/readme/PRODUCTS_WAVE.png)

- Product Detail Page
![image](/readme/PRODUCT_DETAIL_WAVE.png)

- Sign Up Page
![image](/readme/SIGNUP_WAVE.png)

- Log In Page
![image](/readme/LOGIN_WAVE.png)

- News Letter Page 
![image](/readme/NEWS_LETTER_WAVE.png)

- Cart Page
![image](/readme/SHOP_BAG_WAVE.png)

- 404 Page
![image](/readme/404wave.png)

- Wishlist Page
![image](/readme/CART_LIGHTHOUSE.png)

</details>

# Lighthouse Test

<details>

- Home Page
![image](/readme/HOME_PAGE_LIGHTHOUSE.png)

- Product Page
![image](/readme/PRODUCTS_LIGHTHOUSE.png)

- Product Detail Page
![image](/readme/PRODUCT_DETAIL_LIGHTHOUSE.png)

- Sign Up Page
![image](/readme/SIGN_UP_LIGHTHOUSE.png)

- Log In Page
![image](/readme/LOG_IN_LIGHTHOUSE.png)

- News Letter Page 
![image](/readme/NEWSLETTERS_LIGHTHOUSE.png)

- Cart Page
![image](/readme/CART_LIGHTHOUSE.png)

- 404 Page
![image](/readme/404_PAGELIGHTHOUSE.png)

- Wishlist Page
![image](/readme/CART_LIGHTHOUSE.png)

</details>

</details>
<hr>

## E-commerce Business Model
### Facebook Business Page

![image](/readme/fac-page.png)

<hr>


- **Audience Engagement:** The Facebook Page serves as a platform to engage with our audience directly.

### Newsletter Signup

![image](/readme/newsl-singup-page.png)

- **Audience Expansion:** With the Newsletter Signup tool, we can interact with a larger audience and extend beyond our current clientele.
- **Direct Communication:** Signing up for the newsletter indicates a clear interest in our brand from the subscriber. Give us a clear, focused line of communication so that you can help us with future marketing initiatives.  


## SEO Strategy
- I focused on improving our website's search engine exposure as part of our SEO plan. I made a conscious effort to carefully consider our keyword choices, enhance titles and descriptions, and strategically insert keywords into our writing.

### Keywords
- To find the major themes, goods, and services that "match" our target market, I conducted extensive research into our sector. 
- We were able to refine our own keyword list by gaining insight into the terms that our competitors target through a thorough review of their websites.
- We used a combination of long-tail and short-tail keywords in our strategy to support different types of search queries.

### Description
- The description meta tag caught my eye in particular. These summaries function as a succinct synopsis of our material and include the designated keywords. Additionally, I remain flexible in updating these descriptions whenever the content on a particular page changes.

### Title
- The title tag on our website is located in the base.html template, which gives us the ability to personalise page titles. Our SEO efforts are improved by this creative approach to titles.


### Sitemap
- For the website, I've developed a sitemap so that search engines like Google can effectively crawl and index the material when it's ready.
- [sitemap.xml file]()

### Robots.txt
- Authentication and other pages are restricted in order to limit the pages that Google should search for, allowing it to only find relevant results.
- [robots.txt file]() 

## Technologies Used
Several technologies have been used to enable this website works:
| Technology               | Description                                                                                                                                          |
|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Django                   | Django is the framework that has been used in the project, enables efficient development, database interactions and secure authentication.           |
| Python                   | Python is the core programming language that was used to write all of the code in this application, to make it fully functional.                     |
| JavaScript               | JavaScript was used to provide dynamic interactivity to the messages and enhancing the functionality of the  timepicker.                             |
| Bootstrap                | Bootstrap was utilized to ensure a responsive design.                                                                                                |
| Git                      | Git was utilized as the version control system for tracking changes, and maintaining the project's codebase.                                         |
| PostgreSQL               | PostgreSQL was employed as the relational database management system to store and manage the project's data.                                         |
| GitHub                   | Github was used as development environment, code management and tracking of changes.                                                                 |
| Font Awesome             | Font Awesome was used to obtain the icons of the website, enhancing the overall design.                                                              |
| Google Developer Tools   | DevTools was the primary toll for bug detection, testing the responsiveness and resolving issues across the website.                                 |
| Heroku                   | Heroku was used to deploy the website.                                                                                                               |
| CI's pep8                | CI's pep8 tool was used to validate all the python code.                                                                                             |
| Jigsaw                   | Jigsaw was used to validate CSS code.                                                                                                                |
| W3 HTML                  | W3 HTML was used to validate HTML code.                                                                                                              |
| Jshint                   | Jshint was used to validate JavaScript Code.                                                                                                         |
| Coloors                  | Coloors was utilized to generate color palette for the website design.                                                                               |
| AWS Amazon               | AWS Amazon was utilized to store all of my static files and images.                                                                                  |
| Stripe                   | Stripe payments was used to host/receive all the payments on the website.                                                                            |                     |
| AmIResponsive            | AmIResponsive was used to generate screenshots of the website in various device sizes, allowing for a quick visual assessment of its responsiveness. |
| Markdown Table Generator | Markdown Table Generator was utilized as a tool to create tables in Markdown format.                                                                 |
| Gitpod                   | Gitpod was used to write and edit the project code.                                                                                                  |diagrams.                                                                                                         |                                                                                                                                                                                                 |                                                                                           
### Languages
- HTML
- CSS
- Python
- JavaScript 

### Frameworks, Libraries & Programs Used
- Django
- Bootstrap
- Git 
- PostgreSQL
- GitHub
- Font Awesome
- Google Developer Tools
- Heroku
- W3 HTML
- AWS Amazon
- AmIResponsive
- Gitpod

## Stripe Payments 

- The platform for processing credit cards and online payments for purchases is called Stripe Payments. [here](https://dashboard.stripe.com/register)

### Payments
- To set up stripe payments you can follow their guid [here](https://stripe.com/ie/guides)

## Production Deployment
To deploy your application on Heroku, follow the steps bellow:

1. **Create a Heroku Account:**
- Visit the [Heroku](https://signup.heroku.com/login) website.
- Sign up for a free account or log in if you already have one.

2. **Create a New Heroku App:**
- Once you are logged in to your Heroku account, click on the "New" button and select "Create new app".
- Choose a unique name for your app. This name will be used in the App's URL.
- Select the region closest to your location for better performance.

3. **Connect the App to Your Git Repository:**
- After creating the app, go to the "Deploy" tab in your app's dashboard.
- Choose the deployment method based on your Git repository: (e.g. GitHub).
- Connect your app to the appropriate repository and branch.

4. **Configure Environment Variables:**
- In the "Settings" tab of your heroku app's dashboard, locate the "Config Vars" section.
- Set the necessary enviroment variables required for your aplication. 
- Click on the "Reveal Config Vars" button to add the key-value pairs for your enviroment variables:

e.g.

| **KEY**               | **VALUE**    |
|-----------------------|--------------|
| DATABASE_URL,         | <YOUR_VALUE> |
| AWS_SECRET_ACCESS_KEY | <YOUR_VALUE> |
| AWS_ACCESS_KEY_ID     | <YOUR_VALUE> |
| USE_AWS               | <YOUR_VALUE> |
| EMAIL_HOST_PASS       | <YOUR_VALUE> |
| EMAIL_HOST_USER       | <YOUR_VALUE> |
| SECRET_KEY            | <YOUR_VALUE> |
| USE_AWS               | <YOUR_VALUE> |
| STRIPE_PUBLIC_KEY     | <YOUR_VALUE> |
| STRIPE_SECRET_KEY     | <YOUR_VALUE> |
| STRIPE_WH_SECRET      | <YOUR_VALUE> |
| COLLECT_STATIC        | 1            |


## Credits

**Online Sources:**
- [Code Institue Template](https://github.com/Code-Institute-Org/ci-full-template)
- [Stack Overflow](https://stackoverflow.co/)
- [Django Documentation](https://docs.djangoproject.com/en/4.2/)

**Modules and Libraries:**
- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)
- [JavaScript](https://www.javascript.com/)
- [Font Awesome](https://fontawesome.com/)
- [jQuery](https://jquery.com/)
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
- [Django allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)
- [AWS](https://aws.amazon.com/)
- [Stripe](https://stripe.com/ie)
- [Git](https://git-scm.com/)
- [PostgreSQL](https://www.postgresql.org/)

## Media
- [Google Fonts](https://fonts.google.com/) - The fonts were sourced using Google Fonts.
- [Font Awesome](https://fontawesome.com/) - The icons was taken from Font Awesome.


