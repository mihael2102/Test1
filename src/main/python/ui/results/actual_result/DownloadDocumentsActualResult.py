class DownloadDocumentsActualResult(object):
    def __init__(self) -> None:
        super().__init__()

    def print_actual_result(self, status_document_ca):
        print(
            '\n' + "Actual result: " + "Download  was performed successfully " + ", the document status is   "
            + status_document_ca + " status in CA" + '\n')
