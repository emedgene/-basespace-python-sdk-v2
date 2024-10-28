# V2PostRunsStartRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jwt** | **str** | Stratus JWT issued by platform upon user login | 
**planned_run_id** | **str** | The GLS planned run ID | 
**instrument_run_id** | **str** | The instrument run ID value that should be used (instrument generated) | 
**run_name** | **str** | The name of run that was edited in the instrument | [optional] 
**flowcell_barcode** | **str** | Flowcell barcode | 
**reagent_barcode** | **str** | ReagentBarcode for the run | 
**run_mode** | **str** | Run mode | 
**run_parameters_xml** | **str** | Run parameters xml | 
**instrument_run_number** | **int** | Run number | 
**instrument_software_version** | **str** | Instrument software version | 
**sample_sheet_name** | **str** | Sample sheet name used in instrument | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

