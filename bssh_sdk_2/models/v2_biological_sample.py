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

class V2BiologicalSample(object):
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
        'yield_calculation_logs': 'str',
        'has_fastq_datasets_aggregated_from_multiple_sources': 'bool',
        'user_has_unlocked_bio_sample_for_aggregation': 'bool',
        'id': 'str',
        'href': 'str',
        'user_owned_by': 'V1pre3UserCompact',
        'bio_sample_name': 'str',
        'nickname': 'str',
        'default_project': 'V1pre3ProjectCompact',
        'date_modified': 'datetime',
        'date_created': 'datetime',
        'subject': 'V2SubjectCompact',
        'container_name': 'str',
        'container_position': 'str',
        'status': 'str',
        'lab_status': 'str',
        'href_ica_uri_samples': 'str',
        'prep_requests': 'list[V2PrepRequest]',
        'library_preps': 'list[NameAndId]',
        'output_project_ids': 'list[str]',
        'yields': 'list[V2BiologicalSampleLibraryYield]',
        'properties': 'V2PropertyContainer',
        'has_qc_passed_fastq_datasets': 'bool'
    }

    attribute_map = {
        'yield_calculation_logs': 'YieldCalculationLogs',
        'has_fastq_datasets_aggregated_from_multiple_sources': 'HasFastqDatasetsAggregatedFromMultipleSources',
        'user_has_unlocked_bio_sample_for_aggregation': 'UserHasUnlockedBioSampleForAggregation',
        'id': 'Id',
        'href': 'Href',
        'user_owned_by': 'UserOwnedBy',
        'bio_sample_name': 'BioSampleName',
        'nickname': 'Nickname',
        'default_project': 'DefaultProject',
        'date_modified': 'DateModified',
        'date_created': 'DateCreated',
        'subject': 'Subject',
        'container_name': 'ContainerName',
        'container_position': 'ContainerPosition',
        'status': 'Status',
        'lab_status': 'LabStatus',
        'href_ica_uri_samples': 'HrefIcaUriSamples',
        'prep_requests': 'PrepRequests',
        'library_preps': 'LibraryPreps',
        'output_project_ids': 'OutputProjectIds',
        'yields': 'Yields',
        'properties': 'Properties',
        'has_qc_passed_fastq_datasets': 'HasQcPassedFastqDatasets'
    }

    def __init__(self, yield_calculation_logs=None, has_fastq_datasets_aggregated_from_multiple_sources=None, user_has_unlocked_bio_sample_for_aggregation=None, id=None, href=None, user_owned_by=None, bio_sample_name=None, nickname=None, default_project=None, date_modified=None, date_created=None, subject=None, container_name=None, container_position=None, status=None, lab_status=None, href_ica_uri_samples=None, prep_requests=None, library_preps=None, output_project_ids=None, yields=None, properties=None, has_qc_passed_fastq_datasets=None):  # noqa: E501
        """V2BiologicalSample - a model defined in Swagger"""  # noqa: E501
        self._yield_calculation_logs = None
        self._has_fastq_datasets_aggregated_from_multiple_sources = None
        self._user_has_unlocked_bio_sample_for_aggregation = None
        self._id = None
        self._href = None
        self._user_owned_by = None
        self._bio_sample_name = None
        self._nickname = None
        self._default_project = None
        self._date_modified = None
        self._date_created = None
        self._subject = None
        self._container_name = None
        self._container_position = None
        self._status = None
        self._lab_status = None
        self._href_ica_uri_samples = None
        self._prep_requests = None
        self._library_preps = None
        self._output_project_ids = None
        self._yields = None
        self._properties = None
        self._has_qc_passed_fastq_datasets = None
        self.discriminator = None
        if yield_calculation_logs is not None:
            self.yield_calculation_logs = yield_calculation_logs
        if has_fastq_datasets_aggregated_from_multiple_sources is not None:
            self.has_fastq_datasets_aggregated_from_multiple_sources = has_fastq_datasets_aggregated_from_multiple_sources
        if user_has_unlocked_bio_sample_for_aggregation is not None:
            self.user_has_unlocked_bio_sample_for_aggregation = user_has_unlocked_bio_sample_for_aggregation
        self.id = id
        if href is not None:
            self.href = href
        if user_owned_by is not None:
            self.user_owned_by = user_owned_by
        if bio_sample_name is not None:
            self.bio_sample_name = bio_sample_name
        if nickname is not None:
            self.nickname = nickname
        if default_project is not None:
            self.default_project = default_project
        if date_modified is not None:
            self.date_modified = date_modified
        if date_created is not None:
            self.date_created = date_created
        if subject is not None:
            self.subject = subject
        if container_name is not None:
            self.container_name = container_name
        if container_position is not None:
            self.container_position = container_position
        if status is not None:
            self.status = status
        if lab_status is not None:
            self.lab_status = lab_status
        if href_ica_uri_samples is not None:
            self.href_ica_uri_samples = href_ica_uri_samples
        if prep_requests is not None:
            self.prep_requests = prep_requests
        if library_preps is not None:
            self.library_preps = library_preps
        if output_project_ids is not None:
            self.output_project_ids = output_project_ids
        if yields is not None:
            self.yields = yields
        if properties is not None:
            self.properties = properties
        if has_qc_passed_fastq_datasets is not None:
            self.has_qc_passed_fastq_datasets = has_qc_passed_fastq_datasets

    @property
    def yield_calculation_logs(self):
        """Gets the yield_calculation_logs of this V2BiologicalSample.  # noqa: E501


        :return: The yield_calculation_logs of this V2BiologicalSample.  # noqa: E501
        :rtype: str
        """
        return self._yield_calculation_logs

    @yield_calculation_logs.setter
    def yield_calculation_logs(self, yield_calculation_logs):
        """Sets the yield_calculation_logs of this V2BiologicalSample.


        :param yield_calculation_logs: The yield_calculation_logs of this V2BiologicalSample.  # noqa: E501
        :type: str
        """

        self._yield_calculation_logs = yield_calculation_logs

    @property
    def has_fastq_datasets_aggregated_from_multiple_sources(self):
        """Gets the has_fastq_datasets_aggregated_from_multiple_sources of this V2BiologicalSample.  # noqa: E501


        :return: The has_fastq_datasets_aggregated_from_multiple_sources of this V2BiologicalSample.  # noqa: E501
        :rtype: bool
        """
        return self._has_fastq_datasets_aggregated_from_multiple_sources

    @has_fastq_datasets_aggregated_from_multiple_sources.setter
    def has_fastq_datasets_aggregated_from_multiple_sources(self, has_fastq_datasets_aggregated_from_multiple_sources):
        """Sets the has_fastq_datasets_aggregated_from_multiple_sources of this V2BiologicalSample.


        :param has_fastq_datasets_aggregated_from_multiple_sources: The has_fastq_datasets_aggregated_from_multiple_sources of this V2BiologicalSample.  # noqa: E501
        :type: bool
        """

        self._has_fastq_datasets_aggregated_from_multiple_sources = has_fastq_datasets_aggregated_from_multiple_sources

    @property
    def user_has_unlocked_bio_sample_for_aggregation(self):
        """Gets the user_has_unlocked_bio_sample_for_aggregation of this V2BiologicalSample.  # noqa: E501


        :return: The user_has_unlocked_bio_sample_for_aggregation of this V2BiologicalSample.  # noqa: E501
        :rtype: bool
        """
        return self._user_has_unlocked_bio_sample_for_aggregation

    @user_has_unlocked_bio_sample_for_aggregation.setter
    def user_has_unlocked_bio_sample_for_aggregation(self, user_has_unlocked_bio_sample_for_aggregation):
        """Sets the user_has_unlocked_bio_sample_for_aggregation of this V2BiologicalSample.


        :param user_has_unlocked_bio_sample_for_aggregation: The user_has_unlocked_bio_sample_for_aggregation of this V2BiologicalSample.  # noqa: E501
        :type: bool
        """

        self._user_has_unlocked_bio_sample_for_aggregation = user_has_unlocked_bio_sample_for_aggregation

    @property
    def id(self):
        """Gets the id of this V2BiologicalSample.  # noqa: E501


        :return: The id of this V2BiologicalSample.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this V2BiologicalSample.


        :param id: The id of this V2BiologicalSample.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def href(self):
        """Gets the href of this V2BiologicalSample.  # noqa: E501


        :return: The href of this V2BiologicalSample.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this V2BiologicalSample.


        :param href: The href of this V2BiologicalSample.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def user_owned_by(self):
        """Gets the user_owned_by of this V2BiologicalSample.  # noqa: E501


        :return: The user_owned_by of this V2BiologicalSample.  # noqa: E501
        :rtype: V1pre3UserCompact
        """
        return self._user_owned_by

    @user_owned_by.setter
    def user_owned_by(self, user_owned_by):
        """Sets the user_owned_by of this V2BiologicalSample.


        :param user_owned_by: The user_owned_by of this V2BiologicalSample.  # noqa: E501
        :type: V1pre3UserCompact
        """

        self._user_owned_by = user_owned_by

    @property
    def bio_sample_name(self):
        """Gets the bio_sample_name of this V2BiologicalSample.  # noqa: E501


        :return: The bio_sample_name of this V2BiologicalSample.  # noqa: E501
        :rtype: str
        """
        return self._bio_sample_name

    @bio_sample_name.setter
    def bio_sample_name(self, bio_sample_name):
        """Sets the bio_sample_name of this V2BiologicalSample.


        :param bio_sample_name: The bio_sample_name of this V2BiologicalSample.  # noqa: E501
        :type: str
        """

        self._bio_sample_name = bio_sample_name

    @property
    def nickname(self):
        """Gets the nickname of this V2BiologicalSample.  # noqa: E501


        :return: The nickname of this V2BiologicalSample.  # noqa: E501
        :rtype: str
        """
        return self._nickname

    @nickname.setter
    def nickname(self, nickname):
        """Sets the nickname of this V2BiologicalSample.


        :param nickname: The nickname of this V2BiologicalSample.  # noqa: E501
        :type: str
        """

        self._nickname = nickname

    @property
    def default_project(self):
        """Gets the default_project of this V2BiologicalSample.  # noqa: E501


        :return: The default_project of this V2BiologicalSample.  # noqa: E501
        :rtype: V1pre3ProjectCompact
        """
        return self._default_project

    @default_project.setter
    def default_project(self, default_project):
        """Sets the default_project of this V2BiologicalSample.


        :param default_project: The default_project of this V2BiologicalSample.  # noqa: E501
        :type: V1pre3ProjectCompact
        """

        self._default_project = default_project

    @property
    def date_modified(self):
        """Gets the date_modified of this V2BiologicalSample.  # noqa: E501


        :return: The date_modified of this V2BiologicalSample.  # noqa: E501
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this V2BiologicalSample.


        :param date_modified: The date_modified of this V2BiologicalSample.  # noqa: E501
        :type: datetime
        """

        self._date_modified = date_modified

    @property
    def date_created(self):
        """Gets the date_created of this V2BiologicalSample.  # noqa: E501


        :return: The date_created of this V2BiologicalSample.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this V2BiologicalSample.


        :param date_created: The date_created of this V2BiologicalSample.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def subject(self):
        """Gets the subject of this V2BiologicalSample.  # noqa: E501


        :return: The subject of this V2BiologicalSample.  # noqa: E501
        :rtype: V2SubjectCompact
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this V2BiologicalSample.


        :param subject: The subject of this V2BiologicalSample.  # noqa: E501
        :type: V2SubjectCompact
        """

        self._subject = subject

    @property
    def container_name(self):
        """Gets the container_name of this V2BiologicalSample.  # noqa: E501


        :return: The container_name of this V2BiologicalSample.  # noqa: E501
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name):
        """Sets the container_name of this V2BiologicalSample.


        :param container_name: The container_name of this V2BiologicalSample.  # noqa: E501
        :type: str
        """

        self._container_name = container_name

    @property
    def container_position(self):
        """Gets the container_position of this V2BiologicalSample.  # noqa: E501


        :return: The container_position of this V2BiologicalSample.  # noqa: E501
        :rtype: str
        """
        return self._container_position

    @container_position.setter
    def container_position(self, container_position):
        """Sets the container_position of this V2BiologicalSample.


        :param container_position: The container_position of this V2BiologicalSample.  # noqa: E501
        :type: str
        """

        self._container_position = container_position

    @property
    def status(self):
        """Gets the status of this V2BiologicalSample.  # noqa: E501


        :return: The status of this V2BiologicalSample.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this V2BiologicalSample.


        :param status: The status of this V2BiologicalSample.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def lab_status(self):
        """Gets the lab_status of this V2BiologicalSample.  # noqa: E501


        :return: The lab_status of this V2BiologicalSample.  # noqa: E501
        :rtype: str
        """
        return self._lab_status

    @lab_status.setter
    def lab_status(self, lab_status):
        """Sets the lab_status of this V2BiologicalSample.


        :param lab_status: The lab_status of this V2BiologicalSample.  # noqa: E501
        :type: str
        """

        self._lab_status = lab_status

    @property
    def href_ica_uri_samples(self):
        """Gets the href_ica_uri_samples of this V2BiologicalSample.  # noqa: E501


        :return: The href_ica_uri_samples of this V2BiologicalSample.  # noqa: E501
        :rtype: str
        """
        return self._href_ica_uri_samples

    @href_ica_uri_samples.setter
    def href_ica_uri_samples(self, href_ica_uri_samples):
        """Sets the href_ica_uri_samples of this V2BiologicalSample.


        :param href_ica_uri_samples: The href_ica_uri_samples of this V2BiologicalSample.  # noqa: E501
        :type: str
        """

        self._href_ica_uri_samples = href_ica_uri_samples

    @property
    def prep_requests(self):
        """Gets the prep_requests of this V2BiologicalSample.  # noqa: E501


        :return: The prep_requests of this V2BiologicalSample.  # noqa: E501
        :rtype: list[V2PrepRequest]
        """
        return self._prep_requests

    @prep_requests.setter
    def prep_requests(self, prep_requests):
        """Sets the prep_requests of this V2BiologicalSample.


        :param prep_requests: The prep_requests of this V2BiologicalSample.  # noqa: E501
        :type: list[V2PrepRequest]
        """

        self._prep_requests = prep_requests

    @property
    def library_preps(self):
        """Gets the library_preps of this V2BiologicalSample.  # noqa: E501


        :return: The library_preps of this V2BiologicalSample.  # noqa: E501
        :rtype: list[NameAndId]
        """
        return self._library_preps

    @library_preps.setter
    def library_preps(self, library_preps):
        """Sets the library_preps of this V2BiologicalSample.


        :param library_preps: The library_preps of this V2BiologicalSample.  # noqa: E501
        :type: list[NameAndId]
        """

        self._library_preps = library_preps

    @property
    def output_project_ids(self):
        """Gets the output_project_ids of this V2BiologicalSample.  # noqa: E501


        :return: The output_project_ids of this V2BiologicalSample.  # noqa: E501
        :rtype: list[str]
        """
        return self._output_project_ids

    @output_project_ids.setter
    def output_project_ids(self, output_project_ids):
        """Sets the output_project_ids of this V2BiologicalSample.


        :param output_project_ids: The output_project_ids of this V2BiologicalSample.  # noqa: E501
        :type: list[str]
        """

        self._output_project_ids = output_project_ids

    @property
    def yields(self):
        """Gets the yields of this V2BiologicalSample.  # noqa: E501


        :return: The yields of this V2BiologicalSample.  # noqa: E501
        :rtype: list[V2BiologicalSampleLibraryYield]
        """
        return self._yields

    @yields.setter
    def yields(self, yields):
        """Sets the yields of this V2BiologicalSample.


        :param yields: The yields of this V2BiologicalSample.  # noqa: E501
        :type: list[V2BiologicalSampleLibraryYield]
        """

        self._yields = yields

    @property
    def properties(self):
        """Gets the properties of this V2BiologicalSample.  # noqa: E501


        :return: The properties of this V2BiologicalSample.  # noqa: E501
        :rtype: V2PropertyContainer
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this V2BiologicalSample.


        :param properties: The properties of this V2BiologicalSample.  # noqa: E501
        :type: V2PropertyContainer
        """

        self._properties = properties

    @property
    def has_qc_passed_fastq_datasets(self):
        """Gets the has_qc_passed_fastq_datasets of this V2BiologicalSample.  # noqa: E501


        :return: The has_qc_passed_fastq_datasets of this V2BiologicalSample.  # noqa: E501
        :rtype: bool
        """
        return self._has_qc_passed_fastq_datasets

    @has_qc_passed_fastq_datasets.setter
    def has_qc_passed_fastq_datasets(self, has_qc_passed_fastq_datasets):
        """Sets the has_qc_passed_fastq_datasets of this V2BiologicalSample.


        :param has_qc_passed_fastq_datasets: The has_qc_passed_fastq_datasets of this V2BiologicalSample.  # noqa: E501
        :type: bool
        """

        self._has_qc_passed_fastq_datasets = has_qc_passed_fastq_datasets

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
        if issubclass(V2BiologicalSample, dict):
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
        if not isinstance(other, V2BiologicalSample):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
