# coding: utf-8

"""
    Basespace API

    Basespace REST API  # noqa: E501

    OpenAPI spec version: 5.0.0

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class V2RunCompact(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'name': 'str',
        'experiment_name': 'str',
        'date_created': 'datetime',
        'date_modified': 'datetime',
        'status': 'str',
        'user_owned_by': 'IUserCompact',
        'instrument': 'V2RunInstrumentCompact',
        'instrument_run_status': 'str',
        'date_instrument_started': 'datetime',
        'date_instrument_completed': 'datetime',
        'flowcell_barcode': 'str',
        'reagent_barcode': 'str',
        'buffer_barcode': 'str',
        'flowcell_position': 'str',
        'lane_and_qc_status': 'str',
        'prep_kit_name': 'str',
        'workflow': 'str',
        'sample_sheet_name': 'str',
        'total_size': 'int',
        'user_uploaded_by': 'IUserCompact',
        'upload_status': 'str',
        'date_upload_started': 'datetime',
        'date_upload_completed': 'datetime',
        'is_deleted': 'bool',
        'is_file_data_deleted': 'bool',
        'is_archived': 'bool',
        'is_zipping': 'bool',
        'is_zipped': 'bool',
        'is_unzipping': 'bool',
        'href': 'str',
        'href_files': 'str',
        'href_ica_uri_files': 'str',
        'has_files_in_ica': 'bool',
        'properties': 'V2PropertyContainer',
        'v1_pre3_id': 'str',
        'is_transfer_pending': 'bool',
        'is_transfer_in_progress': 'bool'
    }

    attribute_map = {
        'id': 'Id',
        'name': 'Name',
        'experiment_name': 'ExperimentName',
        'date_created': 'DateCreated',
        'date_modified': 'DateModified',
        'status': 'Status',
        'user_owned_by': 'UserOwnedBy',
        'instrument': 'Instrument',
        'instrument_run_status': 'InstrumentRunStatus',
        'date_instrument_started': 'DateInstrumentStarted',
        'date_instrument_completed': 'DateInstrumentCompleted',
        'flowcell_barcode': 'FlowcellBarcode',
        'reagent_barcode': 'ReagentBarcode',
        'buffer_barcode': 'BufferBarcode',
        'flowcell_position': 'FlowcellPosition',
        'lane_and_qc_status': 'LaneAndQcStatus',
        'prep_kit_name': 'PrepKitName',
        'workflow': 'Workflow',
        'sample_sheet_name': 'SampleSheetName',
        'total_size': 'TotalSize',
        'user_uploaded_by': 'UserUploadedBy',
        'upload_status': 'UploadStatus',
        'date_upload_started': 'DateUploadStarted',
        'date_upload_completed': 'DateUploadCompleted',
        'is_deleted': 'IsDeleted',
        'is_file_data_deleted': 'IsFileDataDeleted',
        'is_archived': 'IsArchived',
        'is_zipping': 'IsZipping',
        'is_zipped': 'IsZipped',
        'is_unzipping': 'IsUnzipping',
        'href': 'Href',
        'href_files': 'HrefFiles',
        'href_ica_uri_files': 'HrefIcaUriFiles',
        'has_files_in_ica': 'HasFilesInIca',
        'properties': 'Properties',
        'v1_pre3_id': 'V1Pre3Id',
        'is_transfer_pending': 'IsTransferPending',
        'is_transfer_in_progress': 'IsTransferInProgress'
    }

    def __init__(self, id=None, name=None, experiment_name=None, date_created=None, date_modified=None, status=None, user_owned_by=None, instrument=None, instrument_run_status=None, date_instrument_started=None, date_instrument_completed=None, flowcell_barcode=None, reagent_barcode=None, buffer_barcode=None, flowcell_position=None, lane_and_qc_status=None, prep_kit_name=None, workflow=None, sample_sheet_name=None, total_size=None, user_uploaded_by=None, upload_status=None, date_upload_started=None, date_upload_completed=None, is_deleted=None, is_file_data_deleted=None, is_archived=None, is_zipping=None, is_zipped=None, is_unzipping=None, href=None, href_files=None, href_ica_uri_files=None, has_files_in_ica=None, properties=None, v1_pre3_id=None, is_transfer_pending=None, is_transfer_in_progress=None):  # noqa: E501
        """V2RunCompact - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._experiment_name = None
        self._date_created = None
        self._date_modified = None
        self._status = None
        self._user_owned_by = None
        self._instrument = None
        self._instrument_run_status = None
        self._date_instrument_started = None
        self._date_instrument_completed = None
        self._flowcell_barcode = None
        self._reagent_barcode = None
        self._buffer_barcode = None
        self._flowcell_position = None
        self._lane_and_qc_status = None
        self._prep_kit_name = None
        self._workflow = None
        self._sample_sheet_name = None
        self._total_size = None
        self._user_uploaded_by = None
        self._upload_status = None
        self._date_upload_started = None
        self._date_upload_completed = None
        self._is_deleted = None
        self._is_file_data_deleted = None
        self._is_archived = None
        self._is_zipping = None
        self._is_zipped = None
        self._is_unzipping = None
        self._href = None
        self._href_files = None
        self._href_ica_uri_files = None
        self._has_files_in_ica = None
        self._properties = None
        self._v1_pre3_id = None
        self._is_transfer_pending = None
        self._is_transfer_in_progress = None
        self.discriminator = None
        self.id = id
        if name is not None:
            self.name = name
        if experiment_name is not None:
            self.experiment_name = experiment_name
        if date_created is not None:
            self.date_created = date_created
        if date_modified is not None:
            self.date_modified = date_modified
        if status is not None:
            self.status = status
        if user_owned_by is not None:
            self.user_owned_by = user_owned_by
        if instrument is not None:
            self.instrument = instrument
        if instrument_run_status is not None:
            self.instrument_run_status = instrument_run_status
        if date_instrument_started is not None:
            self.date_instrument_started = date_instrument_started
        if date_instrument_completed is not None:
            self.date_instrument_completed = date_instrument_completed
        if flowcell_barcode is not None:
            self.flowcell_barcode = flowcell_barcode
        if reagent_barcode is not None:
            self.reagent_barcode = reagent_barcode
        if buffer_barcode is not None:
            self.buffer_barcode = buffer_barcode
        if flowcell_position is not None:
            self.flowcell_position = flowcell_position
        if lane_and_qc_status is not None:
            self.lane_and_qc_status = lane_and_qc_status
        if prep_kit_name is not None:
            self.prep_kit_name = prep_kit_name
        if workflow is not None:
            self.workflow = workflow
        if sample_sheet_name is not None:
            self.sample_sheet_name = sample_sheet_name
        if total_size is not None:
            self.total_size = total_size
        if user_uploaded_by is not None:
            self.user_uploaded_by = user_uploaded_by
        if upload_status is not None:
            self.upload_status = upload_status
        if date_upload_started is not None:
            self.date_upload_started = date_upload_started
        if date_upload_completed is not None:
            self.date_upload_completed = date_upload_completed
        if is_deleted is not None:
            self.is_deleted = is_deleted
        if is_file_data_deleted is not None:
            self.is_file_data_deleted = is_file_data_deleted
        if is_archived is not None:
            self.is_archived = is_archived
        if is_zipping is not None:
            self.is_zipping = is_zipping
        if is_zipped is not None:
            self.is_zipped = is_zipped
        if is_unzipping is not None:
            self.is_unzipping = is_unzipping
        self.href = href
        if href_files is not None:
            self.href_files = href_files
        if href_ica_uri_files is not None:
            self.href_ica_uri_files = href_ica_uri_files
        if has_files_in_ica is not None:
            self.has_files_in_ica = has_files_in_ica
        if properties is not None:
            self.properties = properties
        if v1_pre3_id is not None:
            self.v1_pre3_id = v1_pre3_id
        if is_transfer_pending is not None:
            self.is_transfer_pending = is_transfer_pending
        if is_transfer_in_progress is not None:
            self.is_transfer_in_progress = is_transfer_in_progress

    @property
    def id(self):
        """Gets the id of this V2RunCompact.  # noqa: E501


        :return: The id of this V2RunCompact.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this V2RunCompact.


        :param id: The id of this V2RunCompact.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this V2RunCompact.  # noqa: E501


        :return: The name of this V2RunCompact.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V2RunCompact.


        :param name: The name of this V2RunCompact.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def experiment_name(self):
        """Gets the experiment_name of this V2RunCompact.  # noqa: E501


        :return: The experiment_name of this V2RunCompact.  # noqa: E501
        :rtype: str
        """
        return self._experiment_name

    @experiment_name.setter
    def experiment_name(self, experiment_name):
        """Sets the experiment_name of this V2RunCompact.


        :param experiment_name: The experiment_name of this V2RunCompact.  # noqa: E501
        :type: str
        """

        self._experiment_name = experiment_name

    @property
    def date_created(self):
        """Gets the date_created of this V2RunCompact.  # noqa: E501


        :return: The date_created of this V2RunCompact.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this V2RunCompact.


        :param date_created: The date_created of this V2RunCompact.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def date_modified(self):
        """Gets the date_modified of this V2RunCompact.  # noqa: E501


        :return: The date_modified of this V2RunCompact.  # noqa: E501
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this V2RunCompact.


        :param date_modified: The date_modified of this V2RunCompact.  # noqa: E501
        :type: datetime
        """

        self._date_modified = date_modified

    @property
    def status(self):
        """Gets the status of this V2RunCompact.  # noqa: E501


        :return: The status of this V2RunCompact.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this V2RunCompact.


        :param status: The status of this V2RunCompact.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def user_owned_by(self):
        """Gets the user_owned_by of this V2RunCompact.  # noqa: E501


        :return: The user_owned_by of this V2RunCompact.  # noqa: E501
        :rtype: IUserCompact
        """
        return self._user_owned_by

    @user_owned_by.setter
    def user_owned_by(self, user_owned_by):
        """Sets the user_owned_by of this V2RunCompact.


        :param user_owned_by: The user_owned_by of this V2RunCompact.  # noqa: E501
        :type: IUserCompact
        """

        self._user_owned_by = user_owned_by

    @property
    def instrument(self):
        """Gets the instrument of this V2RunCompact.  # noqa: E501


        :return: The instrument of this V2RunCompact.  # noqa: E501
        :rtype: V2RunInstrumentCompact
        """
        return self._instrument

    @instrument.setter
    def instrument(self, instrument):
        """Sets the instrument of this V2RunCompact.


        :param instrument: The instrument of this V2RunCompact.  # noqa: E501
        :type: V2RunInstrumentCompact
        """

        self._instrument = instrument

    @property
    def instrument_run_status(self):
        """Gets the instrument_run_status of this V2RunCompact.  # noqa: E501


        :return: The instrument_run_status of this V2RunCompact.  # noqa: E501
        :rtype: str
        """
        return self._instrument_run_status

    @instrument_run_status.setter
    def instrument_run_status(self, instrument_run_status):
        """Sets the instrument_run_status of this V2RunCompact.


        :param instrument_run_status: The instrument_run_status of this V2RunCompact.  # noqa: E501
        :type: str
        """

        self._instrument_run_status = instrument_run_status

    @property
    def date_instrument_started(self):
        """Gets the date_instrument_started of this V2RunCompact.  # noqa: E501


        :return: The date_instrument_started of this V2RunCompact.  # noqa: E501
        :rtype: datetime
        """
        return self._date_instrument_started

    @date_instrument_started.setter
    def date_instrument_started(self, date_instrument_started):
        """Sets the date_instrument_started of this V2RunCompact.


        :param date_instrument_started: The date_instrument_started of this V2RunCompact.  # noqa: E501
        :type: datetime
        """

        self._date_instrument_started = date_instrument_started

    @property
    def date_instrument_completed(self):
        """Gets the date_instrument_completed of this V2RunCompact.  # noqa: E501


        :return: The date_instrument_completed of this V2RunCompact.  # noqa: E501
        :rtype: datetime
        """
        return self._date_instrument_completed

    @date_instrument_completed.setter
    def date_instrument_completed(self, date_instrument_completed):
        """Sets the date_instrument_completed of this V2RunCompact.


        :param date_instrument_completed: The date_instrument_completed of this V2RunCompact.  # noqa: E501
        :type: datetime
        """

        self._date_instrument_completed = date_instrument_completed

    @property
    def flowcell_barcode(self):
        """Gets the flowcell_barcode of this V2RunCompact.  # noqa: E501


        :return: The flowcell_barcode of this V2RunCompact.  # noqa: E501
        :rtype: str
        """
        return self._flowcell_barcode

    @flowcell_barcode.setter
    def flowcell_barcode(self, flowcell_barcode):
        """Sets the flowcell_barcode of this V2RunCompact.


        :param flowcell_barcode: The flowcell_barcode of this V2RunCompact.  # noqa: E501
        :type: str
        """

        self._flowcell_barcode = flowcell_barcode

    @property
    def reagent_barcode(self):
        """Gets the reagent_barcode of this V2RunCompact.  # noqa: E501


        :return: The reagent_barcode of this V2RunCompact.  # noqa: E501
        :rtype: str
        """
        return self._reagent_barcode

    @reagent_barcode.setter
    def reagent_barcode(self, reagent_barcode):
        """Sets the reagent_barcode of this V2RunCompact.


        :param reagent_barcode: The reagent_barcode of this V2RunCompact.  # noqa: E501
        :type: str
        """

        self._reagent_barcode = reagent_barcode

    @property
    def buffer_barcode(self):
        """Gets the buffer_barcode of this V2RunCompact.  # noqa: E501


        :return: The buffer_barcode of this V2RunCompact.  # noqa: E501
        :rtype: str
        """
        return self._buffer_barcode

    @buffer_barcode.setter
    def buffer_barcode(self, buffer_barcode):
        """Sets the buffer_barcode of this V2RunCompact.


        :param buffer_barcode: The buffer_barcode of this V2RunCompact.  # noqa: E501
        :type: str
        """

        self._buffer_barcode = buffer_barcode

    @property
    def flowcell_position(self):
        """Gets the flowcell_position of this V2RunCompact.  # noqa: E501


        :return: The flowcell_position of this V2RunCompact.  # noqa: E501
        :rtype: str
        """
        return self._flowcell_position

    @flowcell_position.setter
    def flowcell_position(self, flowcell_position):
        """Sets the flowcell_position of this V2RunCompact.


        :param flowcell_position: The flowcell_position of this V2RunCompact.  # noqa: E501
        :type: str
        """

        self._flowcell_position = flowcell_position

    @property
    def lane_and_qc_status(self):
        """Gets the lane_and_qc_status of this V2RunCompact.  # noqa: E501


        :return: The lane_and_qc_status of this V2RunCompact.  # noqa: E501
        :rtype: str
        """
        return self._lane_and_qc_status

    @lane_and_qc_status.setter
    def lane_and_qc_status(self, lane_and_qc_status):
        """Sets the lane_and_qc_status of this V2RunCompact.


        :param lane_and_qc_status: The lane_and_qc_status of this V2RunCompact.  # noqa: E501
        :type: str
        """

        self._lane_and_qc_status = lane_and_qc_status

    @property
    def prep_kit_name(self):
        """Gets the prep_kit_name of this V2RunCompact.  # noqa: E501


        :return: The prep_kit_name of this V2RunCompact.  # noqa: E501
        :rtype: str
        """
        return self._prep_kit_name

    @prep_kit_name.setter
    def prep_kit_name(self, prep_kit_name):
        """Sets the prep_kit_name of this V2RunCompact.


        :param prep_kit_name: The prep_kit_name of this V2RunCompact.  # noqa: E501
        :type: str
        """

        self._prep_kit_name = prep_kit_name

    @property
    def workflow(self):
        """Gets the workflow of this V2RunCompact.  # noqa: E501


        :return: The workflow of this V2RunCompact.  # noqa: E501
        :rtype: str
        """
        return self._workflow

    @workflow.setter
    def workflow(self, workflow):
        """Sets the workflow of this V2RunCompact.


        :param workflow: The workflow of this V2RunCompact.  # noqa: E501
        :type: str
        """

        self._workflow = workflow

    @property
    def sample_sheet_name(self):
        """Gets the sample_sheet_name of this V2RunCompact.  # noqa: E501


        :return: The sample_sheet_name of this V2RunCompact.  # noqa: E501
        :rtype: str
        """
        return self._sample_sheet_name

    @sample_sheet_name.setter
    def sample_sheet_name(self, sample_sheet_name):
        """Sets the sample_sheet_name of this V2RunCompact.


        :param sample_sheet_name: The sample_sheet_name of this V2RunCompact.  # noqa: E501
        :type: str
        """

        self._sample_sheet_name = sample_sheet_name

    @property
    def total_size(self):
        """Gets the total_size of this V2RunCompact.  # noqa: E501


        :return: The total_size of this V2RunCompact.  # noqa: E501
        :rtype: int
        """
        return self._total_size

    @total_size.setter
    def total_size(self, total_size):
        """Sets the total_size of this V2RunCompact.


        :param total_size: The total_size of this V2RunCompact.  # noqa: E501
        :type: int
        """

        self._total_size = total_size

    @property
    def user_uploaded_by(self):
        """Gets the user_uploaded_by of this V2RunCompact.  # noqa: E501


        :return: The user_uploaded_by of this V2RunCompact.  # noqa: E501
        :rtype: IUserCompact
        """
        return self._user_uploaded_by

    @user_uploaded_by.setter
    def user_uploaded_by(self, user_uploaded_by):
        """Sets the user_uploaded_by of this V2RunCompact.


        :param user_uploaded_by: The user_uploaded_by of this V2RunCompact.  # noqa: E501
        :type: IUserCompact
        """

        self._user_uploaded_by = user_uploaded_by

    @property
    def upload_status(self):
        """Gets the upload_status of this V2RunCompact.  # noqa: E501


        :return: The upload_status of this V2RunCompact.  # noqa: E501
        :rtype: str
        """
        return self._upload_status

    @upload_status.setter
    def upload_status(self, upload_status):
        """Sets the upload_status of this V2RunCompact.


        :param upload_status: The upload_status of this V2RunCompact.  # noqa: E501
        :type: str
        """

        self._upload_status = upload_status

    @property
    def date_upload_started(self):
        """Gets the date_upload_started of this V2RunCompact.  # noqa: E501


        :return: The date_upload_started of this V2RunCompact.  # noqa: E501
        :rtype: datetime
        """
        return self._date_upload_started

    @date_upload_started.setter
    def date_upload_started(self, date_upload_started):
        """Sets the date_upload_started of this V2RunCompact.


        :param date_upload_started: The date_upload_started of this V2RunCompact.  # noqa: E501
        :type: datetime
        """

        self._date_upload_started = date_upload_started

    @property
    def date_upload_completed(self):
        """Gets the date_upload_completed of this V2RunCompact.  # noqa: E501


        :return: The date_upload_completed of this V2RunCompact.  # noqa: E501
        :rtype: datetime
        """
        return self._date_upload_completed

    @date_upload_completed.setter
    def date_upload_completed(self, date_upload_completed):
        """Sets the date_upload_completed of this V2RunCompact.


        :param date_upload_completed: The date_upload_completed of this V2RunCompact.  # noqa: E501
        :type: datetime
        """

        self._date_upload_completed = date_upload_completed

    @property
    def is_deleted(self):
        """Gets the is_deleted of this V2RunCompact.  # noqa: E501


        :return: The is_deleted of this V2RunCompact.  # noqa: E501
        :rtype: bool
        """
        return self._is_deleted

    @is_deleted.setter
    def is_deleted(self, is_deleted):
        """Sets the is_deleted of this V2RunCompact.


        :param is_deleted: The is_deleted of this V2RunCompact.  # noqa: E501
        :type: bool
        """

        self._is_deleted = is_deleted

    @property
    def is_file_data_deleted(self):
        """Gets the is_file_data_deleted of this V2RunCompact.  # noqa: E501


        :return: The is_file_data_deleted of this V2RunCompact.  # noqa: E501
        :rtype: bool
        """
        return self._is_file_data_deleted

    @is_file_data_deleted.setter
    def is_file_data_deleted(self, is_file_data_deleted):
        """Sets the is_file_data_deleted of this V2RunCompact.


        :param is_file_data_deleted: The is_file_data_deleted of this V2RunCompact.  # noqa: E501
        :type: bool
        """

        self._is_file_data_deleted = is_file_data_deleted

    @property
    def is_archived(self):
        """Gets the is_archived of this V2RunCompact.  # noqa: E501


        :return: The is_archived of this V2RunCompact.  # noqa: E501
        :rtype: bool
        """
        return self._is_archived

    @is_archived.setter
    def is_archived(self, is_archived):
        """Sets the is_archived of this V2RunCompact.


        :param is_archived: The is_archived of this V2RunCompact.  # noqa: E501
        :type: bool
        """

        self._is_archived = is_archived

    @property
    def is_zipping(self):
        """Gets the is_zipping of this V2RunCompact.  # noqa: E501


        :return: The is_zipping of this V2RunCompact.  # noqa: E501
        :rtype: bool
        """
        return self._is_zipping

    @is_zipping.setter
    def is_zipping(self, is_zipping):
        """Sets the is_zipping of this V2RunCompact.


        :param is_zipping: The is_zipping of this V2RunCompact.  # noqa: E501
        :type: bool
        """

        self._is_zipping = is_zipping

    @property
    def is_zipped(self):
        """Gets the is_zipped of this V2RunCompact.  # noqa: E501


        :return: The is_zipped of this V2RunCompact.  # noqa: E501
        :rtype: bool
        """
        return self._is_zipped

    @is_zipped.setter
    def is_zipped(self, is_zipped):
        """Sets the is_zipped of this V2RunCompact.


        :param is_zipped: The is_zipped of this V2RunCompact.  # noqa: E501
        :type: bool
        """

        self._is_zipped = is_zipped

    @property
    def is_unzipping(self):
        """Gets the is_unzipping of this V2RunCompact.  # noqa: E501


        :return: The is_unzipping of this V2RunCompact.  # noqa: E501
        :rtype: bool
        """
        return self._is_unzipping

    @is_unzipping.setter
    def is_unzipping(self, is_unzipping):
        """Sets the is_unzipping of this V2RunCompact.


        :param is_unzipping: The is_unzipping of this V2RunCompact.  # noqa: E501
        :type: bool
        """

        self._is_unzipping = is_unzipping

    @property
    def href(self):
        """Gets the href of this V2RunCompact.  # noqa: E501


        :return: The href of this V2RunCompact.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this V2RunCompact.


        :param href: The href of this V2RunCompact.  # noqa: E501
        :type: str
        """
        if href is None:
            raise ValueError("Invalid value for `href`, must not be `None`")  # noqa: E501

        self._href = href

    @property
    def href_files(self):
        """Gets the href_files of this V2RunCompact.  # noqa: E501


        :return: The href_files of this V2RunCompact.  # noqa: E501
        :rtype: str
        """
        return self._href_files

    @href_files.setter
    def href_files(self, href_files):
        """Sets the href_files of this V2RunCompact.


        :param href_files: The href_files of this V2RunCompact.  # noqa: E501
        :type: str
        """

        self._href_files = href_files

    @property
    def href_ica_uri_files(self):
        """Gets the href_ica_uri_files of this V2RunCompact.  # noqa: E501


        :return: The href_ica_uri_files of this V2RunCompact.  # noqa: E501
        :rtype: str
        """
        return self._href_ica_uri_files

    @href_ica_uri_files.setter
    def href_ica_uri_files(self, href_ica_uri_files):
        """Sets the href_ica_uri_files of this V2RunCompact.


        :param href_ica_uri_files: The href_ica_uri_files of this V2RunCompact.  # noqa: E501
        :type: str
        """

        self._href_ica_uri_files = href_ica_uri_files

    @property
    def has_files_in_ica(self):
        """Gets the has_files_in_ica of this V2RunCompact.  # noqa: E501


        :return: The has_files_in_ica of this V2RunCompact.  # noqa: E501
        :rtype: bool
        """
        return self._has_files_in_ica

    @has_files_in_ica.setter
    def has_files_in_ica(self, has_files_in_ica):
        """Sets the has_files_in_ica of this V2RunCompact.


        :param has_files_in_ica: The has_files_in_ica of this V2RunCompact.  # noqa: E501
        :type: bool
        """

        self._has_files_in_ica = has_files_in_ica

    @property
    def properties(self):
        """Gets the properties of this V2RunCompact.  # noqa: E501


        :return: The properties of this V2RunCompact.  # noqa: E501
        :rtype: V2PropertyContainer
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this V2RunCompact.


        :param properties: The properties of this V2RunCompact.  # noqa: E501
        :type: V2PropertyContainer
        """

        self._properties = properties

    @property
    def v1_pre3_id(self):
        """Gets the v1_pre3_id of this V2RunCompact.  # noqa: E501


        :return: The v1_pre3_id of this V2RunCompact.  # noqa: E501
        :rtype: str
        """
        return self._v1_pre3_id

    @v1_pre3_id.setter
    def v1_pre3_id(self, v1_pre3_id):
        """Sets the v1_pre3_id of this V2RunCompact.


        :param v1_pre3_id: The v1_pre3_id of this V2RunCompact.  # noqa: E501
        :type: str
        """

        self._v1_pre3_id = v1_pre3_id

    @property
    def is_transfer_pending(self):
        """Gets the is_transfer_pending of this V2RunCompact.  # noqa: E501


        :return: The is_transfer_pending of this V2RunCompact.  # noqa: E501
        :rtype: bool
        """
        return self._is_transfer_pending

    @is_transfer_pending.setter
    def is_transfer_pending(self, is_transfer_pending):
        """Sets the is_transfer_pending of this V2RunCompact.


        :param is_transfer_pending: The is_transfer_pending of this V2RunCompact.  # noqa: E501
        :type: bool
        """

        self._is_transfer_pending = is_transfer_pending

    @property
    def is_transfer_in_progress(self):
        """Gets the is_transfer_in_progress of this V2RunCompact.  # noqa: E501


        :return: The is_transfer_in_progress of this V2RunCompact.  # noqa: E501
        :rtype: bool
        """
        return self._is_transfer_in_progress

    @is_transfer_in_progress.setter
    def is_transfer_in_progress(self, is_transfer_in_progress):
        """Sets the is_transfer_in_progress of this V2RunCompact.


        :param is_transfer_in_progress: The is_transfer_in_progress of this V2RunCompact.  # noqa: E501
        :type: bool
        """

        self._is_transfer_in_progress = is_transfer_in_progress

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(V2RunCompact, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V2RunCompact):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
