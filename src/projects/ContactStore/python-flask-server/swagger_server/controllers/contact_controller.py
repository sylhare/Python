import connexion

from swagger_server.models.contact import Contact  # noqa: E501


def add_contact(body=None):  # noqa: E501
    """Add a new contact

    description for add new contact # noqa: E501

    :param body: Contact object that needs to be added to the store
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Contact.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_contact(contactId):  # noqa: E501
    """Deletes a contact

     # noqa: E501

    :param contactId: Contact id to delete
    :type contactId: int

    :rtype: None
    """
    return 'do some magic!'


def get_contact_by_id(contactId):  # noqa: E501
    """Find contact by ID

    Returns a contact # noqa: E501

    :param contactId: ID of contact that needs to be fetched
    :type contactId: int

    :rtype: Contact
    """
    return 'do some magic!'


def get_contacts(limit=None):  # noqa: E501
    """list of all contact

    Returns list of contact # noqa: E501

    :param limit: limit of return
    :type limit: int

    :rtype: List[Contact]
    """
    return 'do some magic!'


def update_contact(contactId, body=None):  # noqa: E501
    """Updates a contact in the store with form data

     # noqa: E501

    :param contactId: ID of contact that needs to be updated
    :type contactId: str
    :param body: Contact object that needs to be added to the store
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Contact.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
