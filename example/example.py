import os

from lapa_file_store_helper import LAPAFileStoreHelper

lapa_file_store_helper = LAPAFileStoreHelper()

input_file_path = os.path.dirname(os.path.abspath(__file__)) + os.sep + "test.txt"
output_folder_path = os.path.dirname(os.path.abspath(__file__)) + os.sep + "output"

# Example: Upload File using file path
upload_file_using_path_output = lapa_file_store_helper.upload_file_using_file_path(
    file_path=input_file_path,
    file_purpose=None,
    system_relative_path="others/misc",
)
print(upload_file_using_path_output)

# Example: Upload File using binary io
with open(input_file_path, "rb") as file:
    upload_file_using_io_output = lapa_file_store_helper.upload_file_using_binary_io(
        file=file,
        file_purpose=None,
        system_relative_path="others/misc",
    )
print(upload_file_using_io_output)

# Example: Download file
download_file_output = lapa_file_store_helper.download_file(
    file_storage_token=upload_file_using_io_output["additional_info"][
        "FileStorageToken"
    ],
    output_folder_path=output_folder_path,
)
print(download_file_output)
