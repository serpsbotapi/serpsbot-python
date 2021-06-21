# serpsbot.GoogleSearchAPIApi

All URIs are relative to *https://api.serpsbot.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**organic_extended_google_organic_extended_post**](GoogleSearchAPIApi.md#organic_extended_google_organic_extended_post) | **POST** /google/organic-extended | Organic Extended
[**organic_results_google_organic_search_post**](GoogleSearchAPIApi.md#organic_results_google_organic_search_post) | **POST** /google/organic-search | Organic Results
[**search_suggestions_google_search_suggestions_post**](GoogleSearchAPIApi.md#search_suggestions_google_search_suggestions_post) | **POST** /google/search-suggestions | Search Suggestions

# **organic_extended_google_organic_extended_post**
> ExtendedResultResponse organic_extended_google_organic_extended_post(body)

Organic Extended

Get extended search results from Google Search including knowledge card data and more SERP elements. You can also request raw SERPs HTML.

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
api_instance = serpsbot.GoogleSearchAPIApi(serpsbot.ApiClient(configuration))
body = serpsbot.ExtendedSearchRequest() # ExtendedSearchRequest | 

try:
    # Organic Extended
    api_response = api_instance.organic_extended_google_organic_extended_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GoogleSearchAPIApi->organic_extended_google_organic_extended_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExtendedSearchRequest**](ExtendedSearchRequest.md)|  | 

### Return type

[**ExtendedResultResponse**](ExtendedResultResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organic_results_google_organic_search_post**
> AppApisGoogleOrganicSchemasResultResponse organic_results_google_organic_search_post(body)

Organic Results

This endpoint gets you the organic results and it is designed to handle very high-volume use keeping the cost lower. You can request multiple Google Search pages in a single API call.

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
api_instance = serpsbot.GoogleSearchAPIApi(serpsbot.ApiClient(configuration))
body = serpsbot.AppApisGoogleOrganicSchemasSearchRequest() # AppApisGoogleOrganicSchemasSearchRequest | 

try:
    # Organic Results
    api_response = api_instance.organic_results_google_organic_search_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GoogleSearchAPIApi->organic_results_google_organic_search_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AppApisGoogleOrganicSchemasSearchRequest**](AppApisGoogleOrganicSchemasSearchRequest.md)|  | 

### Return type

[**AppApisGoogleOrganicSchemasResultResponse**](AppApisGoogleOrganicSchemasResultResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_suggestions_google_search_suggestions_post**
> SuggestionsResponse search_suggestions_google_search_suggestions_post(body)

Search Suggestions

Get search suggestions from Google for your provided list of keywords.

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
api_instance = serpsbot.GoogleSearchAPIApi(serpsbot.ApiClient(configuration))
body = serpsbot.SuggestionRequest() # SuggestionRequest | 

try:
    # Search Suggestions
    api_response = api_instance.search_suggestions_google_search_suggestions_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GoogleSearchAPIApi->search_suggestions_google_search_suggestions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SuggestionRequest**](SuggestionRequest.md)|  | 

### Return type

[**SuggestionsResponse**](SuggestionsResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

