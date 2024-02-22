# _Zanfe_

This e-commerce platform is a haven for fashion enthusiasts and home decor aficionados alike, with a primary focus on clothing, particularly jeans and t-shirts, it provides a diverse array of styles, fits, and designs to suit every taste and occasion, from classic denim staples to trendy graphic tees, customers can explore an extensive selection of apparel that combines comfort, quality, and style.



  ![Mock Up](/img/mockup.png)

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

- Products Description: Customers can easily find product details, such as specifications, photos, other customers testimonial and full descriptions. Making planned purchasing decisions having access to complete and accurate information.
  
- Secure Checkout Process: A smooth and safe checkout experience is our priority for customers. This entails safe payment methods, and personal data security.
Order tracking: In order to keep track of their purchases, customers want to have access to order tracking information's. Keeping them informed and in control by providing updates on order processing, shipping, and delivery.

**Business Goals:**
- ⁤Customer Satisfaction: Offering professional styling guidance demonstrates our dedication to making sure customers are happy with the clothes we choose, making them feel and look their best. ⁤

- ⁤Loyal Customers: We are compromised with customer loyalty, always offering the best user experience making our customer wish to buy again. ⁤

- ⁤Safety: We place a high priority on protecting the financial and personal data of our clients. ⁤⁤The following safety precautions are in place to guarantee a secure purchasing experience: ⁤

1. **User Experience:**

⁤- Design a user-friendly, aesthetically pleasing website that makes it simple for customers to browse and locate the products. ⁤
   
⁤- Create a user-friendly search and filtering system that makes it easy for customers to find particular supplements depending on their dietary preferences and fitness objectives. ⁤

⁤- Optimise the website for quick loading times and flawless cross-platform operation to boost user happiness and promote return visits. ⁤

3. **Segure Checkout Process:**

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

1. **Products Page:** Well-structured product page, allowing users to see each product rating category and price, and functions to add to card or wishlist.
2. **User Accounts:** This application provides account registration, to secure a checkout and visualize order history.
3. **Shopping Bag & Wishlist:** Shoppers will be able to add and see bags and wishlists, this feature is implemented using cookies via JavaScript.
4. **Product Reviews:** A review page will be implemented, enabling customers to provide feedback and ratings for products they have purchased and full CRUD operations for their testimonials.
5. **User-Friendly & Responsive Design:** The website will be optimized for various devices, ensuring a consistent and user-friendly experience for both desktop and mobile users.

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

  
8. **Testimonial
   - User(Foreingkey to AUTH_USER): The user associated with the order.
   - Testimonial Text(TextField): Indicates the testimonial text of the product associeted with the user.
   - Rating(DecimalField): Indicates the rating of the product, and its evaluated after each user review by update rating function.
   - Product(Foreingkey to Product Model): The product associated with the order item.
   - Date added(DateTimeField): The date and time when the order item was added.

</details>
<hr>

## Database Choice
I used PostgreSQL as the database for this project. Hosting the application on Heroku allows for easy deployment and scalability, and PostgreSQL is one of the supported and recommemdede databases on the Heroku platform.

<hr>

### CRUD
<details>
<summary>CRUD Details</summary>

- **Bag:**
  
- Inscrease item quantity
- [Product Backlog](/readme/in-bag.png)

- Decrease item quantity
- [Product Backlog](/readme/ds-bag.png)

- Remove item from bag
- [Product Backlog](/readme/ex-bag.png)


- **Wishlist:**
  
- Remove item from wishlist
- [Product Backlog](/readme/ex-wishlist.png)

- **Testimonial:**
  
- Edit only text testimonial
- [Product Backlog](/readme/ed-testimonal.png)

- Remove text testimonial 
- [Product Backlog](/readme/ex-testimonal.png)

- **Rating:**
  
