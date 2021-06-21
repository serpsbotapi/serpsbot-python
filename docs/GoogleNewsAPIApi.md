# serpsbot.GoogleNewsAPIApi

All URIs are relative to *https://api.serpsbot.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_news_results_google_news_post**](GoogleNewsAPIApi.md#get_news_results_google_news_post) | **POST** /google/news | Get News Results

# **get_news_results_google_news_post**
> AppApisGoogleNewsSchemasResultResponse get_news_results_google_news_post(body)

Get News Results

This endpoint allows you to get Google News results as JSON data.

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
api_instance = serpsbot.GoogleNewsAPIApi(serpsbot.ApiClient(configuration))
body = serpsbot.AppApisGoogleNewsSchemasSearchRequest() # AppApisGoogleNewsSchemasSearchRequest | 

try:
    # Get News Results
    api_response = api_instance.get_news_results_google_news_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GoogleNewsAPIApi->get_news_results_google_news_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AppApisGoogleNewsSchemasSearchRequest**](AppApisGoogleNewsSchemasSearchRequest.md)|  | 

### Return type

[**AppApisGoogleNewsSchemasResultResponse**](AppApisGoogleNewsSchemasResultResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

