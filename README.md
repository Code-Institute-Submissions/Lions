# Lions

Lions is a gymnasium, providing great prices, lovely and helpful staff, as well as a welcoming environment for anyone and everyone. The business works off of a paper system, asking customers
to fill out physical forms either provided by the staff or printed off of at home. The benefits of the website is that customers are able to signup for a subscription and manage it all from 
their own homes, with the convenience of a smart device or computer. Staff are also able to see all subscriptions and search the database through the use of Django, whereas they couldn't before.

## UX

## Features

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