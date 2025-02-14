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

class SampleLibrary(object):
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
        'properties': 'V2PropertyContainer',
        'owner_user': 'V1pre3UserCompact',
        'id': 'str',
        'href': 'str',
        'biological_sample': 'V1pre3BiologicalSampleCompact',
        'container_position': 'str',
        'index1': 'LibraryIndexCompact',
        'index2': 'LibraryIndexCompact',
        'date_modified': 'datetime',
        'library_prep': 'LibraryPrepKitCompact',
        'project': 'V1pre3ProjectCompact',
        'container': 'LibraryContainerCompact',
        'container_end_position': 'str',
        'library_name': 'str',
        'insert_size': 'str',
        'state': 'str'
    }

    attribute_map = {
        'properties': 'Properties',
        'owner_user': 'OwnerUser',
        'id': 'Id',
        'href': 'Href',
        'biological_sample': 'BiologicalSample',
        'container_position': 'ContainerPosition',
        'index1': 'Index1',
        'index2': 'Index2',
        'date_modified': 'DateModified',
        'library_prep': 'LibraryPrep',
        'project': 'Project',
        'container': 'Container',
        'container_end_position': 'ContainerEndPosition',
        'library_name': 'LibraryName',
        'insert_size': 'InsertSize',
        'state': 'State'
    }

    def __init__(self, properties=None, owner_user=None, id=None, href=None, biological_sample=None, container_position=None, index1=None, index2=None, date_modified=None, library_prep=None, project=None, container=None, container_end_position=None, library_name=None, insert_size=None, state=None):  # noqa: E501
        """SampleLibrary - a model defined in Swagger"""  # noqa: E501
        self._properties = None
        self._owner_user = None
        self._id = None
        self._href = None
        self._biological_sample = None
        self._container_position = None
        self._index1 = None
        self._index2 = None
        self._date_modified = None
        self._library_prep = None
        self._project = None
        self._container = None
        self._container_end_position = None
        self._library_name = None
        self._insert_size = None
        self._state = None
        self.discriminator = None
        if properties is not None:
            self.properties = properties
        if owner_user is not None:
            self.owner_user = owner_user
        self.id = id
        if href is not None:
            self.href = href
        if biological_sample is not None:
            self.biological_sample = biological_sample
        if container_position is not None:
            self.container_position = container_position
        if index1 is not None:
            self.index1 = index1
        if index2 is not None:
            self.index2 = index2
        if date_modified is not None:
            self.date_modified = date_modified
        if library_prep is not None:
            self.library_prep = library_prep
        if project is not None:
            self.project = project
        if container is not None:
            self.container = container
        if container_end_position is not None:
            self.container_end_position = container_end_position
        if library_name is not None:
            self.library_name = library_name
        if insert_size is not None:
            self.insert_size = insert_size
        if state is not None:
            self.state = state

    @property
    def properties(self):
        """Gets the properties of this SampleLibrary.  # noqa: E501


        :return: The properties of this SampleLibrary.  # noqa: E501
        :rtype: V2PropertyContainer
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this SampleLibrary.


        :param properties: The properties of this SampleLibrary.  # noqa: E501
        :type: V2PropertyContainer
        """

        self._properties = properties

    @property
    def owner_user(self):
        """Gets the owner_user of this SampleLibrary.  # noqa: E501


        :return: The owner_user of this SampleLibrary.  # noqa: E501
        :rtype: V1pre3UserCompact
        """
        return self._owner_user

    @owner_user.setter
    def owner_user(self, owner_user):
        """Sets the owner_user of this SampleLibrary.


        :param owner_user: The owner_user of this SampleLibrary.  # noqa: E501
        :type: V1pre3UserCompact
        """

        self._owner_user = owner_user

    @property
    def id(self):
        """Gets the id of this SampleLibrary.  # noqa: E501


        :return: The id of this SampleLibrary.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SampleLibrary.


        :param id: The id of this SampleLibrary.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def href(self):
        """Gets the href of this SampleLibrary.  # noqa: E501


        :return: The href of this SampleLibrary.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this SampleLibrary.


        :param href: The href of this SampleLibrary.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def biological_sample(self):
        """Gets the biological_sample of this SampleLibrary.  # noqa: E501


        :return: The biological_sample of this SampleLibrary.  # noqa: E501
        :rtype: V1pre3BiologicalSampleCompact
        """
        return self._biological_sample

    @biological_sample.setter
    def biological_sample(self, biological_sample):
        """Sets the biological_sample of this SampleLibrary.


        :param biological_sample: The biological_sample of this SampleLibrary.  # noqa: E501
        :type: V1pre3BiologicalSampleCompact
        """

        self._biological_sample = biological_sample

    @property
    def container_position(self):
        """Gets the container_position of this SampleLibrary.  # noqa: E501


        :return: The container_position of this SampleLibrary.  # noqa: E501
        :rtype: str
        """
        return self._container_position

    @container_position.setter
    def container_position(self, container_position):
        """Sets the container_position of this SampleLibrary.


        :param container_position: The container_position of this SampleLibrary.  # noqa: E501
        :type: str
        """

        self._container_position = container_position

    @property
    def index1(self):
        """Gets the index1 of this SampleLibrary.  # noqa: E501


        :return: The index1 of this SampleLibrary.  # noqa: E501
        :rtype: LibraryIndexCompact
        """
        return self._index1

    @index1.setter
    def index1(self, index1):
        """Sets the index1 of this SampleLibrary.


        :param index1: The index1 of this SampleLibrary.  # noqa: E501
        :type: LibraryIndexCompact
        """

        self._index1 = index1

    @property
    def index2(self):
        """Gets the index2 of this SampleLibrary.  # noqa: E501


        :return: The index2 of this SampleLibrary.  # noqa: E501
        :rtype: LibraryIndexCompact
        """
        return self._index2

    @index2.setter
    def index2(self, index2):
        """Sets the index2 of this SampleLibrary.


        :param index2: The index2 of this SampleLibrary.  # noqa: E501
        :type: LibraryIndexCompact
        """

        self._index2 = index2

    @property
    def date_modified(self):
        """Gets the date_modified of this SampleLibrary.  # noqa: E501


        :return: The date_modified of this SampleLibrary.  # noqa: E501
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this SampleLibrary.


        :param date_modified: The date_modified of this SampleLibrary.  # noqa: E501
        :type: datetime
        """

        self._date_modified = date_modified

    @property
    def library_prep(self):
        """Gets the library_prep of this SampleLibrary.  # noqa: E501


        :return: The library_prep of this SampleLibrary.  # noqa: E501
        :rtype: LibraryPrepKitCompact
        """
        return self._library_prep

    @library_prep.setter
    def library_prep(self, library_prep):
        """Sets the library_prep of this SampleLibrary.


        :param library_prep: The library_prep of this SampleLibrary.  # noqa: E501
        :type: LibraryPrepKitCompact
        """

        self._library_prep = library_prep

    @property
    def project(self):
        """Gets the project of this SampleLibrary.  # noqa: E501


        :return: The project of this SampleLibrary.  # noqa: E501
        :rtype: V1pre3ProjectCompact
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this SampleLibrary.


        :param project: The project of this SampleLibrary.  # noqa: E501
        :type: V1pre3ProjectCompact
        """

        self._project = project

    @property
    def container(self):
        """Gets the container of this SampleLibrary.  # noqa: E501


        :return: The container of this SampleLibrary.  # noqa: E501
        :rtype: LibraryContainerCompact
        """
        return self._container

    @container.setter
    def container(self, container):
        """Sets the container of this SampleLibrary.


        :param container: The container of this SampleLibrary.  # noqa: E501
        :type: LibraryContainerCompact
        """

        self._container = container

    @property
    def container_end_position(self):
        """Gets the container_end_position of this SampleLibrary.  # noqa: E501


        :return: The container_end_position of this SampleLibrary.  # noqa: E501
        :rtype: str
        """
        return self._container_end_position

    @container_end_position.setter
    def container_end_position(self, container_end_position):
        """Sets the container_end_position of this SampleLibrary.


        :param container_end_position: The container_end_position of this SampleLibrary.  # noqa: E501
        :type: str
        """

        self._container_end_position = container_end_position

    @property
    def library_name(self):
        """Gets the library_name of this SampleLibrary.  # noqa: E501


        :return: The library_name of this SampleLibrary.  # noqa: E501
        :rtype: str
        """
        return self._library_name

    @library_name.setter
    def library_name(self, library_name):
        """Sets the library_name of this SampleLibrary.


        :param library_name: The library_name of this SampleLibrary.  # noqa: E501
        :type: str
        """

        self._library_name = library_name

    @property
    def insert_size(self):
        """Gets the insert_size of this SampleLibrary.  # noqa: E501


        :return: The insert_size of this SampleLibrary.  # noqa: E501
        :rtype: str
        """
        return self._insert_size

    @insert_size.setter
    def insert_size(self, insert_size):
        """Sets the insert_size of this SampleLibrary.


        :param insert_size: The insert_size of this SampleLibrary.  # noqa: E501
        :type: str
        """

        self._insert_size = insert_size

    @property
    def state(self):
        """Gets the state of this SampleLibrary.  # noqa: E501


        :return: The state of this SampleLibrary.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this SampleLibrary.


        :param state: The state of this SampleLibrary.  # noqa: E501
        :type: str
        """

        self._state = state

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
        if issubclass(SampleLibrary, dict):
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
        if not isinstance(other, SampleLibrary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
