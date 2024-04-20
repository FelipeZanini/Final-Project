# _Zanfe_

This e-commerce platform is a haven for fashion enthusiasts and home decor aficionados alike, with a primary focus on clothing, particularly jeans and t-shirts, it provides a diverse array of styles, fits, and designs to suit every taste and occasion, from classic denim staples to trendy graphic tees, customers can explore an extensive selection of apparel that combines comfort, quality, and style.



  ![Mock Up](/readme//MOCKUP.png)
# Power Protein - Testing Documentation

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/3ef1c980-bde6-48d3-aea4-af1ed0debdd8)

# Table of Contents
<details>
<summary>Table of Contents</summary>

- [Compatibility and Responsive Testing](#compatibility-and-responsive-testing)
    - [Most Popular browser & Operating System](#most-popular-browser--operating-system)
- [Accessibility Testing](#accessibility-testing)
- [Manual Testing](#manual-testing)
- [Validation Testing](#validation-testing)
- [Automated Testing](#automated-testing)
- [Defects](#defects)
    - [Defects of Note](#defects-of-note)
- [Outstanding Defects](#outstanding-defects)

</details>
<hr>

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

### Most Popular browser & Operating System

| Device             | Browser               | Operating System | Description                                              |
|--------------------|-----------------------|------------------|----------------------------------------------------------|
| iPhone             | Safari                | iOS              | Popular combination with significant market share        |
| Android Smartphone | Chrome                | Android          | Widely used browser on the Android platform              |
| Desktop/Laptop     | Chrome                | Windows          | Popular browser on the Windows operating system          |
| Desktop/Laptop     | Chrome                | MacOS            | Popular browser on the macOS operating system            |
| Desktop/Laptop     | Edge                  | Windows          | Microsoft Edge is gaining popularity among users         |
| Other              | Firefox/Samsung/Opera | Various          | Represents a compromise due to limited testing resources |

The choices in the table are base on the browser market share data provided by [gs.statcounter.com](https://gs.statcounter.com/). Chrome and Safari are the dominant browsers, so they are included for testing on different devices and operating systems. Edge is also included as it has a noticeable market share. Since firefox, Samsung Internet and Opera have smaller market shares, they are grouped under the "Other" category to represent a compromise due to limited testing resources.

| **BROWSER**      | **PERCENTAGE** |
|------------------|----------------|
| Chrome           | 63.55%         |
| Safari           | 19.95%         |
| Edge             | 5.13%          |
| Opera            | 2.99%          |
| Firefox          | 2.79%          |
| Samsung Internet | 2.38%          |

**Browser Market Share Worldwide - July 2023**

## Accessibility Testing
To ensure our website is accessible, I have conducted extensive testing to ensure that it caters for users with disabilities.

| **PAGE**                                                         | **TEST CASE LINK**                                | **RESULT** |
|------------------------------------------------------------------|---------------------------------------------------|------------|
| Home Page - Lighthouse Audit (Desktop)                           | https://github.com/Giov3ss/PowerProtein/issues/55 | 100        |
| Home Page - Lighthouse Audit (Mobile)                            | https://github.com/Giov3ss/PowerProtein/issues/56 | 100        |
| Products Page - Lighthouse Audit (Desktop)                       | https://github.com/Giov3ss/PowerProtein/issues/57 | 100        |
| Products Page - Lighthouse Audit (Mobile)                        | https://github.com/Giov3ss/PowerProtein/issues/58 | 100        |
| Blog Page - Lighthouse Audit (Desktop)                           | https://github.com/Giov3ss/PowerProtein/issues/59 | 100        |
| Blog Page - Lighthouse Audit (Mobile)                            | https://github.com/Giov3ss/PowerProtein/issues/60 | 100        |
| Blog Post Details - Lighthouse Audit (Desktop)                   | https://github.com/Giov3ss/PowerProtein/issues/61 | 100        |
| Blog Post Details - Lighthouse Audit (Mobile)                    | https://github.com/Giov3ss/PowerProtein/issues/62 | 100        |
| Contact Nutritionist - Lighthouse Audit (Desktop)                | https://github.com/Giov3ss/PowerProtein/issues/63 | 100        |
| Contact Nutritionist - Lighthouse Audit (Mobile)                 | https://github.com/Giov3ss/PowerProtein/issues/64 | 100        |
| Contact Nutritionist (Success Page) - Lighthouse Audit (Desktop) | https://github.com/Giov3ss/PowerProtein/issues/65 | 100        |
| Contact Nutritionist (Success Page) - Lighthouse Audit (Mobile)  | https://github.com/Giov3ss/PowerProtein/issues/66 | 100        |
| Reviews - Lighthouse Audit (Desktop)                             | https://github.com/Giov3ss/PowerProtein/issues/67 | 100        |
| Reviews - Lighthouse Audit (Mobile)                              | https://github.com/Giov3ss/PowerProtein/issues/68 | 100        |
| Reviews (Add/Edit Reviews) - Lighthouse Audit (Desktop)          | https://github.com/Giov3ss/PowerProtein/issues/69 | 100        |
| Reviews (Add/Edit Reviews) - Lighthouse Audit (Mobile)           | https://github.com/Giov3ss/PowerProtein/issues/70 | 100        |
| My Profile - Lighthouse Audit (Desktop)                          | https://github.com/Giov3ss/PowerProtein/issues/71 | 97         |
| My Profile - Lighthouse Audit (Mobile)                           | https://github.com/Giov3ss/PowerProtein/issues/72 | 97         |
| Products Details - Lighthouse Audit (Desktop)                    | https://github.com/Giov3ss/PowerProtein/issues/73 | 100        |
| Products Details - Lighthouse Audit (Mobile)                     | https://github.com/Giov3ss/PowerProtein/issues/74 | 100        |

**NOTES**
- For the test case 71/72 I notice that I got a 97 with a false positive on a contrast issue around the Order Number. When I further inspected with [webaim](https://webaim.org/resources/contrastchecker/), I determined that a 20px font-size with those colors is considered large text, which actually passes WCAG AA standards of accessibility

## Manual Testing
In the Testing section of the README, I extensively conducted manual testing to ensure the functionality and usability of the PowerProtein website. The manual testing process involved following predefined scenarios and documenting the results using a custom issue template on GitHub. To view the detailed testing results, please [CLICK HERE](https://github.com/Giov3ss/PowerProtein/issues).

## Validation Testing
<details>
<summary>Validation Testing</summary>

The following site were used to aid in validation testing:

- **[CSS Validator](https://jigsaw.w3.org/css-validator/)**

**BLOG.CSS:**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/ca4c51d8-f505-4286-916a-0ecb14590416)

<hr>

**CHECKOUT.CSS:**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/586b2df2-fc4f-49d4-be38-dd8b6b9e0f9b)

<hr>

**EXPERT_ADVICE.CSS:**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/e96aa23d-16cf-419e-8a23-b4aab6a6a7c7)

<hr>

**PROFILE.CSS:**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/2329837b-b087-4ac4-b772-60c14dd2818a)

<hr>

**REVIEWS.CSS:**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/2f4bffb6-b34e-4532-a4ea-3b217bc4bcb8)

<hr>

**BASE.CSS:**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/a860d504-7955-44e6-b689-d7df91f4e911)

<hr>

The following site were used to aid in validation testing:

- **[HTML Validator](https://validator.w3.org/)**

**HOME PAGE:**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/14974565-cfd7-4f1d-a643-745cc14d7830)

<hr>

**PRODUCTS PAGE:**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/b09adbb6-b5ed-4923-93b9-ef59c713259c)

<hr>

**PRODUCTS DETAILS PAGE:**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/45bec81e-85c2-4edb-90fa-67bab94239ed)

<hr>

**BLOG PAGE:**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/70eaeea5-9812-401b-9cc0-76447e7bcf09)

<hr>

**BLOG PAGE DETAILS:**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/cbd1f762-5530-4cb7-9a8b-049dcdf82521)

<hr>

**CONTACT NUTRITIONIST PAGE:**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/4b3329ae-8077-465a-94b8-5407b2611ced)

<hr>

**REVIEWS PAGE:**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/52be60e0-cd66-4dae-9625-6ebef6c7013c)

<hr>

**REVIEWS PAGE DETAILS:**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/876b26ab-9bfb-42b9-9da3-da0485ce80ed)

