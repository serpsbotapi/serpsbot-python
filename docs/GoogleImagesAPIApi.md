# serpsbot.GoogleImagesAPIApi

All URIs are relative to *https://api.serpsbot.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_images_google_images_post**](GoogleImagesAPIApi.md#get_images_google_images_post) | **POST** /google/images | Get Images

# **get_images_google_images_post**
> AppApisGoogleImagesSchemasResultResponse get_images_google_images_post(body)

Get Images

This endpoint allows you to find images using Google Images search.

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
api_instance = serpsbot.GoogleImagesAPIApi(serpsbot.ApiClient(configuration))
body = serpsbot.AppApisGoogleImagesSchemasSearchRequest() # AppApisGoogleImagesSchemasSearchRequest | 

try:
    # Get Images
    api_response = api_instance.get_images_google_images_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GoogleImagesAPIApi->get_images_google_images_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AppApisGoogleImagesSchemasSearchRequest**](AppApisGoogleImagesSchemasSearchRequest.md)|  | 

### Return type

[**AppApisGoogleImagesSchemasResultResponse**](AppApisGoogleImagesSchemasResultResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

