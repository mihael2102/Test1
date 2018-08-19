from src.test.python.ui.automation.BaseTest import *
from src.main.python.utils.logs.ExcelWriter import ExcelWriter
import importlib
import xmlrunner


class MultiRunner(unittest.TestCase):

    def test_brands(self):
        self.data_provider = ConfigProvider()
        brands = self.data_provider.get_brands()

        test_list = self.data_provider.get_tests()
        print("Starting tests. Test configuration includes %d brands" % len(brands))

        overall_results = {}
        brand_pretty_names = []
        for brand in brands:
            self.data_provider.load_brand_config(brand)
            brand_pretty_name = self.data_provider.get_data_client('pretty_name')
            brand_pretty_names.append(brand_pretty_name)
            print("Testing %s\n" % brand_pretty_name)
            brand_results = self.single_brand_test(brand, test_list, self.data_provider)
            overall_results[brand_pretty_name] = brand_results
            print("Finished testing %s\n" % brand_pretty_name)

        # write the results to an Excel file
        result_writer = ExcelWriter()
        result_writer.write_test_results(brand_pretty_names, test_list, overall_results)

    def single_brand_test(self, brand, test_list, data_provider):
        runner = xmlrunner.XMLTestRunner(output='result')
        results = {}

        # suite = unittest.TestSuite()

        for test_data in test_list:
            test_module = importlib.import_module(test_data['module'])
            test_class = getattr(test_module, test_data['class'])
            test = test_class()
            test._testMethodName = test_data['method']

            test.driver_type = 'Chrome'
            data_provider.reload_configuration()
            test.config = data_provider
            # suite.addTest(test)
            # result = runner.run(suite)
            runner.outsuffix = test_data['method'] + "-" + brand
            result = runner.run(test)

            test_name = test_data['class'] + '.' + test_data['method']
            if not result or result.errors:
                results[test_name] = "ERROR"
            elif result.failures:
                results[test_name] = "FAIL"
            elif not result.testsRun:
                results[test_name] = "SKIP"
            else:
                results[test_name] = "PASS"
        return results

        # results = runner.run(suite)
        # return results


if __name__ == "__main__":
    client = MultiRunner()
    client.test_brands()
