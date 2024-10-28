# V2UpdateBiologicalSampleRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bio_sample_name** | **str** | The name of the biosample, which must be unique and only contain alphanumeric, dash, or underscore letters | 
**default_project_id** | **str** | Define the ID of the project to set as the default project | 
**subject_id** | **str** |  | 
**container_name** | **str** | The name of the plate or tube containing the biosample, typically its barcode | 
**container_position** | **str** | The location of the biosample within a plate or other container, typically the well it is in | 
**status** | **str** | Possible values are: New, Active, Done, QcFailed, Canceled | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

