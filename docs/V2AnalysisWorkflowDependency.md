# V2AnalysisWorkflowDependency

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of dependency to add, valid operators include: “BioSampleYield”, “AppCompletion” | 
**attributes** | **dict(str, object)** | Sections containing a list of attributes and their values defining the app launch dependency, specific to the dependency type given | 
**dependencies** | [**list[V2AnalysisWorkflowDependency]**](V2AnalysisWorkflowDependency.md) | Optional nested dependencies, not needed for BioSampleYield or AppCompletion dependency types | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