<hr>

**LOGOUT PAGE**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/bd97ead0-8b29-42c8-a3a9-d6f49287b37d)

<hr>

**LOGIN PAGE**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/1c500cbe-0958-4086-906d-5f80afedfa19)

<hr>

**REGISTER PAGE**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/829eeab9-4849-4ea6-bf46-b63fd6716b43)

<hr>

**RECOVER PASSWORD PAGE**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/7cf83021-db40-43ba-92ec-0c09fad85e45)

<hr>

**MY PROFILE PAGE**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/49d7bc2d-42aa-464f-94e5-3e21510ae2c3)

**SHOPPING BAG PAGE**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/f2fea239-5c2d-421c-8bb4-268f923aa548)

<hr>

**CHECKOUT PAGE**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/db52ccfb-a475-45f9-805c-eb07f92b3bdd)

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/6fad4d53-0a3c-4f4f-a0d9-787d6ea0b0f7)

<hr>

**CHECKOUT SUCCESS PAGE**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/f8b75a02-ab2b-44f9-8a4b-d48ad06b4b5c)

<hr>

**403 PAGE**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/f8c78654-6dbb-4cd5-b2cd-82313941a6f9)

<hr>

**404 PAGE**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/cdd0c655-7914-423f-942c-cc7262e24992)