- Edit product rating
- [Product Backlog](/readme//ed-review.png)

  
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

<hr>

- Our website incorporates a user-friendly navigation system to enhance the browsing experience and ensure easy access to important actions and content.
- Fixed Navigation: The navigation bar remain visible at the top of the page even as users scroll down.
- Standard Burguer Menu for Mobile: On mobile devices, we utilize a "burguer" menu, simplifying navigation and providing a consistent interface for user accessing the site on smaller screens. 

</details>
<hr>

**Sign in/ Sign up:**
<details>
<summary>Sign in/ Sign up Details</summary>
  
![image](/readme/sign-up.png)

<hr>

![image](/readme/singin-page.png)

<hr>

- Our website offers a streamline and user-centric sign-in and sign-up process that prioritizes convenience and accessibility.
- Easy Password Recovery: On the sign-in page, users can easily find a link to the "Forgot Password" feature, allowing them to reset their password without unnecessary hassle.
- Sign-in: Users can log in via name or email. For new users who aren't registered yet, the sign-in page provides a prominent link to the sign-up process.
- Sign-up: Sign up page has link to sign in page in case user is already registered, clear error messages if user name or email is already in system, username and emails are unique to the system, so a user cannot hack another user's identity or impersonate another user
  
</details>
<hr>

**Products Page:**
<details>
<summary>Products Page Details</summary>

![image](/readme/produc-page.png)

<hr>

![image](/readme/product-detail-page.png)

<hr>

- Our Products Page provides users with a hassle-free shopping experience, enhancing their journey from browsing to purchasing.
- Quick Buy Buttons: The product list page showcases "Quick Buy" buttons bellow  each product, allowing users to swiftly add items to their cart without navigations through multiple pages.
- Product Information: Users can make informed decisions with easily digestible and essential details about each product, ensuring they have the necessary information at a glance.
- Quantities & Descriptions: The product detail page provides clear information of the product, such as name, prices, rating, category. User can easily select the desired amount of products they want in the quantity section.

</details>
<hr>

**Bag, Wishlist & Checkout:**
<details>
<summary>Bag & Checkout Details</summary>

![image](/readme/shoping-bag.png)

<hr>

![image](/readme/wishlist-page.png)

![image](/readme/checkout-page.png)

<hr>

- Our Bag & Checkout functionality streamlines the purchase process, ensuring a smooth and efficient transaction for users.
- Bag Page: On the bag page, users can easily manage their selected products. Each product is displayed with image, name, price, SKU. The user has the convenience of a quantity button to adjust the quantity of items or remove products from the bag, ensuring total control over the order.
- Checkout Page: Our checkout page is designed for simplicity and security. An easy-to-use checkout form collects essential information, including shipping details and payment card information. The checkout page also features an order summary where users can review their order. This summary increases transparency by helping users confirm their selection before completing their purchase.

</details>
<hr>

**Profile:**
<details>
<summary>Profile Details</summary>

![image](/readme/profile-page.png)

<hr>

<hr>

- Our profile feature provides users with a personalized hub to manage their account details and track their order history.
- My Profile Page: In "My Profile Page", users can easily view and modify their default delivery information. This convenient option ensures that users can easily keep their shipping details up to date, eliminating potential hassles during the checkout process.
- Order History: Users can access a comprehensive list of their past orders, conveniently organized by order number. With a simple click on the order number, the user can revisit the details of their previous purchases, facilitating reordering or tracking.

</details>
<hr>

**Order Detail:**
<details>
<summary>Order Detail</summary>

![image](/readme/order-detail-page.png)


<hr>

- Our blog feature offers users a wealth of insightful content related to health, wellness, recipes and more.
- Informative Content: The blog page serves to help the user with health tips, wellness advice and delicious recipes. The user can easily navigate through the blog post and access a wide range of informative articles that cater to their interests and needs.
- Post Details: Clicking on a post title opens the post detail view. Here, users can read the entire post, interacting with the content in a focused and immersive way. They can also interact with the post by liking it.
- Related Products: To provide users with a seamless experience that unites content and commerce, I have integrated related products at the end of the blog post (if applicable). These products are carefully selected to complement the blog theme.

</details>
<hr>

**News Letters SignUp:**
<details>
<summary>News Letters SignUp</summary>

![image](/readme/newsl-singup-page.png)


<hr>

- Our Contact Nutritionist Page is designed to connect users with professional nutritionist from our partner website, [iHealthy](https://ihealthy.herokuapp.com/). This features offer user personalized guidance and expert advice on their dietary and nutritional needs.
- Personalized Nutritional Advice: Through a form, users can easily submit their questions and concerns to an experienced nutritionist.
- Book an Appointment: For users looking for a more in-depth consultation, the "Schedule Now" button provides an easy way to schedule an appointment with the iHealthy nutritionist. Upon clicking the button, users are redirected to the iHealthy website.
- Appointment Process: For added transparency and clarity, I've included a GIF video on the page that demonstrates the process of booking an appointment with an iHealthy nutritionist. This video provides a visual guide, making the appointment booking process user-friendly and efficient.

</details>

<hr>

**Reviews:**
<details>
<summary>Reviews Details</summary>

![image](/readme/reviews-page.png)

<hr>

- **(Authorized User - Update)**

![image](/readme/ed-testimonal.png)
![image](/readme/ex-testimonal.png)

<hr>

- **(Authorized User - Delete)**

![image](/readme/ed-review.png)

<hr>

- The reviews page feature allows users to engage with our products and services by sharing their feedback. This feature serves as platform for users to express their thoughts about our products, company and overall experience.
- User-generated Reviews: This feature lies in the ability for logged-in users to leave reviews. Whether it's about a specific product, our customer service or the overall experience, user can provide detailed feedback to help us improve and assist other potential customers in making informed decisions.
- Editing and Deletign Reviews: We value autheticity, and to ensure that users have control over their feedback, we allow them to edit or delete their reviews. This user-friendly approach empowers users to modify their reviews if their opinions change over the time.
- Responsive Design: The reviews page is designed to provide a seamless experience across all devies. Whether users access it from their desktop, tablet or smartphone the page maintains its functionality and readability, ensuring that users can engage with review conveniently.

</details>
<hr>

<hr>

**Messages Notifications:**
<details>
<summary>Messages Notifications Details</summary>

<hr>

![image](/readme/signin-msg.png)

- There's a succes message if the user logged in. 

![image](/readme/signout-msg.png)

- There's a success message if the user update their bag. 

<hr>

![image](/readme/test-sub-msg.png)

- There's an alert message if the superuser/admin edit a product. 

<hr>

![image](/readme/edt-rating-msg.png)

- There's a success message if the user remove the product from their bag. 

<hr>

![image](/readme/ex-testimonial-msg.png)

- There's a success message if the user like the blog (only authorized user). 

<hr>
![image](/readme/form-sub-msg.png)

- There's a success message if the user like the blog (only authorized user). 
<hr>

</details>
<hr>


### Error 404
<details>
<summary>Error Page Details</summary>

- **404 Error Page:**
  
  ![image]()

<hr>

</details>
<hr>

## Future Features

- BLA BLA BLA BLA

## Testing

Please refer to the [TESTING.MD](TESTING.md) file for all testing performed 


## E-commerce Business Model
### Facebook Business Page

![image](/readme/fac-page.png)

<hr>


- **Audience Engagement:** The Facebook Page serves as a platform to engage with our audience directly.
- **Products Updates:** Keeping our followers informed about new product launches, restocks and upcoming collections.
- **Educational Content:** Sharing informative and educational content related to our products or industry establishes our brand as an authority in the field.
- **Feedback & Insights:** The Facebook page can be a valuable source of feedback, understanding what customers like and dislike helps us improve our products and services.

### Newsletter Signup

![image](/readme/newsl-singup-page.png)

- **Audience Expansion:** The Newsletter Signup feature expands our reach beyond existing customers and allows us to engage with a wider audience.
- **Direct Communication:** Subscribers who sign up for the newsletter have explicity shown in our brand. Provide us with a direct and targeted communication channel to becomes a valuable asset for future marketing efforts. 
- **Product & Updates:** Subscribers stay informed about the latest product releases, company news and updates.
- **Relationship Building:** Regular newsletter provide an opportunity to establish a relationship with subscribers.


## SEO Strategy
In our SEO strategy, I worked on optimizing our website to increase its visibility in search engines. I took specific steps to refine our keyword selection, optimize descriptions and titles, and intentionally incorporate keywords into our content.

### Keywords
- I dug deep into our industry to identify the key themes, products, and services that "match" our target audience. 
- Through a comprehensive analysis of our competitors' websites, we gained insight into the keywords they target, which helped me refine our own keyword list.
- Our approach covered both short-tailed and long-tailed keywords to cater to varios search queries.

### Description
I paid special attention to the description meta tag. These descriptions serve as a concise introduction to our content, incorporating the identified keywords. Additionally, I remain flexible in updating these descriptions whenever the content on a particular page changes.

### Title
Our website's base.html template houses the title tag, allowing us to customize titles for each page. This dynamic approach to titles enhances our SEO efforts.


### Sitemap
I've created a sitemap for the website, ensuring that when it's fully prepared, search engines like Google can efficiently crawl and index its content.
- [sitemap.xml file]()

### Robots.txt
To restrict pages that are should be searched by google, authentication and others are blocked to only allow relevant pages to be searched by google.
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
| Stripe                   | Stripe payments was used to host/receive all the payments on the website.                                                                            |
| Lighthouse               | Lighthouse was used to test the accessibility of the website.                                                                                        |
| Balsamiq                 | Balsamiq was utilized as a tool for creating wireframes, providing a visual representation of the website layout and structure.                      |
| AmIResponsive            | AmIResponsive was used to generate screenshots of the website in various device sizes, allowing for a quick visual assessment of its responsiveness. |
| Markdown Table Generator | Markdown Table Generator was utilized as a tool to create tables in Markdown format.                                                                 |
| Gitpod                   | Gitpod was used to write and edit the project code.                                                                                                  |
| Mermaid                  | Mermaid was used to create all the diagrams.                                                                                                         |                                                                                                                                                                                                 |                                                                                           
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
- Favicon
- Gitpod


## Deployment


## Stripe Payments 

- The Stripe Payments is set up as the online payment processing and credit card processing platform for the purchases.
You will need a stripe account which you can sign up for [here](https://dashboard.stripe.com/register)

### Payments
- To set up stripe payments you can follow their guid [here](https://stripe.com/ie/guides)

### API Keys
1. Click on 'Developers' in the navbar-side.
2. Beside 'Overview' click on the API Keys and you will see your 'Publishable key' & 'Secret key'.


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
Throughout the process of building the PowerProtein website, I would like to acknowledge the following:

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

## Content

- I took some inspiration from the [My Protein](https://www.myprotein.ie/) website.

## Media
- [Google Fonts](https://fonts.google.com/) - The fonts were sourced using Google Fonts.
- [Font Awesome](https://fontawesome.com/) - The icons was taken from Font Awesome.


[Back to the beginning](#table-of-contents)
