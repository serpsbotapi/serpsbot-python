# ExtendedSearchRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | The search query phrase. All Google Search filters are supported. | 
**gl** | **str** | The ISO code of the country to get targeted search results. | [optional] [default to 'US']
**hl** | **str** | The language to get targeted search results. | [optional] [default to 'en_US']
**device** | **str** |  | [optional] [default to 'desktop']
**duration** | **str** | Duration to get search results updated during the specified time period. &lt;code&gt;d&lt;/code&gt; for last 24 hours, &lt;code&gt;w&lt;/code&gt; for last 1 week, &lt;code&gt;m&lt;/code&gt; for last 1 month, &lt;code&gt;mn&lt;/code&gt; for last n months, and &lt;code&gt;y&lt;/code&gt; for last 1 year. | [optional] 
**autocorrect** | **int** | Should Google autocorrect your typos? Send 1 if that&#x27;s the case or send 0 if you want to disable autocorrection. | [optional] [default to 0]
**page** | **int** | The page to get search results for. By default, the first page&#x27;s results are returned. | [optional] [default to 1]
**uule** | **str** | An encoded string to force a place or an exact location to get targeted results. | [optional] 
**num** | **int** | Specify how many results should be retrieved per page. | [optional] [default to 20]
**output** | **str** | Result output format. You can request either parsed JSON or the raw HTML. | [optional] [default to 'json']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

