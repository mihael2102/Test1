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
        # result_writer.write_test_results_all_report(brand_pretty_names, test_list, overall_results)

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
            # content_fail_err = content_fail_err.replace(' ', '')
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

    from requests import get

    ip = get('https://api.ipify.org').text
    print('My public IP address is: {}'.format(ip))

    if ip == '35.158.30.212' or ip == '35.158.90.50':


        all_brands_yml = "brands.yml"
        path_to_brands_suite_1 = "brands1.yml"
        path_to_brands_suite_2 = "brands2.yml"
        path_to_brands_suite_3 = "brands3.yml"
        path_to_brands_suite_4 = "brands4.yml"
        path_to_brands_suite_5 = "brands5.yml"
        path_to_brands_suite_6 = "brands6.yml"
        path_to_brands_suite_7 = "brands7.yml"
        path_to_brands_suite_8 = "brands8.yml"
        path_to_brands_suite_9 = "brands9.yml"
        path_to_brands_suite_10 = "brands10.yml"
        path_to_brands_suite_11 = "brands11.yml"
        path_to_brands_suite_12 = "brands12.yml"
        path_to_brands_suite_13 = "brands13.yml"

        # Form input list where each parameter is filename of TestSuite file


        # input_list = [path_to_brands_suite_1, path_to_brands_suite_2, path_to_brands_suite_3, path_to_brands_suite_4,
        #               path_to_brands_suite_5, path_to_brands_suite_6, path_to_brands_suite_7, path_to_brands_suite_8,
        #               path_to_brands_suite_9, path_to_brands_suite_10, path_to_brands_suite_11, path_to_brands_suite_12,
        #               path_to_brands_suite_13]
        # input_list = [path_to_brands_suite_1, path_to_brands_suite_2, path_to_brands_suite_3, path_to_brands_suite_4,
        #                        path_to_brands_suite_5, path_to_brands_suite_6]
        input_list = [path_to_brands_suite_1]
        # Init multiprocess
        pool = multiprocessing.Pool(processes=1)

        # Run Test Suites as separate processes
        pool.map(__simple_run, input_list)


        pool.close()
        pool.join()

        import xlsxwriter

        # Join all results in one excel
        all_excel = Config.file_path_1
        # writer = EX('C:/Program Files (x86)/Jenkins/workspace/Old forex job 1/result/final_file.xlsx')

        all_file_frames = []
        for filename in glob.glob(Config.file_path_2):
            if "test_results" in filename:
                tab = pd.read_excel(filename)
                all_file_frames.append(tab)
                all_frame = pd.concat(all_file_frames, axis=1)
                writer = EX(Config.file_path_1)
                all_frame.to_excel(writer, sheet_name='Sheet1')
                workbook = writer.book
                worksheet = writer.sheets['Sheet1']
                format1 = workbook.add_format({'bg_color': '#FFC7CE',
                                               'font_color': '#9C0006'})

                format2 = workbook.add_format({'bg_color': '#C4D79B',
                                               'font_color': '#000000'})

                format3 = workbook.add_format({'bg_color': '#a1f1f0',
                                               'font_color': '#000000'})
                worksheet.conditional_format(0, 0, 841, 200, {'type': 'text',
                                                             'criteria': 'beginsWith',
                                                             'value': 'PASS',
                                                             'format': format2})

                worksheet.conditional_format(0, 0, 841, 200, {'type': 'text',
                                                             'criteria': 'beginsWith',
                                                             'value': 'ERROR',
                                                             'format': format1})
                worksheet.conditional_format(0, 0, 896, 200, {'type': 'text',
                                                              'criteria': 'beginsWith',
                                                              'value': 'NOT RUNNED',
                                                              'format': format3})
                worksheet.freeze_panes(1, 1)
                worksheet.set_row(2, None, None, {'level': 1, 'hidden': True})
                for i in range(3, 25):
                    worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})

                worksheet.set_row(26, None, None, {'level': 1, 'hidden': True})
                for i in range(27, 73):
                    worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})

                worksheet.set_row(74, None, None, {'level': 1, 'hidden': True})
                for i in range(75, 101):
                    worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})

                worksheet.set_row(102, None, None, {'level': 1, 'hidden': True})
                for i in range(103, 130):
                    worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})

                worksheet.set_row(131, None, None, {'level': 1, 'hidden': True})
                for i in range(132, 173):
                    worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})

                worksheet.set_row(174, None, None, {'level': 1, 'hidden': True})
                for i in range(175, 218):
                    worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})

                worksheet.set_row(219, None, None, {'level': 1, 'hidden': True})
                for i in range(220, 247):
                    worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})

                worksheet.set_row(248, None, None, {'level': 1, 'hidden': True})
                for i in range(249, 277):
                    worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})

                writer.save()

            # Join all results in one excel
        short_excel = Config.short_excel_path
        # writer = EX('C:/Program Files (x86)/Jenkins/workspace/Old forex job 1/result/final_file.xlsx')

        short_file_frames = []
        for filename in glob.glob(Config.file_path_2):
            if "short_results" in filename:
                tab = pd.read_excel(filename)
                short_file_frames.append(tab)
                short_frame = pd.concat(short_file_frames, axis=1)
                writer = EX(Config.short_excel_path)
                short_frame.to_excel(writer, sheet_name='Sheet1')
                workbook = writer.book
                worksheet = writer.sheets['Sheet1']
                worksheet.freeze_panes(1, 1)
                format1 = workbook.add_format({'bg_color': '#FFC7CE',
                                               'font_color': '#9C0006'})

                format2 = workbook.add_format({'bg_color': '#C4D79B',
                                               'font_color': '#000000'})
                worksheet.conditional_format(0, 0, 841, 200, {'type': 'text',
                                                              'criteria': 'beginsWith',
                                                              'value': 'PASS',
                                                              'format': format2})

                worksheet.conditional_format(0, 0, 841, 200, {'type': 'text',
                                                              'criteria': 'beginsWith',
                                                              'value': 'ERROR',
                                                              'format': format1})


                writer.save()

        # Send_ALL_XLS(all_excel)
        Send_ALL_XLS(short_excel)



    else:
        print("TURN ON VPN")