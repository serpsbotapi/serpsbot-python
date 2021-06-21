# AppApisAccountSchemasResultResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID of the user. This uniquely identifies the user in our database. | 
**first_name** | **str** | The first name of the user. | 
**last_name** | **str** | The last name of the user. | 
**email** | **str** | The email address of the user. | 
**has_api_access** | **bool** | Tells either the user has the API access or not. i.e When balance falls to zero, API access is diabled for users. | 
**balance** | **float** | Prepaid account balance of the user (in USD). | 
**statistics** | [**AllOfappApisAccountSchemasResultResponseStatistics**](AllOfappApisAccountSchemasResultResponseStatistics.md) | The account statistics including stats on monthly and all-time API calls, jobs count, and so on. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

