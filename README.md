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
* The signup process asks for a gender, not all users are comfortable to assign themselves one specific gender and therefore there is an "Other" option for those that do not identify with the traditional "Male" or "Female".
* At the end of the signup process is a checkbox asking the user if they want their information to be remember, if it is not checked information about the user will not be saved, and if it details will be saved and input into a form on the user's profile where they may update them if needs be.
* The profile app is able to display the user's saved information if they asked for it to be stored and update if they need to, keeping records all up to date.
* An aspect of the profile app is the list that holds all of the subscriptions that the user has signed up for, in a way that is clear to understand, and nicely displayed.
 
### Developer and Business Goals
 
* Have a safe place for all to come and workout without feeling judged, prejudiced or discriminated against.
* Have an easy method to update all outdatable fields, such as the "Categories”, “Subscriptions” and "Slides" fields which change as the business changes.
* A database with all subscriptions so staff can view all subscriptions, easily and without hassle.
 
Lions achieves these goals by:
 
* Lions thrive on presenting an environment where all feel welcome, this is done by adding additional options where necessary to help all customers feel welcome, such as the "Other" gender field. And omitting any fields including race and other sensitive information users may be afraid to pass on. This allows everyone to feel comfortable in the environment that Lions is creating.
* Staff are able to Create, Read, Update and Delete the "Categories", "Subscriptions" and "Slides" fields within the app, rather than needing to navigate to the admin. The forms are simple and clear for new and old staff to make use of.
* Django allows for an easily accessible database storing all the information staff would want to get their hands on. Going above the initial subscriptions options.
 
### User Stories
 
* As an older user, I want to be able to sign up for a subscription in a quick and simple manner.
* As a frequent user, I want to be able to easily be kept up to date on the business' current status.
* As an LGBTQ+ user, I want a welcoming platform where I don't have to assign a gender that doesn't fit to me.
* As an owner, I want users to be able to understand what the business is, and our goal.
* As a frequent user, I want to be able to find the opening times quick and easily, without having to search for them.
* As a member of staff, I want a clear view of everything that is editable and currently available to customers.
* As an owner, I want my staff to be able to see all subscriptions past and present.
 
### Design Choices
 