<hr>

**500 PAGE**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/0c282358-1c8c-4863-892b-3ffb3b56e2d9)

<hr>

The following site were used to aid in validation testing:

**[JS validation](https://jshint.com)**

**STRIPE_ELEMENT.JS**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/b0e9a422-9137-457e-8a7a-59e8e46906e0)

<hr>

**QUANTITY_INPUT_SCRIPT**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/a50e1ad9-f9dc-4eab-af43-bb03c7f4c894)

<hr>

**COUNTRYFIELD.JS** 

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/4cc6946f-c96e-4db3-8071-ee5873610b24)

<hr>

The following site were used to aid in validation testing:

**[CI's pep8 tool](https://pep8ci.herokuapp.com/)** 

**BAG APP**

- **context.py**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/897497f7-4e49-4dae-a4b5-4474396703c2)

- **apps.py**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/81d29e4e-b062-4ad5-bda5-6b063d8c22de)


- **urls.py**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/576de569-3931-4ed7-9efa-07f55d1fad96)

- **views.py**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/ee5adb02-9c78-4d15-add0-9fddaed02e2a)

<hr>

**BLOG APP**

- **admin.py**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/023b2cc9-9f18-493c-bacc-31b2d4aeb0a9)

- **apps.py**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/c99e6daf-03ca-41dd-bbab-d0f8923d857a)

- **models.py**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/690d72b5-1d69-456c-9b69-91d42949f8f6)

- **urls.py**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/1ba08c12-0bfe-435a-ab18-d3adbf5b0a1a)

- **views.py**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/bfc2d1ef-d301-48ff-bf60-4244590f3331)

<hr>

**CHECKOUT APP**

- **admin.py**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/c7901a4d-5184-42bf-b563-67ff0ee35b01)

- **apps.py**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/0c8cb5b5-57f9-4eeb-beb8-34925d0e57ea)

- **forms.py**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/618d2563-7ac2-4c02-954c-6b009222a0df)

- **models.py**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/39f228a2-deed-45c5-b1bb-dee4e120abe4)

- **signals.py**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/a1ad68a6-8688-42e8-be8f-ad4e039f21fe)

- **urls.py**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/30c161c2-c459-4078-9d37-60ba3d102373)

- **views.py**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/1bc69164-899f-4796-afb0-907beb43e1c6)

- **webhook_handler.py**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/1861d1c8-e112-4b54-9f3f-b750f7b341b0)

- **webhooks.py**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/6f87917d-197b-4c57-b00e-bf12691eb63d)

<hr>

**EXPERT_ADVICE APP**

