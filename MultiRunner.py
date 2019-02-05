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
        input_list = [path_to_brands_suite_1]
        # Init multiprocess
        pool = multiprocessing.Pool(processes=1)

        # Run Test Suites as separate processes
        pool.map(__simple_run, input_list)


        pool.close()
        pool.join()

        import xlsxwriter

        # Join all results in one excel
        all_excel = "C:/Program Files (x86)/Jenkins/workspace/New forex job 1/result/final_file.xlsx"
        # writer = EX('C:/Program Files (x86)/Jenkins/workspace/Old forex job 1/result/final_file.xlsx')

        all_file_frames = []
        for filename in glob.glob('C:/Program Files (x86)/Jenkins/workspace/New Forex Stage/result/*.xlsx'):
            tab = pd.read_excel(filename)
            all_file_frames.append(tab)
            all_frame = pd.concat(all_file_frames, axis=1)
            writer = EX('C:/Program Files (x86)/Jenkins/workspace/New Forex Stage/result/final_file.xlsx')
            all_frame.to_excel(writer, sheet_name='Sheet1')
            workbook = writer.book
            worksheet = writer.sheets['Sheet1']
            format1 = workbook.add_format({'bg_color': '#FFC7CE',
                                           'font_color': '#9C0006'})

            format2 = workbook.add_format({'bg_color': '#C4D79B',
                                           'font_color': '#000000'})
            worksheet.conditional_format(0, 0, 934, 200, {'type': 'text',
                                                          'criteria': 'beginsWith',
                                                          'value': 'PASS',
                                                          'format': format2})

            worksheet.conditional_format(0, 0, 934, 200, {'type': 'text',
                                                          'criteria': 'beginsWith',
                                                          'value': 'ERROR',
                                                          'format': format1})
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
            for i in range(532, 549):
                worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})

            worksheet.set_row(550, None, None, {'level': 1, 'hidden': True})
            for i in range(551, 568):
                worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})

            worksheet.set_row(569, None, None, {'level': 1, 'hidden': True})
            for i in range(570, 589):
                worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})

            worksheet.set_row(590, None, None, {'level': 1, 'hidden': True})
            for i in range(591, 608):
                worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})

            worksheet.set_row(609, None, None, {'level': 1, 'hidden': True})
            for i in range(610, 639):
                worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})

            worksheet.set_row(640, None, None, {'level': 1, 'hidden': True})
            for i in range(641, 676):
                worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})

            worksheet.set_row(677, None, None, {'level': 1, 'hidden': True})
            for i in range(678, 697):
                worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})

            worksheet.set_row(698, None, None, {'level': 1, 'hidden': True})
            for i in range(699, 735):
                worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})

            worksheet.set_row(736, None, None, {'level': 1, 'hidden': True})
            for i in range(737, 763):
                worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})

            worksheet.set_row(764, None, None, {'level': 1, 'hidden': True})
            for i in range(765, 788):
                worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})

            worksheet.set_row(789, None, None, {'level': 1, 'hidden': True})
            for i in range(790, 810):
                worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})

            worksheet.set_row(811, None, None, {'level': 1, 'hidden': True})
            for i in range(812, 820):
                worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})

            worksheet.set_row(821, None, None, {'level': 1, 'hidden': True})
            for i in range(822, 836):
                worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})

            worksheet.set_row(837, None, None, {'level': 1, 'hidden': True})
            for i in range(838, 845):
                worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})

            worksheet.set_row(846, None, None, {'level': 1, 'hidden': True})
            for i in range(847, 858):
                worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})

            worksheet.set_row(859, None, None, {'level': 1, 'hidden': True})
            for i in range(860, 873):
                worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})

            worksheet.set_row(874, None, None, {'level': 1, 'hidden': True})
            for i in range(875, 889):
                worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})

            worksheet.set_row(890, None, None, {'level': 1, 'hidden': True})
            for i in range(891, 907):
                worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})

            worksheet.set_row(908, None, None, {'level': 1, 'hidden': True})
            for i in range(909, 922):
                worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})

            worksheet.set_row(923, None, None, {'level': 1, 'hidden': True})
            for i in range(924, 934):
                worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})

            writer.save()

        Send_ALL_XLS(all_excel)



    else:
        print("TURN ON VPN")
