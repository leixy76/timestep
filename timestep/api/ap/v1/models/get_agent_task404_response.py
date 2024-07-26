from datetime import date, datetime  # noqa: F401
from typing import Dict, List  # noqa: F401

from timestep.api.ap.v1 import util
from timestep.api.ap.v1.models.base_model import Model


class GetAgentTask404Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, message=None):  # noqa: E501
        """GetAgentTask404Response - a model defined in OpenAPI

        :param message: The message of this GetAgentTask404Response.  # noqa: E501
        :type message: str
        """
        self.openapi_types = {
            'message': str
        }

        self.attribute_map = {
            'message': 'message'
        }

        self._message = message

    @classmethod
    def from_dict(cls, dikt) -> 'GetAgentTask404Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The getAgentTask_404_response of this GetAgentTask404Response.  # noqa: E501
        :rtype: GetAgentTask404Response
        """
        return util.deserialize_model(dikt, cls)

    @property
    def message(self) -> str:
        """Gets the message of this GetAgentTask404Response.

        Message stating the entity was not found  # noqa: E501

        :return: The message of this GetAgentTask404Response.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this GetAgentTask404Response.

        Message stating the entity was not found  # noqa: E501

        :param message: The message of this GetAgentTask404Response.
        :type message: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message