# V2QcThreshold

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the metric | 
**optional** | **bool** | Describes whether the QCThreshold is Optional or Required. By default it is set to Required | [optional] 
**operator** | **str** | Valid operators: “Equal”, “LessThan”, “GreaterThan”, “LessThanOrEqual”, “GreaterThanOrEqual”, “NotEqual”, “Between”, “Outside” | 
**dataset_type_id** | **str** | The dataset type slug, e.g. illumina.issac.v4 | 
**threshold_values** | **list[object]** | Integer values of the thresholds. A comma separated list can be given for the “Between” and “Outside” operators | 
**group** | **str** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

