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

class V1pre3Application(object):
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
        'long_description': 'str',
        'user_owned_by': 'IUserCompact',
        'href_settings': 'str',
        'href_agreements': 'str',
        'files': 'list[V1pre3FileCompact]',
        'agreements': 'list[ApiAgreementCompact]',
        'href_store_version': 'str',
        'href_user_version': 'str',
        'client_id': 'str',
        'properties': 'IPropertyContainer',
        'release_notes': 'str',
        'whats_new': 'str',
        'bypass_form': 'bool',
        'is_free': 'bool',
        'compute_cost_per_minute': 'float',
        'dataset_types_output': 'list[V2DatasetTypeCompact]',
        'dataset_types_input': 'list[V2DatasetTypeCompact]',
        'id': 'str',
        'href': 'str',
        'name': 'str',
        'company_name': 'str',
        'version_number': 'str',
        'href_logo': 'str',
        'homepage_uri': 'str',
        'short_description': 'str',
        'date_created': 'datetime',
        'date_published': 'datetime',
        'publish_status': 'str',
        'is_billing_activated': 'bool',
        'category': 'str',
        'classifications': 'list[str]',
        'app_family_slug': 'str',
        'app_version_slug': 'str',
        'features': 'list[str]',
        'lock_status': 'str',
        'workflow_source_application': 'V1pre3ApplicationCompact'
    }

    attribute_map = {
        'long_description': 'LongDescription',
        'user_owned_by': 'UserOwnedBy',
        'href_settings': 'HrefSettings',
        'href_agreements': 'HrefAgreements',
        'files': 'Files',
        'agreements': 'Agreements',
        'href_store_version': 'HrefStoreVersion',
        'href_user_version': 'HrefUserVersion',
        'client_id': 'ClientId',
        'properties': 'Properties',
        'release_notes': 'ReleaseNotes',
        'whats_new': 'WhatsNew',
        'bypass_form': 'BypassForm',
        'is_free': 'IsFree',
        'compute_cost_per_minute': 'ComputeCostPerMinute',
        'dataset_types_output': 'DatasetTypesOutput',
        'dataset_types_input': 'DatasetTypesInput',
        'id': 'Id',
        'href': 'Href',
        'name': 'Name',
        'company_name': 'CompanyName',
        'version_number': 'VersionNumber',
        'href_logo': 'HrefLogo',
        'homepage_uri': 'HomepageUri',
        'short_description': 'ShortDescription',
        'date_created': 'DateCreated',
        'date_published': 'DatePublished',
        'publish_status': 'PublishStatus',
        'is_billing_activated': 'IsBillingActivated',
        'category': 'Category',
        'classifications': 'Classifications',
        'app_family_slug': 'AppFamilySlug',
        'app_version_slug': 'AppVersionSlug',
        'features': 'Features',
        'lock_status': 'LockStatus',
        'workflow_source_application': 'WorkflowSourceApplication'
    }

    def __init__(self, long_description=None, user_owned_by=None, href_settings=None, href_agreements=None, files=None, agreements=None, href_store_version=None, href_user_version=None, client_id=None, properties=None, release_notes=None, whats_new=None, bypass_form=None, is_free=None, compute_cost_per_minute=None, dataset_types_output=None, dataset_types_input=None, id=None, href=None, name=None, company_name=None, version_number=None, href_logo=None, homepage_uri=None, short_description=None, date_created=None, date_published=None, publish_status=None, is_billing_activated=None, category=None, classifications=None, app_family_slug=None, app_version_slug=None, features=None, lock_status=None, workflow_source_application=None):  # noqa: E501
        """V1pre3Application - a model defined in Swagger"""  # noqa: E501
        self._long_description = None
        self._user_owned_by = None
        self._href_settings = None
        self._href_agreements = None
        self._files = None
        self._agreements = None
        self._href_store_version = None
        self._href_user_version = None
        self._client_id = None
        self._properties = None
        self._release_notes = None
        self._whats_new = None
        self._bypass_form = None
        self._is_free = None
        self._compute_cost_per_minute = None
        self._dataset_types_output = None
        self._dataset_types_input = None
        self._id = None
        self._href = None
        self._name = None
        self._company_name = None
        self._version_number = None
        self._href_logo = None
        self._homepage_uri = None
        self._short_description = None
        self._date_created = None
        self._date_published = None
        self._publish_status = None
        self._is_billing_activated = None
        self._category = None
        self._classifications = None
        self._app_family_slug = None
        self._app_version_slug = None
        self._features = None
        self._lock_status = None
        self._workflow_source_application = None
        self.discriminator = None
        if long_description is not None:
            self.long_description = long_description
        if user_owned_by is not None:
            self.user_owned_by = user_owned_by
        if href_settings is not None:
            self.href_settings = href_settings
        if href_agreements is not None:
            self.href_agreements = href_agreements
        if files is not None:
            self.files = files
        if agreements is not None:
            self.agreements = agreements
        if href_store_version is not None:
            self.href_store_version = href_store_version
        if href_user_version is not None:
            self.href_user_version = href_user_version
        if client_id is not None:
            self.client_id = client_id
        if properties is not None:
            self.properties = properties
        if release_notes is not None:
            self.release_notes = release_notes
        if whats_new is not None:
            self.whats_new = whats_new
        if bypass_form is not None:
            self.bypass_form = bypass_form
        if is_free is not None:
            self.is_free = is_free
        if compute_cost_per_minute is not None:
            self.compute_cost_per_minute = compute_cost_per_minute
        if dataset_types_output is not None:
            self.dataset_types_output = dataset_types_output
        if dataset_types_input is not None:
            self.dataset_types_input = dataset_types_input
        self.id = id
        self.href = href
        if name is not None:
            self.name = name
        if company_name is not None:
            self.company_name = company_name
        if version_number is not None:
            self.version_number = version_number
        if href_logo is not None:
            self.href_logo = href_logo
        if homepage_uri is not None:
            self.homepage_uri = homepage_uri
        if short_description is not None:
            self.short_description = short_description
        if date_created is not None:
            self.date_created = date_created
        if date_published is not None:
            self.date_published = date_published
        if publish_status is not None:
            self.publish_status = publish_status
        if is_billing_activated is not None:
            self.is_billing_activated = is_billing_activated
        if category is not None:
            self.category = category
        if classifications is not None:
            self.classifications = classifications
        if app_family_slug is not None:
            self.app_family_slug = app_family_slug
        if app_version_slug is not None:
            self.app_version_slug = app_version_slug
        if features is not None:
            self.features = features
        if lock_status is not None:
            self.lock_status = lock_status
        if workflow_source_application is not None:
            self.workflow_source_application = workflow_source_application

    @property
    def long_description(self):
        """Gets the long_description of this V1pre3Application.  # noqa: E501


        :return: The long_description of this V1pre3Application.  # noqa: E501
        :rtype: str
        """
        return self._long_description

    @long_description.setter
    def long_description(self, long_description):
        """Sets the long_description of this V1pre3Application.


        :param long_description: The long_description of this V1pre3Application.  # noqa: E501
        :type: str
        """

        self._long_description = long_description

    @property
    def user_owned_by(self):
        """Gets the user_owned_by of this V1pre3Application.  # noqa: E501


        :return: The user_owned_by of this V1pre3Application.  # noqa: E501
        :rtype: IUserCompact
        """
        return self._user_owned_by

    @user_owned_by.setter
    def user_owned_by(self, user_owned_by):
        """Sets the user_owned_by of this V1pre3Application.


        :param user_owned_by: The user_owned_by of this V1pre3Application.  # noqa: E501
        :type: IUserCompact
        """

        self._user_owned_by = user_owned_by

    @property
    def href_settings(self):
        """Gets the href_settings of this V1pre3Application.  # noqa: E501


        :return: The href_settings of this V1pre3Application.  # noqa: E501
        :rtype: str
        """
        return self._href_settings

    @href_settings.setter
    def href_settings(self, href_settings):
        """Sets the href_settings of this V1pre3Application.


        :param href_settings: The href_settings of this V1pre3Application.  # noqa: E501
        :type: str
        """

        self._href_settings = href_settings

    @property
    def href_agreements(self):
        """Gets the href_agreements of this V1pre3Application.  # noqa: E501


        :return: The href_agreements of this V1pre3Application.  # noqa: E501
        :rtype: str
        """
        return self._href_agreements

    @href_agreements.setter
    def href_agreements(self, href_agreements):
        """Sets the href_agreements of this V1pre3Application.


        :param href_agreements: The href_agreements of this V1pre3Application.  # noqa: E501
        :type: str
        """

        self._href_agreements = href_agreements

    @property
    def files(self):
        """Gets the files of this V1pre3Application.  # noqa: E501


        :return: The files of this V1pre3Application.  # noqa: E501
        :rtype: list[V1pre3FileCompact]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this V1pre3Application.


        :param files: The files of this V1pre3Application.  # noqa: E501
        :type: list[V1pre3FileCompact]
        """

        self._files = files

    @property
    def agreements(self):
        """Gets the agreements of this V1pre3Application.  # noqa: E501


        :return: The agreements of this V1pre3Application.  # noqa: E501
        :rtype: list[ApiAgreementCompact]
        """
        return self._agreements

    @agreements.setter
    def agreements(self, agreements):
        """Sets the agreements of this V1pre3Application.


        :param agreements: The agreements of this V1pre3Application.  # noqa: E501
        :type: list[ApiAgreementCompact]
        """

        self._agreements = agreements

    @property
    def href_store_version(self):
        """Gets the href_store_version of this V1pre3Application.  # noqa: E501


        :return: The href_store_version of this V1pre3Application.  # noqa: E501
        :rtype: str
        """
        return self._href_store_version

    @href_store_version.setter
    def href_store_version(self, href_store_version):
        """Sets the href_store_version of this V1pre3Application.


        :param href_store_version: The href_store_version of this V1pre3Application.  # noqa: E501
        :type: str
        """

        self._href_store_version = href_store_version

    @property
    def href_user_version(self):
        """Gets the href_user_version of this V1pre3Application.  # noqa: E501


        :return: The href_user_version of this V1pre3Application.  # noqa: E501
        :rtype: str
        """
        return self._href_user_version

    @href_user_version.setter
    def href_user_version(self, href_user_version):
        """Sets the href_user_version of this V1pre3Application.


        :param href_user_version: The href_user_version of this V1pre3Application.  # noqa: E501
        :type: str
        """

        self._href_user_version = href_user_version

    @property
    def client_id(self):
        """Gets the client_id of this V1pre3Application.  # noqa: E501


        :return: The client_id of this V1pre3Application.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this V1pre3Application.


        :param client_id: The client_id of this V1pre3Application.  # noqa: E501
        :type: str
        """

        self._client_id = client_id

    @property
    def properties(self):
        """Gets the properties of this V1pre3Application.  # noqa: E501


        :return: The properties of this V1pre3Application.  # noqa: E501
        :rtype: IPropertyContainer
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this V1pre3Application.


        :param properties: The properties of this V1pre3Application.  # noqa: E501
        :type: IPropertyContainer
        """

        self._properties = properties

    @property
    def release_notes(self):
        """Gets the release_notes of this V1pre3Application.  # noqa: E501


        :return: The release_notes of this V1pre3Application.  # noqa: E501
        :rtype: str
        """
        return self._release_notes

    @release_notes.setter
    def release_notes(self, release_notes):
        """Sets the release_notes of this V1pre3Application.


        :param release_notes: The release_notes of this V1pre3Application.  # noqa: E501
        :type: str
        """

        self._release_notes = release_notes

    @property
    def whats_new(self):
        """Gets the whats_new of this V1pre3Application.  # noqa: E501


        :return: The whats_new of this V1pre3Application.  # noqa: E501
        :rtype: str
        """
        return self._whats_new

    @whats_new.setter
    def whats_new(self, whats_new):
        """Sets the whats_new of this V1pre3Application.


        :param whats_new: The whats_new of this V1pre3Application.  # noqa: E501
        :type: str
        """

        self._whats_new = whats_new

    @property
    def bypass_form(self):
        """Gets the bypass_form of this V1pre3Application.  # noqa: E501


        :return: The bypass_form of this V1pre3Application.  # noqa: E501
        :rtype: bool
        """
        return self._bypass_form

    @bypass_form.setter
    def bypass_form(self, bypass_form):
        """Sets the bypass_form of this V1pre3Application.


        :param bypass_form: The bypass_form of this V1pre3Application.  # noqa: E501
        :type: bool
        """

        self._bypass_form = bypass_form

    @property
    def is_free(self):
        """Gets the is_free of this V1pre3Application.  # noqa: E501


        :return: The is_free of this V1pre3Application.  # noqa: E501
        :rtype: bool
        """
        return self._is_free

    @is_free.setter
    def is_free(self, is_free):
        """Sets the is_free of this V1pre3Application.


        :param is_free: The is_free of this V1pre3Application.  # noqa: E501
        :type: bool
        """

        self._is_free = is_free

    @property
    def compute_cost_per_minute(self):
        """Gets the compute_cost_per_minute of this V1pre3Application.  # noqa: E501


        :return: The compute_cost_per_minute of this V1pre3Application.  # noqa: E501
        :rtype: float
        """
        return self._compute_cost_per_minute

    @compute_cost_per_minute.setter
    def compute_cost_per_minute(self, compute_cost_per_minute):
        """Sets the compute_cost_per_minute of this V1pre3Application.


        :param compute_cost_per_minute: The compute_cost_per_minute of this V1pre3Application.  # noqa: E501
        :type: float
        """

        self._compute_cost_per_minute = compute_cost_per_minute

    @property
    def dataset_types_output(self):
        """Gets the dataset_types_output of this V1pre3Application.  # noqa: E501


        :return: The dataset_types_output of this V1pre3Application.  # noqa: E501
        :rtype: list[V2DatasetTypeCompact]
        """
        return self._dataset_types_output

    @dataset_types_output.setter
    def dataset_types_output(self, dataset_types_output):
        """Sets the dataset_types_output of this V1pre3Application.


        :param dataset_types_output: The dataset_types_output of this V1pre3Application.  # noqa: E501
        :type: list[V2DatasetTypeCompact]
        """

        self._dataset_types_output = dataset_types_output

    @property
    def dataset_types_input(self):
        """Gets the dataset_types_input of this V1pre3Application.  # noqa: E501


        :return: The dataset_types_input of this V1pre3Application.  # noqa: E501
        :rtype: list[V2DatasetTypeCompact]
        """
        return self._dataset_types_input

    @dataset_types_input.setter
    def dataset_types_input(self, dataset_types_input):
        """Sets the dataset_types_input of this V1pre3Application.


        :param dataset_types_input: The dataset_types_input of this V1pre3Application.  # noqa: E501
        :type: list[V2DatasetTypeCompact]
        """

        self._dataset_types_input = dataset_types_input

    @property
    def id(self):
        """Gets the id of this V1pre3Application.  # noqa: E501


        :return: The id of this V1pre3Application.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this V1pre3Application.


        :param id: The id of this V1pre3Application.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def href(self):
        """Gets the href of this V1pre3Application.  # noqa: E501


        :return: The href of this V1pre3Application.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this V1pre3Application.


        :param href: The href of this V1pre3Application.  # noqa: E501
        :type: str
        """
        if href is None:
            raise ValueError("Invalid value for `href`, must not be `None`")  # noqa: E501

        self._href = href

    @property
    def name(self):
        """Gets the name of this V1pre3Application.  # noqa: E501


        :return: The name of this V1pre3Application.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1pre3Application.


        :param name: The name of this V1pre3Application.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def company_name(self):
        """Gets the company_name of this V1pre3Application.  # noqa: E501


        :return: The company_name of this V1pre3Application.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this V1pre3Application.


        :param company_name: The company_name of this V1pre3Application.  # noqa: E501
        :type: str
        """

        self._company_name = company_name

    @property
    def version_number(self):
        """Gets the version_number of this V1pre3Application.  # noqa: E501


        :return: The version_number of this V1pre3Application.  # noqa: E501
        :rtype: str
        """
        return self._version_number

    @version_number.setter
    def version_number(self, version_number):
        """Sets the version_number of this V1pre3Application.


        :param version_number: The version_number of this V1pre3Application.  # noqa: E501
        :type: str
        """

        self._version_number = version_number

    @property
    def href_logo(self):
        """Gets the href_logo of this V1pre3Application.  # noqa: E501


        :return: The href_logo of this V1pre3Application.  # noqa: E501
        :rtype: str
        """
        return self._href_logo

    @href_logo.setter
    def href_logo(self, href_logo):
        """Sets the href_logo of this V1pre3Application.


        :param href_logo: The href_logo of this V1pre3Application.  # noqa: E501
        :type: str
        """

        self._href_logo = href_logo

    @property
    def homepage_uri(self):
        """Gets the homepage_uri of this V1pre3Application.  # noqa: E501


        :return: The homepage_uri of this V1pre3Application.  # noqa: E501
        :rtype: str
        """
        return self._homepage_uri

    @homepage_uri.setter
    def homepage_uri(self, homepage_uri):
        """Sets the homepage_uri of this V1pre3Application.


        :param homepage_uri: The homepage_uri of this V1pre3Application.  # noqa: E501
        :type: str
        """

        self._homepage_uri = homepage_uri

    @property
    def short_description(self):
        """Gets the short_description of this V1pre3Application.  # noqa: E501


        :return: The short_description of this V1pre3Application.  # noqa: E501
        :rtype: str
        """
        return self._short_description

    @short_description.setter
    def short_description(self, short_description):
        """Sets the short_description of this V1pre3Application.


        :param short_description: The short_description of this V1pre3Application.  # noqa: E501
        :type: str
        """

        self._short_description = short_description

    @property
    def date_created(self):
        """Gets the date_created of this V1pre3Application.  # noqa: E501


        :return: The date_created of this V1pre3Application.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this V1pre3Application.


        :param date_created: The date_created of this V1pre3Application.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def date_published(self):
        """Gets the date_published of this V1pre3Application.  # noqa: E501


        :return: The date_published of this V1pre3Application.  # noqa: E501
        :rtype: datetime
        """
        return self._date_published

    @date_published.setter
    def date_published(self, date_published):
        """Sets the date_published of this V1pre3Application.


        :param date_published: The date_published of this V1pre3Application.  # noqa: E501
        :type: datetime
        """

        self._date_published = date_published

    @property
    def publish_status(self):
        """Gets the publish_status of this V1pre3Application.  # noqa: E501


        :return: The publish_status of this V1pre3Application.  # noqa: E501
        :rtype: str
        """
        return self._publish_status

    @publish_status.setter
    def publish_status(self, publish_status):
        """Sets the publish_status of this V1pre3Application.


        :param publish_status: The publish_status of this V1pre3Application.  # noqa: E501
        :type: str
        """

        self._publish_status = publish_status

    @property
    def is_billing_activated(self):
        """Gets the is_billing_activated of this V1pre3Application.  # noqa: E501


        :return: The is_billing_activated of this V1pre3Application.  # noqa: E501
        :rtype: bool
        """
        return self._is_billing_activated

    @is_billing_activated.setter
    def is_billing_activated(self, is_billing_activated):
        """Sets the is_billing_activated of this V1pre3Application.


        :param is_billing_activated: The is_billing_activated of this V1pre3Application.  # noqa: E501
        :type: bool
        """

        self._is_billing_activated = is_billing_activated

    @property
    def category(self):
        """Gets the category of this V1pre3Application.  # noqa: E501


        :return: The category of this V1pre3Application.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this V1pre3Application.


        :param category: The category of this V1pre3Application.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def classifications(self):
        """Gets the classifications of this V1pre3Application.  # noqa: E501


        :return: The classifications of this V1pre3Application.  # noqa: E501
        :rtype: list[str]
        """
        return self._classifications

    @classifications.setter
    def classifications(self, classifications):
        """Sets the classifications of this V1pre3Application.


        :param classifications: The classifications of this V1pre3Application.  # noqa: E501
        :type: list[str]
        """

        self._classifications = classifications

    @property
    def app_family_slug(self):
        """Gets the app_family_slug of this V1pre3Application.  # noqa: E501


        :return: The app_family_slug of this V1pre3Application.  # noqa: E501
        :rtype: str
        """
        return self._app_family_slug

    @app_family_slug.setter
    def app_family_slug(self, app_family_slug):
        """Sets the app_family_slug of this V1pre3Application.


        :param app_family_slug: The app_family_slug of this V1pre3Application.  # noqa: E501
        :type: str
        """

        self._app_family_slug = app_family_slug

    @property
    def app_version_slug(self):
        """Gets the app_version_slug of this V1pre3Application.  # noqa: E501


        :return: The app_version_slug of this V1pre3Application.  # noqa: E501
        :rtype: str
        """
        return self._app_version_slug

    @app_version_slug.setter
    def app_version_slug(self, app_version_slug):
        """Sets the app_version_slug of this V1pre3Application.


        :param app_version_slug: The app_version_slug of this V1pre3Application.  # noqa: E501
        :type: str
        """

        self._app_version_slug = app_version_slug

    @property
    def features(self):
        """Gets the features of this V1pre3Application.  # noqa: E501


        :return: The features of this V1pre3Application.  # noqa: E501
        :rtype: list[str]
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this V1pre3Application.


        :param features: The features of this V1pre3Application.  # noqa: E501
        :type: list[str]
        """

        self._features = features

    @property
    def lock_status(self):
        """Gets the lock_status of this V1pre3Application.  # noqa: E501


        :return: The lock_status of this V1pre3Application.  # noqa: E501
        :rtype: str
        """
        return self._lock_status

    @lock_status.setter
    def lock_status(self, lock_status):
        """Sets the lock_status of this V1pre3Application.


        :param lock_status: The lock_status of this V1pre3Application.  # noqa: E501
        :type: str
        """

        self._lock_status = lock_status

    @property
    def workflow_source_application(self):
        """Gets the workflow_source_application of this V1pre3Application.  # noqa: E501


        :return: The workflow_source_application of this V1pre3Application.  # noqa: E501
        :rtype: V1pre3ApplicationCompact
        """
        return self._workflow_source_application

    @workflow_source_application.setter
    def workflow_source_application(self, workflow_source_application):
        """Sets the workflow_source_application of this V1pre3Application.


        :param workflow_source_application: The workflow_source_application of this V1pre3Application.  # noqa: E501
        :type: V1pre3ApplicationCompact
        """

        self._workflow_source_application = workflow_source_application

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
        if issubclass(V1pre3Application, dict):
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
        if not isinstance(other, V1pre3Application):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