- **admin.py**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/b8f3a03f-0845-4e80-bc46-bc5acb586479)

- **apps.py**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/510454a4-d6de-4522-8ca5-204fdfe21f16)

- **forms.py**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/defe8687-cdbb-4946-997f-34ca7da331e8)

- **models.py**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/0872990c-d351-4068-b392-ff87e1620d33)

- **ulrs.py**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/fe8144f1-89c6-4c1d-b734-c4c41162487e)

- **views.py**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/ca050678-1633-4d04-9ed9-ba2fb0cf6cb9)

<hr>

**HOME APP**

- **apps.py**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/2d0371ea-f471-4c67-a04b-9b4f0357fd0b)

- **urls.py**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/71b251e8-1a92-457c-93d0-0f8bd25c26b6)

- **views.py**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/4a8a4c83-9d52-4bfb-99e2-9b8d3ab8b461)

<hr>

**POWERPROTEIN APP**

- **asgi.py**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/55c90d53-2b64-484b-aba8-d462a152e768)

- **settings.py**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/99ef5f51-a305-41d2-a7f4-00cd4437f25d)

- **urls.py**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/825452d3-fe94-4024-884b-e222592083b3)

- **views.py**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/eceba847-b000-4bac-b5c8-fe208e45fc9c)

- **wsgi.py**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/e8cab8a1-40ca-45cb-a16a-c3bac8c6c1b6)

**PRODUCTS APP**

- **admin.py**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/87c6c67d-52cf-469e-b321-7f5892b94a75)

- **apps.py**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/24ce3c7e-a986-4f1a-b4e3-2eec62c94621)

- **forms.py**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/9fd8b485-5ccb-4902-bbe3-73ba810d76d5)

- **models.py**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/5dee93da-ab30-4398-a523-3246c93194fd)

- **urls.py**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/1067fa33-8510-47d4-9313-d986f42c6e2c)

- **views.py**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/debe1ea2-b593-44dc-a436-774a4c13e77d)

- **widgtes.py**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/97a9594a-fff4-430a-9383-c5ea0fa63744)

<hr>

**PROFILES APP**

- **apps.py**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/41685eb1-b285-4ad5-9ee1-45cf15a699aa)

- **forms.py**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/678da330-6861-49c2-89da-49fd37ab5ff1)

- **models.py**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/bf81a948-357e-4299-8a93-9c21c02c618b)

- **urls.py**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/70c0139b-8a08-47c1-af06-727380971092)

- **views.py**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/fc93272a-6c4e-4fb4-9404-4c4ceab8c004)

**REVIEWS APP**

- **admin.py**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/8cbbef68-30e9-4b7f-a0f4-42349805b97a)

- **apps.py**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/a02b8929-4c31-4d7d-b40d-4b2e96dd09e2)

- **context.py**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/425f3d32-e4d9-494f-99de-f6740df7588a)

- **forms.py**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/d51f6c5b-62a6-4277-97ab-63406e8a994f)

- **models.py**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/7a8d406d-92b7-4d8c-a65e-656cade80ec2)

- **urls.py**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/2cebb9f8-71ec-4584-9a9a-d36e645b5cd3)

- **views.py**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/bb20b56a-3538-4aca-8325-b0dfd3765d03)

- **widgets.py**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/08b5c157-46d9-4673-b4a1-826d4111d001)

<hr>

**CUSTOM_STORAGES.PY**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/56f7c98c-944c-4656-a463-1d76b432e5c2)

<hr>

**MANAGE.PY**

