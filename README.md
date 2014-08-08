member-distribution
===================

Installation
------------
Clone this repository using

    git clone https://github.com/jghyllebert/member-distribution.git

Install the requirements

    pip install -r member-distribution/requirements/requirements.txt

Don't forget to set a ``SECRET_KEY``.

Sync the database

    cd member-distribution/project
    python manage.py syncdb


Optional: fill the database with random members, personal shoppers and orders

    python manage.py fill_database

Run the server

    python manage.py runserver
