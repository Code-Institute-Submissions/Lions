# Lions

Lions is a gymnasium, providing great prices, lovely and helpful staff, as well as a welcoming environment for anyone and everyone. The business works off of a paper system, asking customers
to fill out physical forms either provided by the staff or printed off of at home. The benefits of the website is that customers are able to signup for a subscription and manage it all from 
their own homes, with the convenience of a smart device or computer. Staff are also able to see all subscriptions and search the database through the use of Django, whereas they couldn't before.

## UX

### Project Goals

Lions' goal is a safe and welcoming environment where anyone can come and better themselve phyically without facing judgement, prejudice or discrimination. To help advance this vision the Lions website will 
allow users to signup for gym subscriptions online within their own homes. It will also allow them view the latest news about the business, see all subscriptions that are available and have their own personal profile 
where they can view their subscriptions.

### User Goals

The target audience for Lions is those 16 and up of all races, gender and sexuality, Lions is a place all are welcome and get the exercise they want and need.

* A clear landing page, displaying all the latest news and offers.
* Easy signup process.
* A judgement free signup process.
* A remember me field to allow for faster signups.
* A profile to hold default information.
* A profile to store subscription memberships.

Lions achieves these goals by:

* Lions has a stylised landing page, that is fierce to resemble the lion that Lions is named after, at the top of the page is a carousel, showing all the current news of the business. That is easily updatable through superuser accounts to keep all the information up to date.
* The signup process for Lions requires the user to go to the subscriptions page, click on one and be taken to the signup form, which is a single form asking for a few personal details, and payment information. With just that little information they are all set.
* The signup process asks for a gender, not all users are comfortable to assign themselves one specific gender and therefore there is an "Other" option for those that do not identify with the tradiational "Male" or "Female".
* At the end of the signup process is a checkbox asking the user if they want their information to be remember, if it is not checked information about the user will not be saved, and if it details will be saved and input into a form on the user's profile where they may update them if needs be.
* The profile app is able to display the user's saved information if they asked for it to be stored and update if they need to, keeping records all up to date.
* An aspect of the profile app is the list that holds all of the subscriptions that the user has signed up for, in a way that is clear to understand, and nicely displayed.

### Developer and Business Goals

* Have a safe place for all to come and workout without feeling judged, preduiced or discriminated against.
* Have an easy method to update all outdatable fields, such as the "Categories", "Subscriptions" and "Slides" fields which relavence change as the business changes.
* A database with all subscriptions so staff can view all subscriptions, easily and without hassale.

Lions achieves these goals by:

* Lions thrives on presenting an environament where all feel welcome, this is done by adding additional options where nessasary to help all customers feel welcome, such as the "Other" gender field. And omitting any fields including race and other sensitive information users maybe afraid to pass on. This is allow everyone to feel comfortable in the environment that Lions is creating.
* Staff are able to Create, Read, Update and Delete, the "Categories", "Subscriptions" and "Slides" fields within the app, rather than needing to navigate to the admin. The forms are simple and clear for new and old staff to make use of.
* Django allows for an easily accessible database storing all the information staff would want to get there hands on. Going above the intial subscriptions options.

### User Stories

* As an older user, I want to be able to signup for a subscription in a quick and simple manner.
* As a frequent user, I want to be able to easily be kept up to date on the business' current status.
* As an LGBTQ+ user, I want a welcoming platform where I don't have to assign a gender that doesn't fit to me.
* As an owner, I want users to be able to understand what the business is, and our goal.
* As a frequent user, I want to be able to find the opening times quick and easily, without having to search for them.
* As a member of staff, I want a clear view of everything that is editable and currently available to customers.
* As an owner, I want my staff to be able to see all subscriptions past and present.

### Design Choices

### Wireframes

* [Home](wireframes/home.pdf)
* [Login](wireframes/login.pdf)
* [Products](wireframes/Products/Products.pdf)
* [Product Details](wireframes/Products/ProductsDetails.pdf)
* [Register Desktop M-L](wireframes/Register/RegisterProcessDesktopM-L.pdf)
* [Register Desktop XL](wireframes/Register/RegisterProcessDesktopXL.pdf)
* [Register Desktop Mobile](wireframes/Register/RegisterProcessDesktopMobile.pdf)
* [Subscriptions](wireframes/Subscriptions.pdf)
* [Categories](wireframes/Categories.pdf)
* [Profile](wireframes/Profile.pdf)
* [Additions Pages](wireframes/Additions.pdf)

## Features

### Existing Features

### Features to Implement

## Technologies Used
* [Lucidchart](https://lucidchart.zendesk.com/hc/en-us): Used to make wireframes.
* [django](https://www.djangoproject.com/): A high level python framework making the development process quicker and easier, enabling a high quality end product within a tight timeframe.
* [MySQL](https://www.mysql.com/): A relational database management system, it is used as the database for storing data for the project.
* [SQLite](https://www.sqlite.org/index.html): A C-language library that implements a light weight, fast SQL database engine.
* [django-allauth](https://django-allauth.readthedocs.io/en/latest/): Enables to project to use multiple authtication schemes and account verfication.
* [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/): Allows to easy and pleasant styling of form elements without disturbing the flow of django.
* [Bootstrap](https://getbootstrap.com/): Used styling provided to quickly position content as well as create bespoke styling with custom css.
* [Font Awesome](https://fontawesome.com/): The vase array of icons were used as intuitive design to help users find and understand features that were designed in an already established manner. 
* [Pillow](https://pillow.readthedocs.io/en/stable/): Was needed to use the ImageField for the subscriptions and products models.


## Testing

1. Carousel Active Class:
    1. Create if statement so only one generated image has class="active" 
    2. Load home page 
    3. Click left and right arrows to change image 
    4. Image change to next or previous image 

2. Remember My Details:
    ...

This didn't work the first few attempts, this was due to the confusion between the jinja templating language and the django template language. After some research I used forloop.counter, over the 
jinja loop.index. After this change was made the carousel worked as expected allowing for admins to add new carousel slides without consulting an engineer.

### Differences Between Desktop and Mobile Versions

## Deployment

## Credits

### Content

* text used for this project came from [Rhinos](https://www.rhinosgymnasium.co.uk/)

### Media
Images came from the following sources:
* opening-times.jpg - https://www.snowdome.co.uk/fitness-spa/snowdome-fitness/gym/
* gym-front - https://www.pinterest.co.uk/pin/153122456063737469/
* facilities.jpg - https://www.trilogyleisure.co.uk/centres/peterborough-gym/
* gym-equipment.jpg - https://www.westminster.ac.uk/about-us/visit-us/sports-facilities/regent-street-gym
* gym-treadmills.jpg - https://blog.nasm.org/how-to-clean-your-gym

Text used within the project came from the following sources:

* https://www.rhinosgymnasium.co.uk/

### Acknowledgement

* [PureGym](https://www.puregym.com/membership-options/): Subscription/home page
* [thegym](https://www.thegymgroup.com/login/): Payment, login, register
* [Rhinos](https://www.rhinosgymnasium.co.uk/): Membership Options + Why join us page
* [LeisureSK](https://www.leisuresk.co.uk/membership-and-offers): Was used as a guide for gym membership prices.