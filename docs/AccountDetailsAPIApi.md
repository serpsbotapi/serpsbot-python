# serpsbot.AccountDetailsAPIApi

All URIs are relative to *https://api.serpsbot.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account_details_account_info_get**](AccountDetailsAPIApi.md#get_account_details_account_info_get) | **GET** /account/info | Get Account Details

# **get_account_details_account_info_get**
> AppApisAccountSchemasResultResponse get_account_details_account_info_get()

Get Account Details

This endpoint allows you to get details related to the authenticated account.

### Example
```python
from __future__ import print_function
import time
import serpsbot
from serpsbot.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKeyHeader
configuration = serpsbot.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-KEY'] = 'Bearer'

# create an instance of the API class
api_instance = serpsbot.AccountDetailsAPIApi(serpsbot.ApiClient(configuration))

try:
    # Get Account Details
    api_response = api_instance.get_account_details_account_info_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountDetailsAPIApi->get_account_details_account_info_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AppApisAccountSchemasResultResponse**](AppApisAccountSchemasResultResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

