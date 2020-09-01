"""
    Functions that used by function in users_controls directory.
    They provide all main functionality.
    Class Contact that describes the contact card:
        - last name (required)
        - name (required)
        - second name (optional)
        - address(built from City(required) and Street(optional))
        - email list(optional)
        - phone list - one required, additional optional
        - social network list: a list of pairs of values - the name of the messenger (from a predefined list)
        and account. One social network is required, additional optional.
    User can create, update, delete, view(all or chosen) contacts that stored in address book (list).
    User can search for contacts by name, last name and in all fields.
    User can also save address book in .txt file, export inn JSON and import from JSON file.
    Provided validation for email value, and for required contact attributes.
"""

from address_book.controls.contact import Contact
from address_book.controls.global_var import *
from address_book.controls.import_contacts import import_address_book
from address_book.controls.export_contacts import export_address_book
from address_book.controls.save_address_book import save_address_book
from address_book.controls.search_functions import *
from address_book.controls.update_functions import *
from address_book.controls.view_functions import *
from address_book.controls.validation_functions import *

__all__ = (
    'Contact',
)

