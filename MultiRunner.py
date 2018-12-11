from src.test.python.ui.automation.BaseTest import *
from src.main.python.utils.logs.ExcelWriter import ExcelWriter
import importlib
import xmlrunner
import multiprocessing
import os
from pandas import ExcelWriter as EX
import glob
import pandas as pd
from src.test.python.ui.automation.utils.postconditions.SendMail import Send_ALL_XLS
from requests import get

class MultiRunner:

    def __init__(self, path_to_test_suite):
        self.data_provider = ConfigProvider(path_to_test_suite)
        # whether to stop after first failing test
        self.fail_fast = True

    def test_brands(self):
        brands = self.data_provider.get_brands()

        test_list = self.data_provider.get_tests()
        print("Starting tests. Test configuration includes %d brands" % len(brands))

        overall_results = {}
        brand_pretty_names = []
        for brand in brands:
            # Load relevant XPaths for current brand in dict
            import src.main.python.utils.data.globalXpathProvider.GlobalXpathProvider as global_var
            global_var.current_brand_name = brand
            # self.data_provider.set_xpath_for_tests()

            self.data_provider.load_brands(brand)
            brand_pretty_name = self.data_provider.get_data_client('pretty_name')
            brand_pretty_names.append(brand_pretty_name)
            print("Testing %s\n" % brand_pretty_name)
            brand_results = self.single_brand_test(brand, test_list)
            overall_results[brand_pretty_name] = brand_results
            print("Finished testing %s\n" % brand_pretty_name)

        # write the results to an Excel file
        result_writer = ExcelWriter()
        result_writer.write_test_results(brand_pretty_names, test_list, overall_results)




    def single_brand_test(self, brand, test_list):
        runner = xmlrunner.XMLTestRunner(output='result')
        results = {}

        for test_data in test_list:
            test_module = importlib.import_module(test_data['module'])
            test_class = getattr(test_module, test_data['class'])
            test = test_class()
            test._testMethodName = test_data['method']

            test.driver_type = 'Chrome'
            if 'reload_config' in test_data and test_data['reload_config']:
                self.data_provider.reload_configuration()
            test.config = self.data_provider
            runner.outsuffix = test_data['method'] + "-" + brand
            print("Running test %s on %s" % (test_data['method'], brand))
            result, content = runner.run(test)
            # content = runner.run()
            test_name = test_data['class'] + '.' + test_data['method']
            content_fail_err = content.decode("utf-8")
            temp = content_fail_err.find('Open first tabs page')
            index = temp
            content_fail_err = content_fail_err[index:]
            content_fail_err = content_fail_err[1:]

            content_fail_err = content_fail_err.replace(']]>	</system-err','')
            content_fail_err = content_fail_err.replace('</testsuite>', '')
            content_fail_err = content_fail_err.replace('>', '')
            content_fail_err = content_fail_err.replace(' ', '')
            #test_passed = False
            if not result or result.errors:
                results[test_name] = "ERROR" + content_fail_err
            elif result.failures:
                results[test_name] = "FAIL" + content_fail_err
            elif not result.testsRun:
                results[test_name] = "SKIP"
            else:
                results[test_name] = "PASS"
                #test_passed = True
            #if self.fail_fast and not test_passed:
                #break

        return results


def __simple_run(path_to_test_suite):
    client = MultiRunner(path_to_test_suite)
    client.test_brands()


if __name__ == "__main__":

    ip = get('https://api.ipify.org').text
    print('My public IP address is: {}'.format(ip))

    if ip == '35.158.30.212' or ip == '35.158.90.50':

        path_to_brands_suite_1 = "brands.yml"
        path_to_brands_suite_2 = "brands1.yml"
        path_to_brands_suite_3 = "brands2.yml"
        path_to_brands_suite_4 = "brands3.yml"
        path_to_brands_suite_5 = "brands4.yml"

        # Form input list where each parameter is filename of TestSuite file
        input_list = [path_to_brands_suite_1, path_to_brands_suite_2, path_to_brands_suite_3, path_to_brands_suite_4, path_to_brands_suite_5]
        # input_list = [path_to_brands_suite_1]
        # Init multiprocess
        pool = multiprocessing.Pool(processes=5)

        # Run Test Suites as separate processes
        pool.map(__simple_run, input_list)

        #synchronization

        pool.close()
        pool.join()

        # Join all results in one excel
        all_excel = "C:/Program Files (x86)/Jenkins/workspace/Old forex job 1/result/OF.xlsx"
        writer = EX('C:/Program Files (x86)/Jenkins/workspace/Old forex job 1/result/OF.xlsx')
        # writer = EX('D:/automation-newforexqa/result/NF.xlsx')

        for filename in glob.glob('C:/Program Files (x86)/Jenkins/workspace/Old forex job 1/result/*.xlsx'):
            excel_file = pd.ExcelFile(filename)
            (_, f_name) = os.path.split(filename)
            (f_short_name, _) = os.path.splitext(f_name)
            for sheet_name in excel_file.sheet_names:
                df_excel = pd.read_excel(filename, sheet_name=sheet_name)
                df_excel.to_excel(writer, f_short_name, index=False)
                workbook = writer.book
                worksheet = writer.sheets[f_short_name]
                format1 = workbook.add_format({'bg_color': '#FFC7CE',
                                               'font_color': '#9C0006'})

                format2 = workbook.add_format({'bg_color': '#C4D79B',
                                               'font_color': '#000000'})
                worksheet.conditional_format(0, 0, 841, 10, {'type': 'text',
                                                             'criteria': 'beginsWith',
                                                             'value': 'PASS',
                                                             'format': format2})

                worksheet.conditional_format(0, 0, 841, 10, {'type': 'text',
                                                             'criteria': 'beginsWith',
                                                             'value': 'ERROR',
                                                             'format': format1})

        writer.save()
        Send_ALL_XLS(all_excel)

        # os.system('start allure generate D:/automation-newforexqa/result -o D:/automation-newforexqa/result/allure-result')

    else:
        print("TURN ON VPN")