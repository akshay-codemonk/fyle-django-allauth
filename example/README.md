## Running the example application

Follow these steps to download and run the fyle-django-allauth example application in this directory:

    $ git clone https://github.com/fylein/fyle-xero.git
    $ cd fyle-django-allauth/example


### Install dependencies    
Install the python dependencies from requirements.txt file

If using virtualenv do

    $ virtualenv venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt

Once all dependencies are installed, apply migrations to create the database tables.

    $ python manage.py migrate
    
then, create a superuser

    $ python manage.py createsuperuser

Finally, start the Django development server:

    $ python manage.py runserver

### Admin Configuration
Goto django-admin at [http://localhost:8000/admin](http://localhost:8000/admin) and login with the above created superuser credentials

1. First go to the Sites portion and set the domain name and display name to ```localhost```

2. Create your OAuth 2.0 Application in Fyle and get your client_id and client_secret by following this [guide](https://www.fylehq.com/help/en/articles/3045578-integrating-with-fyle)

    For Redirect URI enter the following URL ``http://localhost:8000/accounts/fyle/login/callback/``
    
    When you deploy your Django application live you’d replace localhost with your actual production homepage. We use the localhost for testing purposes.
    
3. Next go back to the admin homepage and click on the add button for Social Applications on the bottom.
   This is where we configure Fyle OAuth. 
   1. Select Fyle as provider
   2. Enter a name 
   3. Enter the Client ID and Secret ID obtained from Fyle.
   4. Final step is to add our site, in this case localhost to the Chosen sites on the bottom. Then click save.

### Sign in using Fyle
Logout from django admin and head to ``http://localhost:8000/home`` and you should see a page with links to sign in using fyle.
