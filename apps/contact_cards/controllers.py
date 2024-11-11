"""
This file defines actions, i.e., functions the URLs are mapped into.
"""

from py4web import action, request, abort, redirect, URL
from .common import db, session, T, auth, flash
import json

@action('get_contacts')
@action.uses(db, session, auth.user)
def get_contacts():
    # Fetch all contact cards for the logged-in user
    user_email = auth.current_user.get('email')
    contacts = db(db.contact_card.user_email == user_email).select().as_list()
    return dict(contacts=contacts)

@action('add_contact', method='POST')
@action.uses(db, session, auth.user)
def add_contact():
    # Add a new contact card
    data = request.json
    if not data:
        abort(400, "No data provided")
    
    db.contact_card.insert(
        user_email=auth.current_user.get('email'),
        contact_name=data.get('name', ''),
        contact_affiliation=data.get('affiliation', ''),
        contact_description=data.get('description', ''),
        contact_image=data.get('photo', 'https://bulma.io/assets/images/placeholders/96x96.png')
    )
    return dict(success=True)

@action('delete_contact/<contact_id:int>', method='DELETE')
@action.uses(db, session, auth.user)
def delete_contact(contact_id):
    # Delete a contact card by ID
    user_email = auth.current_user.get('email')
    contact = db.contact_card(contact_id)
    
    if contact and contact.user_email == user_email:
        contact.delete_record()
        return dict(success=True)
    else:
        abort(403, "Not authorized or contact not found")
