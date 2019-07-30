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

    ip = get('https://api.ipify.org').text
    print('My public IP address is: {}'.format(ip))

    if ip == '35.158.30.212' or ip == '35.158.90.50':

        path_to_brands_suite_all = "brands.yml"
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

        # Form input list where each parameter is filename of TestSuite file
        input_list = [path_to_brands_suite_1, path_to_brands_suite_2, path_to_brands_suite_3, path_to_brands_suite_4,
                      path_to_brands_suite_5]
        # input_list = [path_to_brands_suite_5]

        # Init multiprocess

        pool = multiprocessing.Pool(processes=5)

        # Run Test Suites as separate processes
        pool.map(__simple_run, input_list)

        #synchronization

        pool.close()
        pool.join()

        import xlsxwriter
        # Join all results in one excel
        all_excel = Config.file_path_1
        # writer = EX('C:/Program Files (x86)/Jenkins/workspace/Old forex special job/result/final_file.xlsx')



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
                                               'font_color': '#1500cf'})
                worksheet.conditional_format(0, 0, 922, 200, {'type': 'text',
                                                              'criteria': 'beginsWith',
                                                              'value': 'PASS',
                                                              'format': format2})

                worksheet.conditional_format(0, 0, 922, 200, {'type': 'text',
                                                              'criteria': 'beginsWith',
                                                              'value': 'ERROR',
                                                              'format': format1})

                worksheet.conditional_format(0, 0, 922, 200, {'type': 'text',
                                                              'criteria': 'beginsWith',
                                                              'value': 'NOT RUNNED',
                                                              'format': format3})
                worksheet.freeze_panes(1, 1)
                worksheet.set_row(2, None, None, {'level': 1, 'hidden': True})
                for i in range(3, 34):
                    worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})

                worksheet.set_row(35, None, None, {'level': 1, 'hidden': True})
                for i in range(36, 53):
                    worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})

                worksheet.set_row(54, None, None, {'level': 1, 'hidden': True})
                for i in range(55, 80):
                    worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})

                worksheet.set_row(81, None, None, {'level': 1, 'hidden': True})
                for i in range(82, 111):
                    worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})

                worksheet.set_row(112, None, None, {'level': 1, 'hidden': True})
                for i in range(113, 144):
                    worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})

                worksheet.set_row(145, None, None, {'level': 1, 'hidden': True})
                for i in range(146, 186):
                    worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})

                worksheet.set_row(187, None, None, {'level': 1, 'hidden': True})
                for i in range(188, 239):
                    worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})

                worksheet.set_row(240, None, None, {'level': 1, 'hidden': True})
                for i in range(241, 338):
                    worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})

                worksheet.set_row(339, None, None, {'level': 1, 'hidden': True})
                for i in range(340, 389):
                    worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})

                worksheet.set_row(390, None, None, {'level': 1, 'hidden': True})
                for i in range(391, 408):
                    worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})

                worksheet.set_row(409, None, None, {'level': 1, 'hidden': True})
                for i in range(410, 439):
                    worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})

                worksheet.set_row(440, None, None, {'level': 1, 'hidden': True})
                for i in range(441, 451):
                    worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})

                worksheet.set_row(452, None, None, {'level': 1, 'hidden': True})
                for i in range(453, 472):
                    worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})

                worksheet.set_row(473, None, None, {'level': 1, 'hidden': True})
                for i in range(474, 492):
                    worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})

                worksheet.set_row(493, None, None, {'level': 1, 'hidden': True})
                for i in range(494, 511):
                    worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})

                worksheet.set_row(512, None, None, {'level': 1, 'hidden': True})
                for i in range(513, 530):
                    worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})

                worksheet.set_row(531, None, None, {'level': 1, 'hidden': True})
                for i in range(532, 551):
                    worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})

                worksheet.set_row(552, None, None, {'level': 1, 'hidden': True})
                for i in range(553, 570):
                    worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})

                worksheet.set_row(571, None, None, {'level': 1, 'hidden': True})
                for i in range(572, 601):
                    worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})

                worksheet.set_row(602, None, None, {'level': 1, 'hidden': True})
                for i in range(603, 638):
                    worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})

                worksheet.set_row(639, None, None, {'level': 1, 'hidden': True})
                for i in range(640, 659):
                    worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})

                worksheet.set_row(660, None, None, {'level': 1, 'hidden': True})
                for i in range(661, 697):
                    worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})

                worksheet.set_row(698, None, None, {'level': 1, 'hidden': True})
                for i in range(699, 725):
                    worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})

                worksheet.set_row(726, None, None, {'level': 1, 'hidden': True})
                for i in range(727, 750):
                    worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})

                worksheet.set_row(751, None, None, {'level': 1, 'hidden': True})
                for i in range(752, 772):
                    worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})

                worksheet.set_row(773, None, None, {'level': 1, 'hidden': True})
                for i in range(774, 782):
                    worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})

                worksheet.set_row(783, None, None, {'level': 1, 'hidden': True})
                for i in range(784, 798):
                    worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})

                worksheet.set_row(799, None, None, {'level': 1, 'hidden': True})
                for i in range(800, 807):
                    worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})

                worksheet.set_row(808, None, None, {'level': 1, 'hidden': True})
                for i in range(809, 820):
                    worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})

                worksheet.set_row(821, None, None, {'level': 1, 'hidden': True})
                for i in range(822, 835):
                    worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})

                worksheet.set_row(836, None, None, {'level': 1, 'hidden': True})
                for i in range(837, 851):
                    worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})

                worksheet.set_row(852, None, None, {'level': 1, 'hidden': True})
                for i in range(853, 869):
                    worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})

                worksheet.set_row(870, None, None, {'level': 1, 'hidden': True})
                for i in range(871, 884):
                    worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})

                worksheet.set_row(885, None, None, {'level': 1, 'hidden': True})
                for i in range(886, 896):
                    worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})

                worksheet.set_row(897, None, None, {'level': 1, 'hidden': True})
                for i in range(898, 922):
                    worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})

                writer.save()

        short_excel = Config.short_excel_path
        # writer = EX('C:/Program Files (x86)/Jenkins/workspace/Old forex special job/result/final_file.xlsx')

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

                format3 = workbook.add_format({'bg_color': '#a1f1f0',
                                               'font_color': '#1500cf'})

                worksheet.conditional_format(0, 0, 841, 200, {'type': 'text',
                                                              'criteria': 'beginsWith',
                                                              'value': 'PASS',
                                                              'format': format2})

                worksheet.conditional_format(0, 0, 841, 200, {'type': 'text',
                                                              'criteria': 'beginsWith',
                                                              'value': 'ERROR',
                                                              'format': format1})

                worksheet.conditional_format(0, 0, 841, 200, {'type': 'text',
                                                              'criteria': 'beginsWith',
                                                              'value': 'NOT RUNNED',
                                                              'format': format3})

                writer.save()

        # Send_ALL_XLS(all_excel)
        Send_ALL_XLS(short_excel)

        # os.system('start allure generate D:/automation-newforexqa/result -o D:/automation-newforexqa/result/allure-result')

    else:
        print("TURN ON VPN")