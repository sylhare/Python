# coding: utf-8

from __future__ import absolute_import

from flask import json
from swagger_server.models.contact import Contact  # noqa: E501
from swagger_server.test import BaseTestCase


class TestContactController(BaseTestCase):
    """ContactController integration test stubs"""

    def test_add_contact(self):
        """Test case for add_contact

        Add a new contact
        """
        body = Contact()
        response = self.client.open(
            '/v1/contacts',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_contact(self):
        """Test case for delete_contact

        Deletes a contact
        """
        response = self.client.open(
            '/v1/contact/{contactId}'.format(contactId=789),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_contact_by_id(self):
        """Test case for get_contact_by_id

        Find contact by ID
        """
        response = self.client.open(
            '/v1/contact/{contactId}'.format(contactId=789),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_contacts(self):
        """Test case for get_contacts

        list of all contact
        """
        query_string = [('limit', 10000)]
        response = self.client.open(
            '/v1/contacts',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_contact(self):
        """Test case for update_contact

        Updates a contact in the store with form data
        """
        body = Contact()
        response = self.client.open(
            '/v1/contact/{contactId}'.format(contactId='contactId_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest

    unittest.main()