* __Colour Scheme:__ Inspired by a lion's own colours, using the color scheme provided by SchemeColor, some colours were slightly lightened or darkened to better follow the flow of the other elements.
* __Navbar Desktop:__ A black background, with light text, this allows for eye catching and hard to miss links, so the user is easily able to navigate to the links. The navbar is split into 2 columns, the leftmost holding the logo and name of the business linking to the home page. And the right most holding the navigation links, this is to split up the two columns making it clear to users where one begins and another ends.
* __Navbar Mobile:__ The mobile variation uses a customised button, not following the usual black background and opting for a dark brown. Making it clear where the button is. Opening the navbar the links are positioned on top of eachother.
* __Footer:__ A simple footer, covering the opening times, this is to inform users who may have missed the information above, or those who are in a rush to view when the business opens and closes.
* __Home Page:__ At the top of the page is a carousel with the latest news for the site. The purpose of this is to catch the user's attention as soon as the page appears on their screen. This almost forces the user to be aware of what is going on with the business. Following is a darkened background welcoming users to the website this is to give users a basic understanding for what the business is and stands for. After is a lighter block, this is to make the page more interesting, rather than a continuous block of colour, the shifting palette keeps the user focused and receptive to the information.
* __Subscriptions Page:__ This page is split up into 2 columns that situate ontop of eachother on the mobile view. Headers are light brown, and informative text is a white. This allows for a clear difference between the 2. The Edit and Delete links that are visible to superusers, are white for the edit and red for the delete making it clear to users that this function should only be done when intended to and avoided when you have no intention to do so. In the second column is white informative text, continuing the theme.
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
* __Navbar:__ Holds navigation links, which allow the user to navigate around the site, on mobile view it becomes an expandable button, taking up less screen real estate.
* __Carousel:__ An informative slideshow which displays current news and updates within the business.
* __Welcome Text:__ Informs the user what the business is about and what they stand for.
* __Why Train Text:__ Encourages users to sign up for a subscription.
* __Footer:__ Holds opening time information in a place that is consistent and easy to find by users.
* __Login:__ Enables users to access their account.
* __Register:__ Allows users to create an account.
* __Subscriptions:__ Lists all the subscriptions available to users, by clicking on a subscription the user is taken to the signup form, with the information for the selected subscription prefilled into the form. Superusers are able to edit and delete subscriptions from this page.
* __Subscriptions Information:__ Encourages signups by making all the information clear and accessible to the user. Hiding no details from them, building trust with customers and business.
* __Edit Subscription:__ A superuser can access this page that is a prefilled form of the selected subscription, pressing the update button will update the selected subscription.
* __Delete Subscription:__ Superusers have access to a delete link once pressed will remove that subscription from the database.
* __Signup Form:__ Asks the user to input their information for the database, after signup is complete the subscription is attached to the user's profile.
* __Stripe Payment:__ Allows users to pay for their subscription in a secure manner, by inputting their payment information.
* __Remember Me:__ After the form is submitted if checked will attach the user's details to their profile and can be accessed by the database, users are able to update this information from their profile.
* __Payment Success:__ Informs the user that a confirmation email has been sent to the email address used in the form on the page before, and links them to the home page.
* __Categories:__ Super Users can view this page, it contains all the categories within the database, there are edit and delete links for all categories.
* __Edit Categories:__ Super Users have access to the edit page similar to the edit subscription is a prefilled form with the categories information, altering the information and pressing the update button will update the information stored in the database.
* __Delete Categories:__ If the user is a superuser they can delete categories, removing the instance from the database.
* __Slides:__ A tabular view of all the slides rotating within the slideshow on the home page. This page is only accessible by superusers.
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
* [Gitpod](https://www.gitpod.io/): Was used for its IDE, allowing for the project to be coded.
* [Github](https://github.com/): Was helpful in storing the website, especially for version control.
* [Lucidchart](https://lucidchart.zendesk.com/hc/en-us): Used to make wireframes.
* [django](https://www.djangoproject.com/): A high level python framework making the development process quicker and easier, enabling a high quality end product within a tight timeframe.
* [MySQL](https://www.mysql.com/): A relational database management system, it is used as the database for storing data for the project.
* [SQLite](https://www.sqlite.org/index.html): A C-language library that implements a light weight, fast SQL database engine.
* [django-allauth](https://django-allauth.readthedocs.io/en/latest/): Enables to project to use multiple authentication schemes and account verification.
* [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/): Allows to easy and pleasant styling of form elements without disturbing the flow of django.
* [Bootstrap](https://getbootstrap.com/): Used styling provided to quickly position content as well as create bespoke styling with custom css.
* [Font Awesome](https://fontawesome.com/): The vase array of icons were used as intuitive design to help users find and understand features that were designed in an already established manner. 
* [Pillow](https://pillow.readthedocs.io/en/stable/): Was needed to use the ImageField for the subscriptions and products models.
* [psychopg2](https://pypi.org/project/psycopg2/): A PostgreSQL database adapter for the Python programming language.
* [dj-database-url](https://pypi.org/project/dj-database-url/): Allows the ability to utilize the 12factor inspired DATABASE_URL environment variable to configure your Django application.
* [Amazon Web Services](https://aws.amazon.com/): Used to store media and static files for the deployed version of the project.
 
 
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
    2. Sign into superuser account, making sure the categories link is visible
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
    3. Signup for a subscription using the signup form
    4. navigate back to the profile view, subscription has been input into table
 
7. Signup Form:
    1. Navigate to subscriptions view
    2. Select subscription type, be pushed to signup form.
    3. Input invalid details, form gives error.
    4. Input valid details. Be taken to the payment success page.
 
There were many issues with this aspect of the project and what most of the production time was spent on. I had little understanding of Django and how to set up a model which was the first hurdle. 
After this the initial form of the form was a 3 step process that the website would guide the user through. The issue with this was accessing object data beyond the first step, as JSON wouldn't allow a non string 
type object to be sent through a cookie, which caused trouble for some of the validation aspects. The final step was passing through the subscription type and getting the payment amount for the payment intent,
This needed to be done before Stripe was initialized and present on the page for the user to finalise. So having this on a separate page felt like a must. After some time I decided to shift focus and make the approach 
simpler as the production deadline was coming up. Thus the final form involves selecting the subscription type, passing the ID to the view and having all the important information processed by the view, such as 
the payment intent before the user can witness it.
 
8. Additions Pages:
    1. Navigate to add subscriptions link
    2. Fill out form
    3. Click add subscription button
    4. Navigate to subscriptions page to see if the subscription has been added to the database successfully and is visible to users
 
The process and testing of the add slide, add category and add subscriptions page are all the same, all have been tested, the issues were variable names not being changed within the views, 
as well as the templates.
 
9. Email Confirmation:
    1. Go to register view
    2. fill out form
    3. Wait for email to be sent
    4. Go to link and have email confirmed
 
This worked completely fine during development, but when it came to deploying the site after an account was registered it returned a server error. The solution involved checking variables names; 
where one was incorrect; and refactoring the order of the code.
 
10. Stripe Payment:
    1. Go to subscriptions page, select subscription
    2. fill out signup form, with test card details
    3. Be taken to payment success page
    4. Go to Stripe's development tab to ensure payment has gone through
 
My approach in using Stripe is what made this difficult, I originally wanted to have a 3 step sign up process. This was cut short when I struggled with getting the right price in 
the payment intent when passing variables through views and cookies. In the end it was for the best as keeping payment amounts in cookies isn't the best practise.
    
### Differences Between Desktop and Mobile Versions
 
* __Navbar:__ On the desktop version the navbar stretches across the top of the screen with all the links visible, whereas on the mobile version the navbar is shrunk down into a button that can expand to reveal all the links.
* __Home Page:__ The __Why Train at Lions__ blocks go from being side by side to being on top of eachother to avoid the elements becoming too squished. The carousel's height on screen smaller than 768px becomes 300px, rather than 440px. The carousel container gives different padding depending on the size of the screen, going from 0px on a mobile, 100px on medium desktops and 200px on larger screens.
* __Subscriptions Page:__ The list of available subscriptions and the text elements sit next to each other, but as the available screen size reduces the element go on top of eachother.
* __Profile Page:__ The default details form and the subscription history are side by side on a large desktop, but go to sitting on top of each other on smaller screens.
 
## Deployment
 
### Local Deployment
 
This project was coded within the [Gitpod IDE](https://www.gitpod.io/) and then pushed to [Github](https://github.com/) using the built in functions.
 
1. Log into Github.
2. From the list of repositories on screen, select __lions__.
3. install the requirements.txt using the "pip3 install -r requirements" terminal command
4. After this it's as simple as typing "python3 app.py" within the terminal which will run the file
 
### How to run this project locally
 
To clone this project into Gitpod you will need:
 
1. A GitHub account. [Create a Github account here](https://github.com/)
2. Be using the Chrome browser
 
After follow these steps:
 
1. install the [Gitpod Browser Extension](https://gitpod.io) for Chrome.
2. After installation, restart the browser.
3. Log into your Gitpod account.
4. Navigate to the [Github repository](https://github.com/FabianMarsh/lions).
5. Click the green "Gitpod" button in the top right corner of the repository
6. This will trigger a new Gitpod workspace to be created from the code in github where you can work locally.
 
To work on this project within a local IDE such as Gitpod
 
1. Follow this link to the [Github repository](https://github.com/FabianMarsh/lions).
2. Under the repository name click "Clone or download".
3. In the Clone with HTTPs section, copy the clone URL for the repository.
4. In your local IDE open the terminal.
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type git clone , and then paste the URL you copied in step 3.
 
git clone https://github.com/FabianMarsh/lions
 
7. Press Enter. Your local clone will be created.
 
### Heroku Deployment
 
To deploy __lions__ to Heroku take the following steps
 
1. Create a requirements.txt file using the terminal command pip3 freeze > requirements.txt.
2. Create a Procfile using the terminal command echo web: python3 app.py > Procfile.
3. git add , git commit , and git push using the terminal commands to push to Github.
4. Sign into or register to [Heroku](https://dashboard.heroku.com/apps).
5. Create a new app on Heroku by clicking the "New" button in the dashboard. Give it a bespoke name and set the region to the closest to you.
6. From the Heroku dashboard of the newly created application, click on "Deployment method" and select Github.
7. Confirm the linking of Heroku and the GitHub repository.
8. Within the Heroku dashboard for the application, click on "Settings" then "Reveal Config Vars".
9. Set the following config vars:
 
Key | Value
--- | -----
AWS_ACCESS_KEY_ID | <your_access_key_id>
AWS_SECRET_ACCESS_KEY | <your_secret_access_key> 
DATABASE_URL | <your_database_url> 
EMAIL_HOST_PASS | <your_email_password> 
EMAIL_HOST_USER | <your_email> 
SECRET_KEY | <your_secret_key> 
STRIPE_PUBLIC_KEY | <your_public_key> 
STRIPE_SECREY_KEY | <your_stripe_secret_key> 
USE_AWS | True
 
10. In the dashboard click "Deploy"
11. In the "Manual Deployment" section of this page, make sure the master branch is selected and click "Deploy Branch".
 
12. Go to [Amazon Web Services](https://aws.amazon.com/), and create an account.
13. Search for the S3 service, within the services menu.
14. Click create bucket. 
15. Give it a name, select the region closest to you, uncheck block all public, and check the acknowledge box, finally click create bucket.
16. Click on your new bucket, and navigate to the properties tab, static website hosting, and check use this bucket to host a website.
17. Set index document and error document to some default values, such as index.html and error.html and save.
18. Going to the permissions tab, then CORS configuration, copy and paste the code, indent correctly and click save. 
    * Note as of the writing of this document this code is relevant, Amazon Web Services may have updated, and the code outdated.
 
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
 
19. Navigating to the bucket policy tab, select policy generator.
20. Set the following values. And add a statement, then generate policy and copy and paste the policy into the policy editor. Before saving the policy at the end of your Resource value add a "/*" and save.
    * Select Type of Policy: S3 Bucket Policy
    * Principal: *
    * Actions: GetObject
    * Amazon Resource Name (ARN): <your_ARN>
        * You can find this on the Bucket Policy tab.
21. Navigating to the Access Control List tab set public access for everyone to List Objects.
22. Back on the services menu search and open IAM.
23. Within the IAM dashboard select groups, then create a new group, naming it "manage-<your-website>", click next step, until you get to the create group button.
24. In the dashboard select policies, then create policy, in the JSON tab, select import policy and find the "AmazonS3FullAccess" policy and import it.
25. Within the Resource value create a list and input your ARN twice, the second add a trailing "/*" to allow for files to be used. Review the policy.
26. Going back to the groups, find the group you made earlier, within permissions, click attach policy, search the policy you just made, and attach the policy.
27. With the users menu, in the dashboard, click add user, provide them a username, allow them programmatic access, and then click next.
28. Add the user to the group you made, next until you get to create user. After creating a user ensure to download the .csv file, as you won't have access to this again.
29. Within settings.py alter "AWS_STORAGE_BUCKET_NAME" to be the name of your bucket, and "AWS_S3_REGION_NAME" to your closest region.
30. git add, git commit and git push the changes to Heroku
31. Going back to AWS, create a media folder within S3.
32. Within the folder select upload and supply any images you wish to use, then click next.
33. Under manage public permission, grant read access to the objects. click through to the end and then click upload.
34. Add this point if you do not have a [Stripe](https://stripe.com/gb) account create one, and then go to the Developer's tab and API keys, and get your Pushiable key and Secret key. And supply them to the Heroku Config Vars
35. The site has been deployed.
 
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
