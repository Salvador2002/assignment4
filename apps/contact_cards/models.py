"""
This file defines the database models
"""

import datetime
from .common import db, Field, auth
from pydal.validators import *

# Utility function to get the current user's email
def get_user_email():
    return auth.current_user.get('email') if auth.current_user else None

# Utility function to get the current UTC time
def get_time():
    return datetime.datetime.utcnow()

# Define the contact_card table
db.define_table(
    'contact_card',
    Field('user_email', default=get_user_email),  # Stores the email of the user who owns the contact
    Field('contact_name', 'string', requires=IS_NOT_EMPTY()),  # Name of the contact, required field
    Field('contact_affiliation', 'string', default=''),  # Affiliation, optional field
    Field('contact_description', 'text', default=''),  # Description, optional field
    Field('contact_image', 'text', default='https://bulma.io/assets/images/placeholders/96x96.png'),  # Image URL, default placeholder
    Field('created_on', 'datetime', default=get_time),  # Timestamp for when the contact was created
    Field('updated_on', 'datetime', update=get_time),  # Timestamp for last update
)

# Commit the changes to the database to ensure the table is created
db.commit()
