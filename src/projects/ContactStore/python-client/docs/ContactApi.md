# swagger_client.ContactApi

All URIs are relative to *http://myurl.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_contact**](ContactApi.md#add_contact) | **POST** /contacts | Add a new contact
[**delete_contact**](ContactApi.md#delete_contact) | **DELETE** /contact/{contactId} | Deletes a contact
[**get_contact_by_id**](ContactApi.md#get_contact_by_id) | **GET** /contact/{contactId} | Find contact by ID
[**get_contacts**](ContactApi.md#get_contacts) | **GET** /contacts | list of all contact
[**update_contact**](ContactApi.md#update_contact) | **POST** /contact/{contactId} | Updates a contact in the store with form data


# **add_contact**
> add_contact(body=body)

Add a new contact

description for add new contact

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContactApi()
body = swagger_client.Contact() # Contact | Contact object that needs to be added to the store (optional)

try:
    # Add a new contact
    api_instance.add_contact(body=body)
except ApiException as e:
    print("Exception when calling ContactApi->add_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Contact**](Contact.md)| Contact object that needs to be added to the store | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_contact**
> delete_contact(contact_id)

Deletes a contact



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContactApi()
contact_id = 789 # int | Contact id to delete

try:
    # Deletes a contact
    api_instance.delete_contact(contact_id)
except ApiException as e:
    print("Exception when calling ContactApi->delete_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_id** | **int**| Contact id to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_by_id**
> Contact get_contact_by_id(contact_id)

Find contact by ID

Returns a contact

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContactApi()
contact_id = 789 # int | ID of contact that needs to be fetched

try:
    # Find contact by ID
    api_response = api_instance.get_contact_by_id(contact_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactApi->get_contact_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_id** | **int**| ID of contact that needs to be fetched | 

### Return type

[**Contact**](Contact.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contacts**
> list[Contact] get_contacts(limit=limit)

list of all contact

Returns list of contact

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContactApi()
limit = 11 # int | limit of return (optional) (default to 11)

try:
    # list of all contact
    api_response = api_instance.get_contacts(limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactApi->get_contacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| limit of return | [optional] [default to 11]

### Return type

[**list[Contact]**](Contact.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_contact**
> update_contact(contact_id, body=body)

Updates a contact in the store with form data



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ContactApi()
contact_id = 'contact_id_example' # str | ID of contact that needs to be updated
body = swagger_client.Contact() # Contact | Contact object that needs to be added to the store (optional)

try:
    # Updates a contact in the store with form data
    api_instance.update_contact(contact_id, body=body)
except ApiException as e:
    print("Exception when calling ContactApi->update_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_id** | **str**| ID of contact that needs to be updated | 
 **body** | [**Contact**](Contact.md)| Contact object that needs to be added to the store | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

