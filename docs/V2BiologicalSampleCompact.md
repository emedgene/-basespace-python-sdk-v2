# V2BiologicalSampleCompact

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**href** | **str** |  | [optional] 
**user_owned_by** | [**V1pre3UserCompact**](V1pre3UserCompact.md) |  | [optional] 
**bio_sample_name** | **str** |  | [optional] 
**nickname** | **str** |  | [optional] 
**default_project** | [**V1pre3ProjectCompact**](V1pre3ProjectCompact.md) |  | [optional] 
**date_modified** | **datetime** |  | [optional] 
**date_created** | **datetime** |  | [optional] 
**subject** | [**V2SubjectCompact**](V2SubjectCompact.md) |  | [optional] 
**container_name** | **str** |  | [optional] 
**container_position** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**lab_status** | **str** |  | [optional] 
**href_ica_uri_samples** | **str** |  | [optional] 
**prep_requests** | [**list[V2PrepRequest]**](V2PrepRequest.md) |  | [optional] 
**library_preps** | [**list[NameAndId]**](NameAndId.md) |  | [optional] 
**output_project_ids** | **list[str]** |  | [optional] 
**yields** | [**list[V2BiologicalSampleLibraryYield]**](V2BiologicalSampleLibraryYield.md) |  | [optional] 
**properties** | [**V2PropertyContainer**](V2PropertyContainer.md) |  | [optional] 
**has_qc_passed_fastq_datasets** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

