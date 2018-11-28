import xlsxwriter
from time import gmtime, strftime


class ExcelWriter:

    def write_test_results(self, brands, tests, results):
        # Create a workbook and add a worksheet.
        workbook = xlsxwriter.Workbook("result/test_results_" + strftime("%Y%m%d_%H%M%S", gmtime()) + ".xlsx")
        worksheet = workbook.add_worksheet()

        # create styles for the PASS/FAIL results
        cell_format_pass = workbook.add_format({'align': 'center', 'bg_color': '#C4D79B'})
        cell_format_fail = workbook.add_format({'align': 'center', 'bg_color': 'red', 'text_wrap': True})

        # set column widths
        worksheet.write(0, 0, "Brand \ Test")
        worksheet.set_column(0, 0, 60)
        worksheet.set_column(1, len(brands), 20)

        # Write the test names
        row = 1
        for test in tests:
            worksheet.write(row, 0, self.get_test_pretty_name_new(test))
            # row += 1
            # write the test results per brand
            col = 1
            for brand in brands:
                row = 0
                worksheet.write(row, col, brand)
                for test in tests:
                    row += 1
                    test_result = results[brand][self.get_test_pretty_name(test)] \
                        if self.get_test_pretty_name(test) in results[brand] else ""

                    if test_result == 'PASS':
                        worksheet.write(row, col, test_result, cell_format_pass)
                    else:
                        # worksheet.write(row, col, test_result, cell_format_fail)
                        # row = 1
                        s = "\n"
                        if s in test_result:
                            new_row_data = test_result.split("\n")
                            for data in new_row_data:
                                worksheet.write(row, col, data, cell_format_fail)
                                row += 1
                    row += row

                col += 1

            row += row

        workbook.close()

    @staticmethod
    def get_test_pretty_name(test):
        return test['class'] + '.' + test['method']

    @staticmethod
    def get_test_pretty_name_new(test):
        return test['class'] + ': ' + test['method'].replace('_', ' ')
