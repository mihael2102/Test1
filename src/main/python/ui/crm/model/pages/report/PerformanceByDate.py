from src.main.python.ui.crm.model.pages.crm_base_page.CRMBasePage import CRMBasePage


class PerformanceByDate(CRMBasePage):
    def __init__(self):
        super().__init__()

    def perform_export_to_excel(self):
        export_to_excel_button = super().wait_element_to_be_clickable("//button[@id='excelExport']")
        export_to_excel_button.click()
        return PerformanceByDate()