![image](https://github.com/Giov3ss/PowerProtein/assets/112728772/4af71d0a-6ebc-471c-9e0b-1caf7f4c551f)

</details>
<hr>

## Automated Testing
- Manual Testing was conducted due to time constrains.
- The examination of each app's views will be carried out using Django unittest module in the upcoming iteration.

## Defects
**DEFECTS** were documented in github using a custom issue template. 
- Here is my [DEFECT Template](https://github.com/Giov3ss/PowerProtein/blob/main/.github/ISSUE_TEMPLATE/bug_report.md)

### Defects of Note

**Purchase confirmation email not received**
- During the final testing phase of store's functionality, I encountered a significant bug related to the purchase confirmation email system. Upon completing a purchase, I expected to receive a confirmation email detailing the order. However, the email failed to be delivered to the test users, leading to concerns about the reliability of the purchase process.

- [Issue Link](https://github.com/Giov3ss/PowerProtein/issues/75)

**Security Vulnerability - Unauthorized Access to User reviews / Order History**
- While conducting a review in the platform's security, I identified a bug that poses a significant risk to user accounts and their associated reviews. This bug allows unauthorized users to access and edit reviews, also order history that belonging to other user's accounts. Furthermore, the bug enables users to copy links that lead directly to other user's accounts, granting unauthorized access.

- [Issue Link](https://github.com/Giov3ss/PowerProtein/issues/76)

### Outstanding Defects
I found an issue if invalid HTML was entered in the WYSIWYG blog entries. This happens a lot if you copy/paste line returns in bullet lists. Ideally there would be some HTML validation on the text area input to ensure bad HTML isn't entered, but that is beyond the scope of the MVP project. Editors of the blog will be viewing their entries after publishing and can easily fix any issues copy/paste might encounter.

[Back to the README.md](https://github.com/Giov3ss/PowerProtein/blob/main/README.md)
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
 ![image](/readme/PROFILE_WIREFRAME.png) 

- Wishlist Page:
 ![image](/readme/WISHLIST_WIREFRAME.png)

- Newsletter Page:
 ![image](/readme/NEWSLETTERS_WIREFRAME.png)

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

## Database Choice
I used PostgreSQL as the database for this project. Hosting the application on Heroku allows for easy deployment and scalability, and PostgreSQL is one of the supported and recommemdede databases on the Heroku platform.

<hr>

### CRUD
<details>
<summary>CRUD Details</summary>

- **Bag:**
  
- Increase item quantity
- ![image](/readme/in-bag.png)

- Decrease item quantity
- ![image](/readme/ds-bag.png)

- Remove item from bag
- ![image](/readme/ex-bag.png)


- **Wishlist:**
  
- Remove item from wishlist
- ![image](/readme/ex-wishlist.png)

- **Testimonial:**
  
- Edit testimonial
- ![image](/readme/ed-testimonal.png)

- Remove text testimonial 
- ![image](/readme/ex-testimonal.png)

- **Rating:**
  
- Edit product rating
- ![image](/readme//ed-review.png)

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

![image](/readme/profile-page.png)

<hr>

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

## Defects
**DEFECTS** were documented in github using a custom issue template. 
- Here is my [DEFECT Template]()

### Defects of Note

**Purchase confirmation email not received**
- DESCRIBE A BUG

- [Issue Link]()

**Security Vulnerability - Unauthorized Access to User reviews / Order History**
- DESCRIBE ANOTHER BUG RELATED TO SECURITY AND VULNERABILITY

- [Issue Link]()

### Outstanding Defects
I found an issue if invalid HTML was entered in the WYSIWYG blog entries. This happens a lot if you copy/paste line returns in bullet lists. Ideally there would be some HTML validation on the text area input to ensure bad HTML isn't entered, but that is beyond the scope of the MVP project. Editors of the blog will be viewing their entries after publishing and can easily fix any issues copy/paste might encounter.

[Back to the README.md]()

- **404 Testing Page:**
  I have tested the code by the following methods:
  - Passed on the Django test built-in function, no issues found.
  - Passed on the validator code PEPE8, no issues found.
  - I manually tested the code, attempting to visit pages forbidden for non-registered users.
  - I added a login required decorator in each function that just registered users can access.
  - I tested each button individually in different screen sizes, and no problems were found.
  - I inserted url to try to hack the site, but my code seems to be safe.
  - I started the secret variables in the protected virtual environment. 
  - The site was tested on the Heroku terminal and the local terminal.

  - Css validator
  ![image](/readme/css-test-validator.png)

  - HTML Validator
  ![image](/readme/html-base.png)

- Products
  ![image](/readme/html-products.png)

- Newsletters
  ![image](/readme/html-products.png)


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


