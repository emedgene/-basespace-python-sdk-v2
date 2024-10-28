# bssh_sdk_2.BasespaceApi

All URIs are relative to *https://api.basespace.illumina.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_v2_appsessions_id**](BasespaceApi.md#delete_v2_appsessions_id) | **DELETE** /appsessions/{id} | Delete a specific analysis
[**delete_v2_appsessions_id_properties_name**](BasespaceApi.md#delete_v2_appsessions_id_properties_name) | **DELETE** /appsessions/{id}/properties/{name} | Delete a property of an analysis
[**delete_v2_icauploads_foldertype_dataid**](BasespaceApi.md#delete_v2_icauploads_foldertype_dataid) | **DELETE** /icauploads/{foldertype}/{dataid} |
[**delete_v2_notifications_id**](BasespaceApi.md#delete_v2_notifications_id) | **DELETE** /notifications/{id} |
[**delete_v2_oauthv2tokens_current**](BasespaceApi.md#delete_v2_oauthv2tokens_current) | **DELETE** /oauthv2tokens/current |
[**delete_v2_session_invalidate**](BasespaceApi.md#delete_v2_session_invalidate) | **DELETE** /session/invalidate | Log out user from Sequence Hub and end session
[**delete_v2_trash**](BasespaceApi.md#delete_v2_trash) | **DELETE** /trash | Delete all items in the trash
[**get_v2_agreements_id**](BasespaceApi.md#get_v2_agreements_id) | **GET** /agreements/{id} | Get detailed information about a single agreement
[**get_v2_applicationmetadata**](BasespaceApi.md#get_v2_applicationmetadata) | **GET** /applicationmetadata | Request metadata about applications
[**get_v2_applications**](BasespaceApi.md#get_v2_applications) | **GET** /applications | Get a list of available applications
[**get_v2_applications_id**](BasespaceApi.md#get_v2_applications_id) | **GET** /applications/{id} | Get information about an app
[**get_v2_applications_id_qcthresholds**](BasespaceApi.md#get_v2_applications_id_qcthresholds) | **GET** /applications/{id}/qcthresholds | Get a list of QC thresholds applied to an analysis workflow
[**get_v2_applications_id_screenshots**](BasespaceApi.md#get_v2_applications_id_screenshots) | **GET** /applications/{id}/screenshots | Get screenshots of an app
[**get_v2_applications_id_settings**](BasespaceApi.md#get_v2_applications_id_settings) | **GET** /applications/{id}/settings | Get the settings of an application or workflow
[**get_v2_applications_id_versions**](BasespaceApi.md#get_v2_applications_id_versions) | **GET** /applications/{id}/versions | Get versions of an app
[**get_v2_applications_id_workflowdependencies**](BasespaceApi.md#get_v2_applications_id_workflowdependencies) | **GET** /applications/{id}/workflowdependencies | Get a list of workflow dependencies on an analysis workflow
[**get_v2_appresults_id_file_upload_info**](BasespaceApi.md#get_v2_appresults_id_file_upload_info) | **GET** /appresults/{id}/file-upload-info |
[**get_v2_appsessions**](BasespaceApi.md#get_v2_appsessions) | **GET** /appsessions | Get a list of analyses
[**get_v2_appsessions_id**](BasespaceApi.md#get_v2_appsessions_id) | **GET** /appsessions/{id} | Get information about an analysis
[**get_v2_appsessions_id_comments**](BasespaceApi.md#get_v2_appsessions_id_comments) | **GET** /appsessions/{id}/comments | Get a list of comments made about an analysis
[**get_v2_appsessions_id_icalogs**](BasespaceApi.md#get_v2_appsessions_id_icalogs) | **GET** /appsessions/{id}/icalogs | Get ICA log steps for workflows and analyses
[**get_v2_appsessions_id_icalogs_analyses_analysisid_stepid**](BasespaceApi.md#get_v2_appsessions_id_icalogs_analyses_analysisid_stepid) | **GET** /appsessions/{id}/icalogs/analyses/{analysisid}/{stepid} | Get ICA analysis log step stdout stderr log paths
[**get_v2_appsessions_id_icalogs_analyses_analysisid_stepid_stderr**](BasespaceApi.md#get_v2_appsessions_id_icalogs_analyses_analysisid_stepid_stderr) | **GET** /appsessions/{id}/icalogs/analyses/{analysisid}/{stepid}/stderr | Get ICA analysis step stderr log
[**get_v2_appsessions_id_icalogs_analyses_analysisid_stepid_stdout**](BasespaceApi.md#get_v2_appsessions_id_icalogs_analyses_analysisid_stepid_stdout) | **GET** /appsessions/{id}/icalogs/analyses/{analysisid}/{stepid}/stdout | Get ICA analysis step stdout log
[**get_v2_appsessions_id_icalogs_analyses_icaanalysisid**](BasespaceApi.md#get_v2_appsessions_id_icalogs_analyses_icaanalysisid) | **GET** /appsessions/{id}/icalogs/analyses/{icaanalysisid} | Get ICA analysis log steps
[**get_v2_appsessions_id_icalogs_orchestrated_analyses**](BasespaceApi.md#get_v2_appsessions_id_icalogs_orchestrated_analyses) | **GET** /appsessions/{id}/icalogs/orchestrated-analyses | Get orchestrated analyses
[**get_v2_appsessions_id_icalogs_workflowsession**](BasespaceApi.md#get_v2_appsessions_id_icalogs_workflowsession) | **GET** /appsessions/{id}/icalogs/workflowsession | Get ICA workflow session log steps
[**get_v2_appsessions_id_icalogs_workflowsession_stepid**](BasespaceApi.md#get_v2_appsessions_id_icalogs_workflowsession_stepid) | **GET** /appsessions/{id}/icalogs/workflowsession/{stepid} | Get ICA workflow session log step stdout stderr log paths
[**get_v2_appsessions_id_icalogs_workflowsession_stepid_stderr**](BasespaceApi.md#get_v2_appsessions_id_icalogs_workflowsession_stepid_stderr) | **GET** /appsessions/{id}/icalogs/workflowsession/{stepid}/stderr | Get ICA workflow session log step stderr
[**get_v2_appsessions_id_icalogs_workflowsession_stepid_stdout**](BasespaceApi.md#get_v2_appsessions_id_icalogs_workflowsession_stepid_stdout) | **GET** /appsessions/{id}/icalogs/workflowsession/{stepid}/stdout | Get ICA workflow session log step stdout
[**get_v2_appsessions_id_logfiles**](BasespaceApi.md#get_v2_appsessions_id_logfiles) | **GET** /appsessions/{id}/logfiles | Get a list of logs of an analysis
[**get_v2_appsessions_id_properties**](BasespaceApi.md#get_v2_appsessions_id_properties) | **GET** /appsessions/{id}/properties | Get a list of properties of an analysis
[**get_v2_appsessions_id_properties_name**](BasespaceApi.md#get_v2_appsessions_id_properties_name) | **GET** /appsessions/{id}/properties/{name} | Get information about a property of an analysis
[**get_v2_appsessions_id_properties_name_items**](BasespaceApi.md#get_v2_appsessions_id_properties_name_items) | **GET** /appsessions/{id}/properties/{name}/items | Get a list of items from a property of an analysis
[**get_v2_appsessions_id_reports**](BasespaceApi.md#get_v2_appsessions_id_reports) | **GET** /appsessions/{id}/reports |
[**get_v2_archivingstats**](BasespaceApi.md#get_v2_archivingstats) | **GET** /archivingstats | Get a summary of total archiving Data Managment Events , their status  .
[**get_v2_archivingstatsdetails**](BasespaceApi.md#get_v2_archivingstatsdetails) | **GET** /archivingstatsdetails | Get list of archiving Data Managment Events , their status  .
[**get_v2_autodeletionevents**](BasespaceApi.md#get_v2_autodeletionevents) | **GET** /autodeletionevents | Get a list of all auto-deletion events.
[**get_v2_autodeletionpipeline**](BasespaceApi.md#get_v2_autodeletionpipeline) | **GET** /autodeletionpipeline | Get the list of users who have entered the auto-deletion pipeline due to inactivity or exceeding their storage limit.
[**get_v2_autodeletionusers**](BasespaceApi.md#get_v2_autodeletionusers) | **GET** /autodeletionusers | Get a summary of users who are about to have their account data deleted due to data retention policy.
[**get_v2_biosamples**](BasespaceApi.md#get_v2_biosamples) | **GET** /biosamples | Get a list of biosamples
[**get_v2_biosamples_biosampleid_labrequeues**](BasespaceApi.md#get_v2_biosamples_biosampleid_labrequeues) | **GET** /biosamples/{biosampleid}/labrequeues | Get a list of a biosample�s lab requeues
[**get_v2_biosamples_id**](BasespaceApi.md#get_v2_biosamples_id) | **GET** /biosamples/{id} | Get information about a biosample
[**get_v2_biosamples_id_aggregatedfastqdatasets**](BasespaceApi.md#get_v2_biosamples_id_aggregatedfastqdatasets) | **GET** /biosamples/{id}/aggregatedfastqdatasets | Get aggregated datasets for a given biosample
[**get_v2_biosamples_id_libraries**](BasespaceApi.md#get_v2_biosamples_id_libraries) | **GET** /biosamples/{id}/libraries | Get a list of a biosample�s libraries
[**get_v2_biosamples_id_properties**](BasespaceApi.md#get_v2_biosamples_id_properties) | **GET** /biosamples/{id}/properties |
[**get_v2_biosamples_id_properties_name**](BasespaceApi.md#get_v2_biosamples_id_properties_name) | **GET** /biosamples/{id}/properties/{name} |
[**get_v2_biosamples_id_properties_name_items**](BasespaceApi.md#get_v2_biosamples_id_properties_name_items) | **GET** /biosamples/{id}/properties/{name}/items |
[**get_v2_biosamples_id_runlanesummaries**](BasespaceApi.md#get_v2_biosamples_id_runlanesummaries) | **GET** /biosamples/{id}/runlanesummaries | Get information about biosample’s lane mapping
[**get_v2_datasets**](BasespaceApi.md#get_v2_datasets) | **GET** /datasets | Get a list of datasets
[**get_v2_datasets_id**](BasespaceApi.md#get_v2_datasets_id) | **GET** /datasets/{id} | Get information about a dataset
[**get_v2_datasets_id_comments**](BasespaceApi.md#get_v2_datasets_id_comments) | **GET** /datasets/{id}/comments | Get a list of comments made about a dataset
[**get_v2_datasets_id_direct_upload_info**](BasespaceApi.md#get_v2_datasets_id_direct_upload_info) | **GET** /datasets/{id}/direct-upload-info |
[**get_v2_datasets_id_file_upload_info**](BasespaceApi.md#get_v2_datasets_id_file_upload_info) | **GET** /datasets/{id}/file-upload-info |
[**get_v2_datasets_id_files**](BasespaceApi.md#get_v2_datasets_id_files) | **GET** /datasets/{id}/files | Get a list of files of a dataset
[**get_v2_datasets_id_properties**](BasespaceApi.md#get_v2_datasets_id_properties) | **GET** /datasets/{id}/properties |
[**get_v2_datasets_id_properties_name**](BasespaceApi.md#get_v2_datasets_id_properties_name) | **GET** /datasets/{id}/properties/{name} |
[**get_v2_datasets_id_properties_name_items**](BasespaceApi.md#get_v2_datasets_id_properties_name_items) | **GET** /datasets/{id}/properties/{name}/items |
[**get_v2_datasettypes_id**](BasespaceApi.md#get_v2_datasettypes_id) | **GET** /datasettypes/{id} | Get information about a dataset type
[**get_v2_gdssharetransferstats**](BasespaceApi.md#get_v2_gdssharetransferstats) | **GET** /gdssharetransferstats | Get a summary of GDS share or transfer operations.
[**get_v2_instrumentconnectioncheck_file_upload_info**](BasespaceApi.md#get_v2_instrumentconnectioncheck_file_upload_info) | **GET** /instrumentconnectioncheck/file-upload-info |
[**get_v2_instrumentdiagnostics_id**](BasespaceApi.md#get_v2_instrumentdiagnostics_id) | **GET** /instrumentdiagnostics/{id} |
[**get_v2_instruments**](BasespaceApi.md#get_v2_instruments) | **GET** /instruments |
[**get_v2_instrumentstatistics**](BasespaceApi.md#get_v2_instrumentstatistics) | **GET** /instrumentstatistics | Get instrument statistics
[**get_v2_instrumentstatus**](BasespaceApi.md#get_v2_instrumentstatus) | **GET** /instrumentstatus |
[**get_v2_labrequeues**](BasespaceApi.md#get_v2_labrequeues) | **GET** /labrequeues | Get a list of lab requeues
[**get_v2_labrequeues_id**](BasespaceApi.md#get_v2_labrequeues_id) | **GET** /labrequeues/{id} | Get information about a specific labrequeue
[**get_v2_laneqcthresholds**](BasespaceApi.md#get_v2_laneqcthresholds) | **GET** /laneqcthresholds | Get a list of QC thresholds applied to lanes
[**get_v2_lanes_id**](BasespaceApi.md#get_v2_lanes_id) | **GET** /lanes/{id} | Get information about a lane
[**get_v2_lanes_id_comments**](BasespaceApi.md#get_v2_lanes_id_comments) | **GET** /lanes/{id}/comments | Get a list of comments on a lane
[**get_v2_libraries**](BasespaceApi.md#get_v2_libraries) | **GET** /libraries | Get a list of libraries
[**get_v2_libraries_id_properties**](BasespaceApi.md#get_v2_libraries_id_properties) | **GET** /libraries/{id}/properties |
[**get_v2_libraries_id_properties_name**](BasespaceApi.md#get_v2_libraries_id_properties_name) | **GET** /libraries/{id}/properties/{name} |
[**get_v2_libraries_id_properties_name_items**](BasespaceApi.md#get_v2_libraries_id_properties_name_items) | **GET** /libraries/{id}/properties/{name}/items |
[**get_v2_librarypools**](BasespaceApi.md#get_v2_librarypools) | **GET** /librarypools | Get a list of library pools
[**get_v2_librarypools_id_libraries**](BasespaceApi.md#get_v2_librarypools_id_libraries) | **GET** /librarypools/{id}/libraries | Get a list of libraries of a pool
[**get_v2_librarypools_id_properties**](BasespaceApi.md#get_v2_librarypools_id_properties) | **GET** /librarypools/{id}/properties |
[**get_v2_librarypools_id_properties_name**](BasespaceApi.md#get_v2_librarypools_id_properties_name) | **GET** /librarypools/{id}/properties/{name} |
[**get_v2_librarypools_id_properties_name_items**](BasespaceApi.md#get_v2_librarypools_id_properties_name_items) | **GET** /librarypools/{id}/properties/{name}/items |
[**get_v2_projects_id**](BasespaceApi.md#get_v2_projects_id) | **GET** /projects/{id} | Get information about a project
[**get_v2_projects_id_datasets**](BasespaceApi.md#get_v2_projects_id_datasets) | **GET** /projects/{id}/datasets | Get a list of datasets in a project
[**get_v2_projects_id_properties**](BasespaceApi.md#get_v2_projects_id_properties) | **GET** /projects/{id}/properties |
[**get_v2_projects_id_properties_name**](BasespaceApi.md#get_v2_projects_id_properties_name) | **GET** /projects/{id}/properties/{name} |
[**get_v2_projects_id_properties_name_items**](BasespaceApi.md#get_v2_projects_id_properties_name_items) | **GET** /projects/{id}/properties/{name}/items |
[**get_v2_resourcemanifest**](BasespaceApi.md#get_v2_resourcemanifest) | **GET** /resourcemanifest | Get a manifest of filesets for the requested resources (max 300 items)
[**get_v2_runs**](BasespaceApi.md#get_v2_runs) | **GET** /runs | Get a list of runs accessible by current user
[**get_v2_runs_accesscheck**](BasespaceApi.md#get_v2_runs_accesscheck) | **GET** /runs/accesscheck |
[**get_v2_runs_id**](BasespaceApi.md#get_v2_runs_id) | **GET** /runs/{id} | Get information about a run
[**get_v2_runs_id_file_upload_info**](BasespaceApi.md#get_v2_runs_id_file_upload_info) | **GET** /runs/{id}/file-upload-info |
[**get_v2_runs_id_files**](BasespaceApi.md#get_v2_runs_id_files) | **GET** /runs/{id}/files | Get a list of files of a run
[**get_v2_runs_id_properties**](BasespaceApi.md#get_v2_runs_id_properties) | **GET** /runs/{id}/properties |
[**get_v2_runs_id_properties_name**](BasespaceApi.md#get_v2_runs_id_properties_name) | **GET** /runs/{id}/properties/{name} |
[**get_v2_runs_id_properties_name_items**](BasespaceApi.md#get_v2_runs_id_properties_name_items) | **GET** /runs/{id}/properties/{name}/items |
[**get_v2_runs_id_samplesheet**](BasespaceApi.md#get_v2_runs_id_samplesheet) | **GET** /runs/{id}/samplesheet |
[**get_v2_runs_id_sequencingstats**](BasespaceApi.md#get_v2_runs_id_sequencingstats) | **GET** /runs/{id}/sequencingstats |
[**get_v2_runuploadtest**](BasespaceApi.md#get_v2_runuploadtest) | **GET** /runuploadtest |
[**get_v2_samples_id_file_upload_info**](BasespaceApi.md#get_v2_samples_id_file_upload_info) | **GET** /samples/{id}/file-upload-info |
[**get_v2_subjects_id_properties**](BasespaceApi.md#get_v2_subjects_id_properties) | **GET** /subjects/{id}/properties |
[**get_v2_subjects_id_properties_name**](BasespaceApi.md#get_v2_subjects_id_properties_name) | **GET** /subjects/{id}/properties/{name} |
[**get_v2_subjects_id_properties_name_items**](BasespaceApi.md#get_v2_subjects_id_properties_name_items) | **GET** /subjects/{id}/properties/{name}/items |
[**get_v2_trash**](BasespaceApi.md#get_v2_trash) | **GET** /trash | Get a list of items in the trash
[**get_v2_trash_id**](BasespaceApi.md#get_v2_trash_id) | **GET** /trash/{id} | Get information about an item in the trash
[**get_v2_useragreements**](BasespaceApi.md#get_v2_useragreements) | **GET** /useragreements/ | Get information about agreements visible to the current user
[**get_v2_users_current**](BasespaceApi.md#get_v2_users_current) | **GET** /users/current | Get information about the current user&#x27;s account
[**get_v2_users_current_labtype**](BasespaceApi.md#get_v2_users_current_labtype) | **GET** /users/current/labtype | Is user a wet lab or dry lab user?
[**get_v2_users_current_messages**](BasespaceApi.md#get_v2_users_current_messages) | **GET** /users/current/messages | Get a list of messages that have been sent to the requesting user.
[**get_v2_users_current_notifications**](BasespaceApi.md#get_v2_users_current_notifications) | **GET** /users/current/notifications |
[**get_v2_users_current_properties**](BasespaceApi.md#get_v2_users_current_properties) | **GET** /users/current/properties |
[**get_v2_users_current_properties_name**](BasespaceApi.md#get_v2_users_current_properties_name) | **GET** /users/current/properties/{name} |
[**get_v2_users_current_properties_name_items**](BasespaceApi.md#get_v2_users_current_properties_name_items) | **GET** /users/current/properties/{name}/items |
[**get_v2_users_current_subscription**](BasespaceApi.md#get_v2_users_current_subscription) | **GET** /users/current/subscription | Get information about the current user�s subscriptions
[**get_v2_users_current_usage**](BasespaceApi.md#get_v2_users_current_usage) | **GET** /users/current/usage | Get usage statistics for the user
[**get_v2_users_id**](BasespaceApi.md#get_v2_users_id) | **GET** /users/{id} | Get information about a user
[**get_v2_users_id_autodeletionevents**](BasespaceApi.md#get_v2_users_id_autodeletionevents) | **GET** /users/{id}/autodeletionevents | Get a list of auto-deletion events for the specified user.
[**get_v2_users_id_messages**](BasespaceApi.md#get_v2_users_id_messages) | **GET** /users/{id}/messages | Get a list of messages that have been sent to a specific user.
[**get_v2_users_id_notifications**](BasespaceApi.md#get_v2_users_id_notifications) | **GET** /users/{id}/notifications |
[**get_v2_users_id_settings**](BasespaceApi.md#get_v2_users_id_settings) | **GET** /users/{id}/settings | Get a list of the user&#x27;s settings
[**get_v2_users_id_subscription**](BasespaceApi.md#get_v2_users_id_subscription) | **GET** /users/{id}/subscription | Get information about a user&#x27;s subscriptions
[**get_v2_users_id_workgroups**](BasespaceApi.md#get_v2_users_id_workgroups) | **GET** /users/{id}/workgroups | Get a list of workgroups the user belongs to
[**get_v2_v2migration_status_stepname**](BasespaceApi.md#get_v2_v2migration_status_stepname) | **GET** migration/status/{stepname} | Get status report on migration
[**get_v2_workgroups_id**](BasespaceApi.md#get_v2_workgroups_id) | **GET** /workgroups/{id} | Get information about a workgroup
[**post_v2_applications_id_workflows**](BasespaceApi.md#post_v2_applications_id_workflows) | **POST** /applications/{id}/workflows | Create or update an analysis workflow
[**post_v2_appresults_id_file_upload_info**](BasespaceApi.md#post_v2_appresults_id_file_upload_info) | **POST** /appresults/{id}/file-upload-info |
[**post_v2_appsessions**](BasespaceApi.md#post_v2_appsessions) | **POST** /appsessions | Create a new interactive AppSession with ExecutionStatus Running
[**post_v2_appsessions_id**](BasespaceApi.md#post_v2_appsessions_id) | **POST** /appsessions/{id} | Update an analysis
[**post_v2_appsessions_id_logfiles**](BasespaceApi.md#post_v2_appsessions_id_logfiles) | **POST** /appsessions/{id}/logfiles | Add a log file to a specific analysis
[**post_v2_appsessions_id_properties**](BasespaceApi.md#post_v2_appsessions_id_properties) | **POST** /appsessions/{id}/properties | Add or update properties of an analysis
[**post_v2_appsessions_id_reschedule**](BasespaceApi.md#post_v2_appsessions_id_reschedule) | **POST** /appsessions/{id}/reschedule | Reschedule a workflow
[**post_v2_appsessions_id_stop**](BasespaceApi.md#post_v2_appsessions_id_stop) | **POST** /appsessions/{id}/stop | Stop an analysis from running
[**post_v2_appsessions_track**](BasespaceApi.md#post_v2_appsessions_track) | **POST** /appsessions/track | Track ICA analyses
[**post_v2_appsessions_workflowsessions_track**](BasespaceApi.md#post_v2_appsessions_workflowsessions_track) | **POST** /appsessions/workflowsessions/track | Track workflow sessions
[**post_v2_archive**](BasespaceApi.md#post_v2_archive) | **POST** /archive | Bulk archive.
[**post_v2_biosamples**](BasespaceApi.md#post_v2_biosamples) | **POST** /biosamples |
[**post_v2_biosamples_bulkupdate**](BasespaceApi.md#post_v2_biosamples_bulkupdate) | **POST** /biosamples/bulkupdate | Update the default project of many biosamples
[**post_v2_biosamples_id**](BasespaceApi.md#post_v2_biosamples_id) | **POST** /biosamples/{id} | Update a Biosample
[**post_v2_biosamples_id_aggregation**](BasespaceApi.md#post_v2_biosamples_id_aggregation) | **POST** /biosamples/{id}/aggregation | Update Biosample aggregation
[**post_v2_biosamples_id_libraries**](BasespaceApi.md#post_v2_biosamples_id_libraries) | **POST** /biosamples/{id}/libraries | Create a library for a biosample
[**post_v2_datacompress**](BasespaceApi.md#post_v2_datacompress) | **POST** /datacompress | Bulk Data Compression.
[**post_v2_datasets**](BasespaceApi.md#post_v2_datasets) | **POST** /datasets | Create a dataset that doesn&#x27;t belong in a specific project
[**post_v2_datasets_id**](BasespaceApi.md#post_v2_datasets_id) | **POST** /datasets/{id} | Update an existing dataset
[**post_v2_datasets_id_copy**](BasespaceApi.md#post_v2_datasets_id_copy) | **POST** /datasets/{id}/copy | Copy a dataset to a project
[**post_v2_datasets_id_direct_upload_info**](BasespaceApi.md#post_v2_datasets_id_direct_upload_info) | **POST** /datasets/{id}/direct-upload-info |
[**post_v2_datasets_id_file_upload_info**](BasespaceApi.md#post_v2_datasets_id_file_upload_info) | **POST** /datasets/{id}/file-upload-info |
[**post_v2_datasets_id_files**](BasespaceApi.md#post_v2_datasets_id_files) | **POST** /datasets/{id}/files |
[**post_v2_icadownloads_create_download_url**](BasespaceApi.md#post_v2_icadownloads_create_download_url) | **POST** /icadownloads/create-download-url |
[**post_v2_icauploads_foldertype_complete_upload**](BasespaceApi.md#post_v2_icauploads_foldertype_complete_upload) | **POST** /icauploads/{foldertype}/complete-upload |
[**post_v2_icauploads_foldertype_direct_upload_info**](BasespaceApi.md#post_v2_icauploads_foldertype_direct_upload_info) | **POST** /icauploads/{foldertype}/direct-upload-info |
[**post_v2_instrumentdiagnostics**](BasespaceApi.md#post_v2_instrumentdiagnostics) | **POST** /instrumentdiagnostics |
[**post_v2_instrumentdiagnostics_id**](BasespaceApi.md#post_v2_instrumentdiagnostics_id) | **POST** /instrumentdiagnostics/{id} |
[**post_v2_instruments_errors**](BasespaceApi.md#post_v2_instruments_errors) | **POST** /instruments/errors |
[**post_v2_lanes_id**](BasespaceApi.md#post_v2_lanes_id) | **POST** /lanes/{id} | Update a lane
[**post_v2_libraries_libraryid_labrequeues**](BasespaceApi.md#post_v2_libraries_libraryid_labrequeues) | **POST** /libraries/{libraryid}/labrequeues | Add a lab requeue request for more yield from a library
[**post_v2_librarypools_id**](BasespaceApi.md#post_v2_librarypools_id) | **POST** /librarypools/{id} | Update a pool
[**post_v2_librarypools_poolid_labrequeues**](BasespaceApi.md#post_v2_librarypools_poolid_labrequeues) | **POST** /librarypools/{poolid}/labrequeues | Add a lab requeue request for more yield from a pool
[**post_v2_oauthv1_tokenfromoauthv2**](BasespaceApi.md#post_v2_oauthv1_tokenfromoauthv2) | **POST** /oauthv1/tokenfromoauthv2 |
[**post_v2_oauthv2_token**](BasespaceApi.md#post_v2_oauthv2_token) | **POST** /oauthv2/token |
[**post_v2_oauthv2_tokenfromapplicationjwt**](BasespaceApi.md#post_v2_oauthv2_tokenfromapplicationjwt) | **POST** /oauthv2/tokenfromapplicationjwt |
[**post_v2_oauthv2tokens_userid**](BasespaceApi.md#post_v2_oauthv2tokens_userid) | **POST** /oauthv2tokens/{userid} |
[**post_v2_preprequests_preprequestid_labrequeues**](BasespaceApi.md#post_v2_preprequests_preprequestid_labrequeues) | **POST** /preprequests/{preprequestid}/labrequeues | Add a lab requeue request for more yield from a biosample
[**post_v2_projects**](BasespaceApi.md#post_v2_projects) | **POST** /projects | Create a project by name
[**post_v2_projects_id_datasets**](BasespaceApi.md#post_v2_projects_id_datasets) | **POST** /projects/{id}/datasets | Create a dataset within a specific project
[**post_v2_publishappsessionstatus**](BasespaceApi.md#post_v2_publishappsessionstatus) | **POST** /publishappsessionstatus |
[**post_v2_restore**](BasespaceApi.md#post_v2_restore) | **POST** /restore | Bulk restore.
[**post_v2_runs**](BasespaceApi.md#post_v2_runs) | **POST** /runs | Create a new run
[**post_v2_runs_id**](BasespaceApi.md#post_v2_runs_id) | **POST** /runs/{id} | Update an existing run
[**post_v2_runs_id_file_upload_info**](BasespaceApi.md#post_v2_runs_id_file_upload_info) | **POST** /runs/{id}/file-upload-info |
[**post_v2_runs_id_files**](BasespaceApi.md#post_v2_runs_id_files) | **POST** /runs/{id}/files |
[**post_v2_runs_start**](BasespaceApi.md#post_v2_runs_start) | **POST** /runs/start | Create a new run using GSS
[**post_v2_samples_id_file_upload_info**](BasespaceApi.md#post_v2_samples_id_file_upload_info) | **POST** /samples/{id}/file-upload-info |
[**post_v2_tokens_instruments**](BasespaceApi.md#post_v2_tokens_instruments) | **POST** /tokens/instruments | Creates a Platform JWT token for an instrument
[**post_v2_trash_id_restorefromtrash**](BasespaceApi.md#post_v2_trash_id_restorefromtrash) | **POST** /trash/{id}/restorefromtrash | Restore an item from the trash back to its active state
[**post_v2_unzip**](BasespaceApi.md#post_v2_unzip) | **POST** /unzip | Bulk Unzip.
[**post_v2_useraccounttransfer**](BasespaceApi.md#post_v2_useraccounttransfer) | **POST** /useraccounttransfer | User account transfer. Requires Administrator role
[**post_v2_useragreements**](BasespaceApi.md#post_v2_useragreements) | **POST** /useragreements/ |
[**post_v2_users_current**](BasespaceApi.md#post_v2_users_current) | **POST** /users/current |
[**post_v2_users_files**](BasespaceApi.md#post_v2_users_files) | **POST** /users/files | Upload a file to the user&#x27;s volume in GDS
[**post_v2_users_id_settings**](BasespaceApi.md#post_v2_users_id_settings) | **POST** /users/{id}/settings | Update the user&#x27;s settings
[**post_v2_users_id_v2analysisconfigtemplate**](BasespaceApi.md#post_v2_users_id_v2analysisconfigtemplate) | **POST** /users/{id}analysisconfigtemplate | Change Analysis Configuration Template Feature Enabled for calling user
[**post_v2_users_id_v2biosampleregistry**](BasespaceApi.md#post_v2_users_id_v2biosampleregistry) | **POST** /users/{id}biosampleregistry | Change V2 BioSample Registry Enabled for calling user
[**post_v2_validatesignedurl**](BasespaceApi.md#post_v2_validatesignedurl) | **POST** /validatesignedurl |
[**put_v2_applications_id_qcthresholds**](BasespaceApi.md#put_v2_applications_id_qcthresholds) | **PUT** /applications/{id}/qcthresholds | Add or update the QC thresholds applied to an analysis workflow
[**put_v2_applications_id_workflowdependencies**](BasespaceApi.md#put_v2_applications_id_workflowdependencies) | **PUT** /applications/{id}/workflowdependencies | Add or update the workflow dependencies of an analysis workflow
[**put_v2_laneqcthresholds**](BasespaceApi.md#put_v2_laneqcthresholds) | **PUT** /laneqcthresholds | Add or update the QC thresholds applied to lanes
[**put_v2_notifications_dismiss**](BasespaceApi.md#put_v2_notifications_dismiss) | **PUT** /notifications/dismiss | Dismiss a user notification.

# **delete_v2_appsessions_id**
> V1pre3TrashItem delete_v2_appsessions_id(id, preserve=preserve, bypasstrash=bypasstrash)

Delete a specific analysis

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | Appsession ID
preserve = 'preserve_example' # str | Preserve \"Metadata\", to keep records, but not files, of an appsession (optional)
bypasstrash = true # bool | Select true to go straight to deletion (optional)

try:
    # Delete a specific analysis
    api_response = api_instance.delete_v2_appsessions_id(id, preserve=preserve, bypasstrash=bypasstrash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->delete_v2_appsessions_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Appsession ID |
 **preserve** | **str**| Preserve \&quot;Metadata\&quot;, to keep records, but not files, of an appsession | [optional]
 **bypasstrash** | **bool**| Select true to go straight to deletion | [optional]

### Return type

[**V1pre3TrashItem**](V1pre3TrashItem.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_v2_appsessions_id_properties_name**
> delete_v2_appsessions_id_properties_name(id, name)

Delete a property of an analysis

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | Appsession ID
name = 'name_example' # str | Property name

try:
    # Delete a property of an analysis
    api_instance.delete_v2_appsessions_id_properties_name(id, name)
except ApiException as e:
    print("Exception when calling BasespaceApi->delete_v2_appsessions_id_properties_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Appsession ID |
 **name** | **str**| Property name |

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_v2_icauploads_foldertype_dataid**
> V2Error delete_v2_icauploads_foldertype_dataid(foldertype, dataid)



Delete a resource in ICA

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
foldertype = 'foldertype_example' # str |
dataid = 'dataid_example' # str |

try:
    api_response = api_instance.delete_v2_icauploads_foldertype_dataid(foldertype, dataid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->delete_v2_icauploads_foldertype_dataid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **foldertype** | **str**|  |
 **dataid** | **str**|  |

### Return type

[**V2Error**](V2Error.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_v2_notifications_id**
> delete_v2_notifications_id(id)



Delete a notification

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | The Id of the resource

try:
    api_instance.delete_v2_notifications_id(id)
except ApiException as e:
    print("Exception when calling BasespaceApi->delete_v2_notifications_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of the resource |

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_v2_oauthv2tokens_current**
> delete_v2_oauthv2tokens_current()



Invalidate/delete token for a given user

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))

try:
    api_instance.delete_v2_oauthv2tokens_current()
except ApiException as e:
    print("Exception when calling BasespaceApi->delete_v2_oauthv2tokens_current: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_v2_session_invalidate**
> delete_v2_session_invalidate()

Log out user from Sequence Hub and end session

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))

try:
    # Log out user from Sequence Hub and end session
    api_instance.delete_v2_session_invalidate()
except ApiException as e:
    print("Exception when calling BasespaceApi->delete_v2_session_invalidate: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_v2_trash**
> delete_v2_trash()

Delete all items in the trash

Deleting all items from the trash is a non-reversible action. All items and their files will be removed from Sequence Hub permanently.

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))

try:
    # Delete all items in the trash
    api_instance.delete_v2_trash()
except ApiException as e:
    print("Exception when calling BasespaceApi->delete_v2_trash: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_agreements_id**
> V2Agreement get_v2_agreements_id(id)

Get detailed information about a single agreement

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | Agreement ID

try:
    # Get detailed information about a single agreement
    api_response = api_instance.get_v2_agreements_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_agreements_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Agreement ID |

### Return type

[**V2Agreement**](V2Agreement.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_applicationmetadata**
> ApplicationMetadataV2ApiResponse get_v2_applicationmetadata(id=id)

Request metadata about applications

Request metadata about applications

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | The Id of the resource (optional)

try:
    # Request metadata about applications
    api_response = api_instance.get_v2_applicationmetadata(id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_applicationmetadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of the resource | [optional]

### Return type

[**ApplicationMetadataV2ApiResponse**](ApplicationMetadataV2ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_applications**
> V1pre3ApplicationCompactList get_v2_applications(cwlactive, autolaunchableonruncompleteappsonly, allversions, category=category, references=references, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir, id=id)

Get a list of available applications

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
cwlactive = true # bool | Deprecated as of May 2024. Has no effect, but left here for API backwards compatibility.
autolaunchableonruncompleteappsonly = true # bool | Returns only applications that can be auto-launched after a run completes
allversions = true # bool | Return all the applications versions
category = 'category_example' # str | Return all apps that belong to a specific category that a user has access to (examples include: Native, Workflow, Other). Only a single category can be specified in a given call (optional)
references = 'references_example' # str | Returns all analysis workflows that a user has access to that were created from a particular app, denoted by its unique slug ID (optional)
sortby = 'sortby_example' # str | The field(s) used to sort the result set (optional)
offset = 56 # int | The starting offset to read (optional)
limit = 56 # int | The maximum number of items to return (optional)
sortdir = 'sortdir_example' # str | The sort direction for the result set (optional)
id = 'id_example' # str | The Id of the resource (optional)

try:
    # Get a list of available applications
    api_response = api_instance.get_v2_applications(cwlactive, autolaunchableonruncompleteappsonly, allversions, category=category, references=references, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir, id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_applications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cwlactive** | **bool**| Deprecated as of May 2024. Has no effect, but left here for API backwards compatibility. |
 **autolaunchableonruncompleteappsonly** | **bool**| Returns only applications that can be auto-launched after a run completes |
 **allversions** | **bool**| Return all the applications versions |
 **category** | **str**| Return all apps that belong to a specific category that a user has access to (examples include: Native, Workflow, Other). Only a single category can be specified in a given call | [optional]
 **references** | **str**| Returns all analysis workflows that a user has access to that were created from a particular app, denoted by its unique slug ID | [optional]
 **sortby** | **str**| The field(s) used to sort the result set | [optional]
 **offset** | **int**| The starting offset to read | [optional]
 **limit** | **int**| The maximum number of items to return | [optional]
 **sortdir** | **str**| The sort direction for the result set | [optional]
 **id** | **str**| The Id of the resource | [optional]

### Return type

[**V1pre3ApplicationCompactList**](V1pre3ApplicationCompactList.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_applications_id**
> V1pre3Application get_v2_applications_id(id, propertieslimit=propertieslimit, propertyitemslimit=propertyitemslimit)

Get information about an app

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str |
propertieslimit = 56 # int | Returns only the specified number of properties for the application. (optional)
propertyitemslimit = 56 # int | Returns only the specified number of property items per property for the application (optional)

try:
    # Get information about an app
    api_response = api_instance.get_v2_applications_id(id, propertieslimit=propertieslimit, propertyitemslimit=propertyitemslimit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_applications_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **propertieslimit** | **int**| Returns only the specified number of properties for the application. | [optional]
 **propertyitemslimit** | **int**| Returns only the specified number of property items per property for the application | [optional]

### Return type

[**V1pre3Application**](V1pre3Application.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_applications_id_qcthresholds**
> V2QcThresholdResponse get_v2_applications_id_qcthresholds(id)

Get a list of QC thresholds applied to an analysis workflow

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | The Id of the resource

try:
    # Get a list of QC thresholds applied to an analysis workflow
    api_response = api_instance.get_v2_applications_id_qcthresholds(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_applications_id_qcthresholds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of the resource |

### Return type

[**V2QcThresholdResponse**](V2QcThresholdResponse.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_applications_id_screenshots**
> ApplicationScreenshotsV2ApiResponse get_v2_applications_id_screenshots(id, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)

Get screenshots of an app

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | The Id of the resource
sortby = 'sortby_example' # str | The field(s) used to sort the result set (optional)
offset = 56 # int | The starting offset to read (optional)
limit = 56 # int | The maximum number of items to return (optional)
sortdir = 'sortdir_example' # str | The sort direction for the result set (optional)

try:
    # Get screenshots of an app
    api_response = api_instance.get_v2_applications_id_screenshots(id, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_applications_id_screenshots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of the resource |
 **sortby** | **str**| The field(s) used to sort the result set | [optional]
 **offset** | **int**| The starting offset to read | [optional]
 **limit** | **int**| The maximum number of items to return | [optional]
 **sortdir** | **str**| The sort direction for the result set | [optional]

### Return type

[**ApplicationScreenshotsV2ApiResponse**](ApplicationScreenshotsV2ApiResponse.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_applications_id_settings**
> V2ApplicationSettings get_v2_applications_id_settings(id)

Get the settings of an application or workflow

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | The Id of the resource

try:
    # Get the settings of an application or workflow
    api_response = api_instance.get_v2_applications_id_settings(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_applications_id_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of the resource |

### Return type

[**V2ApplicationSettings**](V2ApplicationSettings.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_applications_id_versions**
> V1pre3ApplicationCompactV1pre3ApplicationsSortFieldsV2ListResponse get_v2_applications_id_versions(id, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)

Get versions of an app

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | The Id of the resource
sortby = 'sortby_example' # str | The field(s) used to sort the result set (optional)
offset = 56 # int | The starting offset to read (optional)
limit = 56 # int | The maximum number of items to return (optional)
sortdir = 'sortdir_example' # str | The sort direction for the result set (optional)

try:
    # Get versions of an app
    api_response = api_instance.get_v2_applications_id_versions(id, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_applications_id_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of the resource |
 **sortby** | **str**| The field(s) used to sort the result set | [optional]
 **offset** | **int**| The starting offset to read | [optional]
 **limit** | **int**| The maximum number of items to return | [optional]
 **sortdir** | **str**| The sort direction for the result set | [optional]

### Return type

[**V1pre3ApplicationCompactV1pre3ApplicationsSortFieldsV2ListResponse**](V1pre3ApplicationCompactV1pre3ApplicationsSortFieldsV2ListResponse.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_applications_id_workflowdependencies**
> V2AnalysisWorkflowDependenciesResponse get_v2_applications_id_workflowdependencies(id)

Get a list of workflow dependencies on an analysis workflow

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | The Id of the resource

try:
    # Get a list of workflow dependencies on an analysis workflow
    api_response = api_instance.get_v2_applications_id_workflowdependencies(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_applications_id_workflowdependencies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of the resource |

### Return type

[**V2AnalysisWorkflowDependenciesResponse**](V2AnalysisWorkflowDependenciesResponse.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_appresults_id_file_upload_info**
> V2PresignedUrlForUpload get_v2_appresults_id_file_upload_info(id, filepath=filepath, uploadpartcount=uploadpartcount)



Request direct file upload presigned url information for a new file in the specified resource (dataset or appresult)

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | The Id of the resource
filepath = 'filepath_example' # str |  (optional)
uploadpartcount = 56 # int |  (optional)

try:
    api_response = api_instance.get_v2_appresults_id_file_upload_info(id, filepath=filepath, uploadpartcount=uploadpartcount)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_appresults_id_file_upload_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of the resource |
 **filepath** | **str**|  | [optional]
 **uploadpartcount** | **int**|  | [optional]

### Return type

[**V2PresignedUrlForUpload**](V2PresignedUrlForUpload.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_appsessions**
> V2AppSessionCompactList get_v2_appsessions(appid=appid, applicationfamilyslugs=applicationfamilyslugs, ownedbycurrentuser=ownedbycurrentuser, datemodified=datemodified, executionstatus=executionstatus, qcstatus=qcstatus, deliverystatus=deliverystatus, name=name, output_projects=output_projects, input_runs=input_runs, input_biosamples=input_biosamples, include=include, propertyfilters=propertyfilters, usercreatedby=usercreatedby, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)

Get a list of analyses

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
appid = 56 # int | Filter by ID of application used (optional)
applicationfamilyslugs = ['applicationfamilyslugs_example'] # list[str] | Filter by application family (optional)
ownedbycurrentuser = true # bool | Only include appsessions where the project has WRITE permission by the current user (optional)
datemodified = 'datemodified_example' # str |  (optional)
executionstatus = 'executionstatus_example' # str | Filter by execution status (optional)
qcstatus = 'qcstatus_example' # str | Filter by QC status (optional)
deliverystatus = 'deliverystatus_example' # str | Filter by delivery status (optional)
name = 'name_example' # str |  (optional)
output_projects = [56] # list[int] | Filter by ID of output project (optional)
input_runs = [56] # list[int] | Filter by ID of run input (optional)
input_biosamples = [56] # list[int] | Filter by ID of biosample input (optional)
include = ['include_example'] # list[str] | Additional resources to include (optional)
propertyfilters = ['propertyfilters_example'] # list[str] | Filter by appsessions include the specified property names (optional)
usercreatedby = 56 # int | ID of user who created appsession (optional)
sortby = 'sortby_example' # str | The field(s) used to sort the result set (optional)
offset = 56 # int | The starting offset to read (optional)
limit = 56 # int | The maximum number of items to return (optional)
sortdir = 'sortdir_example' # str | The sort direction for the result set (optional)

try:
    # Get a list of analyses
    api_response = api_instance.get_v2_appsessions(appid=appid, applicationfamilyslugs=applicationfamilyslugs, ownedbycurrentuser=ownedbycurrentuser, datemodified=datemodified, executionstatus=executionstatus, qcstatus=qcstatus, deliverystatus=deliverystatus, name=name, output_projects=output_projects, input_runs=input_runs, input_biosamples=input_biosamples, include=include, propertyfilters=propertyfilters, usercreatedby=usercreatedby, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_appsessions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appid** | **int**| Filter by ID of application used | [optional]
 **applicationfamilyslugs** | [**list[str]**](str.md)| Filter by application family | [optional]
 **ownedbycurrentuser** | **bool**| Only include appsessions where the project has WRITE permission by the current user | [optional]
 **datemodified** | **str**|  | [optional]
 **executionstatus** | **str**| Filter by execution status | [optional]
 **qcstatus** | **str**| Filter by QC status | [optional]
 **deliverystatus** | **str**| Filter by delivery status | [optional]
 **name** | **str**|  | [optional]
 **output_projects** | [**list[int]**](int.md)| Filter by ID of output project | [optional]
 **input_runs** | [**list[int]**](int.md)| Filter by ID of run input | [optional]
 **input_biosamples** | [**list[int]**](int.md)| Filter by ID of biosample input | [optional]
 **include** | [**list[str]**](str.md)| Additional resources to include | [optional]
 **propertyfilters** | [**list[str]**](str.md)| Filter by appsessions include the specified property names | [optional]
 **usercreatedby** | **int**| ID of user who created appsession | [optional]
 **sortby** | **str**| The field(s) used to sort the result set | [optional]
 **offset** | **int**| The starting offset to read | [optional]
 **limit** | **int**| The maximum number of items to return | [optional]
 **sortdir** | **str**| The sort direction for the result set | [optional]

### Return type

[**V2AppSessionCompactList**](V2AppSessionCompactList.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_appsessions_id**
> V2AppSession get_v2_appsessions_id(id, include=include, showhiddenitems=showhiddenitems)

Get information about an analysis

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | Appsession ID
include = ['include_example'] # list[str] | Additional resources to include (optional)
showhiddenitems = 'showhiddenitems_example' # str | ShowHiddenItems  (optional)

try:
    # Get information about an analysis
    api_response = api_instance.get_v2_appsessions_id(id, include=include, showhiddenitems=showhiddenitems)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_appsessions_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Appsession ID |
 **include** | [**list[str]**](str.md)| Additional resources to include | [optional]
 **showhiddenitems** | **str**| ShowHiddenItems  | [optional]

### Return type

[**V2AppSession**](V2AppSession.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_appsessions_id_comments**
> V2CommentList get_v2_appsessions_id_comments(id, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)

Get a list of comments made about an analysis

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | Appsession ID
sortby = 'sortby_example' # str | The field(s) used to sort the result set (optional)
offset = 56 # int | The starting offset to read (optional)
limit = 56 # int | The maximum number of items to return (optional)
sortdir = 'sortdir_example' # str | The sort direction for the result set (optional)

try:
    # Get a list of comments made about an analysis
    api_response = api_instance.get_v2_appsessions_id_comments(id, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_appsessions_id_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Appsession ID |
 **sortby** | **str**| The field(s) used to sort the result set | [optional]
 **offset** | **int**| The starting offset to read | [optional]
 **limit** | **int**| The maximum number of items to return | [optional]
 **sortdir** | **str**| The sort direction for the result set | [optional]

### Return type

[**V2CommentList**](V2CommentList.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_appsessions_id_icalogs**
> V2AppSessionIcaLogPathList get_v2_appsessions_id_icalogs(id, offset=offset, limit=limit, sortdir=sortdir)

Get ICA log steps for workflows and analyses

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | Appsession ID
offset = 56 # int | The starting offset to read (optional)
limit = 56 # int | The maximum number of items to return (optional)
sortdir = 'sortdir_example' # str | The sort direction for the result set (optional)

try:
    # Get ICA log steps for workflows and analyses
    api_response = api_instance.get_v2_appsessions_id_icalogs(id, offset=offset, limit=limit, sortdir=sortdir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_appsessions_id_icalogs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Appsession ID |
 **offset** | **int**| The starting offset to read | [optional]
 **limit** | **int**| The maximum number of items to return | [optional]
 **sortdir** | **str**| The sort direction for the result set | [optional]

### Return type

[**V2AppSessionIcaLogPathList**](V2AppSessionIcaLogPathList.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_appsessions_id_icalogs_analyses_analysisid_stepid**
> V2AppSessionIcaStepLogCompactList get_v2_appsessions_id_icalogs_analyses_analysisid_stepid(id, analysisid, stepid, offset=offset, limit=limit, sortdir=sortdir)

Get ICA analysis log step stdout stderr log paths

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | Appsession ID
analysisid = 'analysisid_example' # str | ICA Analyses Id
stepid = 'stepid_example' # str | Step ID
offset = 56 # int | The starting offset to read (optional)
limit = 56 # int | The maximum number of items to return (optional)
sortdir = 'sortdir_example' # str | The sort direction for the result set (optional)

try:
    # Get ICA analysis log step stdout stderr log paths
    api_response = api_instance.get_v2_appsessions_id_icalogs_analyses_analysisid_stepid(id, analysisid, stepid, offset=offset, limit=limit, sortdir=sortdir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_appsessions_id_icalogs_analyses_analysisid_stepid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Appsession ID |
 **analysisid** | **str**| ICA Analyses Id |
 **stepid** | **str**| Step ID |
 **offset** | **int**| The starting offset to read | [optional]
 **limit** | **int**| The maximum number of items to return | [optional]
 **sortdir** | **str**| The sort direction for the result set | [optional]

### Return type

[**V2AppSessionIcaStepLogCompactList**](V2AppSessionIcaStepLogCompactList.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_appsessions_id_icalogs_analyses_analysisid_stepid_stderr**
> V2AppSessionIcaStepLog get_v2_appsessions_id_icalogs_analyses_analysisid_stepid_stderr(id, analysisid, stepid)

Get ICA analysis step stderr log

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | Appsession ID
analysisid = 'analysisid_example' # str | ICA Analyses Id
stepid = 'stepid_example' # str | Step ID

try:
    # Get ICA analysis step stderr log
    api_response = api_instance.get_v2_appsessions_id_icalogs_analyses_analysisid_stepid_stderr(id, analysisid, stepid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_appsessions_id_icalogs_analyses_analysisid_stepid_stderr: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Appsession ID |
 **analysisid** | **str**| ICA Analyses Id |
 **stepid** | **str**| Step ID |

### Return type

[**V2AppSessionIcaStepLog**](V2AppSessionIcaStepLog.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_appsessions_id_icalogs_analyses_analysisid_stepid_stdout**
> V2AppSessionIcaStepLog get_v2_appsessions_id_icalogs_analyses_analysisid_stepid_stdout(id, analysisid, stepid)

Get ICA analysis step stdout log

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | Appsession ID
analysisid = 'analysisid_example' # str | ICA Analyses Id
stepid = 'stepid_example' # str | Step ID

try:
    # Get ICA analysis step stdout log
    api_response = api_instance.get_v2_appsessions_id_icalogs_analyses_analysisid_stepid_stdout(id, analysisid, stepid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_appsessions_id_icalogs_analyses_analysisid_stepid_stdout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Appsession ID |
 **analysisid** | **str**| ICA Analyses Id |
 **stepid** | **str**| Step ID |

### Return type

[**V2AppSessionIcaStepLog**](V2AppSessionIcaStepLog.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_appsessions_id_icalogs_analyses_icaanalysisid**
> V2AppSessionIcaStepLogCompactList get_v2_appsessions_id_icalogs_analyses_icaanalysisid(id, icaanalysisid, includetechnicalsteps, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)

Get ICA analysis log steps

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | Appsession ID
icaanalysisid = 'icaanalysisid_example' # str | ICA Analyses Id
includetechnicalsteps = true # bool | Include technical steps
sortby = 'sortby_example' # str | The field(s) used to sort the result set (optional)
offset = 56 # int | The starting offset to read (optional)
limit = 56 # int | The maximum number of items to return (optional)
sortdir = 'sortdir_example' # str | The sort direction for the result set (optional)

try:
    # Get ICA analysis log steps
    api_response = api_instance.get_v2_appsessions_id_icalogs_analyses_icaanalysisid(id, icaanalysisid, includetechnicalsteps, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_appsessions_id_icalogs_analyses_icaanalysisid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Appsession ID |
 **icaanalysisid** | **str**| ICA Analyses Id |
 **includetechnicalsteps** | **bool**| Include technical steps |
 **sortby** | **str**| The field(s) used to sort the result set | [optional]
 **offset** | **int**| The starting offset to read | [optional]
 **limit** | **int**| The maximum number of items to return | [optional]
 **sortdir** | **str**| The sort direction for the result set | [optional]

### Return type

[**V2AppSessionIcaStepLogCompactList**](V2AppSessionIcaStepLogCompactList.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_appsessions_id_icalogs_orchestrated_analyses**
> V2AppSessionIcaLogPathList get_v2_appsessions_id_icalogs_orchestrated_analyses(id, offset=offset, limit=limit, sortdir=sortdir)

Get orchestrated analyses

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | Appsession ID
offset = 56 # int | The starting offset to read (optional)
limit = 56 # int | The maximum number of items to return (optional)
sortdir = 'sortdir_example' # str | The sort direction for the result set (optional)

try:
    # Get orchestrated analyses
    api_response = api_instance.get_v2_appsessions_id_icalogs_orchestrated_analyses(id, offset=offset, limit=limit, sortdir=sortdir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_appsessions_id_icalogs_orchestrated_analyses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Appsession ID |
 **offset** | **int**| The starting offset to read | [optional]
 **limit** | **int**| The maximum number of items to return | [optional]
 **sortdir** | **str**| The sort direction for the result set | [optional]

### Return type

[**V2AppSessionIcaLogPathList**](V2AppSessionIcaLogPathList.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_appsessions_id_icalogs_workflowsession**
> V2AppSessionIcaStepLogCompactList get_v2_appsessions_id_icalogs_workflowsession(id, includetechnicalsteps, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)

Get ICA workflow session log steps

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | Appsession ID
includetechnicalsteps = true # bool | Include technical steps
sortby = 'sortby_example' # str | The field(s) used to sort the result set (optional)
offset = 56 # int | The starting offset to read (optional)
limit = 56 # int | The maximum number of items to return (optional)
sortdir = 'sortdir_example' # str | The sort direction for the result set (optional)

try:
    # Get ICA workflow session log steps
    api_response = api_instance.get_v2_appsessions_id_icalogs_workflowsession(id, includetechnicalsteps, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_appsessions_id_icalogs_workflowsession: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Appsession ID |
 **includetechnicalsteps** | **bool**| Include technical steps |
 **sortby** | **str**| The field(s) used to sort the result set | [optional]
 **offset** | **int**| The starting offset to read | [optional]
 **limit** | **int**| The maximum number of items to return | [optional]
 **sortdir** | **str**| The sort direction for the result set | [optional]

### Return type

[**V2AppSessionIcaStepLogCompactList**](V2AppSessionIcaStepLogCompactList.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_appsessions_id_icalogs_workflowsession_stepid**
> V2AppSessionIcaStepLogCompactList get_v2_appsessions_id_icalogs_workflowsession_stepid(id, stepid, offset=offset, limit=limit, sortdir=sortdir)

Get ICA workflow session log step stdout stderr log paths

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | Appsession ID
stepid = 'stepid_example' # str | Step ID
offset = 56 # int | The starting offset to read (optional)
limit = 56 # int | The maximum number of items to return (optional)
sortdir = 'sortdir_example' # str | The sort direction for the result set (optional)

try:
    # Get ICA workflow session log step stdout stderr log paths
    api_response = api_instance.get_v2_appsessions_id_icalogs_workflowsession_stepid(id, stepid, offset=offset, limit=limit, sortdir=sortdir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_appsessions_id_icalogs_workflowsession_stepid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Appsession ID |
 **stepid** | **str**| Step ID |
 **offset** | **int**| The starting offset to read | [optional]
 **limit** | **int**| The maximum number of items to return | [optional]
 **sortdir** | **str**| The sort direction for the result set | [optional]

### Return type

[**V2AppSessionIcaStepLogCompactList**](V2AppSessionIcaStepLogCompactList.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_appsessions_id_icalogs_workflowsession_stepid_stderr**
> V2AppSessionIcaStepLog get_v2_appsessions_id_icalogs_workflowsession_stepid_stderr(id, stepid)

Get ICA workflow session log step stderr

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | Appsession ID
stepid = 'stepid_example' # str | Step ID

try:
    # Get ICA workflow session log step stderr
    api_response = api_instance.get_v2_appsessions_id_icalogs_workflowsession_stepid_stderr(id, stepid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_appsessions_id_icalogs_workflowsession_stepid_stderr: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Appsession ID |
 **stepid** | **str**| Step ID |

### Return type

[**V2AppSessionIcaStepLog**](V2AppSessionIcaStepLog.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_appsessions_id_icalogs_workflowsession_stepid_stdout**
> V2AppSessionIcaStepLog get_v2_appsessions_id_icalogs_workflowsession_stepid_stdout(id, stepid)

Get ICA workflow session log step stdout

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | Appsession ID
stepid = 'stepid_example' # str | Step ID

try:
    # Get ICA workflow session log step stdout
    api_response = api_instance.get_v2_appsessions_id_icalogs_workflowsession_stepid_stdout(id, stepid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_appsessions_id_icalogs_workflowsession_stepid_stdout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Appsession ID |
 **stepid** | **str**| Step ID |

### Return type

[**V2AppSessionIcaStepLog**](V2AppSessionIcaStepLog.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_appsessions_id_logfiles**
> V2FilesList get_v2_appsessions_id_logfiles(id, excludevcfindexfolder, excludebamcoveragefolder, excludesystemfolder, excludeemptyfiles, filehrefcontentresolution, turbomode, filesetid=filesetid, extensions=extensions, excludeextensions=excludeextensions, directory=directory, includesubdirectories=includesubdirectories, statuses=statuses, pathprefix=pathprefix, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)

Get a list of logs of an analysis

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | Appsession ID
excludevcfindexfolder = true # bool | Whether to exclude VCF index folders
excludebamcoveragefolder = true # bool | Whether to exclude BAM coverage folders
excludesystemfolder = true # bool | Whether to exclude system folders
excludeemptyfiles = true # bool | Whether to exclude empty files
filehrefcontentresolution = true # bool | Resolves the HrefContent to the direct file URI to avoid a hop to GET: files/{id}/content
turbomode = true # bool |
filesetid = 'filesetid_example' # str |  (optional)
extensions = 'extensions_example' # str | Filter by file extension (optional)
excludeextensions = 'excludeextensions_example' # str | Exclude by file extension (optional)
directory = 'directory_example' # str | Filter by directory path (root is /) (optional)
includesubdirectories = true # bool | Whether to return subdirectories (optional)
statuses = ['statuses_example'] # list[str] | Optionally filter by status (default complete) (optional)
pathprefix = 'pathprefix_example' # str | To be pre-fixed in the path of the file (optional)
sortby = 'sortby_example' # str | The field(s) used to sort the result set (optional)
offset = 56 # int | The starting offset to read (optional)
limit = 56 # int | The maximum number of items to return (optional)
sortdir = 'sortdir_example' # str | The sort direction for the result set (optional)

try:
    # Get a list of logs of an analysis
    api_response = api_instance.get_v2_appsessions_id_logfiles(id, excludevcfindexfolder, excludebamcoveragefolder, excludesystemfolder, excludeemptyfiles, filehrefcontentresolution, turbomode, filesetid=filesetid, extensions=extensions, excludeextensions=excludeextensions, directory=directory, includesubdirectories=includesubdirectories, statuses=statuses, pathprefix=pathprefix, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_appsessions_id_logfiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Appsession ID |
 **excludevcfindexfolder** | **bool**| Whether to exclude VCF index folders |
 **excludebamcoveragefolder** | **bool**| Whether to exclude BAM coverage folders |
 **excludesystemfolder** | **bool**| Whether to exclude system folders |
 **excludeemptyfiles** | **bool**| Whether to exclude empty files |
 **filehrefcontentresolution** | **bool**| Resolves the HrefContent to the direct file URI to avoid a hop to GET: files/{id}/content |
 **turbomode** | **bool**|  |
 **filesetid** | **str**|  | [optional]
 **extensions** | **str**| Filter by file extension | [optional]
 **excludeextensions** | **str**| Exclude by file extension | [optional]
 **directory** | **str**| Filter by directory path (root is /) | [optional]
 **includesubdirectories** | **bool**| Whether to return subdirectories | [optional]
 **statuses** | [**list[str]**](str.md)| Optionally filter by status (default complete) | [optional]
 **pathprefix** | **str**| To be pre-fixed in the path of the file | [optional]
 **sortby** | **str**| The field(s) used to sort the result set | [optional]
 **offset** | **int**| The starting offset to read | [optional]
 **limit** | **int**| The maximum number of items to return | [optional]
 **sortdir** | **str**| The sort direction for the result set | [optional]

### Return type

[**V2FilesList**](V2FilesList.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_appsessions_id_properties**
> V2PropertyCompactList get_v2_appsessions_id_properties(id, propertieslimit=propertieslimit, propertyitemslimit=propertyitemslimit, propertyfilters=propertyfilters, showhiddenitems=showhiddenitems, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)

Get a list of properties of an analysis

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | Appsession ID
propertieslimit = 56 # int | Limit the # of properties returned (optional)
propertyitemslimit = 56 # int | Limit the # of property items returned per property (optional)
propertyfilters = ['propertyfilters_example'] # list[str] | Filter by property name (optional)
showhiddenitems = 'showhiddenitems_example' # str | Show Hidden projects and Datasets (optional)
sortby = 'sortby_example' # str | The field(s) used to sort the result set (optional)
offset = 56 # int | The starting offset to read (optional)
limit = 56 # int | The maximum number of items to return (optional)
sortdir = 'sortdir_example' # str | The sort direction for the result set (optional)

try:
    # Get a list of properties of an analysis
    api_response = api_instance.get_v2_appsessions_id_properties(id, propertieslimit=propertieslimit, propertyitemslimit=propertyitemslimit, propertyfilters=propertyfilters, showhiddenitems=showhiddenitems, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_appsessions_id_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Appsession ID |
 **propertieslimit** | **int**| Limit the # of properties returned | [optional]
 **propertyitemslimit** | **int**| Limit the # of property items returned per property | [optional]
 **propertyfilters** | [**list[str]**](str.md)| Filter by property name | [optional]
 **showhiddenitems** | **str**| Show Hidden projects and Datasets | [optional]
 **sortby** | **str**| The field(s) used to sort the result set | [optional]
 **offset** | **int**| The starting offset to read | [optional]
 **limit** | **int**| The maximum number of items to return | [optional]
 **sortdir** | **str**| The sort direction for the result set | [optional]

### Return type

[**V2PropertyCompactList**](V2PropertyCompactList.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_appsessions_id_properties_name**
> V2Property get_v2_appsessions_id_properties_name(id, name, propertyitemslimit=propertyitemslimit, showhiddenitems=showhiddenitems)

Get information about a property of an analysis

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | Appsession ID
name = 'name_example' # str | Property name
propertyitemslimit = 56 # int | Limit the # of property items returned per property (optional)
showhiddenitems = 'showhiddenitems_example' # str | Hidden filter (optional)

try:
    # Get information about a property of an analysis
    api_response = api_instance.get_v2_appsessions_id_properties_name(id, name, propertyitemslimit=propertyitemslimit, showhiddenitems=showhiddenitems)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_appsessions_id_properties_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Appsession ID |
 **name** | **str**| Property name |
 **propertyitemslimit** | **int**| Limit the # of property items returned per property | [optional]
 **showhiddenitems** | **str**| Hidden filter | [optional]

### Return type

[**V2Property**](V2Property.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_appsessions_id_properties_name_items**
> V2PropertyItemList get_v2_appsessions_id_properties_name_items(id, name, showhiddenitems=showhiddenitems, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)

Get a list of items from a property of an analysis

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | Appsession ID
name = 'name_example' # str | Property name
showhiddenitems = 'showhiddenitems_example' # str | Hidden filter (optional)
sortby = 'sortby_example' # str | The field(s) used to sort the result set (optional)
offset = 56 # int | The starting offset to read (optional)
limit = 56 # int | The maximum number of items to return (optional)
sortdir = 'sortdir_example' # str | The sort direction for the result set (optional)

try:
    # Get a list of items from a property of an analysis
    api_response = api_instance.get_v2_appsessions_id_properties_name_items(id, name, showhiddenitems=showhiddenitems, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_appsessions_id_properties_name_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Appsession ID |
 **name** | **str**| Property name |
 **showhiddenitems** | **str**| Hidden filter | [optional]
 **sortby** | **str**| The field(s) used to sort the result set | [optional]
 **offset** | **int**| The starting offset to read | [optional]
 **limit** | **int**| The maximum number of items to return | [optional]
 **sortdir** | **str**| The sort direction for the result set | [optional]

### Return type

[**V2PropertyItemList**](V2PropertyItemList.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_appsessions_id_reports**
> V2Error get_v2_appsessions_id_reports(id)



### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | Appsession ID

try:
    api_response = api_instance.get_v2_appsessions_id_reports(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_appsessions_id_reports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Appsession ID |

### Return type

[**V2Error**](V2Error.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_archivingstats**
> V2Error get_v2_archivingstats(eventaction=eventaction)

Get a summary of total archiving Data Managment Events , their status  .

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
eventaction = 'eventaction_example' # str |  (optional)

try:
    # Get a summary of total archiving Data Managment Events , their status  .
    api_response = api_instance.get_v2_archivingstats(eventaction=eventaction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_archivingstats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **eventaction** | **str**|  | [optional]

### Return type

[**V2Error**](V2Error.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_archivingstatsdetails**
> V2Error get_v2_archivingstatsdetails(sortby=sortby, offset=offset, limit=limit, sortdir=sortdir, id=id)

Get list of archiving Data Managment Events , their status  .

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
sortby = 'sortby_example' # str | The field(s) used to sort the result set (optional)
offset = 56 # int | The starting offset to read (optional)
limit = 56 # int | The maximum number of items to return (optional)
sortdir = 'sortdir_example' # str | The sort direction for the result set (optional)
id = 'id_example' # str | The Id of the resource (optional)

try:
    # Get list of archiving Data Managment Events , their status  .
    api_response = api_instance.get_v2_archivingstatsdetails(sortby=sortby, offset=offset, limit=limit, sortdir=sortdir, id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_archivingstatsdetails: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortby** | **str**| The field(s) used to sort the result set | [optional]
 **offset** | **int**| The starting offset to read | [optional]
 **limit** | **int**| The maximum number of items to return | [optional]
 **sortdir** | **str**| The sort direction for the result set | [optional]
 **id** | **str**| The Id of the resource | [optional]

### Return type

[**V2Error**](V2Error.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_autodeletionevents**
> V2Error get_v2_autodeletionevents(sortby=sortby, offset=offset, limit=limit, sortdir=sortdir, id=id)

Get a list of all auto-deletion events.

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
sortby = 'sortby_example' # str | The field(s) used to sort the result set (optional)
offset = 56 # int | The starting offset to read (optional)
limit = 56 # int | The maximum number of items to return (optional)
sortdir = 'sortdir_example' # str | The sort direction for the result set (optional)
id = 'id_example' # str | The Id of the resource (optional)

try:
    # Get a list of all auto-deletion events.
    api_response = api_instance.get_v2_autodeletionevents(sortby=sortby, offset=offset, limit=limit, sortdir=sortdir, id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_autodeletionevents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortby** | **str**| The field(s) used to sort the result set | [optional]
 **offset** | **int**| The starting offset to read | [optional]
 **limit** | **int**| The maximum number of items to return | [optional]
 **sortdir** | **str**| The sort direction for the result set | [optional]
 **id** | **str**| The Id of the resource | [optional]

### Return type

[**V2Error**](V2Error.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_autodeletionpipeline**
> V2Error get_v2_autodeletionpipeline(format, emailtemplatename=emailtemplatename)

Get the list of users who have entered the auto-deletion pipeline due to inactivity or exceeding their storage limit.

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
format = 'format_example' # str |
emailtemplatename = 'emailtemplatename_example' # str |  (optional)

try:
    # Get the list of users who have entered the auto-deletion pipeline due to inactivity or exceeding their storage limit.
    api_response = api_instance.get_v2_autodeletionpipeline(format, emailtemplatename=emailtemplatename)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_autodeletionpipeline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**|  |
 **emailtemplatename** | **str**|  | [optional]

### Return type

[**V2Error**](V2Error.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_autodeletionusers**
> V2Error get_v2_autodeletionusers(sent, illuminausers, emailtemplatename=emailtemplatename, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir, id=id)

Get a summary of users who are about to have their account data deleted due to data retention policy.

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
sent = true # bool |
illuminausers = true # bool |
emailtemplatename = 'emailtemplatename_example' # str |  (optional)
sortby = 'sortby_example' # str | The field(s) used to sort the result set (optional)
offset = 56 # int | The starting offset to read (optional)
limit = 56 # int | The maximum number of items to return (optional)
sortdir = 'sortdir_example' # str | The sort direction for the result set (optional)
id = 'id_example' # str | The Id of the resource (optional)

try:
    # Get a summary of users who are about to have their account data deleted due to data retention policy.
    api_response = api_instance.get_v2_autodeletionusers(sent, illuminausers, emailtemplatename=emailtemplatename, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir, id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_autodeletionusers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sent** | **bool**|  |
 **illuminausers** | **bool**|  |
 **emailtemplatename** | **str**|  | [optional]
 **sortby** | **str**| The field(s) used to sort the result set | [optional]
 **offset** | **int**| The starting offset to read | [optional]
 **limit** | **int**| The maximum number of items to return | [optional]
 **sortdir** | **str**| The sort direction for the result set | [optional]
 **id** | **str**| The Id of the resource | [optional]

### Return type

[**V2Error**](V2Error.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_biosamples**
> V2BiologicalSampleCompactList get_v2_biosamples(biosamplename=biosamplename, include=include, propertynamestartswith=propertynamestartswith, status=status, labstatus=labstatus, projectid=projectid, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)

Get a list of biosamples

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
biosamplename = ['biosamplename_example'] # list[str] | Only return biosamples with the given BioSampleName(s) (optional)
include = ['include_example'] # list[str] | Sub elements to include in the response (optional)
propertynamestartswith = ['propertynamestartswith_example'] # list[str] |  (optional)
status = ['status_example'] # list[str] | Only return biosamples with the given Status(es) (optional)
labstatus = ['labstatus_example'] # list[str] | Only return biosamples with the given LabStatus(es) (optional)
projectid = ['projectid_example'] # list[str] | Only return biosamples with the specified default projects or datasets in those projects (optional)
sortby = 'sortby_example' # str | The field(s) used to sort the result set (optional)
offset = 56 # int | The starting offset to read (optional)
limit = 56 # int | The maximum number of items to return (optional)
sortdir = 'sortdir_example' # str | The sort direction for the result set (optional)

try:
    # Get a list of biosamples
    api_response = api_instance.get_v2_biosamples(biosamplename=biosamplename, include=include, propertynamestartswith=propertynamestartswith, status=status, labstatus=labstatus, projectid=projectid, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_biosamples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **biosamplename** | [**list[str]**](str.md)| Only return biosamples with the given BioSampleName(s) | [optional]
 **include** | [**list[str]**](str.md)| Sub elements to include in the response | [optional]
 **propertynamestartswith** | [**list[str]**](str.md)|  | [optional]
 **status** | [**list[str]**](str.md)| Only return biosamples with the given Status(es) | [optional]
 **labstatus** | [**list[str]**](str.md)| Only return biosamples with the given LabStatus(es) | [optional]
 **projectid** | [**list[str]**](str.md)| Only return biosamples with the specified default projects or datasets in those projects | [optional]
 **sortby** | **str**| The field(s) used to sort the result set | [optional]
 **offset** | **int**| The starting offset to read | [optional]
 **limit** | **int**| The maximum number of items to return | [optional]
 **sortdir** | **str**| The sort direction for the result set | [optional]

### Return type

[**V2BiologicalSampleCompactList**](V2BiologicalSampleCompactList.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_biosamples_biosampleid_labrequeues**
> V2LabRequeueCompactList get_v2_biosamples_biosampleid_labrequeues(biosampleid, type=type, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)

Get a list of a biosample�s lab requeues

All lab requeues, from each of the types, are listed here. A pool lab requeue will show up on the list of lab requeues for all biosamples that make up the pool.

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
biosampleid = 'biosampleid_example' # str | Biosample ID
type = 'type_example' # str | Specify which type of lab requeue to be listed e.g. NewBioSampleLibrary, AdditionalYieldOfLibraryPool, or AdditionalYieldOfFinishedLibrary. (optional)
sortby = 'sortby_example' # str | The field(s) used to sort the result set (optional)
offset = 56 # int | The starting offset to read (optional)
limit = 56 # int | The maximum number of items to return (optional)
sortdir = 'sortdir_example' # str | The sort direction for the result set (optional)

try:
    # Get a list of a biosample�s lab requeues
    api_response = api_instance.get_v2_biosamples_biosampleid_labrequeues(biosampleid, type=type, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_biosamples_biosampleid_labrequeues: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **biosampleid** | **str**| Biosample ID |
 **type** | **str**| Specify which type of lab requeue to be listed e.g. NewBioSampleLibrary, AdditionalYieldOfLibraryPool, or AdditionalYieldOfFinishedLibrary. | [optional]
 **sortby** | **str**| The field(s) used to sort the result set | [optional]
 **offset** | **int**| The starting offset to read | [optional]
 **limit** | **int**| The maximum number of items to return | [optional]
 **sortdir** | **str**| The sort direction for the result set | [optional]

### Return type

[**V2LabRequeueCompactList**](V2LabRequeueCompactList.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_biosamples_id**
> V2BiologicalSample get_v2_biosamples_id(id, include=include)

Get information about a biosample

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | Biosample ID
include = ['include_example'] # list[str] | Sub elements to include in the response (optional)

try:
    # Get information about a biosample
    api_response = api_instance.get_v2_biosamples_id(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_biosamples_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Biosample ID |
 **include** | [**list[str]**](str.md)| Sub elements to include in the response | [optional]

### Return type

[**V2BiologicalSample**](V2BiologicalSample.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_biosamples_id_aggregatedfastqdatasets**
> V2Error get_v2_biosamples_id_aggregatedfastqdatasets(id, mixlibrarytypesallowed, selectedlibraryprepids=selectedlibraryprepids, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)

Get aggregated datasets for a given biosample

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | Biosample ID
mixlibrarytypesallowed = true # bool | If true, mixing datasets of different library types is allowed, false otherwise
selectedlibraryprepids = ['selectedlibraryprepids_example'] # list[str] | Optional comma-separated list of selected LibraryPrepId values to consider (optional)
sortby = 'sortby_example' # str | The field(s) used to sort the result set (optional)
offset = 56 # int | The starting offset to read (optional)
limit = 56 # int | The maximum number of items to return (optional)
sortdir = 'sortdir_example' # str | The sort direction for the result set (optional)

try:
    # Get aggregated datasets for a given biosample
    api_response = api_instance.get_v2_biosamples_id_aggregatedfastqdatasets(id, mixlibrarytypesallowed, selectedlibraryprepids=selectedlibraryprepids, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_biosamples_id_aggregatedfastqdatasets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Biosample ID |
 **mixlibrarytypesallowed** | **bool**| If true, mixing datasets of different library types is allowed, false otherwise |
 **selectedlibraryprepids** | [**list[str]**](str.md)| Optional comma-separated list of selected LibraryPrepId values to consider | [optional]
 **sortby** | **str**| The field(s) used to sort the result set | [optional]
 **offset** | **int**| The starting offset to read | [optional]
 **limit** | **int**| The maximum number of items to return | [optional]
 **sortdir** | **str**| The sort direction for the result set | [optional]

### Return type

[**V2Error**](V2Error.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_biosamples_id_libraries**
> V2LibraryCompactList get_v2_biosamples_id_libraries(id, include=include, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)

Get a list of a biosample�s libraries

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | Biosample ID
include = ['include_example'] # list[str] | Sub elements to include in the response: LibraryIndex, YieldInformation (optional)
sortby = 'sortby_example' # str | The field(s) used to sort the result set (optional)
offset = 56 # int | The starting offset to read (optional)
limit = 56 # int | The maximum number of items to return (optional)
sortdir = 'sortdir_example' # str | The sort direction for the result set (optional)

try:
    # Get a list of a biosample�s libraries
    api_response = api_instance.get_v2_biosamples_id_libraries(id, include=include, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_biosamples_id_libraries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Biosample ID |
 **include** | [**list[str]**](str.md)| Sub elements to include in the response: LibraryIndex, YieldInformation | [optional]
 **sortby** | **str**| The field(s) used to sort the result set | [optional]
 **offset** | **int**| The starting offset to read | [optional]
 **limit** | **int**| The maximum number of items to return | [optional]
 **sortdir** | **str**| The sort direction for the result set | [optional]

### Return type

[**V2LibraryCompactList**](V2LibraryCompactList.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_biosamples_id_properties**
> V2PropertyCompactList get_v2_biosamples_id_properties(id, propertieslimit=propertieslimit, propertyitemslimit=propertyitemslimit, propertyfilters=propertyfilters, showhiddenitems=showhiddenitems, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)



List properties for a resource

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str |
propertieslimit = 56 # int | Limit the # of properties returned (optional)
propertyitemslimit = 56 # int | Limit the # of property items returned per property (optional)
propertyfilters = ['propertyfilters_example'] # list[str] | Filter by property name (optional)
showhiddenitems = 'showhiddenitems_example' # str | Show Hidden projects and Datasets (optional)
sortby = 'sortby_example' # str | The field(s) used to sort the result set (optional)
offset = 56 # int | The starting offset to read (optional)
limit = 56 # int | The maximum number of items to return (optional)
sortdir = 'sortdir_example' # str | The sort direction for the result set (optional)

try:
    api_response = api_instance.get_v2_biosamples_id_properties(id, propertieslimit=propertieslimit, propertyitemslimit=propertyitemslimit, propertyfilters=propertyfilters, showhiddenitems=showhiddenitems, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_biosamples_id_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **propertieslimit** | **int**| Limit the # of properties returned | [optional]
 **propertyitemslimit** | **int**| Limit the # of property items returned per property | [optional]
 **propertyfilters** | [**list[str]**](str.md)| Filter by property name | [optional]
 **showhiddenitems** | **str**| Show Hidden projects and Datasets | [optional]
 **sortby** | **str**| The field(s) used to sort the result set | [optional]
 **offset** | **int**| The starting offset to read | [optional]
 **limit** | **int**| The maximum number of items to return | [optional]
 **sortdir** | **str**| The sort direction for the result set | [optional]

### Return type

[**V2PropertyCompactList**](V2PropertyCompactList.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_biosamples_id_properties_name**
> V2Property get_v2_biosamples_id_properties_name(id, name, propertyitemslimit=propertyitemslimit, showhiddenitems=showhiddenitems)



Get property information

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str |
name = 'name_example' # str | Property name
propertyitemslimit = 56 # int | Limit the # of property items returned per property (optional)
showhiddenitems = 'showhiddenitems_example' # str | Hidden filter (optional)

try:
    api_response = api_instance.get_v2_biosamples_id_properties_name(id, name, propertyitemslimit=propertyitemslimit, showhiddenitems=showhiddenitems)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_biosamples_id_properties_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **name** | **str**| Property name |
 **propertyitemslimit** | **int**| Limit the # of property items returned per property | [optional]
 **showhiddenitems** | **str**| Hidden filter | [optional]

### Return type

[**V2Property**](V2Property.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_biosamples_id_properties_name_items**
> V2PropertyItemList get_v2_biosamples_id_properties_name_items(id, name, showhiddenitems=showhiddenitems, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)



Get property item details

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str |
name = 'name_example' # str | Property name
showhiddenitems = 'showhiddenitems_example' # str | Hidden filter (optional)
sortby = 'sortby_example' # str | The field(s) used to sort the result set (optional)
offset = 56 # int | The starting offset to read (optional)
limit = 56 # int | The maximum number of items to return (optional)
sortdir = 'sortdir_example' # str | The sort direction for the result set (optional)

try:
    api_response = api_instance.get_v2_biosamples_id_properties_name_items(id, name, showhiddenitems=showhiddenitems, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_biosamples_id_properties_name_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **name** | **str**| Property name |
 **showhiddenitems** | **str**| Hidden filter | [optional]
 **sortby** | **str**| The field(s) used to sort the result set | [optional]
 **offset** | **int**| The starting offset to read | [optional]
 **limit** | **int**| The maximum number of items to return | [optional]
 **sortdir** | **str**| The sort direction for the result set | [optional]

### Return type

[**V2PropertyItemList**](V2PropertyItemList.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_biosamples_id_runlanesummaries**
> V2RunLaneSummaryList get_v2_biosamples_id_runlanesummaries(id, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)

Get information about biosample’s lane mapping

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | Biosample ID
sortby = 'sortby_example' # str | The field(s) used to sort the result set (optional)
offset = 56 # int | The starting offset to read (optional)
limit = 56 # int | The maximum number of items to return (optional)
sortdir = 'sortdir_example' # str | The sort direction for the result set (optional)

try:
    # Get information about biosample’s lane mapping
    api_response = api_instance.get_v2_biosamples_id_runlanesummaries(id, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_biosamples_id_runlanesummaries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Biosample ID |
 **sortby** | **str**| The field(s) used to sort the result set | [optional]
 **offset** | **int**| The starting offset to read | [optional]
 **limit** | **int**| The maximum number of items to return | [optional]
 **sortdir** | **str**| The sort direction for the result set | [optional]

### Return type

[**V2RunLaneSummaryList**](V2RunLaneSummaryList.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_datasets**
> V2DatasetCompactList get_v2_datasets(include=include, propertyfilters=propertyfilters, datasettypes=datasettypes, qcstatus=qcstatus, uploadstatus=uploadstatus, inputbiosamples=inputbiosamples, inputruns=inputruns, inputruntokens=inputruntokens, projectid=projectid, appsessionids=appsessionids, isarchived=isarchived, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)

Get a list of datasets

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
include = ['include_example'] # list[str] | Can specify to return Properties, which returns an additional properties section for each dataset. Or return AppSessionRoot, which returns information about the root analysis of a workflow in the AppSession section for each dataset it applies to. (optional)
propertyfilters = ['propertyfilters_example'] # list[str] | Specify which properties to include in the properties section, e.g. Input.BioSamples, Input.Libraries, or Input.Runs. (optional)
datasettypes = ['datasettypes_example'] # list[str] | Return datasets of this type or excluding this type. Supports comma-separated lists. (optional)
qcstatus = ['qcstatus_example'] # list[str] | Return datasets of this QC status. (optional)
uploadstatus = ['uploadstatus_example'] # list[str] | Return datasets of this file upload status. (optional)
inputbiosamples = [56] # list[int] | Return datasets related to this biosample ID. (optional)
inputruns = [56] # list[int] | Return datasets related to this run ID. (optional)
inputruntokens = ['inputruntokens_example'] # list[str] | Return datasets related to this run ID token. (optional)
projectid = 'projectid_example' # str | Return datasets related to this project ID. (optional)
appsessionids = [56] # list[int] | Return datasets related to this app session ID. (optional)
isarchived = 'isarchived_example' # str | The archive states to filter by. Valid values include: True, False. (optional)
sortby = 'sortby_example' # str | The field(s) used to sort the result set (optional)
offset = 56 # int | The starting offset to read (optional)
limit = 56 # int | The maximum number of items to return (optional)
sortdir = 'sortdir_example' # str | The sort direction for the result set (optional)

try:
    # Get a list of datasets
    api_response = api_instance.get_v2_datasets(include=include, propertyfilters=propertyfilters, datasettypes=datasettypes, qcstatus=qcstatus, uploadstatus=uploadstatus, inputbiosamples=inputbiosamples, inputruns=inputruns, inputruntokens=inputruntokens, projectid=projectid, appsessionids=appsessionids, isarchived=isarchived, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_datasets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include** | [**list[str]**](str.md)| Can specify to return Properties, which returns an additional properties section for each dataset. Or return AppSessionRoot, which returns information about the root analysis of a workflow in the AppSession section for each dataset it applies to. | [optional]
 **propertyfilters** | [**list[str]**](str.md)| Specify which properties to include in the properties section, e.g. Input.BioSamples, Input.Libraries, or Input.Runs. | [optional]
 **datasettypes** | [**list[str]**](str.md)| Return datasets of this type or excluding this type. Supports comma-separated lists. | [optional]
 **qcstatus** | [**list[str]**](str.md)| Return datasets of this QC status. | [optional]
 **uploadstatus** | [**list[str]**](str.md)| Return datasets of this file upload status. | [optional]
 **inputbiosamples** | [**list[int]**](int.md)| Return datasets related to this biosample ID. | [optional]
 **inputruns** | [**list[int]**](int.md)| Return datasets related to this run ID. | [optional]
 **inputruntokens** | [**list[str]**](str.md)| Return datasets related to this run ID token. | [optional]
 **projectid** | **str**| Return datasets related to this project ID. | [optional]
 **appsessionids** | [**list[int]**](int.md)| Return datasets related to this app session ID. | [optional]
 **isarchived** | **str**| The archive states to filter by. Valid values include: True, False. | [optional]
 **sortby** | **str**| The field(s) used to sort the result set | [optional]
 **offset** | **int**| The starting offset to read | [optional]
 **limit** | **int**| The maximum number of items to return | [optional]
 **sortdir** | **str**| The sort direction for the result set | [optional]

### Return type

[**V2DatasetCompactList**](V2DatasetCompactList.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_datasets_id**
> V2Dataset get_v2_datasets_id(id)

Get information about a dataset

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | Dataset ID

try:
    # Get information about a dataset
    api_response = api_instance.get_v2_datasets_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_datasets_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Dataset ID |

### Return type

[**V2Dataset**](V2Dataset.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_datasets_id_comments**
> V2CommentList get_v2_datasets_id_comments(id, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)

Get a list of comments made about a dataset

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | Dataset ID
sortby = 'sortby_example' # str | The field(s) used to sort the result set (optional)
offset = 56 # int | The starting offset to read (optional)
limit = 56 # int | The maximum number of items to return (optional)
sortdir = 'sortdir_example' # str | The sort direction for the result set (optional)

try:
    # Get a list of comments made about a dataset
    api_response = api_instance.get_v2_datasets_id_comments(id, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_datasets_id_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Dataset ID |
 **sortby** | **str**| The field(s) used to sort the result set | [optional]
 **offset** | **int**| The starting offset to read | [optional]
 **limit** | **int**| The maximum number of items to return | [optional]
 **sortdir** | **str**| The sort direction for the result set | [optional]

### Return type

[**V2CommentList**](V2CommentList.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_datasets_id_direct_upload_info**
> V1pre3DirectUploadInformation get_v2_datasets_id_direct_upload_info(id)



Request direct upload information for a new dataset

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | The Id of the resource

try:
    api_response = api_instance.get_v2_datasets_id_direct_upload_info(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_datasets_id_direct_upload_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of the resource |

### Return type

[**V1pre3DirectUploadInformation**](V1pre3DirectUploadInformation.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_datasets_id_file_upload_info**
> V2PresignedUrlForUpload get_v2_datasets_id_file_upload_info(id, filepath=filepath, uploadpartcount=uploadpartcount)



Request direct file upload presigned url information for a new file in the specified resource (dataset or appresult)

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | The Id of the resource
filepath = 'filepath_example' # str |  (optional)
uploadpartcount = 56 # int |  (optional)

try:
    api_response = api_instance.get_v2_datasets_id_file_upload_info(id, filepath=filepath, uploadpartcount=uploadpartcount)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_datasets_id_file_upload_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of the resource |
 **filepath** | **str**|  | [optional]
 **uploadpartcount** | **int**|  | [optional]

### Return type

[**V2PresignedUrlForUpload**](V2PresignedUrlForUpload.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_datasets_id_files**
> V2FilesList get_v2_datasets_id_files(excludevcfindexfolder, excludebamcoveragefolder, excludesystemfolder, excludeemptyfiles, filehrefcontentresolution, turbomode, id, filesetid=filesetid, extensions=extensions, excludeextensions=excludeextensions, directory=directory, includesubdirectories=includesubdirectories, statuses=statuses, pathprefix=pathprefix, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)

Get a list of files of a dataset

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
excludevcfindexfolder = true # bool | Whether to exclude VCF index folders
excludebamcoveragefolder = true # bool | Whether to exclude BAM coverage folders
excludesystemfolder = true # bool | Whether to exclude system folders
excludeemptyfiles = true # bool | Whether to exclude empty files
filehrefcontentresolution = true # bool | Resolves the HrefContent to the direct file URI to avoid a hop to GET: files/{id}/content
turbomode = true # bool |
id = 'id_example' # str | The Id of the resource
filesetid = 'filesetid_example' # str |  (optional)
extensions = 'extensions_example' # str | Filter by file extension (optional)
excludeextensions = 'excludeextensions_example' # str | Exclude by file extension (optional)
directory = 'directory_example' # str | Filter by directory path (root is /) (optional)
includesubdirectories = true # bool | Whether to return subdirectories (optional)
statuses = ['statuses_example'] # list[str] | Optionally filter by status (default complete) (optional)
pathprefix = 'pathprefix_example' # str | To be pre-fixed in the path of the file (optional)
sortby = 'sortby_example' # str | The field(s) used to sort the result set (optional)
offset = 56 # int | The starting offset to read (optional)
limit = 56 # int | The maximum number of items to return (optional)
sortdir = 'sortdir_example' # str | The sort direction for the result set (optional)

try:
    # Get a list of files of a dataset
    api_response = api_instance.get_v2_datasets_id_files(excludevcfindexfolder, excludebamcoveragefolder, excludesystemfolder, excludeemptyfiles, filehrefcontentresolution, turbomode, id, filesetid=filesetid, extensions=extensions, excludeextensions=excludeextensions, directory=directory, includesubdirectories=includesubdirectories, statuses=statuses, pathprefix=pathprefix, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_datasets_id_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **excludevcfindexfolder** | **bool**| Whether to exclude VCF index folders |
 **excludebamcoveragefolder** | **bool**| Whether to exclude BAM coverage folders |
 **excludesystemfolder** | **bool**| Whether to exclude system folders |
 **excludeemptyfiles** | **bool**| Whether to exclude empty files |
 **filehrefcontentresolution** | **bool**| Resolves the HrefContent to the direct file URI to avoid a hop to GET: files/{id}/content |
 **turbomode** | **bool**|  |
 **id** | **str**| The Id of the resource |
 **filesetid** | **str**|  | [optional]
 **extensions** | **str**| Filter by file extension | [optional]
 **excludeextensions** | **str**| Exclude by file extension | [optional]
 **directory** | **str**| Filter by directory path (root is /) | [optional]
 **includesubdirectories** | **bool**| Whether to return subdirectories | [optional]
 **statuses** | [**list[str]**](str.md)| Optionally filter by status (default complete) | [optional]
 **pathprefix** | **str**| To be pre-fixed in the path of the file | [optional]
 **sortby** | **str**| The field(s) used to sort the result set | [optional]
 **offset** | **int**| The starting offset to read | [optional]
 **limit** | **int**| The maximum number of items to return | [optional]
 **sortdir** | **str**| The sort direction for the result set | [optional]

### Return type

[**V2FilesList**](V2FilesList.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_datasets_id_properties**
> V2PropertyCompactList get_v2_datasets_id_properties(id, propertieslimit=propertieslimit, propertyitemslimit=propertyitemslimit, propertyfilters=propertyfilters, showhiddenitems=showhiddenitems, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)



List properties for a resource

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str |
propertieslimit = 56 # int | Limit the # of properties returned (optional)
propertyitemslimit = 56 # int | Limit the # of property items returned per property (optional)
propertyfilters = ['propertyfilters_example'] # list[str] | Filter by property name (optional)
showhiddenitems = 'showhiddenitems_example' # str | Show Hidden projects and Datasets (optional)
sortby = 'sortby_example' # str | The field(s) used to sort the result set (optional)
offset = 56 # int | The starting offset to read (optional)
limit = 56 # int | The maximum number of items to return (optional)
sortdir = 'sortdir_example' # str | The sort direction for the result set (optional)

try:
    api_response = api_instance.get_v2_datasets_id_properties(id, propertieslimit=propertieslimit, propertyitemslimit=propertyitemslimit, propertyfilters=propertyfilters, showhiddenitems=showhiddenitems, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_datasets_id_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **propertieslimit** | **int**| Limit the # of properties returned | [optional]
 **propertyitemslimit** | **int**| Limit the # of property items returned per property | [optional]
 **propertyfilters** | [**list[str]**](str.md)| Filter by property name | [optional]
 **showhiddenitems** | **str**| Show Hidden projects and Datasets | [optional]
 **sortby** | **str**| The field(s) used to sort the result set | [optional]
 **offset** | **int**| The starting offset to read | [optional]
 **limit** | **int**| The maximum number of items to return | [optional]
 **sortdir** | **str**| The sort direction for the result set | [optional]

### Return type

[**V2PropertyCompactList**](V2PropertyCompactList.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_datasets_id_properties_name**
> V2Property get_v2_datasets_id_properties_name(id, name, propertyitemslimit=propertyitemslimit, showhiddenitems=showhiddenitems)



Get property information

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str |
name = 'name_example' # str | Property name
propertyitemslimit = 56 # int | Limit the # of property items returned per property (optional)
showhiddenitems = 'showhiddenitems_example' # str | Hidden filter (optional)

try:
    api_response = api_instance.get_v2_datasets_id_properties_name(id, name, propertyitemslimit=propertyitemslimit, showhiddenitems=showhiddenitems)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_datasets_id_properties_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **name** | **str**| Property name |
 **propertyitemslimit** | **int**| Limit the # of property items returned per property | [optional]
 **showhiddenitems** | **str**| Hidden filter | [optional]

### Return type

[**V2Property**](V2Property.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_datasets_id_properties_name_items**
> V2PropertyItemList get_v2_datasets_id_properties_name_items(id, name, showhiddenitems=showhiddenitems, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)



Get property item details

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str |
name = 'name_example' # str | Property name
showhiddenitems = 'showhiddenitems_example' # str | Hidden filter (optional)
sortby = 'sortby_example' # str | The field(s) used to sort the result set (optional)
offset = 56 # int | The starting offset to read (optional)
limit = 56 # int | The maximum number of items to return (optional)
sortdir = 'sortdir_example' # str | The sort direction for the result set (optional)

try:
    api_response = api_instance.get_v2_datasets_id_properties_name_items(id, name, showhiddenitems=showhiddenitems, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_datasets_id_properties_name_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **name** | **str**| Property name |
 **showhiddenitems** | **str**| Hidden filter | [optional]
 **sortby** | **str**| The field(s) used to sort the result set | [optional]
 **offset** | **int**| The starting offset to read | [optional]
 **limit** | **int**| The maximum number of items to return | [optional]
 **sortdir** | **str**| The sort direction for the result set | [optional]

### Return type

[**V2PropertyItemList**](V2PropertyItemList.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_datasettypes_id**
> V2DatasetType get_v2_datasettypes_id(id, include=include)

Get information about a dataset type

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | Dataset type ID
include = ['include_example'] # list[str] |  (optional)

try:
    # Get information about a dataset type
    api_response = api_instance.get_v2_datasettypes_id(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_datasettypes_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Dataset type ID |
 **include** | [**list[str]**](str.md)|  | [optional]

### Return type

[**V2DatasetType**](V2DatasetType.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_gdssharetransferstats**
> V2Error get_v2_gdssharetransferstats(operationtype=operationtype, status=status, maxitems=maxitems)

Get a summary of GDS share or transfer operations.

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
operationtype = 'operationtype_example' # str |  (optional)
status = 'status_example' # str |  (optional)
maxitems = 'maxitems_example' # str |  (optional)

try:
    # Get a summary of GDS share or transfer operations.
    api_response = api_instance.get_v2_gdssharetransferstats(operationtype=operationtype, status=status, maxitems=maxitems)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_gdssharetransferstats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operationtype** | **str**|  | [optional]
 **status** | **str**|  | [optional]
 **maxitems** | **str**|  | [optional]

### Return type

[**V2Error**](V2Error.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_instrumentconnectioncheck_file_upload_info**
> V2PresignedUrlForUpload get_v2_instrumentconnectioncheck_file_upload_info(filepath=filepath, uploadpartcount=uploadpartcount, id=id)



Request access to temporary data presigned URL for upload to test connectivity

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
filepath = 'filepath_example' # str |  (optional)
uploadpartcount = 56 # int |  (optional)
id = 'id_example' # str | The Id of the resource (optional)

try:
    api_response = api_instance.get_v2_instrumentconnectioncheck_file_upload_info(filepath=filepath, uploadpartcount=uploadpartcount, id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_instrumentconnectioncheck_file_upload_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filepath** | **str**|  | [optional]
 **uploadpartcount** | **int**|  | [optional]
 **id** | **str**| The Id of the resource | [optional]

### Return type

[**V2PresignedUrlForUpload**](V2PresignedUrlForUpload.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_instrumentdiagnostics_id**
> V2InstrumentDiagnostic get_v2_instrumentdiagnostics_id(id)



Get non-run instrument diagnostic data.

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | The Id of the resource

try:
    api_response = api_instance.get_v2_instrumentdiagnostics_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_instrumentdiagnostics_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of the resource |

### Return type

[**V2InstrumentDiagnostic**](V2InstrumentDiagnostic.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_instruments**
> V2InstrumentCompactList get_v2_instruments(allworkgroups, activeruns, fromdate=fromdate, todate=todate, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir, id=id)



List available instruments for a user.

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
allworkgroups = true # bool |
activeruns = true # bool |
fromdate = 'fromdate_example' # str |  (optional)
todate = 'todate_example' # str |  (optional)
sortby = 'sortby_example' # str | The field(s) used to sort the result set (optional)
offset = 56 # int | The starting offset to read (optional)
limit = 56 # int | The maximum number of items to return (optional)
sortdir = 'sortdir_example' # str | The sort direction for the result set (optional)
id = 'id_example' # str | The Id of the resource (optional)

try:
    api_response = api_instance.get_v2_instruments(allworkgroups, activeruns, fromdate=fromdate, todate=todate, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir, id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_instruments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **allworkgroups** | **bool**|  |
 **activeruns** | **bool**|  |
 **fromdate** | **str**|  | [optional]
 **todate** | **str**|  | [optional]
 **sortby** | **str**| The field(s) used to sort the result set | [optional]
 **offset** | **int**| The starting offset to read | [optional]
 **limit** | **int**| The maximum number of items to return | [optional]
 **sortdir** | **str**| The sort direction for the result set | [optional]
 **id** | **str**| The Id of the resource | [optional]

### Return type

[**V2InstrumentCompactList**](V2InstrumentCompactList.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_instrumentstatistics**
> V2InstrumentStatList get_v2_instrumentstatistics(serialnumbers, fromdate, timezone, todate=todate, binby=binby, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir, id=id)

Get instrument statistics

Get instrument statistics for given serial numbers and time range. Returned data can be grouped by month or week.

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
serialnumbers = 'serialnumbers_example' # str | Comma-separated list of serial numbers.
fromdate = NULL # object | From date in user ISO 8601 format.
timezone = 'timezone_example' # str | User timezone for binning.
todate = NULL # object | To date in ISO 8601 format. Defaults to current date if not specified. (optional)
binby = 'binby_example' # str | BinBy can be 'week' or 'month'. (optional)
sortby = 'sortby_example' # str | The field(s) used to sort the result set (optional)
offset = 56 # int | The starting offset to read (optional)
limit = 56 # int | The maximum number of items to return (optional)
sortdir = 'sortdir_example' # str | The sort direction for the result set (optional)
id = 'id_example' # str | The Id of the resource (optional)

try:
    # Get instrument statistics
    api_response = api_instance.get_v2_instrumentstatistics(serialnumbers, fromdate, timezone, todate=todate, binby=binby, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir, id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_instrumentstatistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serialnumbers** | **str**| Comma-separated list of serial numbers. |
 **fromdate** | [**object**](.md)| From date in user ISO 8601 format. |
 **timezone** | **str**| User timezone for binning. |
 **todate** | [**object**](.md)| To date in ISO 8601 format. Defaults to current date if not specified. | [optional]
 **binby** | **str**| BinBy can be &#x27;week&#x27; or &#x27;month&#x27;. | [optional]
 **sortby** | **str**| The field(s) used to sort the result set | [optional]
 **offset** | **int**| The starting offset to read | [optional]
 **limit** | **int**| The maximum number of items to return | [optional]
 **sortdir** | **str**| The sort direction for the result set | [optional]
 **id** | **str**| The Id of the resource | [optional]

### Return type

[**V2InstrumentStatList**](V2InstrumentStatList.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_instrumentstatus**
> V2InstrumentStatusCompactList get_v2_instrumentstatus(includeactiveruns, serialnumbers=serialnumbers, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir, id=id)



List of instruments with active runs

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
includeactiveruns = true # bool | Set to true to include a list of active runs for each instrument.  Default is false.
serialnumbers = 'serialnumbers_example' # str | A comma-delimited list of instrument serial numbers. (optional)
sortby = 'sortby_example' # str | The field(s) used to sort the result set (optional)
offset = 56 # int | The starting offset to read (optional)
limit = 56 # int | The maximum number of items to return (optional)
sortdir = 'sortdir_example' # str | The sort direction for the result set (optional)
id = 'id_example' # str | The Id of the resource (optional)

try:
    api_response = api_instance.get_v2_instrumentstatus(includeactiveruns, serialnumbers=serialnumbers, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir, id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_instrumentstatus: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **includeactiveruns** | **bool**| Set to true to include a list of active runs for each instrument.  Default is false. |
 **serialnumbers** | **str**| A comma-delimited list of instrument serial numbers. | [optional]
 **sortby** | **str**| The field(s) used to sort the result set | [optional]
 **offset** | **int**| The starting offset to read | [optional]
 **limit** | **int**| The maximum number of items to return | [optional]
 **sortdir** | **str**| The sort direction for the result set | [optional]
 **id** | **str**| The Id of the resource | [optional]

### Return type

[**V2InstrumentStatusCompactList**](V2InstrumentStatusCompactList.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_labrequeues**
> V2LabRequeueList get_v2_labrequeues(status=status, type=type, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir, id=id)

Get a list of lab requeues

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
status = ['status_example'] # list[str] | Only return labrequeues with the given Status(es) (optional)
type = ['type_example'] # list[str] | Only return labrequeues with the given LabRequeueTypes(s) (optional)
sortby = 'sortby_example' # str | The field(s) used to sort the result set (optional)
offset = 56 # int | The starting offset to read (optional)
limit = 56 # int | The maximum number of items to return (optional)
sortdir = 'sortdir_example' # str | The sort direction for the result set (optional)
id = 'id_example' # str | The Id of the resource (optional)

try:
    # Get a list of lab requeues
    api_response = api_instance.get_v2_labrequeues(status=status, type=type, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir, id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_labrequeues: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | [**list[str]**](str.md)| Only return labrequeues with the given Status(es) | [optional]
 **type** | [**list[str]**](str.md)| Only return labrequeues with the given LabRequeueTypes(s) | [optional]
 **sortby** | **str**| The field(s) used to sort the result set | [optional]
 **offset** | **int**| The starting offset to read | [optional]
 **limit** | **int**| The maximum number of items to return | [optional]
 **sortdir** | **str**| The sort direction for the result set | [optional]
 **id** | **str**| The Id of the resource | [optional]

### Return type

[**V2LabRequeueList**](V2LabRequeueList.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_labrequeues_id**
> V2LabRequeue get_v2_labrequeues_id(id)

Get information about a specific labrequeue

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | Labrequeue ID

try:
    # Get information about a specific labrequeue
    api_response = api_instance.get_v2_labrequeues_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_labrequeues_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Labrequeue ID |

### Return type

[**V2LabRequeue**](V2LabRequeue.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_laneqcthresholds**
> V2QcThresholdResponse get_v2_laneqcthresholds(id=id)

Get a list of QC thresholds applied to lanes

The QC thresholds are applied to a user's account. Any runs uploaded in that user's context will automatically have all lanes of the flowcell undergo automatic QC based on the QC thresholds. Thresholds are saved either to a lane, or to a lane and read number.

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | The Id of the resource (optional)

try:
    # Get a list of QC thresholds applied to lanes
    api_response = api_instance.get_v2_laneqcthresholds(id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_laneqcthresholds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of the resource | [optional]

### Return type

[**V2QcThresholdResponse**](V2QcThresholdResponse.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_lanes_id**
> Lane get_v2_lanes_id(id)

Get information about a lane

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | The Id of the resource

try:
    # Get information about a lane
    api_response = api_instance.get_v2_lanes_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_lanes_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of the resource |

### Return type

[**Lane**](Lane.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_lanes_id_comments**
> V2CommentList get_v2_lanes_id_comments(id, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)

Get a list of comments on a lane

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | Lane ID
sortby = 'sortby_example' # str | The field(s) used to sort the result set (optional)
offset = 56 # int | The starting offset to read (optional)
limit = 56 # int | The maximum number of items to return (optional)
sortdir = 'sortdir_example' # str | The sort direction for the result set (optional)

try:
    # Get a list of comments on a lane
    api_response = api_instance.get_v2_lanes_id_comments(id, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_lanes_id_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Lane ID |
 **sortby** | **str**| The field(s) used to sort the result set | [optional]
 **offset** | **int**| The starting offset to read | [optional]
 **limit** | **int**| The maximum number of items to return | [optional]
 **sortdir** | **str**| The sort direction for the result set | [optional]

### Return type

[**V2CommentList**](V2CommentList.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_libraries**
> V2LibraryCompactList get_v2_libraries(status=status, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir, id=id)

Get a list of libraries

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
status = ['status_example'] # list[str] |  (optional)
sortby = 'sortby_example' # str | The field(s) used to sort the result set (optional)
offset = 56 # int | The starting offset to read (optional)
limit = 56 # int | The maximum number of items to return (optional)
sortdir = 'sortdir_example' # str | The sort direction for the result set (optional)
id = 'id_example' # str | The Id of the resource (optional)

try:
    # Get a list of libraries
    api_response = api_instance.get_v2_libraries(status=status, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir, id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_libraries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | [**list[str]**](str.md)|  | [optional]
 **sortby** | **str**| The field(s) used to sort the result set | [optional]
 **offset** | **int**| The starting offset to read | [optional]
 **limit** | **int**| The maximum number of items to return | [optional]
 **sortdir** | **str**| The sort direction for the result set | [optional]
 **id** | **str**| The Id of the resource | [optional]

### Return type

[**V2LibraryCompactList**](V2LibraryCompactList.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_libraries_id_properties**
> V2PropertyCompactList get_v2_libraries_id_properties(id, propertieslimit=propertieslimit, propertyitemslimit=propertyitemslimit, propertyfilters=propertyfilters, showhiddenitems=showhiddenitems, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)



List properties for a resource

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str |
propertieslimit = 56 # int | Limit the # of properties returned (optional)
propertyitemslimit = 56 # int | Limit the # of property items returned per property (optional)
propertyfilters = ['propertyfilters_example'] # list[str] | Filter by property name (optional)
showhiddenitems = 'showhiddenitems_example' # str | Show Hidden projects and Datasets (optional)
sortby = 'sortby_example' # str | The field(s) used to sort the result set (optional)
offset = 56 # int | The starting offset to read (optional)
limit = 56 # int | The maximum number of items to return (optional)
sortdir = 'sortdir_example' # str | The sort direction for the result set (optional)

try:
    api_response = api_instance.get_v2_libraries_id_properties(id, propertieslimit=propertieslimit, propertyitemslimit=propertyitemslimit, propertyfilters=propertyfilters, showhiddenitems=showhiddenitems, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_libraries_id_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **propertieslimit** | **int**| Limit the # of properties returned | [optional]
 **propertyitemslimit** | **int**| Limit the # of property items returned per property | [optional]
 **propertyfilters** | [**list[str]**](str.md)| Filter by property name | [optional]
 **showhiddenitems** | **str**| Show Hidden projects and Datasets | [optional]
 **sortby** | **str**| The field(s) used to sort the result set | [optional]
 **offset** | **int**| The starting offset to read | [optional]
 **limit** | **int**| The maximum number of items to return | [optional]
 **sortdir** | **str**| The sort direction for the result set | [optional]

### Return type

[**V2PropertyCompactList**](V2PropertyCompactList.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_libraries_id_properties_name**
> V2Property get_v2_libraries_id_properties_name(id, name, propertyitemslimit=propertyitemslimit, showhiddenitems=showhiddenitems)



Get property information

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str |
name = 'name_example' # str | Property name
propertyitemslimit = 56 # int | Limit the # of property items returned per property (optional)
showhiddenitems = 'showhiddenitems_example' # str | Hidden filter (optional)

try:
    api_response = api_instance.get_v2_libraries_id_properties_name(id, name, propertyitemslimit=propertyitemslimit, showhiddenitems=showhiddenitems)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_libraries_id_properties_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **name** | **str**| Property name |
 **propertyitemslimit** | **int**| Limit the # of property items returned per property | [optional]
 **showhiddenitems** | **str**| Hidden filter | [optional]

### Return type

[**V2Property**](V2Property.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_libraries_id_properties_name_items**
> V2PropertyItemList get_v2_libraries_id_properties_name_items(id, name, showhiddenitems=showhiddenitems, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)



Get property item details

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str |
name = 'name_example' # str | Property name
showhiddenitems = 'showhiddenitems_example' # str | Hidden filter (optional)
sortby = 'sortby_example' # str | The field(s) used to sort the result set (optional)
offset = 56 # int | The starting offset to read (optional)
limit = 56 # int | The maximum number of items to return (optional)
sortdir = 'sortdir_example' # str | The sort direction for the result set (optional)

try:
    api_response = api_instance.get_v2_libraries_id_properties_name_items(id, name, showhiddenitems=showhiddenitems, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_libraries_id_properties_name_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **name** | **str**| Property name |
 **showhiddenitems** | **str**| Hidden filter | [optional]
 **sortby** | **str**| The field(s) used to sort the result set | [optional]
 **offset** | **int**| The starting offset to read | [optional]
 **limit** | **int**| The maximum number of items to return | [optional]
 **sortdir** | **str**| The sort direction for the result set | [optional]

### Return type

[**V2PropertyItemList**](V2PropertyItemList.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_librarypools**
> V1pre3LibraryPoolCompact get_v2_librarypools(status=status, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir, id=id)

Get a list of library pools

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
status = ['status_example'] # list[str] | Possible values are: Active, Failed, Consumed, QCFailed (optional)
sortby = 'sortby_example' # str | The field(s) used to sort the result set (optional)
offset = 56 # int | The starting offset to read (optional)
limit = 56 # int | The maximum number of items to return (optional)
sortdir = 'sortdir_example' # str | The sort direction for the result set (optional)
id = 'id_example' # str | The Id of the resource (optional)

try:
    # Get a list of library pools
    api_response = api_instance.get_v2_librarypools(status=status, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir, id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_librarypools: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | [**list[str]**](str.md)| Possible values are: Active, Failed, Consumed, QCFailed | [optional]
 **sortby** | **str**| The field(s) used to sort the result set | [optional]
 **offset** | **int**| The starting offset to read | [optional]
 **limit** | **int**| The maximum number of items to return | [optional]
 **sortdir** | **str**| The sort direction for the result set | [optional]
 **id** | **str**| The Id of the resource | [optional]

### Return type

[**V1pre3LibraryPoolCompact**](V1pre3LibraryPoolCompact.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_librarypools_id_libraries**
> V2LibraryCompactExtendedV2LibrarySortFieldsResourceList get_v2_librarypools_id_libraries(id, include=include, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)

Get a list of libraries of a pool

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | The Id of the resource
include = ['include_example'] # list[str] | Sub elements to include in the response: LibraryIndex, YieldInformation (optional)
sortby = 'sortby_example' # str | The field(s) used to sort the result set (optional)
offset = 56 # int | The starting offset to read (optional)
limit = 56 # int | The maximum number of items to return (optional)
sortdir = 'sortdir_example' # str | The sort direction for the result set (optional)

try:
    # Get a list of libraries of a pool
    api_response = api_instance.get_v2_librarypools_id_libraries(id, include=include, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_librarypools_id_libraries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of the resource |
 **include** | [**list[str]**](str.md)| Sub elements to include in the response: LibraryIndex, YieldInformation | [optional]
 **sortby** | **str**| The field(s) used to sort the result set | [optional]
 **offset** | **int**| The starting offset to read | [optional]
 **limit** | **int**| The maximum number of items to return | [optional]
 **sortdir** | **str**| The sort direction for the result set | [optional]

### Return type

[**V2LibraryCompactExtendedV2LibrarySortFieldsResourceList**](V2LibraryCompactExtendedV2LibrarySortFieldsResourceList.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_librarypools_id_properties**
> V2PropertyCompactList get_v2_librarypools_id_properties(id, propertieslimit=propertieslimit, propertyitemslimit=propertyitemslimit, propertyfilters=propertyfilters, showhiddenitems=showhiddenitems, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)



List properties for a resource

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str |
propertieslimit = 56 # int | Limit the # of properties returned (optional)
propertyitemslimit = 56 # int | Limit the # of property items returned per property (optional)
propertyfilters = ['propertyfilters_example'] # list[str] | Filter by property name (optional)
showhiddenitems = 'showhiddenitems_example' # str | Show Hidden projects and Datasets (optional)
sortby = 'sortby_example' # str | The field(s) used to sort the result set (optional)
offset = 56 # int | The starting offset to read (optional)
limit = 56 # int | The maximum number of items to return (optional)
sortdir = 'sortdir_example' # str | The sort direction for the result set (optional)

try:
    api_response = api_instance.get_v2_librarypools_id_properties(id, propertieslimit=propertieslimit, propertyitemslimit=propertyitemslimit, propertyfilters=propertyfilters, showhiddenitems=showhiddenitems, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_librarypools_id_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **propertieslimit** | **int**| Limit the # of properties returned | [optional]
 **propertyitemslimit** | **int**| Limit the # of property items returned per property | [optional]
 **propertyfilters** | [**list[str]**](str.md)| Filter by property name | [optional]
 **showhiddenitems** | **str**| Show Hidden projects and Datasets | [optional]
 **sortby** | **str**| The field(s) used to sort the result set | [optional]
 **offset** | **int**| The starting offset to read | [optional]
 **limit** | **int**| The maximum number of items to return | [optional]
 **sortdir** | **str**| The sort direction for the result set | [optional]

### Return type

[**V2PropertyCompactList**](V2PropertyCompactList.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_librarypools_id_properties_name**
> V2Property get_v2_librarypools_id_properties_name(id, name, propertyitemslimit=propertyitemslimit, showhiddenitems=showhiddenitems)



Get property information

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str |
name = 'name_example' # str | Property name
propertyitemslimit = 56 # int | Limit the # of property items returned per property (optional)
showhiddenitems = 'showhiddenitems_example' # str | Hidden filter (optional)

try:
    api_response = api_instance.get_v2_librarypools_id_properties_name(id, name, propertyitemslimit=propertyitemslimit, showhiddenitems=showhiddenitems)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_librarypools_id_properties_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **name** | **str**| Property name |
 **propertyitemslimit** | **int**| Limit the # of property items returned per property | [optional]
 **showhiddenitems** | **str**| Hidden filter | [optional]

### Return type

[**V2Property**](V2Property.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_librarypools_id_properties_name_items**
> V2PropertyItemList get_v2_librarypools_id_properties_name_items(id, name, showhiddenitems=showhiddenitems, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)



Get property item details

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str |
name = 'name_example' # str | Property name
showhiddenitems = 'showhiddenitems_example' # str | Hidden filter (optional)
sortby = 'sortby_example' # str | The field(s) used to sort the result set (optional)
offset = 56 # int | The starting offset to read (optional)
limit = 56 # int | The maximum number of items to return (optional)
sortdir = 'sortdir_example' # str | The sort direction for the result set (optional)

try:
    api_response = api_instance.get_v2_librarypools_id_properties_name_items(id, name, showhiddenitems=showhiddenitems, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_librarypools_id_properties_name_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **name** | **str**| Property name |
 **showhiddenitems** | **str**| Hidden filter | [optional]
 **sortby** | **str**| The field(s) used to sort the result set | [optional]
 **offset** | **int**| The starting offset to read | [optional]
 **limit** | **int**| The maximum number of items to return | [optional]
 **sortdir** | **str**| The sort direction for the result set | [optional]

### Return type

[**V2PropertyItemList**](V2PropertyItemList.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_projects_id**
> V1pre3Project get_v2_projects_id(id, propertieslimit=propertieslimit, propertyitemslimit=propertyitemslimit, include=include)

Get information about a project

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | The Id of the resource
propertieslimit = 56 # int |  (optional)
propertyitemslimit = 56 # int |  (optional)
include = ['include_example'] # list[str] |  (optional)

try:
    # Get information about a project
    api_response = api_instance.get_v2_projects_id(id, propertieslimit=propertieslimit, propertyitemslimit=propertyitemslimit, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_projects_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of the resource |
 **propertieslimit** | **int**|  | [optional]
 **propertyitemslimit** | **int**|  | [optional]
 **include** | [**list[str]**](str.md)|  | [optional]

### Return type

[**V1pre3Project**](V1pre3Project.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_projects_id_datasets**
> V2DatasetCompactList get_v2_projects_id_datasets(id, isarchived=isarchived, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)

Get a list of datasets in a project

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | Project ID
isarchived = 'isarchived_example' # str | The archive states to filter by. Valid values include: True, False. (optional)
sortby = 'sortby_example' # str | The field(s) used to sort the result set (optional)
offset = 56 # int | The starting offset to read (optional)
limit = 56 # int | The maximum number of items to return (optional)
sortdir = 'sortdir_example' # str | The sort direction for the result set (optional)

try:
    # Get a list of datasets in a project
    api_response = api_instance.get_v2_projects_id_datasets(id, isarchived=isarchived, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_projects_id_datasets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project ID |
 **isarchived** | **str**| The archive states to filter by. Valid values include: True, False. | [optional]
 **sortby** | **str**| The field(s) used to sort the result set | [optional]
 **offset** | **int**| The starting offset to read | [optional]
 **limit** | **int**| The maximum number of items to return | [optional]
 **sortdir** | **str**| The sort direction for the result set | [optional]

### Return type

[**V2DatasetCompactList**](V2DatasetCompactList.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_projects_id_properties**
> V2PropertyCompactList get_v2_projects_id_properties(id, propertieslimit=propertieslimit, propertyitemslimit=propertyitemslimit, propertyfilters=propertyfilters, showhiddenitems=showhiddenitems, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)



List properties for a resource

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str |
propertieslimit = 56 # int | Limit the # of properties returned (optional)
propertyitemslimit = 56 # int | Limit the # of property items returned per property (optional)
propertyfilters = ['propertyfilters_example'] # list[str] | Filter by property name (optional)
showhiddenitems = 'showhiddenitems_example' # str | Show Hidden projects and Datasets (optional)
sortby = 'sortby_example' # str | The field(s) used to sort the result set (optional)
offset = 56 # int | The starting offset to read (optional)
limit = 56 # int | The maximum number of items to return (optional)
sortdir = 'sortdir_example' # str | The sort direction for the result set (optional)

try:
    api_response = api_instance.get_v2_projects_id_properties(id, propertieslimit=propertieslimit, propertyitemslimit=propertyitemslimit, propertyfilters=propertyfilters, showhiddenitems=showhiddenitems, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_projects_id_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **propertieslimit** | **int**| Limit the # of properties returned | [optional]
 **propertyitemslimit** | **int**| Limit the # of property items returned per property | [optional]
 **propertyfilters** | [**list[str]**](str.md)| Filter by property name | [optional]
 **showhiddenitems** | **str**| Show Hidden projects and Datasets | [optional]
 **sortby** | **str**| The field(s) used to sort the result set | [optional]
 **offset** | **int**| The starting offset to read | [optional]
 **limit** | **int**| The maximum number of items to return | [optional]
 **sortdir** | **str**| The sort direction for the result set | [optional]

### Return type

[**V2PropertyCompactList**](V2PropertyCompactList.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_projects_id_properties_name**
> V2Property get_v2_projects_id_properties_name(id, name, propertyitemslimit=propertyitemslimit, showhiddenitems=showhiddenitems)



Get property information

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str |
name = 'name_example' # str | Property name
propertyitemslimit = 56 # int | Limit the # of property items returned per property (optional)
showhiddenitems = 'showhiddenitems_example' # str | Hidden filter (optional)

try:
    api_response = api_instance.get_v2_projects_id_properties_name(id, name, propertyitemslimit=propertyitemslimit, showhiddenitems=showhiddenitems)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_projects_id_properties_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **name** | **str**| Property name |
 **propertyitemslimit** | **int**| Limit the # of property items returned per property | [optional]
 **showhiddenitems** | **str**| Hidden filter | [optional]

### Return type

[**V2Property**](V2Property.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_projects_id_properties_name_items**
> V2PropertyItemList get_v2_projects_id_properties_name_items(id, name, showhiddenitems=showhiddenitems, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)



Get property item details

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str |
name = 'name_example' # str | Property name
showhiddenitems = 'showhiddenitems_example' # str | Hidden filter (optional)
sortby = 'sortby_example' # str | The field(s) used to sort the result set (optional)
offset = 56 # int | The starting offset to read (optional)
limit = 56 # int | The maximum number of items to return (optional)
sortdir = 'sortdir_example' # str | The sort direction for the result set (optional)

try:
    api_response = api_instance.get_v2_projects_id_properties_name_items(id, name, showhiddenitems=showhiddenitems, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_projects_id_properties_name_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **name** | **str**| Property name |
 **showhiddenitems** | **str**| Hidden filter | [optional]
 **sortby** | **str**| The field(s) used to sort the result set | [optional]
 **offset** | **int**| The starting offset to read | [optional]
 **limit** | **int**| The maximum number of items to return | [optional]
 **sortdir** | **str**| The sort direction for the result set | [optional]

### Return type

[**V2PropertyItemList**](V2PropertyItemList.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_resourcemanifest**
> V2ResourceManifest get_v2_resourcemanifest(fileszipped, excludeemptyfiles, projects=projects, appsessions=appsessions, samples=samples, appresults=appresults, datasets=datasets, runmetrics=runmetrics, runlogs=runlogs, runimages=runimages, ipdrunparameters=ipdrunparameters, extensions=extensions, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir, id=id)

Get a manifest of filesets for the requested resources (max 300 items)

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
fileszipped = true # bool |
excludeemptyfiles = true # bool |
projects = ['projects_example'] # list[str] |  (optional)
appsessions = ['appsessions_example'] # list[str] |  (optional)
samples = ['samples_example'] # list[str] |  (optional)
appresults = ['appresults_example'] # list[str] |  (optional)
datasets = ['datasets_example'] # list[str] |  (optional)
runmetrics = ['runmetrics_example'] # list[str] |  (optional)
runlogs = ['runlogs_example'] # list[str] |  (optional)
runimages = ['runimages_example'] # list[str] |  (optional)
ipdrunparameters = ['ipdrunparameters_example'] # list[str] |  (optional)
extensions = ['extensions_example'] # list[str] |  (optional)
sortby = 'sortby_example' # str | The field(s) used to sort the result set (optional)
offset = 56 # int | The starting offset to read (optional)
limit = 56 # int | The maximum number of items to return (optional)
sortdir = 'sortdir_example' # str | The sort direction for the result set (optional)
id = 'id_example' # str | The Id of the resource (optional)

try:
    # Get a manifest of filesets for the requested resources (max 300 items)
    api_response = api_instance.get_v2_resourcemanifest(fileszipped, excludeemptyfiles, projects=projects, appsessions=appsessions, samples=samples, appresults=appresults, datasets=datasets, runmetrics=runmetrics, runlogs=runlogs, runimages=runimages, ipdrunparameters=ipdrunparameters, extensions=extensions, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir, id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_resourcemanifest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fileszipped** | **bool**|  |
 **excludeemptyfiles** | **bool**|  |
 **projects** | [**list[str]**](str.md)|  | [optional]
 **appsessions** | [**list[str]**](str.md)|  | [optional]
 **samples** | [**list[str]**](str.md)|  | [optional]
 **appresults** | [**list[str]**](str.md)|  | [optional]
 **datasets** | [**list[str]**](str.md)|  | [optional]
 **runmetrics** | [**list[str]**](str.md)|  | [optional]
 **runlogs** | [**list[str]**](str.md)|  | [optional]
 **runimages** | [**list[str]**](str.md)|  | [optional]
 **ipdrunparameters** | [**list[str]**](str.md)|  | [optional]
 **extensions** | [**list[str]**](str.md)|  | [optional]
 **sortby** | **str**| The field(s) used to sort the result set | [optional]
 **offset** | **int**| The starting offset to read | [optional]
 **limit** | **int**| The maximum number of items to return | [optional]
 **sortdir** | **str**| The sort direction for the result set | [optional]
 **id** | **str**| The Id of the resource | [optional]

### Return type

[**V2ResourceManifest**](V2ResourceManifest.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_runs**
> V2RunCompactList get_v2_runs(statuses=statuses, instrumenttype=instrumenttype, laneandqcstatuses=laneandqcstatuses, flowcellbarcode=flowcellbarcode, experimentname=experimentname, output_projects=output_projects, include=include, propertynamestartswith=propertynamestartswith, excludepropertynamestartswith=excludepropertynamestartswith, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir, id=id)

Get a list of runs accessible by current user

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
statuses = 'statuses_example' # str | The run statuses to filter by. Valid values include: New, Ready, Running, Paused, Stopped, Uploading, PendingAnalysis, Analyzing, Complete, Failed, NeedsAttention. Multiple values may be provided separated by commas. (optional)
instrumenttype = 'instrumenttype_example' # str | The instrument type to filter by. (optional)
laneandqcstatuses = 'laneandqcstatuses_example' # str | The lane and QC statues to filter by.  Valid values include: Inital, QcPassed, and LaneQcFailed.  Multiple values may be separated by commas. (optional)
flowcellbarcode = 'flowcellbarcode_example' # str | The flowcell barcode to filter by. To request empty barcodes, provide an empty string (optional)
experimentname = 'experimentname_example' # str | The experiment name to filter by. (optional)
output_projects = [56] # list[int] | The project ids to filter by. (optional)
include = ['include_example'] # list[str] | Sub elements to include in the response (optional)
propertynamestartswith = ['propertynamestartswith_example'] # list[str] | Filter properties by name starting with. Max items returned is 1024. (optional)
excludepropertynamestartswith = ['excludepropertynamestartswith_example'] # list[str] | Filter properties by name not starting with. Max items returned is 1024. (optional)
sortby = 'sortby_example' # str | The field(s) used to sort the result set (optional)
offset = 56 # int | The starting offset to read (optional)
limit = 56 # int | The maximum number of items to return (optional)
sortdir = 'sortdir_example' # str | The sort direction for the result set (optional)
id = 'id_example' # str | The Id of the resource (optional)

try:
    # Get a list of runs accessible by current user
    api_response = api_instance.get_v2_runs(statuses=statuses, instrumenttype=instrumenttype, laneandqcstatuses=laneandqcstatuses, flowcellbarcode=flowcellbarcode, experimentname=experimentname, output_projects=output_projects, include=include, propertynamestartswith=propertynamestartswith, excludepropertynamestartswith=excludepropertynamestartswith, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir, id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_runs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **statuses** | **str**| The run statuses to filter by. Valid values include: New, Ready, Running, Paused, Stopped, Uploading, PendingAnalysis, Analyzing, Complete, Failed, NeedsAttention. Multiple values may be provided separated by commas. | [optional]
 **instrumenttype** | **str**| The instrument type to filter by. | [optional]
 **laneandqcstatuses** | **str**| The lane and QC statues to filter by.  Valid values include: Inital, QcPassed, and LaneQcFailed.  Multiple values may be separated by commas. | [optional]
 **flowcellbarcode** | **str**| The flowcell barcode to filter by. To request empty barcodes, provide an empty string | [optional]
 **experimentname** | **str**| The experiment name to filter by. | [optional]
 **output_projects** | [**list[int]**](int.md)| The project ids to filter by. | [optional]
 **include** | [**list[str]**](str.md)| Sub elements to include in the response | [optional]
 **propertynamestartswith** | [**list[str]**](str.md)| Filter properties by name starting with. Max items returned is 1024. | [optional]
 **excludepropertynamestartswith** | [**list[str]**](str.md)| Filter properties by name not starting with. Max items returned is 1024. | [optional]
 **sortby** | **str**| The field(s) used to sort the result set | [optional]
 **offset** | **int**| The starting offset to read | [optional]
 **limit** | **int**| The maximum number of items to return | [optional]
 **sortdir** | **str**| The sort direction for the result set | [optional]
 **id** | **str**| The Id of the resource | [optional]

### Return type

[**V2RunCompactList**](V2RunCompactList.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_runs_accesscheck**
> list[V2RunAccess] get_v2_runs_accesscheck(ids=ids)



check user access for the run ids and returned filtered list

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
ids = [56] # list[int] |  (optional)

try:
    api_response = api_instance.get_v2_runs_accesscheck(ids=ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_runs_accesscheck: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)|  | [optional]

### Return type

[**list[V2RunAccess]**](V2RunAccess.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_runs_id**
> V2Run get_v2_runs_id(id, propertieslimit=propertieslimit, propertyitemslimit=propertyitemslimit, include=include)

Get information about a run

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | The Id of the resource
propertieslimit = 56 # int |  (optional)
propertyitemslimit = 56 # int |  (optional)
include = ['include_example'] # list[str] |  (optional)

try:
    # Get information about a run
    api_response = api_instance.get_v2_runs_id(id, propertieslimit=propertieslimit, propertyitemslimit=propertyitemslimit, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_runs_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of the resource |
 **propertieslimit** | **int**|  | [optional]
 **propertyitemslimit** | **int**|  | [optional]
 **include** | [**list[str]**](str.md)|  | [optional]

### Return type

[**V2Run**](V2Run.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_runs_id_file_upload_info**
> V2PresignedUrlForUpload get_v2_runs_id_file_upload_info(id, filepath=filepath, uploadpartcount=uploadpartcount)



Request direct file upload presigned url information for a new file in the specified resource (sample or run)

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | The Id of the resource
filepath = 'filepath_example' # str |  (optional)
uploadpartcount = 56 # int |  (optional)

try:
    api_response = api_instance.get_v2_runs_id_file_upload_info(id, filepath=filepath, uploadpartcount=uploadpartcount)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_runs_id_file_upload_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of the resource |
 **filepath** | **str**|  | [optional]
 **uploadpartcount** | **int**|  | [optional]

### Return type

[**V2PresignedUrlForUpload**](V2PresignedUrlForUpload.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_runs_id_files**
> V2FilesList get_v2_runs_id_files(filehrefcontentresolution, recursive, id, extensions=extensions, excludeextensions=excludeextensions, directory=directory, statuses=statuses, include=include, pathprefix=pathprefix, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)

Get a list of files of a run

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
filehrefcontentresolution = true # bool | Resolves the HrefContent to the direct file URI to avoid a hop to GET: files/{id}/content
recursive = true # bool | If a 'directory' is provided, files in subfolders of the given directory are also included
id = 'id_example' # str | The Id of the resource
extensions = 'extensions_example' # str | The file extensions to filter by (comma-separated) (optional)
excludeextensions = 'excludeextensions_example' # str | The file extensions to exclude (comma-separated) (optional)
directory = 'directory_example' # str | The directory path to filter by (root is /) (optional)
statuses = ['statuses_example'] # list[str] | Optionally filter by status (default complete) (optional)
include = ['include_example'] # list[str] | Possible values: 'Subdirectories', 'TotalCount' (optional)
pathprefix = 'pathprefix_example' # str | To be pre-fixed in the path of the file (optional)
sortby = 'sortby_example' # str | The field(s) used to sort the result set (optional)
offset = 56 # int | The starting offset to read (optional)
limit = 56 # int | The maximum number of items to return (optional)
sortdir = 'sortdir_example' # str | The sort direction for the result set (optional)

try:
    # Get a list of files of a run
    api_response = api_instance.get_v2_runs_id_files(filehrefcontentresolution, recursive, id, extensions=extensions, excludeextensions=excludeextensions, directory=directory, statuses=statuses, include=include, pathprefix=pathprefix, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_runs_id_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filehrefcontentresolution** | **bool**| Resolves the HrefContent to the direct file URI to avoid a hop to GET: files/{id}/content |
 **recursive** | **bool**| If a &#x27;directory&#x27; is provided, files in subfolders of the given directory are also included |
 **id** | **str**| The Id of the resource |
 **extensions** | **str**| The file extensions to filter by (comma-separated) | [optional]
 **excludeextensions** | **str**| The file extensions to exclude (comma-separated) | [optional]
 **directory** | **str**| The directory path to filter by (root is /) | [optional]
 **statuses** | [**list[str]**](str.md)| Optionally filter by status (default complete) | [optional]
 **include** | [**list[str]**](str.md)| Possible values: &#x27;Subdirectories&#x27;, &#x27;TotalCount&#x27; | [optional]
 **pathprefix** | **str**| To be pre-fixed in the path of the file | [optional]
 **sortby** | **str**| The field(s) used to sort the result set | [optional]
 **offset** | **int**| The starting offset to read | [optional]
 **limit** | **int**| The maximum number of items to return | [optional]
 **sortdir** | **str**| The sort direction for the result set | [optional]

### Return type

[**V2FilesList**](V2FilesList.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_runs_id_properties**
> V2PropertyCompactList get_v2_runs_id_properties(id, propertieslimit=propertieslimit, propertyitemslimit=propertyitemslimit, propertyfilters=propertyfilters, showhiddenitems=showhiddenitems, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)



List properties for a resource

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str |
propertieslimit = 56 # int | Limit the # of properties returned (optional)
propertyitemslimit = 56 # int | Limit the # of property items returned per property (optional)
propertyfilters = ['propertyfilters_example'] # list[str] | Filter by property name (optional)
showhiddenitems = 'showhiddenitems_example' # str | Show Hidden projects and Datasets (optional)
sortby = 'sortby_example' # str | The field(s) used to sort the result set (optional)
offset = 56 # int | The starting offset to read (optional)
limit = 56 # int | The maximum number of items to return (optional)
sortdir = 'sortdir_example' # str | The sort direction for the result set (optional)

try:
    api_response = api_instance.get_v2_runs_id_properties(id, propertieslimit=propertieslimit, propertyitemslimit=propertyitemslimit, propertyfilters=propertyfilters, showhiddenitems=showhiddenitems, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_runs_id_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **propertieslimit** | **int**| Limit the # of properties returned | [optional]
 **propertyitemslimit** | **int**| Limit the # of property items returned per property | [optional]
 **propertyfilters** | [**list[str]**](str.md)| Filter by property name | [optional]
 **showhiddenitems** | **str**| Show Hidden projects and Datasets | [optional]
 **sortby** | **str**| The field(s) used to sort the result set | [optional]
 **offset** | **int**| The starting offset to read | [optional]
 **limit** | **int**| The maximum number of items to return | [optional]
 **sortdir** | **str**| The sort direction for the result set | [optional]

### Return type

[**V2PropertyCompactList**](V2PropertyCompactList.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_runs_id_properties_name**
> V2Property get_v2_runs_id_properties_name(id, name, propertyitemslimit=propertyitemslimit, showhiddenitems=showhiddenitems)



Get property information

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str |
name = 'name_example' # str | Property name
propertyitemslimit = 56 # int | Limit the # of property items returned per property (optional)
showhiddenitems = 'showhiddenitems_example' # str | Hidden filter (optional)

try:
    api_response = api_instance.get_v2_runs_id_properties_name(id, name, propertyitemslimit=propertyitemslimit, showhiddenitems=showhiddenitems)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_runs_id_properties_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **name** | **str**| Property name |
 **propertyitemslimit** | **int**| Limit the # of property items returned per property | [optional]
 **showhiddenitems** | **str**| Hidden filter | [optional]

### Return type

[**V2Property**](V2Property.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_runs_id_properties_name_items**
> V2PropertyItemList get_v2_runs_id_properties_name_items(id, name, showhiddenitems=showhiddenitems, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)



Get property item details

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str |
name = 'name_example' # str | Property name
showhiddenitems = 'showhiddenitems_example' # str | Hidden filter (optional)
sortby = 'sortby_example' # str | The field(s) used to sort the result set (optional)
offset = 56 # int | The starting offset to read (optional)
limit = 56 # int | The maximum number of items to return (optional)
sortdir = 'sortdir_example' # str | The sort direction for the result set (optional)

try:
    api_response = api_instance.get_v2_runs_id_properties_name_items(id, name, showhiddenitems=showhiddenitems, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_runs_id_properties_name_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **name** | **str**| Property name |
 **showhiddenitems** | **str**| Hidden filter | [optional]
 **sortby** | **str**| The field(s) used to sort the result set | [optional]
 **offset** | **int**| The starting offset to read | [optional]
 **limit** | **int**| The maximum number of items to return | [optional]
 **sortdir** | **str**| The sort direction for the result set | [optional]

### Return type

[**V2PropertyItemList**](V2PropertyItemList.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_runs_id_samplesheet**
> V2RunSampleSheet get_v2_runs_id_samplesheet(id)



Request run sample sheet

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | The Id of the resource

try:
    api_response = api_instance.get_v2_runs_id_samplesheet(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_runs_id_samplesheet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of the resource |

### Return type

[**V2RunSampleSheet**](V2RunSampleSheet.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_runs_id_sequencingstats**
> V2SequencingStats get_v2_runs_id_sequencingstats(id)



Request sequencing stats

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | The Id of the resource

try:
    api_response = api_instance.get_v2_runs_id_sequencingstats(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_runs_id_sequencingstats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of the resource |

### Return type

[**V2SequencingStats**](V2SequencingStats.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_runuploadtest**
> V2Run get_v2_runuploadtest()



### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))

try:
    api_response = api_instance.get_v2_runuploadtest()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_runuploadtest: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**V2Run**](V2Run.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_samples_id_file_upload_info**
> V2PresignedUrlForUpload get_v2_samples_id_file_upload_info(id, filepath=filepath, uploadpartcount=uploadpartcount)



Request direct file upload presigned url information for a new file in the specified resource (sample or run)

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | The Id of the resource
filepath = 'filepath_example' # str |  (optional)
uploadpartcount = 56 # int |  (optional)

try:
    api_response = api_instance.get_v2_samples_id_file_upload_info(id, filepath=filepath, uploadpartcount=uploadpartcount)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_samples_id_file_upload_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of the resource |
 **filepath** | **str**|  | [optional]
 **uploadpartcount** | **int**|  | [optional]

### Return type

[**V2PresignedUrlForUpload**](V2PresignedUrlForUpload.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_subjects_id_properties**
> V2PropertyCompactList get_v2_subjects_id_properties(id, propertieslimit=propertieslimit, propertyitemslimit=propertyitemslimit, propertyfilters=propertyfilters, showhiddenitems=showhiddenitems, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)



List properties for a resource

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str |
propertieslimit = 56 # int | Limit the # of properties returned (optional)
propertyitemslimit = 56 # int | Limit the # of property items returned per property (optional)
propertyfilters = ['propertyfilters_example'] # list[str] | Filter by property name (optional)
showhiddenitems = 'showhiddenitems_example' # str | Show Hidden projects and Datasets (optional)
sortby = 'sortby_example' # str | The field(s) used to sort the result set (optional)
offset = 56 # int | The starting offset to read (optional)
limit = 56 # int | The maximum number of items to return (optional)
sortdir = 'sortdir_example' # str | The sort direction for the result set (optional)

try:
    api_response = api_instance.get_v2_subjects_id_properties(id, propertieslimit=propertieslimit, propertyitemslimit=propertyitemslimit, propertyfilters=propertyfilters, showhiddenitems=showhiddenitems, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_subjects_id_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **propertieslimit** | **int**| Limit the # of properties returned | [optional]
 **propertyitemslimit** | **int**| Limit the # of property items returned per property | [optional]
 **propertyfilters** | [**list[str]**](str.md)| Filter by property name | [optional]
 **showhiddenitems** | **str**| Show Hidden projects and Datasets | [optional]
 **sortby** | **str**| The field(s) used to sort the result set | [optional]
 **offset** | **int**| The starting offset to read | [optional]
 **limit** | **int**| The maximum number of items to return | [optional]
 **sortdir** | **str**| The sort direction for the result set | [optional]

### Return type

[**V2PropertyCompactList**](V2PropertyCompactList.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_subjects_id_properties_name**
> V2Property get_v2_subjects_id_properties_name(id, name, propertyitemslimit=propertyitemslimit, showhiddenitems=showhiddenitems)



Get property information

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str |
name = 'name_example' # str | Property name
propertyitemslimit = 56 # int | Limit the # of property items returned per property (optional)
showhiddenitems = 'showhiddenitems_example' # str | Hidden filter (optional)

try:
    api_response = api_instance.get_v2_subjects_id_properties_name(id, name, propertyitemslimit=propertyitemslimit, showhiddenitems=showhiddenitems)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_subjects_id_properties_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **name** | **str**| Property name |
 **propertyitemslimit** | **int**| Limit the # of property items returned per property | [optional]
 **showhiddenitems** | **str**| Hidden filter | [optional]

### Return type

[**V2Property**](V2Property.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_subjects_id_properties_name_items**
> V2PropertyItemList get_v2_subjects_id_properties_name_items(id, name, showhiddenitems=showhiddenitems, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)



Get property item details

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str |
name = 'name_example' # str | Property name
showhiddenitems = 'showhiddenitems_example' # str | Hidden filter (optional)
sortby = 'sortby_example' # str | The field(s) used to sort the result set (optional)
offset = 56 # int | The starting offset to read (optional)
limit = 56 # int | The maximum number of items to return (optional)
sortdir = 'sortdir_example' # str | The sort direction for the result set (optional)

try:
    api_response = api_instance.get_v2_subjects_id_properties_name_items(id, name, showhiddenitems=showhiddenitems, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_subjects_id_properties_name_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **name** | **str**| Property name |
 **showhiddenitems** | **str**| Hidden filter | [optional]
 **sortby** | **str**| The field(s) used to sort the result set | [optional]
 **offset** | **int**| The starting offset to read | [optional]
 **limit** | **int**| The maximum number of items to return | [optional]
 **sortdir** | **str**| The sort direction for the result set | [optional]

### Return type

[**V2PropertyItemList**](V2PropertyItemList.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_trash**
> V1pre3TrashItemCompactList get_v2_trash(sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)

Get a list of items in the trash

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
sortby = 'sortby_example' # str | The field(s) used to sort the result set (optional)
offset = 56 # int | The starting offset to read (optional)
limit = 56 # int | The maximum number of items to return (optional)
sortdir = 'sortdir_example' # str | The sort direction for the result set (optional)

try:
    # Get a list of items in the trash
    api_response = api_instance.get_v2_trash(sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_trash: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortby** | **str**| The field(s) used to sort the result set | [optional]
 **offset** | **int**| The starting offset to read | [optional]
 **limit** | **int**| The maximum number of items to return | [optional]
 **sortdir** | **str**| The sort direction for the result set | [optional]

### Return type

[**V1pre3TrashItemCompactList**](V1pre3TrashItemCompactList.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_trash_id**
> V1pre3TrashItem get_v2_trash_id(id)

Get information about an item in the trash

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | The Id of the resource

try:
    # Get information about an item in the trash
    api_response = api_instance.get_v2_trash_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_trash_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of the resource |

### Return type

[**V1pre3TrashItem**](V1pre3TrashItem.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_useragreements**
> V2UserAgreementCompactList get_v2_useragreements(applicationid=applicationid, title=title, category=category, include=include, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir, id=id)

Get information about agreements visible to the current user

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
applicationid = 'applicationid_example' # str | If specified, only return agreements for this application. If not, only return agreements not associated with an application. (optional)
title = 'title_example' # str | If specified, only return agreements with titles exactly matching the specified value. (optional)
category = 'category_example' # str | If specified, only return agreements with category exactly matching the specified value. (optional)
include = ['include_example'] # list[str] | Expand or filter the agreements returned. Include=Expired will return expired agreements, giving a history of all agreements ever signed by the user. Include=Pending looks for agreements that the user hasn't signed yet. (optional)
sortby = 'sortby_example' # str | The field(s) used to sort the result set (optional)
offset = 56 # int | The starting offset to read (optional)
limit = 56 # int | The maximum number of items to return (optional)
sortdir = 'sortdir_example' # str | The sort direction for the result set (optional)
id = 'id_example' # str | The Id of the resource (optional)

try:
    # Get information about agreements visible to the current user
    api_response = api_instance.get_v2_useragreements(applicationid=applicationid, title=title, category=category, include=include, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir, id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_useragreements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationid** | **str**| If specified, only return agreements for this application. If not, only return agreements not associated with an application. | [optional]
 **title** | **str**| If specified, only return agreements with titles exactly matching the specified value. | [optional]
 **category** | **str**| If specified, only return agreements with category exactly matching the specified value. | [optional]
 **include** | [**list[str]**](str.md)| Expand or filter the agreements returned. Include&#x3D;Expired will return expired agreements, giving a history of all agreements ever signed by the user. Include&#x3D;Pending looks for agreements that the user hasn&#x27;t signed yet. | [optional]
 **sortby** | **str**| The field(s) used to sort the result set | [optional]
 **offset** | **int**| The starting offset to read | [optional]
 **limit** | **int**| The maximum number of items to return | [optional]
 **sortdir** | **str**| The sort direction for the result set | [optional]
 **id** | **str**| The Id of the resource | [optional]

### Return type

[**V2UserAgreementCompactList**](V2UserAgreementCompactList.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_users_current**
> V2User get_v2_users_current(options=options, include=include, id=id)

Get information about the current user's account

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
options = 'options_example' # str |  (optional)
include = ['include_example'] # list[str] |  (optional)
id = 'id_example' # str | The Id of the resource (optional)

try:
    # Get information about the current user's account
    api_response = api_instance.get_v2_users_current(options=options, include=include, id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_users_current: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **options** | **str**|  | [optional]
 **include** | [**list[str]**](str.md)|  | [optional]
 **id** | **str**| The Id of the resource | [optional]

### Return type

[**V2User**](V2User.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_users_current_labtype**
> V2Error get_v2_users_current_labtype(id=id)

Is user a wet lab or dry lab user?

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | The Id of the resource (optional)

try:
    # Is user a wet lab or dry lab user?
    api_response = api_instance.get_v2_users_current_labtype(id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_users_current_labtype: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of the resource | [optional]

### Return type

[**V2Error**](V2Error.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_users_current_messages**
> V2Error get_v2_users_current_messages(sortby=sortby, offset=offset, limit=limit, sortdir=sortdir, id=id)

Get a list of messages that have been sent to the requesting user.

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
sortby = 'sortby_example' # str | The field(s) used to sort the result set (optional)
offset = 56 # int | The starting offset to read (optional)
limit = 56 # int | The maximum number of items to return (optional)
sortdir = 'sortdir_example' # str | The sort direction for the result set (optional)
id = 'id_example' # str | The Id of the resource (optional)

try:
    # Get a list of messages that have been sent to the requesting user.
    api_response = api_instance.get_v2_users_current_messages(sortby=sortby, offset=offset, limit=limit, sortdir=sortdir, id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_users_current_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sortby** | **str**| The field(s) used to sort the result set | [optional]
 **offset** | **int**| The starting offset to read | [optional]
 **limit** | **int**| The maximum number of items to return | [optional]
 **sortdir** | **str**| The sort direction for the result set | [optional]
 **id** | **str**| The Id of the resource | [optional]

### Return type

[**V2Error**](V2Error.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_users_current_notifications**
> V2UserNotificationCompactList get_v2_users_current_notifications(streamtype, attentionrequired, category=category, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir, id=id)



List notifications for a user

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
streamtype = 'streamtype_example' # str | The classification of user notifications to receive. Applicable values are 'All', 'Activity', 'Storage', 'DataDeletion', 'Subscription', 'CMS'
attentionrequired = true # bool | AttentionRequired
category = 'category_example' # str | The category within a 'Stream' of user notifications to receive. Currently only 'Activity' Stream supports Categories. Applicable values are 'All', 'Run', 'AppSession', 'Invite' (optional)
sortby = 'sortby_example' # str | The field(s) used to sort the result set (optional)
offset = 56 # int | The starting offset to read (optional)
limit = 56 # int | The maximum number of items to return (optional)
sortdir = 'sortdir_example' # str | The sort direction for the result set (optional)
id = 'id_example' # str | The Id of the resource (optional)

try:
    api_response = api_instance.get_v2_users_current_notifications(streamtype, attentionrequired, category=category, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir, id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_users_current_notifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **streamtype** | **str**| The classification of user notifications to receive. Applicable values are &#x27;All&#x27;, &#x27;Activity&#x27;, &#x27;Storage&#x27;, &#x27;DataDeletion&#x27;, &#x27;Subscription&#x27;, &#x27;CMS&#x27;  |
 **attentionrequired** | **bool**| AttentionRequired |
 **category** | **str**| The category within a &#x27;Stream&#x27; of user notifications to receive. Currently only &#x27;Activity&#x27; Stream supports Categories. Applicable values are &#x27;All&#x27;, &#x27;Run&#x27;, &#x27;AppSession&#x27;, &#x27;Invite&#x27; | [optional]
 **sortby** | **str**| The field(s) used to sort the result set | [optional]
 **offset** | **int**| The starting offset to read | [optional]
 **limit** | **int**| The maximum number of items to return | [optional]
 **sortdir** | **str**| The sort direction for the result set | [optional]
 **id** | **str**| The Id of the resource | [optional]

### Return type

[**V2UserNotificationCompactList**](V2UserNotificationCompactList.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_users_current_properties**
> V2PropertyCompactList get_v2_users_current_properties(id=id, propertieslimit=propertieslimit, propertyitemslimit=propertyitemslimit, propertyfilters=propertyfilters, showhiddenitems=showhiddenitems, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)



List properties for a resource

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str |  (optional)
propertieslimit = 56 # int | Limit the # of properties returned (optional)
propertyitemslimit = 56 # int | Limit the # of property items returned per property (optional)
propertyfilters = ['propertyfilters_example'] # list[str] | Filter by property name (optional)
showhiddenitems = 'showhiddenitems_example' # str | Show Hidden projects and Datasets (optional)
sortby = 'sortby_example' # str | The field(s) used to sort the result set (optional)
offset = 56 # int | The starting offset to read (optional)
limit = 56 # int | The maximum number of items to return (optional)
sortdir = 'sortdir_example' # str | The sort direction for the result set (optional)

try:
    api_response = api_instance.get_v2_users_current_properties(id=id, propertieslimit=propertieslimit, propertyitemslimit=propertyitemslimit, propertyfilters=propertyfilters, showhiddenitems=showhiddenitems, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_users_current_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | [optional]
 **propertieslimit** | **int**| Limit the # of properties returned | [optional]
 **propertyitemslimit** | **int**| Limit the # of property items returned per property | [optional]
 **propertyfilters** | [**list[str]**](str.md)| Filter by property name | [optional]
 **showhiddenitems** | **str**| Show Hidden projects and Datasets | [optional]
 **sortby** | **str**| The field(s) used to sort the result set | [optional]
 **offset** | **int**| The starting offset to read | [optional]
 **limit** | **int**| The maximum number of items to return | [optional]
 **sortdir** | **str**| The sort direction for the result set | [optional]

### Return type

[**V2PropertyCompactList**](V2PropertyCompactList.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_users_current_properties_name**
> V2Property get_v2_users_current_properties_name(name, id=id, propertyitemslimit=propertyitemslimit, showhiddenitems=showhiddenitems)



Get property information

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
name = 'name_example' # str | Property name
id = 'id_example' # str |  (optional)
propertyitemslimit = 56 # int | Limit the # of property items returned per property (optional)
showhiddenitems = 'showhiddenitems_example' # str | Hidden filter (optional)

try:
    api_response = api_instance.get_v2_users_current_properties_name(name, id=id, propertyitemslimit=propertyitemslimit, showhiddenitems=showhiddenitems)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_users_current_properties_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Property name |
 **id** | **str**|  | [optional]
 **propertyitemslimit** | **int**| Limit the # of property items returned per property | [optional]
 **showhiddenitems** | **str**| Hidden filter | [optional]

### Return type

[**V2Property**](V2Property.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_users_current_properties_name_items**
> V2PropertyItemList get_v2_users_current_properties_name_items(name, id=id, showhiddenitems=showhiddenitems, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)



Get property item details

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
name = 'name_example' # str | Property name
id = 'id_example' # str |  (optional)
showhiddenitems = 'showhiddenitems_example' # str | Hidden filter (optional)
sortby = 'sortby_example' # str | The field(s) used to sort the result set (optional)
offset = 56 # int | The starting offset to read (optional)
limit = 56 # int | The maximum number of items to return (optional)
sortdir = 'sortdir_example' # str | The sort direction for the result set (optional)

try:
    api_response = api_instance.get_v2_users_current_properties_name_items(name, id=id, showhiddenitems=showhiddenitems, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_users_current_properties_name_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Property name |
 **id** | **str**|  | [optional]
 **showhiddenitems** | **str**| Hidden filter | [optional]
 **sortby** | **str**| The field(s) used to sort the result set | [optional]
 **offset** | **int**| The starting offset to read | [optional]
 **limit** | **int**| The maximum number of items to return | [optional]
 **sortdir** | **str**| The sort direction for the result set | [optional]

### Return type

[**V2PropertyItemList**](V2PropertyItemList.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_users_current_subscription**
> V2UserSubscription get_v2_users_current_subscription(refreshcache, id=id)

Get information about the current user�s subscriptions

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
refreshcache = true # bool |
id = 'id_example' # str | The Id of the resource (optional)

try:
    # Get information about the current user�s subscriptions
    api_response = api_instance.get_v2_users_current_subscription(refreshcache, id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_users_current_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refreshcache** | **bool**|  |
 **id** | **str**| The Id of the resource | [optional]

### Return type

[**V2UserSubscription**](V2UserSubscription.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_users_current_usage**
> V2PeriodAggregateUsageList get_v2_users_current_usage(includeloggedinuser, periods, refreshcache, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir, id=id)

Get usage statistics for the user

Information about storage and compute usage will be returned for the user’s personal account, as well as any workgroups they own.

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
includeloggedinuser = true # bool |
periods = 56 # int |
refreshcache = true # bool |
sortby = 'sortby_example' # str | The field(s) used to sort the result set (optional)
offset = 56 # int | The starting offset to read (optional)
limit = 56 # int | The maximum number of items to return (optional)
sortdir = 'sortdir_example' # str | The sort direction for the result set (optional)
id = 'id_example' # str | The Id of the resource (optional)

try:
    # Get usage statistics for the user
    api_response = api_instance.get_v2_users_current_usage(includeloggedinuser, periods, refreshcache, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir, id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_users_current_usage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **includeloggedinuser** | **bool**|  |
 **periods** | **int**|  |
 **refreshcache** | **bool**|  |
 **sortby** | **str**| The field(s) used to sort the result set | [optional]
 **offset** | **int**| The starting offset to read | [optional]
 **limit** | **int**| The maximum number of items to return | [optional]
 **sortdir** | **str**| The sort direction for the result set | [optional]
 **id** | **str**| The Id of the resource | [optional]

### Return type

[**V2PeriodAggregateUsageList**](V2PeriodAggregateUsageList.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_users_id**
> V2User get_v2_users_id(id, options=options, include=include)

Get information about a user

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | The Id of the resource
options = 'options_example' # str |  (optional)
include = ['include_example'] # list[str] |  (optional)

try:
    # Get information about a user
    api_response = api_instance.get_v2_users_id(id, options=options, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_users_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of the resource |
 **options** | **str**|  | [optional]
 **include** | [**list[str]**](str.md)|  | [optional]

### Return type

[**V2User**](V2User.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_users_id_autodeletionevents**
> V2Error get_v2_users_id_autodeletionevents(id, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)

Get a list of auto-deletion events for the specified user.

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | The Id of the resource
sortby = 'sortby_example' # str | The field(s) used to sort the result set (optional)
offset = 56 # int | The starting offset to read (optional)
limit = 56 # int | The maximum number of items to return (optional)
sortdir = 'sortdir_example' # str | The sort direction for the result set (optional)

try:
    # Get a list of auto-deletion events for the specified user.
    api_response = api_instance.get_v2_users_id_autodeletionevents(id, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_users_id_autodeletionevents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of the resource |
 **sortby** | **str**| The field(s) used to sort the result set | [optional]
 **offset** | **int**| The starting offset to read | [optional]
 **limit** | **int**| The maximum number of items to return | [optional]
 **sortdir** | **str**| The sort direction for the result set | [optional]

### Return type

[**V2Error**](V2Error.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_users_id_messages**
> V2Error get_v2_users_id_messages(id, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)

Get a list of messages that have been sent to a specific user.

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | The Id of the resource
sortby = 'sortby_example' # str | The field(s) used to sort the result set (optional)
offset = 56 # int | The starting offset to read (optional)
limit = 56 # int | The maximum number of items to return (optional)
sortdir = 'sortdir_example' # str | The sort direction for the result set (optional)

try:
    # Get a list of messages that have been sent to a specific user.
    api_response = api_instance.get_v2_users_id_messages(id, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_users_id_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of the resource |
 **sortby** | **str**| The field(s) used to sort the result set | [optional]
 **offset** | **int**| The starting offset to read | [optional]
 **limit** | **int**| The maximum number of items to return | [optional]
 **sortdir** | **str**| The sort direction for the result set | [optional]

### Return type

[**V2Error**](V2Error.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_users_id_notifications**
> V2UserNotificationCompactList get_v2_users_id_notifications(streamtype, attentionrequired, id, category=category, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)



List notifications for a user

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
streamtype = 'streamtype_example' # str | The classification of user notifications to receive. Applicable values are 'All', 'Activity', 'Storage', 'DataDeletion', 'Subscription', 'CMS'
attentionrequired = true # bool | AttentionRequired
id = 'id_example' # str | The Id of the resource
category = 'category_example' # str | The category within a 'Stream' of user notifications to receive. Currently only 'Activity' Stream supports Categories. Applicable values are 'All', 'Run', 'AppSession', 'Invite' (optional)
sortby = 'sortby_example' # str | The field(s) used to sort the result set (optional)
offset = 56 # int | The starting offset to read (optional)
limit = 56 # int | The maximum number of items to return (optional)
sortdir = 'sortdir_example' # str | The sort direction for the result set (optional)

try:
    api_response = api_instance.get_v2_users_id_notifications(streamtype, attentionrequired, id, category=category, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_users_id_notifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **streamtype** | **str**| The classification of user notifications to receive. Applicable values are &#x27;All&#x27;, &#x27;Activity&#x27;, &#x27;Storage&#x27;, &#x27;DataDeletion&#x27;, &#x27;Subscription&#x27;, &#x27;CMS&#x27;  |
 **attentionrequired** | **bool**| AttentionRequired |
 **id** | **str**| The Id of the resource |
 **category** | **str**| The category within a &#x27;Stream&#x27; of user notifications to receive. Currently only &#x27;Activity&#x27; Stream supports Categories. Applicable values are &#x27;All&#x27;, &#x27;Run&#x27;, &#x27;AppSession&#x27;, &#x27;Invite&#x27; | [optional]
 **sortby** | **str**| The field(s) used to sort the result set | [optional]
 **offset** | **int**| The starting offset to read | [optional]
 **limit** | **int**| The maximum number of items to return | [optional]
 **sortdir** | **str**| The sort direction for the result set | [optional]

### Return type

[**V2UserNotificationCompactList**](V2UserNotificationCompactList.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_users_id_settings**
> V2UserSettingList get_v2_users_id_settings(id, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)

Get a list of the user's settings

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | The Id of the resource
sortby = 'sortby_example' # str | The field(s) used to sort the result set (optional)
offset = 56 # int | The starting offset to read (optional)
limit = 56 # int | The maximum number of items to return (optional)
sortdir = 'sortdir_example' # str | The sort direction for the result set (optional)

try:
    # Get a list of the user's settings
    api_response = api_instance.get_v2_users_id_settings(id, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_users_id_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of the resource |
 **sortby** | **str**| The field(s) used to sort the result set | [optional]
 **offset** | **int**| The starting offset to read | [optional]
 **limit** | **int**| The maximum number of items to return | [optional]
 **sortdir** | **str**| The sort direction for the result set | [optional]

### Return type

[**V2UserSettingList**](V2UserSettingList.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_users_id_subscription**
> V2UserSubscription get_v2_users_id_subscription(refreshcache, id)

Get information about a user's subscriptions

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
refreshcache = true # bool |
id = 'id_example' # str | The Id of the resource

try:
    # Get information about a user's subscriptions
    api_response = api_instance.get_v2_users_id_subscription(refreshcache, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_users_id_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refreshcache** | **bool**|  |
 **id** | **str**| The Id of the resource |

### Return type

[**V2UserSubscription**](V2UserSubscription.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_users_id_workgroups**
> V2WorkgroupList get_v2_users_id_workgroups(includeloggedinuser, activeonly, refreshcache, includesubscription, id, include=include, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)

Get a list of workgroups the user belongs to

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
includeloggedinuser = true # bool | Includes current user
activeonly = true # bool | Excludes inactive workgroups
refreshcache = true # bool | This will force a refresh on the workgroup subscriptions
includesubscription = true # bool | This will include subscription in the response
id = 'id_example' # str | The Id of the resource
include = ['include_example'] # list[str] | Sub elements to include in the response: LoggedInUser, IsDefaultRunUploadWorkgroup (optional)
sortby = 'sortby_example' # str | The field(s) used to sort the result set (optional)
offset = 56 # int | The starting offset to read (optional)
limit = 56 # int | The maximum number of items to return (optional)
sortdir = 'sortdir_example' # str | The sort direction for the result set (optional)

try:
    # Get a list of workgroups the user belongs to
    api_response = api_instance.get_v2_users_id_workgroups(includeloggedinuser, activeonly, refreshcache, includesubscription, id, include=include, sortby=sortby, offset=offset, limit=limit, sortdir=sortdir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_users_id_workgroups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **includeloggedinuser** | **bool**| Includes current user |
 **activeonly** | **bool**| Excludes inactive workgroups |
 **refreshcache** | **bool**| This will force a refresh on the workgroup subscriptions |
 **includesubscription** | **bool**| This will include subscription in the response |
 **id** | **str**| The Id of the resource |
 **include** | [**list[str]**](str.md)| Sub elements to include in the response: LoggedInUser, IsDefaultRunUploadWorkgroup | [optional]
 **sortby** | **str**| The field(s) used to sort the result set | [optional]
 **offset** | **int**| The starting offset to read | [optional]
 **limit** | **int**| The maximum number of items to return | [optional]
 **sortdir** | **str**| The sort direction for the result set | [optional]

### Return type

[**V2WorkgroupList**](V2WorkgroupList.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_v2migration_status_stepname**
> V2MigrationStatusReport get_v2_v2migration_status_stepname(stepname, id=id)

Get status report on migration

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
stepname = 'stepname_example' # str | Migration Step Name
id = 'id_example' # str | The Id of the resource (optional)

try:
    # Get status report on migration
    api_response = api_instance.get_v2_v2migration_status_stepname(stepname, id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_v2migration_status_stepname: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stepname** | **str**| Migration Step Name |
 **id** | **str**| The Id of the resource | [optional]

### Return type

[**V2MigrationStatusReport**](V2MigrationStatusReport.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_v2_workgroups_id**
> V2Workgroup get_v2_workgroups_id(id)

Get information about a workgroup

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | Workgroup ID

try:
    # Get information about a workgroup
    api_response = api_instance.get_v2_workgroups_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->get_v2_workgroups_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Workgroup ID |

### Return type

[**V2Workgroup**](V2Workgroup.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v2_applications_id_workflows**
> IApplicationCompact post_v2_applications_id_workflows(id, body=body)

Create or update an analysis workflow

Create an analysis workflow using the settings, app, and version of an existing appsession.

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | Applicaiton Id
body = bssh_sdk_2.V2PostApplicationIdWorkflowsRequest() # V2PostApplicationIdWorkflowsRequest |  (optional)

try:
    # Create or update an analysis workflow
    api_response = api_instance.post_v2_applications_id_workflows(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->post_v2_applications_id_workflows: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Applicaiton Id |
 **body** | [**V2PostApplicationIdWorkflowsRequest**](V2PostApplicationIdWorkflowsRequest.md)|  | [optional]

### Return type

[**IApplicationCompact**](IApplicationCompact.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v2_appresults_id_file_upload_info**
> V1pre3FileCompact post_v2_appresults_id_file_upload_info(id, body=body)



Complete multipart upload and report uploaded files to a resource (dataset or appresult)

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | The Id of the resource
body = bssh_sdk_2.V2ResourcePresignedUrlCompleteRequestForEveryone() # V2ResourcePresignedUrlCompleteRequestForEveryone |  (optional)

try:
    api_response = api_instance.post_v2_appresults_id_file_upload_info(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->post_v2_appresults_id_file_upload_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of the resource |
 **body** | [**V2ResourcePresignedUrlCompleteRequestForEveryone**](V2ResourcePresignedUrlCompleteRequestForEveryone.md)|  | [optional]

### Return type

[**V1pre3FileCompact**](V1pre3FileCompact.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v2_appsessions**
> V2AppSession post_v2_appsessions(body=body)

Create a new interactive AppSession with ExecutionStatus Running

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
body = bssh_sdk_2.V2PostAppsessionsRequest() # V2PostAppsessionsRequest |  (optional)

try:
    # Create a new interactive AppSession with ExecutionStatus Running
    api_response = api_instance.post_v2_appsessions(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->post_v2_appsessions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V2PostAppsessionsRequest**](V2PostAppsessionsRequest.md)|  | [optional]

### Return type

[**V2AppSession**](V2AppSession.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v2_appsessions_id**
> V2AppSession post_v2_appsessions_id(id, body=body)

Update an analysis

The Execution Status cannot be changed since it is an automated status tracking the progress of running the app. The Qc Status may be updated only when the Execution Status is set to “Complete” or “Aborted”. Delivery Status may be updated at any time. Comments can be added when updating statuses.

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | Appsession ID
body = bssh_sdk_2.V2PostAppSessionsIdRequest() # V2PostAppSessionsIdRequest |  (optional)

try:
    # Update an analysis
    api_response = api_instance.post_v2_appsessions_id(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->post_v2_appsessions_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Appsession ID |
 **body** | [**V2PostAppSessionsIdRequest**](V2PostAppSessionsIdRequest.md)|  | [optional]

### Return type

[**V2AppSession**](V2AppSession.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v2_appsessions_id_logfiles**
> V2FilesList post_v2_appsessions_id_logfiles(id, body=body)

Add a log file to a specific analysis

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | Appsession ID
body = bssh_sdk_2.V2PostAppSessionsIdFilesRequest() # V2PostAppSessionsIdFilesRequest |  (optional)

try:
    # Add a log file to a specific analysis
    api_response = api_instance.post_v2_appsessions_id_logfiles(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->post_v2_appsessions_id_logfiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Appsession ID |
 **body** | [**V2PostAppSessionsIdFilesRequest**](V2PostAppSessionsIdFilesRequest.md)|  | [optional]

### Return type

[**V2FilesList**](V2FilesList.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v2_appsessions_id_properties**
> V2PropertyCompactList post_v2_appsessions_id_properties(id, body=body)

Add or update properties of an analysis

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | Appsession ID
body = bssh_sdk_2.V2PostAppSessionsPropertiesRequest() # V2PostAppSessionsPropertiesRequest |  (optional)

try:
    # Add or update properties of an analysis
    api_response = api_instance.post_v2_appsessions_id_properties(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->post_v2_appsessions_id_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Appsession ID |
 **body** | [**V2PostAppSessionsPropertiesRequest**](V2PostAppSessionsPropertiesRequest.md)|  | [optional]

### Return type

[**V2PropertyCompactList**](V2PropertyCompactList.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v2_appsessions_id_reschedule**
> V2Error post_v2_appsessions_id_reschedule(id, body=body)

Reschedule a workflow

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str |
body = bssh_sdk_2.V2PostAppSessionsIdRescheduleRequest() # V2PostAppSessionsIdRescheduleRequest |  (optional)

try:
    # Reschedule a workflow
    api_response = api_instance.post_v2_appsessions_id_reschedule(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->post_v2_appsessions_id_reschedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **body** | [**V2PostAppSessionsIdRescheduleRequest**](V2PostAppSessionsIdRescheduleRequest.md)|  | [optional]

### Return type

[**V2Error**](V2Error.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v2_appsessions_id_stop**
> V2AppSession post_v2_appsessions_id_stop(id, body=body)

Stop an analysis from running

The analysis must have a status of “Running” or “Pending”.  Stopping a running analysis will update the status to “Aborted”.  Stopping a pending analysis will update the status to “Canceled”.

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | Appsession ID
body = bssh_sdk_2.V2PostAppSessionsIdStopRequest() # V2PostAppSessionsIdStopRequest |  (optional)

try:
    # Stop an analysis from running
    api_response = api_instance.post_v2_appsessions_id_stop(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->post_v2_appsessions_id_stop: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Appsession ID |
 **body** | [**V2PostAppSessionsIdStopRequest**](V2PostAppSessionsIdStopRequest.md)|  | [optional]

### Return type

[**V2AppSession**](V2AppSession.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v2_appsessions_track**
> V2Error post_v2_appsessions_track(body=body)

Track ICA analyses

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
body = bssh_sdk_2.V2PostAppSessionsTrackRequest() # V2PostAppSessionsTrackRequest |  (optional)

try:
    # Track ICA analyses
    api_response = api_instance.post_v2_appsessions_track(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->post_v2_appsessions_track: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V2PostAppSessionsTrackRequest**](V2PostAppSessionsTrackRequest.md)|  | [optional]

### Return type

[**V2Error**](V2Error.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v2_appsessions_workflowsessions_track**
> V2Error post_v2_appsessions_workflowsessions_track(body=body)

Track workflow sessions

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
body = bssh_sdk_2.V2PostAppSessionsWorkflowSessionsTrackRequest() # V2PostAppSessionsWorkflowSessionsTrackRequest |  (optional)

try:
    # Track workflow sessions
    api_response = api_instance.post_v2_appsessions_workflowsessions_track(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->post_v2_appsessions_workflowsessions_track: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V2PostAppSessionsWorkflowSessionsTrackRequest**](V2PostAppSessionsWorkflowSessionsTrackRequest.md)|  | [optional]

### Return type

[**V2Error**](V2Error.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v2_archive**
> str post_v2_archive(body=body)

Bulk archive.

Archive one or more Runs or Projects.  The status will update right away, but the archive process itself is async.

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
body = bssh_sdk_2.V2BulkArchiveRequest() # V2BulkArchiveRequest |  (optional)

try:
    # Bulk archive.
    api_response = api_instance.post_v2_archive(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->post_v2_archive: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V2BulkArchiveRequest**](V2BulkArchiveRequest.md)|  | [optional]

### Return type

**str**

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v2_biosamples**
> V2BiologicalSample post_v2_biosamples(body=body)



Create a biological sample.

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
body = bssh_sdk_2.V2CreateBiologicalSampleRequest() # V2CreateBiologicalSampleRequest |  (optional)

try:
    api_response = api_instance.post_v2_biosamples(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->post_v2_biosamples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V2CreateBiologicalSampleRequest**](V2CreateBiologicalSampleRequest.md)|  | [optional]

### Return type

[**V2BiologicalSample**](V2BiologicalSample.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v2_biosamples_bulkupdate**
> IBiologicalSampleCompactList post_v2_biosamples_bulkupdate(body=body)

Update the default project of many biosamples

Setting a new default project of a biosample will redirect newly created datasets to the new project.

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
body = bssh_sdk_2.V2PostBioSamplesBulkUpdateRequest() # V2PostBioSamplesBulkUpdateRequest |  (optional)

try:
    # Update the default project of many biosamples
    api_response = api_instance.post_v2_biosamples_bulkupdate(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->post_v2_biosamples_bulkupdate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V2PostBioSamplesBulkUpdateRequest**](V2PostBioSamplesBulkUpdateRequest.md)|  | [optional]

### Return type

[**IBiologicalSampleCompactList**](IBiologicalSampleCompactList.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v2_biosamples_id**
> V2BiologicalSample post_v2_biosamples_id(id, body=body)

Update a Biosample

Setting a new default project of a biosample will redirect newly created datasets to the new project. The biosample status may transition between any of the possible statuses. Setting a biosample to canceled will automatically cancel all analyses in progress for that biosample.

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | Biosample ID
body = bssh_sdk_2.V2UpdateBiologicalSampleRequest() # V2UpdateBiologicalSampleRequest |  (optional)

try:
    # Update a Biosample
    api_response = api_instance.post_v2_biosamples_id(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->post_v2_biosamples_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Biosample ID |
 **body** | [**V2UpdateBiologicalSampleRequest**](V2UpdateBiologicalSampleRequest.md)|  | [optional]

### Return type

[**V2BiologicalSample**](V2BiologicalSample.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v2_biosamples_id_aggregation**
> V2Error post_v2_biosamples_id_aggregation(id, body=body)

Update Biosample aggregation

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | The Id of the resource
body = bssh_sdk_2.V2PostBioSamplesIdAggregationRequest() # V2PostBioSamplesIdAggregationRequest |  (optional)

try:
    # Update Biosample aggregation
    api_response = api_instance.post_v2_biosamples_id_aggregation(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->post_v2_biosamples_id_aggregation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of the resource |
 **body** | [**V2PostBioSamplesIdAggregationRequest**](V2PostBioSamplesIdAggregationRequest.md)|  | [optional]

### Return type

[**V2Error**](V2Error.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v2_biosamples_id_libraries**
> V2LibraryCompact post_v2_biosamples_id_libraries(id, body=body)

Create a library for a biosample

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | The Id of the resource
body = bssh_sdk_2.V2PostBiosampleLibraryRequest() # V2PostBiosampleLibraryRequest |  (optional)

try:
    # Create a library for a biosample
    api_response = api_instance.post_v2_biosamples_id_libraries(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->post_v2_biosamples_id_libraries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of the resource |
 **body** | [**V2PostBiosampleLibraryRequest**](V2PostBiosampleLibraryRequest.md)|  | [optional]

### Return type

[**V2LibraryCompact**](V2LibraryCompact.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v2_datacompress**
> str post_v2_datacompress(body=body)

Bulk Data Compression.

Queue one or more resources for data compression.  Compression process is async.

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
body = bssh_sdk_2.V2BulkDataCompressRequest() # V2BulkDataCompressRequest |  (optional)

try:
    # Bulk Data Compression.
    api_response = api_instance.post_v2_datacompress(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->post_v2_datacompress: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V2BulkDataCompressRequest**](V2BulkDataCompressRequest.md)|  | [optional]

### Return type

**str**

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v2_datasets**
> V2Dataset post_v2_datasets(body=body)

Create a dataset that doesn't belong in a specific project

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
body = bssh_sdk_2.V2PostDatasetsRequest() # V2PostDatasetsRequest |  (optional)

try:
    # Create a dataset that doesn't belong in a specific project
    api_response = api_instance.post_v2_datasets(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->post_v2_datasets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V2PostDatasetsRequest**](V2PostDatasetsRequest.md)|  | [optional]

### Return type

[**V2Dataset**](V2Dataset.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v2_datasets_id**
> V2Dataset post_v2_datasets_id(id, body=body)

Update an existing dataset

The QcStatus of a dataset may only be updated when the UploadStatus is set to “Complete”. The QcStatus may then be updated to one of the following values: QcFailed or QcPassed. A comment may be entered into the Comment field when updating the dataset QcStatus.

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | Dataset ID
body = bssh_sdk_2.V2PostDatasetsIdRequest() # V2PostDatasetsIdRequest |  (optional)

try:
    # Update an existing dataset
    api_response = api_instance.post_v2_datasets_id(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->post_v2_datasets_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Dataset ID |
 **body** | [**V2PostDatasetsIdRequest**](V2PostDatasetsIdRequest.md)|  | [optional]

### Return type

[**V2Dataset**](V2Dataset.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v2_datasets_id_copy**
> V2Dataset post_v2_datasets_id_copy(id, body=body)

Copy a dataset to a project

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | The Id of the resource
body = bssh_sdk_2.V2PostDatasetsIdCopyRequest() # V2PostDatasetsIdCopyRequest |  (optional)

try:
    # Copy a dataset to a project
    api_response = api_instance.post_v2_datasets_id_copy(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->post_v2_datasets_id_copy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of the resource |
 **body** | [**V2PostDatasetsIdCopyRequest**](V2PostDatasetsIdCopyRequest.md)|  | [optional]

### Return type

[**V2Dataset**](V2Dataset.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v2_datasets_id_direct_upload_info**
> V1pre3FileCompactList post_v2_datasets_id_direct_upload_info(id, body=body, sortdir=sortdir)



Report uploaded files to a dataset

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | The Id of the resource
body = bssh_sdk_2.V1pre3PostDatasetIdDirectUploadInfoRequest() # V1pre3PostDatasetIdDirectUploadInfoRequest |  (optional)
sortdir = 'sortdir_example' # str | The sort direction for the result set (optional)

try:
    api_response = api_instance.post_v2_datasets_id_direct_upload_info(id, body=body, sortdir=sortdir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->post_v2_datasets_id_direct_upload_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of the resource |
 **body** | [**V1pre3PostDatasetIdDirectUploadInfoRequest**](V1pre3PostDatasetIdDirectUploadInfoRequest.md)|  | [optional]
 **sortdir** | **str**| The sort direction for the result set | [optional]

### Return type

[**V1pre3FileCompactList**](V1pre3FileCompactList.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v2_datasets_id_file_upload_info**
> V1pre3FileCompact post_v2_datasets_id_file_upload_info(id, body=body)



Complete multipart upload and report uploaded files to a resource (dataset or appresult)

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | The Id of the resource
body = bssh_sdk_2.V2ResourcePresignedUrlCompleteRequestForEveryone() # V2ResourcePresignedUrlCompleteRequestForEveryone |  (optional)

try:
    api_response = api_instance.post_v2_datasets_id_file_upload_info(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->post_v2_datasets_id_file_upload_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of the resource |
 **body** | [**V2ResourcePresignedUrlCompleteRequestForEveryone**](V2ResourcePresignedUrlCompleteRequestForEveryone.md)|  | [optional]

### Return type

[**V1pre3FileCompact**](V1pre3FileCompact.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v2_datasets_id_files**
> V1pre3File post_v2_datasets_id_files(file, id)



### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
file = 'file_example' # str |
id = 'id_example' # str | The Id of the resource

try:
    api_response = api_instance.post_v2_datasets_id_files(file, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->post_v2_datasets_id_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**|  |
 **id** | **str**| The Id of the resource |

### Return type

[**V1pre3File**](V1pre3File.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v2_icadownloads_create_download_url**
> V2Error post_v2_icadownloads_create_download_url(body=body)



Get download url for data on ICA

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
body = bssh_sdk_2.V2IcaFileCreateDownloadUrlRequest() # V2IcaFileCreateDownloadUrlRequest |  (optional)

try:
    api_response = api_instance.post_v2_icadownloads_create_download_url(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->post_v2_icadownloads_create_download_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V2IcaFileCreateDownloadUrlRequest**](V2IcaFileCreateDownloadUrlRequest.md)|  | [optional]

### Return type

[**V2Error**](V2Error.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v2_icauploads_foldertype_complete_upload**
> V2Error post_v2_icauploads_foldertype_complete_upload(foldertype, body=body)



Complete file(s) upload to ICA, and respond with meta data

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
foldertype = 'foldertype_example' # str |
body = bssh_sdk_2.V2IcaCompleteUploadRequest() # V2IcaCompleteUploadRequest |  (optional)

try:
    api_response = api_instance.post_v2_icauploads_foldertype_complete_upload(foldertype, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->post_v2_icauploads_foldertype_complete_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **foldertype** | **str**|  |
 **body** | [**V2IcaCompleteUploadRequest**](V2IcaCompleteUploadRequest.md)|  | [optional]

### Return type

[**V2Error**](V2Error.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v2_icauploads_foldertype_direct_upload_info**
> V2Error post_v2_icauploads_foldertype_direct_upload_info(foldertype, body=body)



Get upload destination on ICA and temporary upload credentials

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
foldertype = 'foldertype_example' # str |
body = bssh_sdk_2.V2IcaFileUploadRequest() # V2IcaFileUploadRequest |  (optional)

try:
    api_response = api_instance.post_v2_icauploads_foldertype_direct_upload_info(foldertype, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->post_v2_icauploads_foldertype_direct_upload_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **foldertype** | **str**|  |
 **body** | [**V2IcaFileUploadRequest**](V2IcaFileUploadRequest.md)|  | [optional]

### Return type

[**V2Error**](V2Error.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v2_instrumentdiagnostics**
> V2InstrumentDiagnostic post_v2_instrumentdiagnostics(body=body)



Create non-run instrument diagnostic data.

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
body = bssh_sdk_2.V2CreateInstrumentDiagnosticRequest() # V2CreateInstrumentDiagnosticRequest |  (optional)

try:
    api_response = api_instance.post_v2_instrumentdiagnostics(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->post_v2_instrumentdiagnostics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V2CreateInstrumentDiagnosticRequest**](V2CreateInstrumentDiagnosticRequest.md)|  | [optional]

### Return type

[**V2InstrumentDiagnostic**](V2InstrumentDiagnostic.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v2_instrumentdiagnostics_id**
> V2InstrumentDiagnostic post_v2_instrumentdiagnostics_id(id, body=body)



Update non-run instrument diagnostic data.

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | The Id of the resource
body = bssh_sdk_2.V2UpdateInstrumentDiagnosticRequest() # V2UpdateInstrumentDiagnosticRequest |  (optional)

try:
    api_response = api_instance.post_v2_instrumentdiagnostics_id(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->post_v2_instrumentdiagnostics_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of the resource |
 **body** | [**V2UpdateInstrumentDiagnosticRequest**](V2UpdateInstrumentDiagnosticRequest.md)|  | [optional]

### Return type

[**V2InstrumentDiagnostic**](V2InstrumentDiagnostic.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v2_instruments_errors**
> V2InstrumentErrorResponse post_v2_instruments_errors(body=body)



Post instrument errors.

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
body = bssh_sdk_2.V2PostInstrumentErrorsRequest() # V2PostInstrumentErrorsRequest |  (optional)

try:
    api_response = api_instance.post_v2_instruments_errors(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->post_v2_instruments_errors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V2PostInstrumentErrorsRequest**](V2PostInstrumentErrorsRequest.md)|  | [optional]

### Return type

[**V2InstrumentErrorResponse**](V2InstrumentErrorResponse.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v2_lanes_id**
> Lane post_v2_lanes_id(id, body=body)

Update a lane

The status of a lane may be updated to the following values: QcFailed, QcPassed.

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str |
body = bssh_sdk_2.V2PostLanesIdRequest() # V2PostLanesIdRequest |  (optional)

try:
    # Update a lane
    api_response = api_instance.post_v2_lanes_id(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->post_v2_lanes_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **body** | [**V2PostLanesIdRequest**](V2PostLanesIdRequest.md)|  | [optional]

### Return type

[**Lane**](Lane.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v2_libraries_libraryid_labrequeues**
> V2LabRequeue post_v2_libraries_libraryid_labrequeues(libraryid, body=body)

Add a lab requeue request for more yield from a library

The requested additional yield is the total yield to be requested for the whole pool. To estimate how much yield will be added from each library, divide the requested additional yield by the number of libraries in the pool.

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
libraryid = 'libraryid_example' # str |
body = bssh_sdk_2.V2CreateExistingLibraryLabRequeueRequest() # V2CreateExistingLibraryLabRequeueRequest |  (optional)

try:
    # Add a lab requeue request for more yield from a library
    api_response = api_instance.post_v2_libraries_libraryid_labrequeues(libraryid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->post_v2_libraries_libraryid_labrequeues: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **libraryid** | **str**|  |
 **body** | [**V2CreateExistingLibraryLabRequeueRequest**](V2CreateExistingLibraryLabRequeueRequest.md)|  | [optional]

### Return type

[**V2LabRequeue**](V2LabRequeue.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v2_librarypools_id**
> V1pre3LibraryPoolCompact post_v2_librarypools_id(id, body=body)

Update a pool

The status of a pool may be updated to the following values: Active, Failed, Consumed or QCFailed. Setting a pool to Failed or QCFailed will exclude all FASTQ datasets created from the pool from app launch when one of its biosamples are selected as an input. This is also reflected on the Actual Yield of each biosample in the pool.

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | The Id of the resource
body = bssh_sdk_2.V2PostLibraryPoolIdRequest() # V2PostLibraryPoolIdRequest |  (optional)

try:
    # Update a pool
    api_response = api_instance.post_v2_librarypools_id(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->post_v2_librarypools_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of the resource |
 **body** | [**V2PostLibraryPoolIdRequest**](V2PostLibraryPoolIdRequest.md)|  | [optional]

### Return type

[**V1pre3LibraryPoolCompact**](V1pre3LibraryPoolCompact.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v2_librarypools_poolid_labrequeues**
> V2LabRequeue post_v2_librarypools_poolid_labrequeues(poolid, body=body)

Add a lab requeue request for more yield from a pool

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
poolid = 'poolid_example' # str |
body = bssh_sdk_2.V2CreateExistingPoolLabRequeueRequest() # V2CreateExistingPoolLabRequeueRequest |  (optional)

try:
    # Add a lab requeue request for more yield from a pool
    api_response = api_instance.post_v2_librarypools_poolid_labrequeues(poolid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->post_v2_librarypools_poolid_labrequeues: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **poolid** | **str**|  |
 **body** | [**V2CreateExistingPoolLabRequeueRequest**](V2CreateExistingPoolLabRequeueRequest.md)|  | [optional]

### Return type

[**V2LabRequeue**](V2LabRequeue.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v2_oauthv1_tokenfromoauthv2**
> V2OAuthV1Token post_v2_oauthv1_tokenfromoauthv2(body=body)



Get OAuthV1 token using an OAuthV2Token

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
body = bssh_sdk_2.V2OAuthV1FromOAuthV2Request() # V2OAuthV1FromOAuthV2Request |  (optional)

try:
    api_response = api_instance.post_v2_oauthv1_tokenfromoauthv2(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->post_v2_oauthv1_tokenfromoauthv2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V2OAuthV1FromOAuthV2Request**](V2OAuthV1FromOAuthV2Request.md)|  | [optional]

### Return type

[**V2OAuthV1Token**](V2OAuthV1Token.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v2_oauthv2_token**
> OAuthV2AccessTokenResponse post_v2_oauthv2_token(body=body)



### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
body = bssh_sdk_2.OAuthV2AccessTokenRequest() # OAuthV2AccessTokenRequest |  (optional)

try:
    api_response = api_instance.post_v2_oauthv2_token(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->post_v2_oauthv2_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OAuthV2AccessTokenRequest**](OAuthV2AccessTokenRequest.md)|  | [optional]

### Return type

[**OAuthV2AccessTokenResponse**](OAuthV2AccessTokenResponse.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v2_oauthv2_tokenfromapplicationjwt**
> V2OAuthV2Token post_v2_oauthv2_tokenfromapplicationjwt(body=body)



Create token for a trusted Platform service

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
body = bssh_sdk_2.V2OAuthV2TokenFromApplicationJwtRequest() # V2OAuthV2TokenFromApplicationJwtRequest |  (optional)

try:
    api_response = api_instance.post_v2_oauthv2_tokenfromapplicationjwt(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->post_v2_oauthv2_tokenfromapplicationjwt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V2OAuthV2TokenFromApplicationJwtRequest**](V2OAuthV2TokenFromApplicationJwtRequest.md)|  | [optional]

### Return type

[**V2OAuthV2Token**](V2OAuthV2Token.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v2_oauthv2tokens_userid**
> V2OAuthV2Token post_v2_oauthv2tokens_userid(userid, body=body)



Create token for a given user id

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
userid = 'userid_example' # str |
body = bssh_sdk_2.V2OAuthV2TokenRequest() # V2OAuthV2TokenRequest |  (optional)

try:
    api_response = api_instance.post_v2_oauthv2tokens_userid(userid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->post_v2_oauthv2tokens_userid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**|  |
 **body** | [**V2OAuthV2TokenRequest**](V2OAuthV2TokenRequest.md)|  | [optional]

### Return type

[**V2OAuthV2Token**](V2OAuthV2Token.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v2_preprequests_preprequestid_labrequeues**
> V2LabRequeue post_v2_preprequests_preprequestid_labrequeues(preprequestid, body=body)

Add a lab requeue request for more yield from a biosample

Request a requeue for a new library, given an existing preprequest.

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
preprequestid = 'preprequestid_example' # str |
body = bssh_sdk_2.V2CreateNewLibraryLabRequeueRequest() # V2CreateNewLibraryLabRequeueRequest |  (optional)

try:
    # Add a lab requeue request for more yield from a biosample
    api_response = api_instance.post_v2_preprequests_preprequestid_labrequeues(preprequestid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->post_v2_preprequests_preprequestid_labrequeues: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **preprequestid** | **str**|  |
 **body** | [**V2CreateNewLibraryLabRequeueRequest**](V2CreateNewLibraryLabRequeueRequest.md)|  | [optional]

### Return type

[**V2LabRequeue**](V2LabRequeue.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v2_projects**
> V1pre3Project post_v2_projects(name, body=body, description=description)

Create a project by name

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
name = 'name_example' # str | The name of the project.
body = bssh_sdk_2.V2PostProjectsRequest() # V2PostProjectsRequest |  (optional)
description = 'description_example' # str | Optional description of the project. (optional)

try:
    # Create a project by name
    api_response = api_instance.post_v2_projects(name, body=body, description=description)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->post_v2_projects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the project. |
 **body** | [**V2PostProjectsRequest**](V2PostProjectsRequest.md)|  | [optional]
 **description** | **str**| Optional description of the project. | [optional]

### Return type

[**V1pre3Project**](V1pre3Project.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v2_projects_id_datasets**
> V2Dataset post_v2_projects_id_datasets(id, body=body)

Create a dataset within a specific project

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | Project ID
body = bssh_sdk_2.V2PostProjectsIdDatasetsRequest() # V2PostProjectsIdDatasetsRequest |  (optional)

try:
    # Create a dataset within a specific project
    api_response = api_instance.post_v2_projects_id_datasets(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->post_v2_projects_id_datasets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project ID |
 **body** | [**V2PostProjectsIdDatasetsRequest**](V2PostProjectsIdDatasetsRequest.md)|  | [optional]

### Return type

[**V2Dataset**](V2Dataset.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v2_publishappsessionstatus**
> V2Error post_v2_publishappsessionstatus(body=body)



### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
body = bssh_sdk_2.V2PostPublishAppSessionStatusRequest() # V2PostPublishAppSessionStatusRequest |  (optional)

try:
    api_response = api_instance.post_v2_publishappsessionstatus(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->post_v2_publishappsessionstatus: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V2PostPublishAppSessionStatusRequest**](V2PostPublishAppSessionStatusRequest.md)|  | [optional]

### Return type

[**V2Error**](V2Error.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v2_restore**
> str post_v2_restore(body=body)

Bulk restore.

Restore one or more Runs or Projects.  The process is async, and may take up to 48 hours.

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
body = bssh_sdk_2.V2BulkRestoreRequest() # V2BulkRestoreRequest |  (optional)

try:
    # Bulk restore.
    api_response = api_instance.post_v2_restore(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->post_v2_restore: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V2BulkRestoreRequest**](V2BulkRestoreRequest.md)|  | [optional]

### Return type

**str**

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v2_runs**
> V2Run post_v2_runs(experimentname, instrumenttype, body=body, samplesheetname=samplesheetname)

Create a new run

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
experimentname = 'experimentname_example' # str | The name of the experiment.
instrumenttype = 'instrumenttype_example' # str | The InstrumentType identifies from which the run is generated. This is REQUIRED for runs uploaded manually. Runs uploaded from an instrument must specify the ClientKey. AllowedValues: 'HiSeq1000', 'HiSeq1500', 'HiSeq2000', 'HiSeq2500', 'HiSeq3000', 'HiSeq4000', 'HiSeqX', 'NovaSeq5000', 'NovaSeq6000', 'MiniSeq', 'MiSeq', 'MiSeqDx', 'NextSeq', 'NextSeqDx', 'iSeq100'
body = bssh_sdk_2.V2PostRunsRequest() # V2PostRunsRequest |  (optional)
samplesheetname = 'samplesheetname_example' # str | The name of the sample sheet. (optional)

try:
    # Create a new run
    api_response = api_instance.post_v2_runs(experimentname, instrumenttype, body=body, samplesheetname=samplesheetname)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->post_v2_runs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experimentname** | **str**| The name of the experiment. |
 **instrumenttype** | **str**| The InstrumentType identifies from which the run is generated. This is REQUIRED for runs uploaded manually. Runs uploaded from an instrument must specify the ClientKey. AllowedValues: &#x27;HiSeq1000&#x27;, &#x27;HiSeq1500&#x27;, &#x27;HiSeq2000&#x27;, &#x27;HiSeq2500&#x27;, &#x27;HiSeq3000&#x27;, &#x27;HiSeq4000&#x27;, &#x27;HiSeqX&#x27;, &#x27;NovaSeq5000&#x27;, &#x27;NovaSeq6000&#x27;, &#x27;MiniSeq&#x27;, &#x27;MiSeq&#x27;, &#x27;MiSeqDx&#x27;, &#x27;NextSeq&#x27;, &#x27;NextSeqDx&#x27;, &#x27;iSeq100&#x27; |
 **body** | [**V2PostRunsRequest**](V2PostRunsRequest.md)|  | [optional]
 **samplesheetname** | **str**| The name of the sample sheet. | [optional]

### Return type

[**V2Run**](V2Run.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v2_runs_id**
> V2Run post_v2_runs_id(id, body=body, uploadstatus=uploadstatus, instrumentrunstatus=instrumentrunstatus, runparametersxml=runparametersxml, instrumentrunid=instrumentrunid, instrumentrunnumber=instrumentrunnumber, flowcellbarcode=flowcellbarcode, prepkitname=prepkitname)

Update an existing run

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | The Id of the resource
body = bssh_sdk_2.V2PostRunIdRequest() # V2PostRunIdRequest |  (optional)
uploadstatus = 'uploadstatus_example' # str | Specifies the updated state of a run. AllowedValues: 'Uploading', 'Completed', 'Failed'. (optional)
instrumentrunstatus = 'instrumentrunstatus_example' # str | Specifies the updated state of a run. AllowedValues: 'Running', 'Stopped', 'InstrumentCompleted', 'Failed', 'Rehybing'. (optional)
runparametersxml = 'runparametersxml_example' # str | Update the run data based on the contents of run parameters. (optional)
instrumentrunid = 'instrumentrunid_example' # str | Specifies the InstrumentRunId. (optional)
instrumentrunnumber = 56 # int | Specifies the InstrumentRunNumber. (optional)
flowcellbarcode = 'flowcellbarcode_example' # str | Specifies the FlowcellBarcode. (optional)
prepkitname = 'prepkitname_example' # str | Specifies the PrepkitName. (optional)

try:
    # Update an existing run
    api_response = api_instance.post_v2_runs_id(id, body=body, uploadstatus=uploadstatus, instrumentrunstatus=instrumentrunstatus, runparametersxml=runparametersxml, instrumentrunid=instrumentrunid, instrumentrunnumber=instrumentrunnumber, flowcellbarcode=flowcellbarcode, prepkitname=prepkitname)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->post_v2_runs_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of the resource |
 **body** | [**V2PostRunIdRequest**](V2PostRunIdRequest.md)|  | [optional]
 **uploadstatus** | **str**| Specifies the updated state of a run. AllowedValues: &#x27;Uploading&#x27;, &#x27;Completed&#x27;, &#x27;Failed&#x27;. | [optional]
 **instrumentrunstatus** | **str**| Specifies the updated state of a run. AllowedValues: &#x27;Running&#x27;, &#x27;Stopped&#x27;, &#x27;InstrumentCompleted&#x27;, &#x27;Failed&#x27;, &#x27;Rehybing&#x27;. | [optional]
 **runparametersxml** | **str**| Update the run data based on the contents of run parameters. | [optional]
 **instrumentrunid** | **str**| Specifies the InstrumentRunId. | [optional]
 **instrumentrunnumber** | **int**| Specifies the InstrumentRunNumber. | [optional]
 **flowcellbarcode** | **str**| Specifies the FlowcellBarcode. | [optional]
 **prepkitname** | **str**| Specifies the PrepkitName. | [optional]

### Return type

[**V2Run**](V2Run.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v2_runs_id_file_upload_info**
> V1pre3FileCompact post_v2_runs_id_file_upload_info(id, body=body)



Complete multipart upload and report uploaded files to a resource (sample or run)

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | The Id of the resource
body = bssh_sdk_2.V2ResourcePresignedUrlCompleteRequest() # V2ResourcePresignedUrlCompleteRequest |  (optional)

try:
    api_response = api_instance.post_v2_runs_id_file_upload_info(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->post_v2_runs_id_file_upload_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of the resource |
 **body** | [**V2ResourcePresignedUrlCompleteRequest**](V2ResourcePresignedUrlCompleteRequest.md)|  | [optional]

### Return type

[**V1pre3FileCompact**](V1pre3FileCompact.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v2_runs_id_files**
> V1pre3File post_v2_runs_id_files(file, id)



### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
file = 'file_example' # str |
id = 'id_example' # str | The Id of the resource

try:
    api_response = api_instance.post_v2_runs_id_files(file, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->post_v2_runs_id_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**|  |
 **id** | **str**| The Id of the resource |

### Return type

[**V1pre3File**](V1pre3File.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v2_runs_start**
> V2Run post_v2_runs_start(body=body)

Create a new run using GSS

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
body = bssh_sdk_2.V2PostRunsStartRequest() # V2PostRunsStartRequest |  (optional)

try:
    # Create a new run using GSS
    api_response = api_instance.post_v2_runs_start(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->post_v2_runs_start: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V2PostRunsStartRequest**](V2PostRunsStartRequest.md)|  | [optional]

### Return type

[**V2Run**](V2Run.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v2_samples_id_file_upload_info**
> V1pre3FileCompact post_v2_samples_id_file_upload_info(id, body=body)



Complete multipart upload and report uploaded files to a resource (sample or run)

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | The Id of the resource
body = bssh_sdk_2.V2ResourcePresignedUrlCompleteRequest() # V2ResourcePresignedUrlCompleteRequest |  (optional)

try:
    api_response = api_instance.post_v2_samples_id_file_upload_info(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->post_v2_samples_id_file_upload_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of the resource |
 **body** | [**V2ResourcePresignedUrlCompleteRequest**](V2ResourcePresignedUrlCompleteRequest.md)|  | [optional]

### Return type

[**V1pre3FileCompact**](V1pre3FileCompact.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v2_tokens_instruments**
> V2InstrumentJwt post_v2_tokens_instruments(body=body)

Creates a Platform JWT token for an instrument

Creates a Platform JWT for an instrument.

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
body = bssh_sdk_2.V2CreateInstrumentJwtRequest() # V2CreateInstrumentJwtRequest |  (optional)

try:
    # Creates a Platform JWT token for an instrument
    api_response = api_instance.post_v2_tokens_instruments(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->post_v2_tokens_instruments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V2CreateInstrumentJwtRequest**](V2CreateInstrumentJwtRequest.md)|  | [optional]

### Return type

[**V2InstrumentJwt**](V2InstrumentJwt.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v2_trash_id_restorefromtrash**
> V1pre3TrashItem post_v2_trash_id_restorefromtrash(id, body=body)

Restore an item from the trash back to its active state

The ID used in this endpoint is the ID given to the item when it is put in the trash, not the original ID from the resource, i.e. its project ID. Please use the GET /v2/trash endpoint to find the item’s trash ID.

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | The Id of the resource
body = bssh_sdk_2.V1pre3PostTrashItemRestoreFromTrashRequest() # V1pre3PostTrashItemRestoreFromTrashRequest |  (optional)

try:
    # Restore an item from the trash back to its active state
    api_response = api_instance.post_v2_trash_id_restorefromtrash(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->post_v2_trash_id_restorefromtrash: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of the resource |
 **body** | [**V1pre3PostTrashItemRestoreFromTrashRequest**](V1pre3PostTrashItemRestoreFromTrashRequest.md)|  | [optional]

### Return type

[**V1pre3TrashItem**](V1pre3TrashItem.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v2_unzip**
> str post_v2_unzip(body=body)

Bulk Unzip.

Unzip one or more Runs. The status will update right away, but the unzip process itself is async

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
body = bssh_sdk_2.V2BulkUnzipRequest() # V2BulkUnzipRequest |  (optional)

try:
    # Bulk Unzip.
    api_response = api_instance.post_v2_unzip(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->post_v2_unzip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V2BulkUnzipRequest**](V2BulkUnzipRequest.md)|  | [optional]

### Return type

**str**

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v2_useraccounttransfer**
> V2AppSession post_v2_useraccounttransfer(body=body)

User account transfer. Requires Administrator role

Intitiates a User account transfer. API only kicks off the process which itself is async.

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
body = bssh_sdk_2.V2UserAccountTransferRequest() # V2UserAccountTransferRequest |  (optional)

try:
    # User account transfer. Requires Administrator role
    api_response = api_instance.post_v2_useraccounttransfer(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->post_v2_useraccounttransfer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V2UserAccountTransferRequest**](V2UserAccountTransferRequest.md)|  | [optional]

### Return type

[**V2AppSession**](V2AppSession.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v2_useragreements**
> V2UserAgreementCompact post_v2_useragreements(body=body)



Sign an agreement.

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
body = bssh_sdk_2.V2SignAgreementRequest() # V2SignAgreementRequest |  (optional)

try:
    api_response = api_instance.post_v2_useragreements(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->post_v2_useragreements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V2SignAgreementRequest**](V2SignAgreementRequest.md)|  | [optional]

### Return type

[**V2UserAgreementCompact**](V2UserAgreementCompact.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v2_users_current**
> V2User post_v2_users_current(body=body)



Change current user context.

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
body = bssh_sdk_2.V2PostUsersCurrentRequest() # V2PostUsersCurrentRequest |  (optional)

try:
    api_response = api_instance.post_v2_users_current(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->post_v2_users_current: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V2PostUsersCurrentRequest**](V2PostUsersCurrentRequest.md)|  | [optional]

### Return type

[**V2User**](V2User.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v2_users_files**
> V2Error post_v2_users_files(body=body)

Upload a file to the user's volume in GDS

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
body = bssh_sdk_2.V2GdsFileUploadRequest() # V2GdsFileUploadRequest |  (optional)

try:
    # Upload a file to the user's volume in GDS
    api_response = api_instance.post_v2_users_files(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->post_v2_users_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V2GdsFileUploadRequest**](V2GdsFileUploadRequest.md)|  | [optional]

### Return type

[**V2Error**](V2Error.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v2_users_id_settings**
> V2UserSettingsResponse post_v2_users_id_settings(id, body=body)

Update the user's settings

A user may have settings such as how they receive notifications and expiration time on lab requeues. This currently only works with a session cookie.

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | The Id of the resource
body = bssh_sdk_2.V2PostUserSettingsRequest() # V2PostUserSettingsRequest |  (optional)

try:
    # Update the user's settings
    api_response = api_instance.post_v2_users_id_settings(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->post_v2_users_id_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of the resource |
 **body** | [**V2PostUserSettingsRequest**](V2PostUserSettingsRequest.md)|  | [optional]

### Return type

[**V2UserSettingsResponse**](V2UserSettingsResponse.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v2_users_id_v2analysisconfigtemplate**
> V2Error post_v2_users_id_v2analysisconfigtemplate(id, body=body)

Change Analysis Configuration Template Feature Enabled for calling user

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | The Id of the resource
body = bssh_sdk_2.V2PostUsersIdAnalysisConfigTemplateRequest() # V2PostUsersIdAnalysisConfigTemplateRequest |  (optional)

try:
    # Change Analysis Configuration Template Feature Enabled for calling user
    api_response = api_instance.post_v2_users_id_v2analysisconfigtemplate(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->post_v2_users_id_v2analysisconfigtemplate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of the resource |
 **body** | [**V2PostUsersIdAnalysisConfigTemplateRequest**](V2PostUsersIdAnalysisConfigTemplateRequest.md)|  | [optional]

### Return type

[**V2Error**](V2Error.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v2_users_id_v2biosampleregistry**
> V2Error post_v2_users_id_v2biosampleregistry(id, body=body)

Change V2 BioSample Registry Enabled for calling user

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | The Id of the resource
body = bssh_sdk_2.V2PostUsersIdV2BioSampleRegistryRequest() # V2PostUsersIdV2BioSampleRegistryRequest |  (optional)

try:
    # Change V2 BioSample Registry Enabled for calling user
    api_response = api_instance.post_v2_users_id_v2biosampleregistry(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->post_v2_users_id_v2biosampleregistry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of the resource |
 **body** | [**V2PostUsersIdV2BioSampleRegistryRequest**](V2PostUsersIdV2BioSampleRegistryRequest.md)|  | [optional]

### Return type

[**V2Error**](V2Error.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_v2_validatesignedurl**
> V2SignedUrlValidation post_v2_validatesignedurl(body=body)



Validate a OAuthV1 signed url for GroundControl

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
body = bssh_sdk_2.V2PostSignedUrlValidationRequest() # V2PostSignedUrlValidationRequest |  (optional)

try:
    api_response = api_instance.post_v2_validatesignedurl(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->post_v2_validatesignedurl: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V2PostSignedUrlValidationRequest**](V2PostSignedUrlValidationRequest.md)|  | [optional]

### Return type

[**V2SignedUrlValidation**](V2SignedUrlValidation.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_v2_applications_id_qcthresholds**
> V2QcThresholdResponse put_v2_applications_id_qcthresholds(id, qcthresholds=qcthresholds)

Add or update the QC thresholds applied to an analysis workflow

List the QC thresholds to be updated. You must include the name of the metric to be thresholded, the type of logical operator, the dataset type unique ID to apply the threshold to, and the threshold values.

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | The Id of the resource
qcthresholds = [bssh_sdk_2.V2QcThreshold()] # list[V2QcThreshold] |  (optional)

try:
    # Add or update the QC thresholds applied to an analysis workflow
    api_response = api_instance.put_v2_applications_id_qcthresholds(id, qcthresholds=qcthresholds)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->put_v2_applications_id_qcthresholds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of the resource |
 **qcthresholds** | [**list[V2QcThreshold]**](V2QcThreshold.md)|  | [optional]

### Return type

[**V2QcThresholdResponse**](V2QcThresholdResponse.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_v2_applications_id_workflowdependencies**
> V2AnalysisWorkflowDependenciesResponse put_v2_applications_id_workflowdependencies(id, version=version, dependencies=dependencies)

Add or update the workflow dependencies of an analysis workflow

Add the required triggers for the analysis workflow to launch. Workflows can depend on a certain amount of biosample actual yield to show up or they can depend on another app completing.

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
id = 'id_example' # str | The Id of the resource
version = 'version_example' # str |  (optional)
dependencies = [bssh_sdk_2.V2AnalysisWorkflowDependency()] # list[V2AnalysisWorkflowDependency] |  (optional)

try:
    # Add or update the workflow dependencies of an analysis workflow
    api_response = api_instance.put_v2_applications_id_workflowdependencies(id, version=version, dependencies=dependencies)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->put_v2_applications_id_workflowdependencies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of the resource |
 **version** | **str**|  | [optional]
 **dependencies** | [**list[V2AnalysisWorkflowDependency]**](V2AnalysisWorkflowDependency.md)|  | [optional]

### Return type

[**V2AnalysisWorkflowDependenciesResponse**](V2AnalysisWorkflowDependenciesResponse.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_v2_laneqcthresholds**
> V2QcThresholdResponse put_v2_laneqcthresholds(qcthresholds=qcthresholds, id=id)

Add or update the QC thresholds applied to lanes

List the QC thresholds to be updated.

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
qcthresholds = [bssh_sdk_2.V2QcThreshold()] # list[V2QcThreshold] |  (optional)
id = 'id_example' # str | The Id of the resource (optional)

try:
    # Add or update the QC thresholds applied to lanes
    api_response = api_instance.put_v2_laneqcthresholds(qcthresholds=qcthresholds, id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BasespaceApi->put_v2_laneqcthresholds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **qcthresholds** | [**list[V2QcThreshold]**](V2QcThreshold.md)|  | [optional]
 **id** | **str**| The Id of the resource | [optional]

### Return type

[**V2QcThresholdResponse**](V2QcThresholdResponse.md)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_v2_notifications_dismiss**
> put_v2_notifications_dismiss(stream, type, id=id)

Dismiss a user notification.

Dismiss a user notification. Only DataDeletion, Storage or Subscription notifications can dismissed. For Deleting an Activity notification, use the DELETE endpoint

### Example
```python
from __future__ import print_function
import time
import bssh_sdk_2
from bssh_sdk_2.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = bssh_sdk_2.Configuration()
configuration.api_key['x-access-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-access-token'] = 'Bearer'
# Configure OAuth2 access token for authorization: basespace_auth
configuration = bssh_sdk_2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bssh_sdk_2.BasespaceApi(bssh_sdk_2.ApiClient(configuration))
stream = 'stream_example' # str | The stream type of the notification to be dismissed.Only DataDeletion, Storage or Subscription notifications can dismissed.  
type = 'type_example' # str | The Type of the notification with in a stream.Only notifications with 'IsDismissable' flag set are dismissable
id = 'id_example' # str | The Id of the resource (optional)

try:
    # Dismiss a user notification.
    api_instance.put_v2_notifications_dismiss(stream, type, id=id)
except ApiException as e:
    print("Exception when calling BasespaceApi->put_v2_notifications_dismiss: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stream** | **str**| The stream type of the notification to be dismissed.Only DataDeletion, Storage or Subscription notifications can dismissed.   |
 **type** | **str**| The Type of the notification with in a stream.Only notifications with &#x27;IsDismissable&#x27; flag set are dismissable |
 **id** | **str**| The Id of the resource | [optional]

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key), [basespace_auth](../README.md#basespace_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
