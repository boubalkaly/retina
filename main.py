# import json

# from unstructured_client import UnstructuredClient
# from unstructured_client.models import operations, shared

# # Update here with your api key and server url
# client = UnstructuredClient(
#     api_key_auth="h5jxV6GjPydFZng0TtuaIsgIYUcJUm",
#     server_url="https://api.unstructuredapp.io/general/v0/general",
# )

# # Update here with your filename
# filename = "./retina/media/uploads/_Cover_Letter_-_Boubacar_Ballo_-_One_Green.pdf"

# with open(filename, "rb") as f:
#     files = shared.Files(
#         content=f.read(),
#         file_name=filename,
#     )

# # You can choose FAST, HI_RES or OCR_ONLY for strategy, learn more in the docs at step 4
# req = operations.PartitionRequest(
#     shared.PartitionParameters(files=files, strategy=shared.Strategy.AUTO)
# )

# try:
#     resp = client.general.partition(req)
#     print(json.dumps(resp.elements, indent=2))
# except Exception as e:
#     print(e)
##########################################################################################################################
# from unstructured.partition.auto import partition

# elements = partition(
#     filename="./retina/media/uploads/_Cover_Letter_-_Boubacar_Ballo_-_One_Green.pdf")
# print("\n\n".join([str(el) for el in elements]))
##########################################################################################################################
# import unstructured_client
# from unstructured_client.models import operations, shared

# client = unstructured_client.UnstructuredClient(
#     api_key_auth="2cqgFSJEj0BvrzcPT9eeMpH8e790a0",
#     server_url="https://api.unstructuredapp.io/general/v0/general",
# )

# filename = "./retina/media/uploads/_Cover_Letter_-_Boubacar_Ballo_-_One_Green.pdf"
# with open(filename, "rb") as f:
#     data = f.read()

# req = operations.PartitionRequest(
#     partition_parameters=shared.PartitionParameters(
#         files=shared.Files(
#             content=data,
#             file_name=filename,
#         ),
#         # --- Other partition parameters ---
#         # Note: Defining `strategy`, `chunking_strategy`, and `output_format`
#         # parameters as strings is accepted, but will not pass strict type checking. It is
#         # advised to use the defined enum classes as shown below.
#         strategy=shared.Strategy.AUTO,
#         languages=['eng'],
#     ),
# )

# try:
#     res = client.general.partition(request=req)
#     print(res.elements[0])
# except Exception as e:
#     print(e)
