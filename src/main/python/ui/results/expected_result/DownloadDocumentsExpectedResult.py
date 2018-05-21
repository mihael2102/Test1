class DownloadDocumentsExpectedResult(object):

    def __init__(self) -> None:
        super().__init__()

    def print_expected_result(self, status_document_crm):
        print(
            '\n' + "Expected result: " + "The status of documents is  "
            + status_document_crm + " status in CRM" + '\n')
