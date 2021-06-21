# serpsbot.GoogleVideosAPIApi

All URIs are relative to *https://api.serpsbot.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_videos_google_videos_post**](GoogleVideosAPIApi.md#get_videos_google_videos_post) | **POST** /google/videos | Get Videos

# **get_videos_google_videos_post**
> AppApisGoogleVideosSchemasResultResponse get_videos_google_videos_post(body)

Get Videos

This endpoint allows you to get Google Videos results as JSON data.

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
api_instance = serpsbot.GoogleVideosAPIApi(serpsbot.ApiClient(configuration))
body = serpsbot.AppApisGoogleVideosSchemasSearchRequest() # AppApisGoogleVideosSchemasSearchRequest | 

try:
    # Get Videos
    api_response = api_instance.get_videos_google_videos_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GoogleVideosAPIApi->get_videos_google_videos_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AppApisGoogleVideosSchemasSearchRequest**](AppApisGoogleVideosSchemasSearchRequest.md)|  | 

### Return type

[**AppApisGoogleVideosSchemasResultResponse**](AppApisGoogleVideosSchemasResultResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

