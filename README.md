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

* __Colour Scheme:__ Inspired by a lion's own colours, using the color scheme provided by SchemeColor, some colours were slighly lightened or darkened to better follow the flow of the other elements.
* __Navbar Desktop:__ A black background, with light text, this allows for eyecatching and hard to miss links, so the user is easily able to navigate to the links. The navbar is split into 2 colums, the left most holding the logo and name of the business linking to the home page. And the right most holding the navigation links, this is to split up the two columns making it clear to users where one begins and another ends.
* __Navbar Mobile:__ The mobile variation uses a customised button, not following the usual black background and opting for a dark brown. Making it clear where the button is. Opening the navbar the links are positioned ontop of eachother.
* __Footer:__ A simple footer, covering the opening times, this is to inform users who may have missed the information above, or those who are in a rush to view when the business opens and closes.
* __Home Page:__ At the top of the page is a carousel with the latest news for the site. The purpose of this is to catch the user's attention as soon as the page appears on their screen. This almost forces the user to be aware of the what is going on with the business. Following is a darkened background welcoming users to the website this is to give users a basic understanding for what the business is and stands for. After is a lighter block, this is to make the page more interesting, rather than a continous block of colour, the shifting palette keeps the user focused and receptive to the information.
* __Subscriptions Page:__ This page is split up into 2 columns that situate ontop of eachother on the mobile view. Headers are a light brown, and informative text is a white. This allows for a clear difference between the 2. The Edit and Delete links that are visible to superusers, are white for the edit and red for the delete making it clear to users that this function should only be done when intended to and avoided when you have no intention to do so. In the second column is white informative text, continuing the theme.
* __Categories Page:__ Similar to the subscriptions page, without the second column. It follows the same scheme as the mentioned page.
* __Slides Page:__ This page has a table holding all of the slides and information a superuser may need. T

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

* __Logo:__ Presents the logo of the business to the user, also acts as a home link.
* __Navbar:__ Holds navigation links, which allow user to navigate around the site, on mobile view it becomes an expandable button, taking up less screen realestate.
* __Carousel:__ An informative slideshow which displays current news and updates within the business.
* __Welcome Text:__ Informs the user what the business is about and what they stand for.
* __Why Train Text:__ Encourages users to signup for a subscription.
* __Footer:__ Holds opening time information in a place that is consitant and easy to find by users.
* __Login:__ Enables user to access their account.
* __Register:__ Allows user to create an account.
* __Subscriptions:__ Lists all the subscriptions available to users, by clicking on a subscription the user is taken to the signup form, with the information for the selected subscription prefilled into the form. Superusers are able to edit and delete subscriptions from this page.
* __Subscriptions Information:__ Encourages signups by making all the information clear and accessible to the user. Hiding no details from them, building trust with customer and business.
* __Edit Subscription:__ A superuser can access this page that is a prefilled form of the selected subscription, pressing the update button will update the selected subscription.
* __Delete Subscription:__ Superusers have access to a delete link once pressed will remove that subscription from the database.
* __Signup Form:__ Asks the user to input their information for the database, after signup is complete the subscription is attached to the user's profile.
* __Stripe Payment:__ Allows users to pay for their subscription in a secure manner, by inputting their payment information.
* __Remember Me:__ After the form is submitted if checked will attach the user's details to their profile and can be accessed by the database, users are able to update this information from their profile.
* __Payment Success:__ Informs the user that a confirmation email has been sent to email address used in the form on the page before, and links them to the home page.
* __Categories:__ Superusers can view this page, it contains all the categories within the database, there are edit and delete links for all categories.
* __Edit Categories:__ Superusers have access to the edit page similar to the edit subscription is a prefilled form with the categories information, altering the information and pressing the update button will update the information stored in the database.
* __Delete Categories:__ If the user is a superuser they can delete categories, removing the instance from the database.
* __Slides:__ A tabular view of all the slide rotating within the slideshow on the home page. This page is only accessible by superusers.
* ___Edit Slides:__ Allows a superuser to edit a slide within the slideshow.
* __Delete Slide:__ A superuser is able to delete a slide from the database.
* __Profile:__ All users after they have signed up for an account have access to their own profile. This holds personal information for the user, as well as their subscription history.
* __Default Information:__ A form that can be prefilled if the user checked the remember me box, the form will be prefilled with that data. This form can be updated with new information of the user. Being accessible by the signup form.
* __Subscription History:__ Holds all of the subscriptions that the user has signed up for, they are presented in a table that is easy to view on desktop and mobile.

### Features to Implement

* __Contact Us:__ This feature would allow users to contact the business directly through an email. This would be done through a form, once filled out sends an email to the business.
* __Subscription Time Out:__ This would inform the user when a subscription has timed out and needs renewing, would also greyed out an outdated subscription.
* __Cancel Subscription:__ Would allow a user to cancel a subscription early through the profile view.

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

This didn't work the first few attempts, this was due to the confusion between the jinja templating language and the django template language. After some research I used forloop.counter, over the 
jinja loop.index. After this change was made the carousel worked as expected allowing for admins to add new carousel slides without consulting an engineer.

2. Subscriptions:
    1. Load subscriptions page
    2. select first subscription / loads signup form
    3. ensure link contains subscription_id
    4. Ensure price to be charged is correct
    5. Repeat for each subscription

The process for getting the price into the payment intent took many forms, this will be covered more in the signup testing. The final form that it took was much more streamlined.

3. Categories:
    1. Sign into non superuser account, making sure categories is not a visible link
    2. Sign into superuser account, making sure the catiegories link is visible
    3. Load categories page
    4. Ensure all categories are visible

3. Slides:
    1. Sign into non superuser account, making sure Slides is not a visible link
    2. Sign into superuser account, making sure the Slides link is visible
    3. Load Slides page
    4. Ensure all Slides are visible

4. Profile:
    1. Ensure profile link is not accessible by a non user, by not being logged in
    2. Create an account through the login page
    3. Load profile page

5. Default Information Form:
    1. Load profile page and ensure form loads correctly, from django forms
    2. Fill out form
    3. Alter fields, into nonvalid data, submit form, form should reject
    4. Fill in fields with valid data, submit form, form submits
    5. Refresh page to ensure information persists

6. Subscription History:
    1. Load profile page
    2. Ensure table loads correctly
    3. 
    


### Differences Between Desktop and Mobile Versions

## Deployment

## Credits

### Content

* Text used for this project came from [Rhinos](https://www.rhinosgymnasium.co.uk/)
* Colour scheme came from [SchemeColor.com](https://www.schemecolor.com/lion-colors.php)

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