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

class SampleCompact(object):
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
        'href': 'str',
        'is_merged': 'bool',
        'user_owned_by': 'V1pre3UserCompact',
        'name': 'str',
        'experiment_name': 'str',
        'sample_id': 'str',
        'status': 'str',
        'status_summary': 'str',
        'date_created': 'datetime',
        'total_size': 'int',
        'app_session': 'AppSessionCompact',
        'projects': 'list[V1pre3ProjectCompact]',
        'library': 'SampleLibrary',
        'genome': 'GenomeCompact',
        'read1': 'int',
        'read2': 'int',
        'num_reads_pf': 'int',
        'num_reads_raw': 'int',
        'total_reads_raw': 'int',
        'total_reads_pf': 'int',
        'total_clusters_raw': 'int',
        'total_clusters_pf': 'int',
        'is_paired_end': 'bool',
        'is_deleted': 'bool'
    }

    attribute_map = {
        'id': 'Id',
        'href': 'Href',
        'is_merged': 'IsMerged',
        'user_owned_by': 'UserOwnedBy',
        'name': 'Name',
        'experiment_name': 'ExperimentName',
        'sample_id': 'SampleId',
        'status': 'Status',
        'status_summary': 'StatusSummary',
        'date_created': 'DateCreated',
        'total_size': 'TotalSize',
        'app_session': 'AppSession',
        'projects': 'Projects',
        'library': 'Library',
        'genome': 'Genome',
        'read1': 'Read1',
        'read2': 'Read2',
        'num_reads_pf': 'NumReadsPF',
        'num_reads_raw': 'NumReadsRaw',
        'total_reads_raw': 'TotalReadsRaw',
        'total_reads_pf': 'TotalReadsPF',
        'total_clusters_raw': 'TotalClustersRaw',
        'total_clusters_pf': 'TotalClustersPF',
        'is_paired_end': 'IsPairedEnd',
        'is_deleted': 'IsDeleted'
    }

    def __init__(self, id=None, href=None, is_merged=None, user_owned_by=None, name=None, experiment_name=None, sample_id=None, status=None, status_summary=None, date_created=None, total_size=None, app_session=None, projects=None, library=None, genome=None, read1=None, read2=None, num_reads_pf=None, num_reads_raw=None, total_reads_raw=None, total_reads_pf=None, total_clusters_raw=None, total_clusters_pf=None, is_paired_end=None, is_deleted=None):  # noqa: E501
        """SampleCompact - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._href = None
        self._is_merged = None
        self._user_owned_by = None
        self._name = None
        self._experiment_name = None
        self._sample_id = None
        self._status = None
        self._status_summary = None
        self._date_created = None
        self._total_size = None
        self._app_session = None
        self._projects = None
        self._library = None
        self._genome = None
        self._read1 = None
        self._read2 = None
        self._num_reads_pf = None
        self._num_reads_raw = None
        self._total_reads_raw = None
        self._total_reads_pf = None
        self._total_clusters_raw = None
        self._total_clusters_pf = None
        self._is_paired_end = None
        self._is_deleted = None
        self.discriminator = None
        self.id = id
        if href is not None:
            self.href = href
        if is_merged is not None:
            self.is_merged = is_merged
        if user_owned_by is not None:
            self.user_owned_by = user_owned_by
        if name is not None:
            self.name = name
        if experiment_name is not None:
            self.experiment_name = experiment_name
        if sample_id is not None:
            self.sample_id = sample_id
        if status is not None:
            self.status = status
        if status_summary is not None:
            self.status_summary = status_summary
        if date_created is not None:
            self.date_created = date_created
        if total_size is not None:
            self.total_size = total_size
        if app_session is not None:
            self.app_session = app_session
        if projects is not None:
            self.projects = projects
        if library is not None:
            self.library = library
        if genome is not None:
            self.genome = genome
        if read1 is not None:
            self.read1 = read1
        if read2 is not None:
            self.read2 = read2
        if num_reads_pf is not None:
            self.num_reads_pf = num_reads_pf
        if num_reads_raw is not None:
            self.num_reads_raw = num_reads_raw
        if total_reads_raw is not None:
            self.total_reads_raw = total_reads_raw
        if total_reads_pf is not None:
            self.total_reads_pf = total_reads_pf
        if total_clusters_raw is not None:
            self.total_clusters_raw = total_clusters_raw
        if total_clusters_pf is not None:
            self.total_clusters_pf = total_clusters_pf
        if is_paired_end is not None:
            self.is_paired_end = is_paired_end
        if is_deleted is not None:
            self.is_deleted = is_deleted

    @property
    def id(self):
        """Gets the id of this SampleCompact.  # noqa: E501


        :return: The id of this SampleCompact.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SampleCompact.


        :param id: The id of this SampleCompact.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def href(self):
        """Gets the href of this SampleCompact.  # noqa: E501


        :return: The href of this SampleCompact.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this SampleCompact.


        :param href: The href of this SampleCompact.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def is_merged(self):
        """Gets the is_merged of this SampleCompact.  # noqa: E501


        :return: The is_merged of this SampleCompact.  # noqa: E501
        :rtype: bool
        """
        return self._is_merged

    @is_merged.setter
    def is_merged(self, is_merged):
        """Sets the is_merged of this SampleCompact.


        :param is_merged: The is_merged of this SampleCompact.  # noqa: E501
        :type: bool
        """

        self._is_merged = is_merged

    @property
    def user_owned_by(self):
        """Gets the user_owned_by of this SampleCompact.  # noqa: E501


        :return: The user_owned_by of this SampleCompact.  # noqa: E501
        :rtype: V1pre3UserCompact
        """
        return self._user_owned_by

    @user_owned_by.setter
    def user_owned_by(self, user_owned_by):
        """Sets the user_owned_by of this SampleCompact.


        :param user_owned_by: The user_owned_by of this SampleCompact.  # noqa: E501
        :type: V1pre3UserCompact
        """

        self._user_owned_by = user_owned_by

    @property
    def name(self):
        """Gets the name of this SampleCompact.  # noqa: E501


        :return: The name of this SampleCompact.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SampleCompact.


        :param name: The name of this SampleCompact.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def experiment_name(self):
        """Gets the experiment_name of this SampleCompact.  # noqa: E501


        :return: The experiment_name of this SampleCompact.  # noqa: E501
        :rtype: str
        """
        return self._experiment_name

    @experiment_name.setter
    def experiment_name(self, experiment_name):
        """Sets the experiment_name of this SampleCompact.


        :param experiment_name: The experiment_name of this SampleCompact.  # noqa: E501
        :type: str
        """

        self._experiment_name = experiment_name

    @property
    def sample_id(self):
        """Gets the sample_id of this SampleCompact.  # noqa: E501


        :return: The sample_id of this SampleCompact.  # noqa: E501
        :rtype: str
        """
        return self._sample_id

    @sample_id.setter
    def sample_id(self, sample_id):
        """Sets the sample_id of this SampleCompact.


        :param sample_id: The sample_id of this SampleCompact.  # noqa: E501
        :type: str
        """

        self._sample_id = sample_id

    @property
    def status(self):
        """Gets the status of this SampleCompact.  # noqa: E501


        :return: The status of this SampleCompact.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SampleCompact.


        :param status: The status of this SampleCompact.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def status_summary(self):
        """Gets the status_summary of this SampleCompact.  # noqa: E501


        :return: The status_summary of this SampleCompact.  # noqa: E501
        :rtype: str
        """
        return self._status_summary

    @status_summary.setter
    def status_summary(self, status_summary):
        """Sets the status_summary of this SampleCompact.


        :param status_summary: The status_summary of this SampleCompact.  # noqa: E501
        :type: str
        """

        self._status_summary = status_summary

    @property
    def date_created(self):
        """Gets the date_created of this SampleCompact.  # noqa: E501


        :return: The date_created of this SampleCompact.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this SampleCompact.


        :param date_created: The date_created of this SampleCompact.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def total_size(self):
        """Gets the total_size of this SampleCompact.  # noqa: E501


        :return: The total_size of this SampleCompact.  # noqa: E501
        :rtype: int
        """
        return self._total_size

    @total_size.setter
    def total_size(self, total_size):
        """Sets the total_size of this SampleCompact.


        :param total_size: The total_size of this SampleCompact.  # noqa: E501
        :type: int
        """

        self._total_size = total_size

    @property
    def app_session(self):
        """Gets the app_session of this SampleCompact.  # noqa: E501


        :return: The app_session of this SampleCompact.  # noqa: E501
        :rtype: AppSessionCompact
        """
        return self._app_session

    @app_session.setter
    def app_session(self, app_session):
        """Sets the app_session of this SampleCompact.


        :param app_session: The app_session of this SampleCompact.  # noqa: E501
        :type: AppSessionCompact
        """

        self._app_session = app_session

    @property
    def projects(self):
        """Gets the projects of this SampleCompact.  # noqa: E501


        :return: The projects of this SampleCompact.  # noqa: E501
        :rtype: list[V1pre3ProjectCompact]
        """
        return self._projects

    @projects.setter
    def projects(self, projects):
        """Sets the projects of this SampleCompact.


        :param projects: The projects of this SampleCompact.  # noqa: E501
        :type: list[V1pre3ProjectCompact]
        """

        self._projects = projects

    @property
    def library(self):
        """Gets the library of this SampleCompact.  # noqa: E501


        :return: The library of this SampleCompact.  # noqa: E501
        :rtype: SampleLibrary
        """
        return self._library

    @library.setter
    def library(self, library):
        """Sets the library of this SampleCompact.


        :param library: The library of this SampleCompact.  # noqa: E501
        :type: SampleLibrary
        """

        self._library = library

    @property
    def genome(self):
        """Gets the genome of this SampleCompact.  # noqa: E501


        :return: The genome of this SampleCompact.  # noqa: E501
        :rtype: GenomeCompact
        """
        return self._genome

    @genome.setter
    def genome(self, genome):
        """Sets the genome of this SampleCompact.


        :param genome: The genome of this SampleCompact.  # noqa: E501
        :type: GenomeCompact
        """

        self._genome = genome

    @property
    def read1(self):
        """Gets the read1 of this SampleCompact.  # noqa: E501


        :return: The read1 of this SampleCompact.  # noqa: E501
        :rtype: int
        """
        return self._read1

    @read1.setter
    def read1(self, read1):
        """Sets the read1 of this SampleCompact.


        :param read1: The read1 of this SampleCompact.  # noqa: E501
        :type: int
        """

        self._read1 = read1

    @property
    def read2(self):
        """Gets the read2 of this SampleCompact.  # noqa: E501


        :return: The read2 of this SampleCompact.  # noqa: E501
        :rtype: int
        """
        return self._read2

    @read2.setter
    def read2(self, read2):
        """Sets the read2 of this SampleCompact.


        :param read2: The read2 of this SampleCompact.  # noqa: E501
        :type: int
        """

        self._read2 = read2

    @property
    def num_reads_pf(self):
        """Gets the num_reads_pf of this SampleCompact.  # noqa: E501


        :return: The num_reads_pf of this SampleCompact.  # noqa: E501
        :rtype: int
        """
        return self._num_reads_pf

    @num_reads_pf.setter
    def num_reads_pf(self, num_reads_pf):
        """Sets the num_reads_pf of this SampleCompact.


        :param num_reads_pf: The num_reads_pf of this SampleCompact.  # noqa: E501
        :type: int
        """

        self._num_reads_pf = num_reads_pf

    @property
    def num_reads_raw(self):
        """Gets the num_reads_raw of this SampleCompact.  # noqa: E501


        :return: The num_reads_raw of this SampleCompact.  # noqa: E501
        :rtype: int
        """
        return self._num_reads_raw

    @num_reads_raw.setter
    def num_reads_raw(self, num_reads_raw):
        """Sets the num_reads_raw of this SampleCompact.


        :param num_reads_raw: The num_reads_raw of this SampleCompact.  # noqa: E501
        :type: int
        """

        self._num_reads_raw = num_reads_raw

    @property
    def total_reads_raw(self):
        """Gets the total_reads_raw of this SampleCompact.  # noqa: E501


        :return: The total_reads_raw of this SampleCompact.  # noqa: E501
        :rtype: int
        """
        return self._total_reads_raw

    @total_reads_raw.setter
    def total_reads_raw(self, total_reads_raw):
        """Sets the total_reads_raw of this SampleCompact.


        :param total_reads_raw: The total_reads_raw of this SampleCompact.  # noqa: E501
        :type: int
        """

        self._total_reads_raw = total_reads_raw

    @property
    def total_reads_pf(self):
        """Gets the total_reads_pf of this SampleCompact.  # noqa: E501


        :return: The total_reads_pf of this SampleCompact.  # noqa: E501
        :rtype: int
        """
        return self._total_reads_pf

    @total_reads_pf.setter
    def total_reads_pf(self, total_reads_pf):
        """Sets the total_reads_pf of this SampleCompact.


        :param total_reads_pf: The total_reads_pf of this SampleCompact.  # noqa: E501
        :type: int
        """

        self._total_reads_pf = total_reads_pf

    @property
    def total_clusters_raw(self):
        """Gets the total_clusters_raw of this SampleCompact.  # noqa: E501


        :return: The total_clusters_raw of this SampleCompact.  # noqa: E501
        :rtype: int
        """
        return self._total_clusters_raw

    @total_clusters_raw.setter
    def total_clusters_raw(self, total_clusters_raw):
        """Sets the total_clusters_raw of this SampleCompact.


        :param total_clusters_raw: The total_clusters_raw of this SampleCompact.  # noqa: E501
        :type: int
        """

        self._total_clusters_raw = total_clusters_raw

    @property
    def total_clusters_pf(self):
        """Gets the total_clusters_pf of this SampleCompact.  # noqa: E501


        :return: The total_clusters_pf of this SampleCompact.  # noqa: E501
        :rtype: int
        """
        return self._total_clusters_pf

    @total_clusters_pf.setter
    def total_clusters_pf(self, total_clusters_pf):
        """Sets the total_clusters_pf of this SampleCompact.


        :param total_clusters_pf: The total_clusters_pf of this SampleCompact.  # noqa: E501
        :type: int
        """

        self._total_clusters_pf = total_clusters_pf

    @property
    def is_paired_end(self):
        """Gets the is_paired_end of this SampleCompact.  # noqa: E501


        :return: The is_paired_end of this SampleCompact.  # noqa: E501
        :rtype: bool
        """
        return self._is_paired_end

    @is_paired_end.setter
    def is_paired_end(self, is_paired_end):
        """Sets the is_paired_end of this SampleCompact.


        :param is_paired_end: The is_paired_end of this SampleCompact.  # noqa: E501
        :type: bool
        """

        self._is_paired_end = is_paired_end

    @property
    def is_deleted(self):
        """Gets the is_deleted of this SampleCompact.  # noqa: E501


        :return: The is_deleted of this SampleCompact.  # noqa: E501
        :rtype: bool
        """
        return self._is_deleted

    @is_deleted.setter
    def is_deleted(self, is_deleted):
        """Sets the is_deleted of this SampleCompact.


        :param is_deleted: The is_deleted of this SampleCompact.  # noqa: E501
        :type: bool
        """

        self._is_deleted = is_deleted

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
        if issubclass(SampleCompact, dict):
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
        if not isinstance(other, SampleCompact):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
