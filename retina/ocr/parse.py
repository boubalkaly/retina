from unstructured.partition.api import partition_via_api


def parse_pdf(filename):  # parse the pdf given the path of it

    elements = partition_via_api(
        filename=filename,
        api_key="2cqgFSJEj0BvrzcPT9eeMpH8e790a0",
        api_url="https://api.unstructuredapp.io/general/v0/general",
        # you may need to specify your unique API URL
        # api_url="YOUR_API_URL",
        content_type="message/rfc822"
    )

    # return elements
    # print(type(elements))
    # print(elements)
    corpus = "\n\n".join([str(el) for el in elements])  # return corpus
    return corpus
