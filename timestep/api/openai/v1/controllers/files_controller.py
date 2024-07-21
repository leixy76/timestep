import time
import uuid
from openai.types.file_object import FileObject
from starlette.datastructures import UploadFile

from timestep.database import InstanceStoreSingleton


# async def create_file(file, purpose):  # noqa: E501
async def create_file(body, file: UploadFile):
    """Upload a file that can be used across various endpoints. Individual files can be up to 512 MB, and the size of all files uploaded by one organization can be up to 100 GB.  The Assistants API supports files up to 2 million tokens and of specific file types. See the [Assistants Tools guide](/docs/assistants/tools) for details.  The Fine-tuning API only supports &#x60;.jsonl&#x60; files. The input also has certain required formats for fine-tuning [chat](/docs/api-reference/fine-tuning/chat-input) or [completions](/docs/api-reference/fine-tuning/completions-input) models.  The Batch API only supports &#x60;.jsonl&#x60; files up to 100 MB in size. The input also has a specific required [format](/docs/api-reference/batch/request-input).  Please [contact us](https://help.openai.com/) if you need to increase these storage limits. 

     # noqa: E501

    :param file: The File object (not file name) to be uploaded. 
    :type file: str
    :param purpose: The intended purpose of the uploaded file.  Use \\\&quot;assistants\\\&quot; for [Assistants](/docs/api-reference/assistants) and [Message](/docs/api-reference/messages) files, \\\&quot;vision\\\&quot; for Assistants image file inputs, \\\&quot;batch\\\&quot; for [Batch API](/docs/guides/batch), and \\\&quot;fine-tune\\\&quot; for [Fine-tuning](/docs/api-reference/fine-tuning). 
    :type purpose: str

    :rtype: Union[OpenAIFile, Tuple[OpenAIFile, int], Tuple[OpenAIFile, int, Dict[str, str]]
    """

    purpose = body.get('purpose')

    if purpose == "fine-tune":
        file_object = FileObject(
            id=str(uuid.uuid4()),
            bytes=file.size,
            created_at=int(time.time()),
            filename=file.filename,
            object="file",
            purpose="fine-tune",
            status="uploaded",
        )

        instance_store = InstanceStoreSingleton()
        instance_store._shared_instance_state["file_objects"][file_object.id] = file_object

        return file_object.model_dump(mode="json")

    else:
        raise NotImplementedError


async def delete_file(file_id):  # noqa: E501
    """Delete a file.

     # noqa: E501

    :param file_id: The ID of the file to use for this request.
    :type file_id: str

    :rtype: Union[DeleteFileResponse, Tuple[DeleteFileResponse, int], Tuple[DeleteFileResponse, int, Dict[str, str]]
    """
    raise NotImplementedError


async def download_file(file_id):  # noqa: E501
    """Returns the contents of the specified file.

     # noqa: E501

    :param file_id: The ID of the file to use for this request.
    :type file_id: str

    :rtype: Union[str, Tuple[str, int], Tuple[str, int, Dict[str, str]]
    """
    raise NotImplementedError


async def list_files(purpose=None):  # noqa: E501
    """Returns a list of files that belong to the user&#39;s organization.

     # noqa: E501

    :param purpose: Only return files with the given purpose.
    :type purpose: str

    :rtype: Union[ListFilesResponse, Tuple[ListFilesResponse, int], Tuple[ListFilesResponse, int, Dict[str, str]]
    """
    raise NotImplementedError


async def retrieve_file(file_id):  # noqa: E501
    """Returns information about a specific file.

     # noqa: E501

    :param file_id: The ID of the file to use for this request.
    :type file_id: str

    :rtype: Union[OpenAIFile, Tuple[OpenAIFile, int], Tuple[OpenAIFile, int, Dict[str, str]]
    """
    raise NotImplementedError