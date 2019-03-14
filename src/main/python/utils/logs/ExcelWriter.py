import xlsxwriter
from time import gmtime, strftime
from src.test.python.ui.automation.utils.postconditions.SendMail import Send_Email_XLS

class ExcelWriter:

    def write_test_results(self, brands, tests, results):
        # Create a workbook and add a worksheet.
        # os.mkdir("C:/Program Files (x86)/Jenkins/workspace/API New Forex/result/short_result")
        filepath = "result/short_results_" + strftime("%Y%m%d_%H%M%S", gmtime()) + ".xlsx"
        workbook = xlsxwriter.Workbook(filepath)
        worksheet = workbook.add_worksheet()

        # create styles for the PASS/FAIL results
        cell_format_pass = workbook.add_format({'align': 'center', 'bg_color': '#C4D79B'})
        cell_format_fail = workbook.add_format({'align': 'center', 'bg_color': 'red'})

        # set column widths
        worksheet.write(0, 0, "Brand \ Test")
        worksheet.set_column(0, 0, 60)
        worksheet.set_column(1, len(brands), 20)
        worksheet.freeze_panes(1, 1)
        # Write the test names
        row = 1
        for test in tests:
            worksheet.write(row, 0, self.get_test_pretty_name_new(test))
            row += 1

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
                    test_result_error = "ERROR"
                    worksheet.write(row, col, test_result_error, cell_format_fail)
                    worksheet.write_comment(row, col, test_result,
                                            {'width': 250, 'height': 400})
            col += 1

        workbook.close()
        Send_Email_XLS(filepath)

    def write_test_results_all_report(self, brands, tests, results):
        # Create a workbook and add a worksheet.
        filepath = "result/test_results_" + strftime("%Y%m%d_%H%M%S", gmtime()) + ".xlsx"
        workbook = xlsxwriter.Workbook(filepath)
        worksheet = workbook.add_worksheet()

        # create styles for the PASS/FAIL results
        cell_format_pass = workbook.add_format({'align': 'center', 'bg_color': '#C4D79B'})
        cell_format_fail = workbook.add_format({'align': 'center', 'bg_color': 'red', 'text_wrap': True})
        cell_format_steps_to_fail = workbook.add_format({'align': 'center', 'bg_color': '#F1F2A2', 'text_wrap': True})

        # set column widths
        worksheet.set_default_row(20)
        worksheet.write(0, 0, "Brand \ Test")
        worksheet.set_column(0, 0, 60)
        worksheet.set_column(1, len(brands), 20)


        # Write the test names
        row = 1
        for test in tests:
            worksheet.write(row, 0, self.get_test_pretty_name_new(test))
            step_suit = ExcelWriter().steps_for_test(test)
            for step in step_suit:
                worksheet.write(row, 1, step)
                row += 1
            # row += row

        # write the test results per brand
        col = 2
        for brand in brands:
            row = 0
            worksheet.write(row, col, brand)
            for test in tests:
                row += 1
                test_result = results[brand][self.get_test_pretty_name(test)] \
                    if self.get_test_pretty_name(test) in results[brand] else ""

                step_suit = ExcelWriter().steps_for_test(test)
                count_steps = len(step_suit)

                if test_result == 'PASS':
                    c = 1
                    while c < count_steps:
                        worksheet.write(row, col, test_result, cell_format_pass)
                        c += 1
                        row += 1
                    if c == count_steps:
                        worksheet.write(row, col, test_result, cell_format_pass)

                else:
                    s = "\n"
                    if s in test_result:
                        new_row_data = test_result.split("\n")


                        while '' in new_row_data:
                            new_row_data.remove('')

                        for data in new_row_data:
                            worksheet.write(row, col, data, cell_format_steps_to_fail)
                            row += 1

                        len_new_row_data = len(new_row_data)
                        if count_steps == len_new_row_data:
                            row -= 1
                        if count_steps > len_new_row_data:
                            different = count_steps - len_new_row_data
                            c = 1
                            while c < different:
                                worksheet.write(row, col, "ERROR", cell_format_fail)
                                c += 1
                                row += 1
                            if c == different:
                                worksheet.write(row, col, "ERROR", cell_format_fail)

                        # if count_steps < len_new_row_data:
                        #     c = 1
                        #     while c < count_steps:
                        #         worksheet.write(row, col, "ERROR", cell_format_fail)
                        #         c += 1
                        #         row += 1
                        #     if c == count_steps:
                        #         worksheet.write(row, col, "ERROR", cell_format_fail)





            col += 1


        # worksheet.set_row(2, None, None, {'level': 1, 'hidden': True})
        # for i in range(3,33):
        #     worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})
        #
        # worksheet.set_row(34, None, None, {'level': 1, 'hidden': True})
        # for i in range(35,51):
        #     worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})
        #
        # worksheet.set_row(52, None, None, {'level': 1, 'hidden': True})
        # for i in range(53, 77):
        #     worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})
        #
        # worksheet.set_row(78, None, None, {'level': 1, 'hidden': True})
        # for i in range(79, 107):
        #     worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})
        #
        # worksheet.set_row(108, None, None, {'level': 1, 'hidden': True})
        # for i in range(109, 139):
        #     worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})
        #
        # worksheet.set_row(140, None, None, {'level': 1, 'hidden': True})
        # for i in range(141, 181):
        #     worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})
        #
        # worksheet.set_row(182, None, None, {'level': 1, 'hidden': True})
        # for i in range(183, 234):
        #     worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})
        #
        # worksheet.set_row(235, None, None, {'level': 1, 'hidden': True})
        # for i in range(236, 333):
        #     worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})
        #
        # worksheet.set_row(334, None, None, {'level': 1, 'hidden': True})
        # for i in range(335, 384):
        #     worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})
        #
        # worksheet.set_row(385, None, None, {'level': 1, 'hidden': True})
        # for i in range(386, 403):
        #     worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})
        #
        # worksheet.set_row(404, None, None, {'level': 1, 'hidden': True})
        # for i in range(405, 434):
        #     worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})
        #
        # worksheet.set_row(435, None, None, {'level': 1, 'hidden': True})
        # for i in range(436, 446):
        #     worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})
        #
        # worksheet.set_row(447, None, None, {'level': 1, 'hidden': True})
        # for i in range(448, 467):
        #     worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})
        #
        # worksheet.set_row(468, None, None, {'level': 1, 'hidden': True})
        # for i in range(469, 487):
        #     worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})
        #
        # worksheet.set_row(488, None, None, {'level': 1, 'hidden': True})
        # for i in range(489, 506):
        #     worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})
        #
        # worksheet.set_row(507, None, None, {'level': 1, 'hidden': True})
        # for i in range(508, 525):
        #     worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})
        #
        # worksheet.set_row(526, None, None, {'level': 1, 'hidden': True})
        # for i in range(527, 546):
        #     worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})
        #
        # worksheet.set_row(547, None, None, {'level': 1, 'hidden': True})
        # for i in range(548, 565):
        #     worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})
        #
        # worksheet.set_row(566, None, None, {'level': 1, 'hidden': True})
        # for i in range(567, 596):
        #     worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})
        #
        # worksheet.set_row(597, None, None, {'level': 1, 'hidden': True})
        # for i in range(598, 633):
        #     worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})
        #
        # worksheet.set_row(634, None, None, {'level': 1, 'hidden': True})
        # for i in range(635, 654):
        #     worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})
        #
        # worksheet.set_row(655, None, None, {'level': 1, 'hidden': True})
        # for i in range(656, 692):
        #     worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})
        #
        # worksheet.set_row(693, None, None, {'level': 1, 'hidden': True})
        # for i in range(694, 720):
        #     worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})
        #
        # worksheet.set_row(721, None, None, {'level': 1, 'hidden': True})
        # for i in range(722, 738):
        #     worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})
        #
        # worksheet.set_row(739, None, None, {'level': 1, 'hidden': True})
        # for i in range(740, 760):
        #     worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})
        #
        # worksheet.set_row(761, None, None, {'level': 1, 'hidden': True})
        # for i in range(762, 770):
        #     worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})
        #
        # worksheet.set_row(771, None, None, {'level': 1, 'hidden': True})
        # for i in range(772, 786):
        #     worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})
        #
        # worksheet.set_row(787, None, None, {'level': 1, 'hidden': True})
        # for i in range(788, 795):
        #     worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})
        #
        # worksheet.set_row(796, None, None, {'level': 1, 'hidden': True})
        # for i in range(797, 808):
        #     worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})
        #
        # worksheet.set_row(809, None, None, {'level': 1, 'hidden': True})
        # for i in range(810, 823):
        #     worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})
        #
        # worksheet.set_row(824, None, None, {'level': 1, 'hidden': True})
        # for i in range(825, 839):
        #     worksheet.set_row(i, None, None, {'level': 2, 'hidden': True})

        workbook.close()

        # Send_Email_XLS(filepath)

    @staticmethod
    def get_test_pretty_name(test):
        return test['class'] + '.' + test['method']

    @staticmethod
    def get_test_pretty_name_new(test):
        return test['class'] + ': ' + test['method'].replace('_', ' ')

    def steps_for_test(self, test):


        if self.get_test_pretty_name_new(test) == "WorkflowsModulesTest: test check workflow by status":
            step_suit = ["Open CRM"
                , "Enter Username"
                , "Enter Password"
                , "Click Login"
                , "No OTP"
                , "'What's new' popup isn't displayed"
                ,"The client module was opened"
                ,"Click the  drop down filter "
                ,"The field found is : Test Clients"
                ,"Click the selected filter"
                ,"Setting  the user's email in the email field  is : @pandats.com"
                ,"Click the search button "
                ,"Click user email: @pandats.com"
                ,"Click Edit"
                ,"Returns the country: Albania"
                ,"Returns the address :Test_addressThe client module was opened"
                ,"Click the  drop down filter "
                ,"The field found is : Test Clients"
                ,"Click the selected filter"
                ,"Setting  the user's email in the email field  is : @pandats.com"
                ,"Click the search button "
                ,"Click user email: @pandats.com"
                ,"Click Edit"
                ,"Returns the country: Albania"
                ,"Returns the address :Test_address"]

        if self.get_test_pretty_name_new(test) == "WorkflowsModulesTest: test check workflow by country":
            step_suit = ["Open CRM"
                , "Enter Username"
                , "Enter Password"
                , "Click Login"
                , "No OTP"
                , "'What's new' popup isn't displayed"
                ,"The client module was opened"
                ,"Click the  drop down filter"
                ,"The field found is : Test Clients"
                ,"Click the selected filter"
                ,"Setting  the user's email in the email field  is : @pandats.com"
                ,"Click the search button "
                ,"Click user email: @pandats.com"
                ,"Click Edit"
                ,"Select countryAustria"
                ,"Click Save"
                ,"Enter b-day"
                ,"Returns the country"
                ,"Returns the address"]


        if self.get_test_pretty_name_new(test) == "WorkflowsModulesTest: test delete workflow":
            step_suit = ["Open CRM"
                , "Enter Username"
                , "Enter Password"
                , "Click Login"
                , "No OTP"
                , "'What's new' popup isn't displayed"
                ,"The CRM Configuration module was opened"
                ,"Workflows is loaded"
                ,"Check name workflow in table"
                ,"Click delete workflow"
                ,"Click OK"
                ,"Check name workflow in table"]

        if self.get_test_pretty_name_new(test) == "WorkflowsModulesTest: test create workflows":
            step_suit = ["Open CRM"
                , "Enter Username"
                , "Enter Password"
                , "Click Login"
                , "No OTP"
                , "'What's new' popup isn't displayed"
                ,"The CRM Configuration module was opened"
                ,"Workflows is loaded"
                ,"Click add new workflow"
                ,"Enter workflow name"
                ,"Enter workflow priority"
                ,"Click Every time the record is modified"
                ,"Click Next"
                ,"Select Clients module"
                ,"Click Add Condition"
                ,"Select Clients Status"
                ,"Select conditionis"
                ,"Select Clients StatusB - Test"
                ,"Click Add Condition"
                ,"Select Email"
                ,"Select condition contains"
                ,"Click enter email"
                ,"Emaer email: @pandats.com"
                ,"Click Save"
                ,"Select condition AND"
                ,"Click Next"
                ,"Click Add Task and select: Update Field"
                ,"Enter task title Test_title"
                ,"Click add field"
                ,"Select Address"
                ,"Click enter value"
                ,"Enter value Test_address"
                ,"Click Save"
                ,"Click add field"
                ,"Select Country"
                ,"Select condition Albania"
                ,"Click Save"
                ,"Click Save"
                ,"Check name workflow in table"]

        if self.get_test_pretty_name_new(test) == "CheckModules: test my dashboard loading":
            step_suit = ["Open CRM"
                , "Enter Username"
                , "Enter Password"
                , "Click Login"
                , "No OTP"
                , "'What's new' popup isn't displayed"
                , "The my dashboard module was opened"
                , "Latest Sales Insights is loaded"
                , "Your Tasks section contain records"
                , "Client Segmentation section contain records"]

        if self.get_test_pretty_name_new(test) == "CheckModules: test audit logs loading":
            step_suit = ["Open CRM"
                , "Enter Username"
                , "Enter Password"
                , "Click Login"
                , "No OTP"
                , "'What's new' popup isn't displayed"
                , "The Audit Logs module was opened"
                , "Audit Logs module is loaded"]

        if self.get_test_pretty_name_new(test) == "CRMConfigurationsTest: test crm configurations pages loading":
            step_suit = ["Open CRM"
                , "Enter Username"
                , "Enter Password"
                , "Click Login"
                , "No OTP"
                , "'What's new' popup isn't displayed"
                , "The CRM Configuration module was opened"
                , "Common configuration is loaded"
                , "Brand Configuration module is loaded"
                , "SMS Configuration is loaded"
                , "SMTP Configuration is loaded"
                , "Minimum Deposit is loaded"
                , "Cashier is loaded"
                , "Manage PSP is loaded"
                , "Click2Call Configuration is loaded"
                , "Referral Configuration is loaded"
                , "Workflows is loaded"
                , "Sharing Access is loaded"
                , "EMAIL Maker is loaded"]

        if self.get_test_pretty_name_new(test) == "CheckModules: test check user management":
            step_suit = ["Open CRM"
                , "Enter Username"
                , "Enter Password"
                , "Click Login"
                , "No OTP"
                , "'What's new' popup isn't displayed"
                , "Go to User Management"
                , "Check name tab User Management"
                , "Check table loaded"]

        if self.get_test_pretty_name_new(test) == "CheckModules: test check leaderboard":
            step_suit = ["Open CRM"
                , "Enter Username"
                , "Enter Password"
                , "Click Login"
                , "No OTP"
                , "'What's new' popup isn't displayed"
                , "Dashboard  module was opened"
                , "Click select all"
                , "Enter name group"
                , "Click Go"]

        if self.get_test_pretty_name_new(test) == "CheckModules: test check dashboard":
            step_suit = ["Open CRM"
                , "Enter Username"
                , "Enter Password"
                , "Click Login"
                , "No OTP"
                , "'What's new' popup isn't displayed"
                , "Dashboard  module was opened"
                , "Check balance"
                , "Check credit"
                , "Check open p and l"]

        if self.get_test_pretty_name_new(test) == "TabLeadsModuleCRM: import leads":
            step_suit = ["Open CRM"
                , "Enter Username"
                , "Enter Password"
                , "Click Login"
                , "No OTP"
                , "'What's new' popup isn't displayed"
                , "Leads module was opened"
                , "Click import leads"
                , "Click on button Choose File"
                , "Click NEXT import leads"
                , "Select source leads"
                , "Enter source name"
                , "Select status leads"
                , "Click NEXT import leads"
                , "Click NEXT import leads"
                , "Leads module was opened"
                , "Click the  drop down filter "
                , "The field found is : Test Leads"
                , "Click the selected filter"
                , "Check"]

        if self.get_test_pretty_name_new(test) == "TabLeadsModuleCRM: export select records":
            step_suit = ["Open CRM"
                , "Enter Username"
                , "Enter Password"
                , "Click Login"
                , "No OTP"
                , "'What's new' popup isn't displayed"
                , "Leads module was opened"
                , "Click the  drop down filter"
                , "The field found is : Test Leads"
                , "Click the selected filter"
                , "The email was entered : pandaqa+"
                , "The search button was clicked "
                , "Click check box all leads"
                , "Click 'Export Leads'"
                , "Click 'Export Leads' in pop ups"
                , "Check"]

        if self.get_test_pretty_name_new(test) == "TabLeadsModuleCRM: export full list":
            step_suit = ["Open CRM"
                , "Enter Username"
                , "Enter Password"
                , "Click Login"
                , "No OTP"
                , "'What's new' popup isn't displayed"
                , "Leads module was opened"
                , "Click the  drop down filter"
                , "The field found is : Test Leads"
                , "Click the selected filter"
                , "The email was entered : pandaqa+"
                , "The search button was clicked "
                , "Click check box all leads"
                , "Click 'Export Leads'"
                , "Click 'Export Leads' in pop ups"
                , "Check"]

        if self.get_test_pretty_name_new(test) == "TabLeadsModuleCRM: test mass edit leads":
            step_suit = ["Open CRM"
                , "Enter Username"
                , "Enter Password"
                , "Click Login"
                , "No OTP"
                , "'What's new' popup isn't displayed"
                , "Leads module was opened"
                , "Click the  drop down filter"
                , "The field found is : Test Leads"
                , "Click the selected filter"
                , "The email was entered : pandaqa+"
                , "The search button was clicked"
                , "Click check box all leads"
                , "Click Mass Edit Leads"
                , "Click 'Status' check box and select status"
                , "Click 'source' check box and select source"
                , "Click 'country' check box and select country"
                , "Click 'Save'"
                , "The email was entered : pandaqa+"
                , "The search button was clicked"
                , "Verify status"
                , "Verify country"
                , "Verify source"]

        if self.get_test_pretty_name_new(test) == "TabLeadsModuleCRM: test mass assign leads":
            step_suit = ["Open CRM"
                , "Enter Username"
                , "Enter Password"
                , "Click Login"
                , "No OTP"
                , "'What's new' popup isn't displayed"
                , "Leads module was opened"
                , "Click the  drop down filter "
                , "The field found is : Test Leads"
                , "Click the selected filter"
                , "The email was entered : pandaqa+"
                , "The search button was clicked"
                , "Click check box all leads"
                , "Click mass assign btn"
                , "Enter user name"
                , "Click user"
                , "Click check box Status"
                , "The status was selected: R - New"
                , "Click assign pop ups"
                , "Close succsesfull result pop ups"
                , "Verify status"
                , "Verify assign"]

        if self.get_test_pretty_name_new(test) == "TabLeadsModuleCRM: sorting lead module":
            step_suit = ["Open CRM"
                , "Enter Username"
                , "Enter Password"
                , "Click Login"
                , "No OTP"
                , "'What's new' popup isn't displayed"
                , "Leads module was opened"
                , "Click the  drop down filter"
                , "The field found is : Test Leads"
                , "Click the selected filter"
                , "The email was entered : pandaqa+"
                , "The search button was clicked"
                , "Click sorting by Leads no"
                , "Verify sorting by Leads no"
                , "Click sorting by Email"
                , "Verify sorting by Email"
                , "Click sorting by Exist"
                , "Verify sorting by Exist"]

        # CalendarView

        if self.get_test_pretty_name_new(test) == "CalendarView: test check add tasks calendar view":
            step_suit = ["Open CRM"
                , "Enter Username"
                , "Enter Password"
                , "Click Login"
                , "No OTP"
                , "No What's new"
                , "Go to Task module"
                , "Go to Calendar View"
                , "Click Add Event"
                , "Set 'Status' to 'In Progress'"
                , "Set 'Event Type' to 'Meeting'"
                , "Set 'Date'"
                , "Set 'Time'"
                , "Set 'Duration' to M"
                , "Set 'Priority' to Medium"
                , "Set 'Assign to' to pandaqa pandaqa"
                , "Set 'Account Name'"
                , "Set 'Subject'"
                , "Set 'Comment'"
                , "Click 'Save'"
                , "Task was created' message is shown"
                , "Verify subject is correct"]

        if self.get_test_pretty_name_new(test) == "CalendarView: test check day tab":
            step_suit = ["Open CRM"
                , "Enter Username"
                , "Enter Password"
                , "Click Login"
                , "No OTP"
                , "No What's new"
                , "Go to Task module"
                , "Go to Calendar View"
                , "Go to 'Day' tab"
                , "Verify date is correct"]

        if self.get_test_pretty_name_new(test) == "CalendarView: test check month tab":
            step_suit = ["Open CRM"
                , "Enter Username"
                , "Enter Password"
                , "Click Login"
                , "No OTP"
                , "No What's new"
                , "Go to Task module"
                , "Go to Calendar View"
                , "Go to 'Month' tab"
                , "Verify first column is 'Sun'"
                , "Verify second column is 'Mon'"
                , "Verify third column is 'Tue'"
                , "Verify fourth column is 'Wed'"
                , "Verify fifth column is 'Thu'"
                , "Verify sixth column is 'Fri'"
                , "Verify seventh column is 'Sat'"]

        if self.get_test_pretty_name_new(test) == "CalendarView: test check week tab":
            step_suit = ["Open CRM"
                , "Enter Username"
                , "Enter Password"
                , "Click Login"
                , "No OTP"
                , "No What's new"
                , "Go to Task module popup"
                , "Go to Calendar View"
                , "Go to 'Week' tab"]

            # TabFinancialTransaction

        if self.get_test_pretty_name_new(test) == "TabFinancialTransaction: test check searching by column":
            step_suit = ["Open CRM"
                , "Enter Username"
                , "Enter Password"
                , "Click Login"
                , "No OTP"
                , "'What's new' popup"
                , "Go to Financial Transactions module"
                , "Search by transaction number"
                , "Search by client name"
                , "Search by transaction type"
                , "Search by modified time"
                , "Click 'Search'"
                , "Perform scroll into view of the element"
                , "Verify correct data was found"
                , "Verify transaction number"]

        if self.get_test_pretty_name_new(
                test) == "TabFinancialTransaction: test check all tab from financial transactions":
            step_suit = ["Open CRM"
                , "Enter Username"
                , "Enter Password"
                , "Click Login"
                , "No OTP"
                , "'What's new' popup"
                , "Go to Financial Transactions module"
                , "Verify All tab is loaded"
                , "Verify Credit In tab is loaded"
                , "Verify Credit Out tab is loaded"
                , "Verify Demo Accounts Transactions tab is loaded"
                , "Verify Deposits tab is loaded"
                , "Verify Withdraw tab is loaded"]

        if self.get_test_pretty_name_new(test) == "TabFinancialTransaction: test check search via button":
            step_suit = ["Open CRM"
                , "Enter Username"
                , "Enter Password"
                , "Click Login"
                , "No OTP"
                , "'What's new' popup"
                , "Go to Financial Transactions module"
                , "Open search form"
                , "Search by transaction ID"
                , "Search by client name"
                , "Search by Transaction type"
                , "Search by modified time"
                , "Verify created/modified time"
                , "Verify Time from the page list"
                , "Verify Correct time"
                , "Verify trading account"]

            # FilterModulesTest

        if self.get_test_pretty_name_new(test) == "FilterModulesTest: test create filter clients module":
            step_suit = ["Open CRM"
                , "Enter Username"
                , "Enter Password"
                , "Click Login"
                , "No OTP"
                , "'What's new' popup"
                , "Go to Clients module"
                , "Click 'Create Filter'"
                , "Set 'View Name'"
                , "Set first column to CRM ID"
                , "Set second column to Client Status"
                , "Set Third column to Lead Exist"
                , "Set Fourth column to Email"
                , "Set Fifth column to Client Name"
                , "Set Sixth column to Assigned To"
                , "Set Seventh column to Country"
                , "Set Eighth column to First Name"
                , "Set Ninth column to Last Name"
                , "Set Tenth column to City"
                , "Set Eleventh column to Brand"
                , "Click 'Save'"
                , "Verify First column is CRM ID"
                , "Verify Second column is Client Status"
                , "Verify Third column is Lead Exist"
                , "Verify Fourth column is Email"
                , "Verify Fifth column is Client Name"
                , "Verify Sixth column is Assigned To"
                , "Verify Seventh column is Country"
                , "Verify Eighth column is First Name"
                , "Verify Ninth column is Last Name"
                , "Verify Tenth column is City"
                , "Verify Eleventh column is Brand"
                , "The filter was deleted"]

        if self.get_test_pretty_name_new(test) == "FilterModulesTest: test create filter documents module":
            step_suit = ["Open CRM"
                , "Enter Username"
                , "Enter Password"
                , "Click Login"
                , "No OTP"
                , "'What's new' popup"
                ,"Go to Clients module"
                ,"Click 'Create Filter'"
                ,"Set 'View Name'"
                ,"Set first column to Document No"
                ,"Set second column to Status"
                ,"Set Third column to Comments"
                ,"Set Fourth column to Assigned To"
                ,"Click 'Save'"
                ,"Verify First column is Document No"
                ,"Verify Second column is Status"
                ,"Verify Third column is Comments"
                ,"Verify Fourth column is Assigned To,"
                , "The filter was deleted"]

        if self.get_test_pretty_name_new(test) == "FilterModulesTest: test create filter leads module":
            step_suit = ["Open CRM"
                , "Enter Username"
                , "Enter Password"
                , "Click Login"
                , "No OTP"
                , "'What's new' popup"
                 , "Go to Leads module"
                 , "Click 'Create Filter'"
                 , "Set 'View Name'"
                 , "Set First column to First Name"
                 , "Set Second column to Last Name"
                 , "Set Third column to Email"
                 , "Set Fourth column to Assigned To"
                 , "Set Fifth column to Title"
                 , "Set Sixth column to Lead Source"
                 , "Set Seventh column to Lead Status"
                 , "Set Eighth column to Language"
                 , "Click 'Save'"
                 , "Verify First column is First Name"
                 , "Verify Second column is Last Name"
                 , "Verify Third column is Email"
                 , "Verify Fourth column is Assigned To"
                 , "Verify Fifth column is Title"
                 , "Verify Sixth column is Lead Source"
                 , "Verify Seventh column is Lead Status"
                 , "Verify Eighth column is Language"
                 , "The filter was deleted"]

        if self.get_test_pretty_name_new(test) == "FilterModulesTest: test create filter help desk":
            step_suit = ["Open CRM"
                , "Enter Username"
                , "Enter Password"
                , "Click Login"
                , "No OTP"
                , "'What's new' popup isn't displayed"
                ,"Go to Help Desk module"
                ,"Click 'Create Filter'"
                ,"Set 'View Name'"
                ,"Set first column to Ticket No"
                ,"Set second column to Title"
                ,"Set Third column to Priority"
                ,"Set Fourth column to Assigned To"
                ,"Set Fifth column to Status"
                ,"Set Sixth column to CA Id"
                ,"Set Seventh column to Category"
                ,"Set Eighth column to Brand"
                ,"Set Nineth column to Description"
                ,"Set Tenth column to Related To"
                ,"Click 'Save'"
                ,"Verify first column is Ticket No"
                ,"Verify second column is Title"
                ,"Verify Third column is Priority"
                ,"Verify Fourth column is Assigned To"
                ,"Verify Fifth column is Status"
                ,"Verify Sixth column is CA Id"
                ,"Verify Seventh column is Category"
                ,"Verify Eighth column is Brand"
                ,"Verify Nineth column is Description"
                ,"Verify Tenth column is Related To"
                , "The filter was deleted"]

        if self.get_test_pretty_name_new(test) == "FilterModulesTest: test create filter trading account module":
            step_suit = ["Open CRM"
                , "Enter Username"
                , "Enter Password"
                , "Click Login"
                , "No OTP"
                , "'What's new' popup isn't displayed"
                , "The client module was opened"
                , "The filter pop-up is opened"
                , "Tha name filter was set"
                , "The first column was selected"
                , "The second column was selected"
                , "The third column was selected"
                , "The fourth column was selected"
                , "The fifth column was selected"
                , "The sixth column was selected"
                , "The seventh column was selected"
                , "The eight column was selected"
                , "The ninth column was selected"
                , "The eleventh column was selected"
                , "The eleventh column was selected"
                , "The filter was created:"
                , "First column name"
                , "Second column name"
                , "Third column name"
                , "Fourth column name"
                , "Fifth column name"
                , "Sixth column name"
                , "Seventh column name"
                , "Eighth column name"
                , "Ninth  column name"
                , "Tenth  column name"
                , "Eleventh  column name"
                , "The filter was deleted"]

            # LeadsModuleTest

        if self.get_test_pretty_name_new(test) == "TabLeadsModuleCRM: test searching lead modules":
            step_suit = ["Open CRM"
                , "Enter Username"
                , "Enter Password"
                , "Click Login"
                , "No OTP"
                , "'What's new' popup isn't displayed"
                , "Go to Leads module"
                , "Click Create Lead"
                ,"Set 'First Name' to ***"
                ,"Set 'Last Name' to ***"
                ,"Set 'Mobile'"
                ,"Set 'Fax'"
                ,"Set 'Email' to pandaqa+***@pandats.com"
                ,"Set 'Secondary Email'"
                ,"Set 'Language' to English"
                ,"Set 'Street' to test"
                ,"Set 'Postal Code' to 123"
                ,"Set 'Country' to Germany"
                ,"Set 'Description' to test"
                ,"Set 'Phone Number'"
                ,"Set 'Title' to test"
                ,"Set 'Conference'"
                ,"Set 'Lead Status' to R - New"
                ,"Set 'Assign to' to pandaqa pandaqa"
                ,"Set 'Source name' to test"
                ,"Set 'Brand'"
                ,"Set 'PO Box'"
                ,"Set 'City' to Berlin"
                ,"Set 'State'"
                ,"Scroll Up"
                ,"Click 'Save'"
                ,"Lead was created"
                ,"Page refreshed"
                ,"Go to CRM home page"
                ,"Go to Leads module"
                ,"Click the 'Filters' drop down"
                ,"Search for 'Test Leads'"
                ,"Select 'Test Leads' filter"
                ,"Add *** to First Name"
                ,"Add *** to Last Name"
                ,"Add pandaqa+***@pandats.com to Email"
                ,"Click 'Search'"]

        if self.get_test_pretty_name_new(test) == "LeadModuleTest: test create lead":
            step_suit = ["Open CRM"
                , "Enter Username"
                , "Enter Password"
                , "Click Login"
                , "No OTP"
                , "'What's new' popup isn't displayed"
                ,"Go to Leads module"
                ,"Click Create Lead"
                ,"Set 'First Name' to ***"
                ,"Set 'Last Name' to ***"
                ,"Set 'Mobile'"
                ,"Set 'Fax'"
                ,"Set 'Email' to pandaqa+***@pandats.com"
                ,"Set 'Secondary Email'"
                ,"Set 'Language' to English"
                ,"Set 'Street' to test"
                ,"Set 'Postal Code' to ***"
                ,"Set 'Country' to Germany"
                ,"Set 'Description' to test"
                ,"Set 'Phone Number'"
                ,"Set 'Title' to test"
                ,"Set 'Conference'"
                ,"Set 'Lead Status' to R - New"
                ,"Set 'Assign to' to pandaqa pandaqa"
                ,"Set 'Source name' to test"
                ,"Set 'Brand'"
                ,"Set 'PO Box'"
                ,"Set 'City' to Berlin"
                ,"Set 'State'"
                ,"Scroll Up"
                ,"Click 'Save'"
                ,"Lead was created"
                ,"Go to lead's details view"
                ,"Verify 'First Name' is '***'"
                ,"Verify 'Last Name' is '***'"
                ,"Verify 'Mobile' is '***'"
                ,"Verify 'Fax' is '***'"
                ,"Verify 'Email' is 'pandaqa+***@pandats.com'"
                ,"Verify 'Secondary Email' is 'pandaqa+***@pandats.com'"
                ,"Verify 'Source Name is Test"
                ,"Verify 'Referral' exists"
                ,"Verify 'Street'"
                ,"Verify 'Postal Code' is '***'"
                ,"Verify 'Country' is 'Germany'"
                ,"Verify 'Description' is 'Description test'"
                ,"Verify 'Phone Number' is '***'"
                ,"Verify 'Title' is 'Title test'"
                ,"Verify 'Conference' is 'Conference test'"
                ,"Verify 'Status' is 'R - New'"
                ,"Verfiy 'Languge' is 'English'"
                ,"Veirfy 'PO Box' is '***'"
                ,"Verify 'City' is 'Berlin'"
                ,"Verify 'State' is '***'"]

        if self.get_test_pretty_name_new(test) == "LeadModuleTest: test edit lead":
            step_suit = ["Open CRM"
                , "Enter Username"
                , "Enter Password"
                , "Click Login"
                , "No OTP"
                , "'What's new' popup isn't displayed"
                ,"Go to Leads module"
                ,"Click Create Lead"
                ,"Set 'First Name' to ***"
                ,"Set 'Last Name' to ***"
                ,"Set 'Mobile'"
                ,"Set 'Fax'"
                ,"Set 'Email' to pandaqa+***@pandats.com"
                ,"Set 'Secondary Email'"
                ,"Set 'Language' to English"
                ,"Set 'Street' to test"
                ,"Set 'Postal Code' to ***"
                ,"Set 'Country' to Germany"
                ,"Set 'Description' to test"
                ,"Set 'Phone Number'"
                ,"Set 'Title' to test"
                ,"Set 'Conference'"
                ,"Set 'Lead Status' to R - New"
                ,"Set 'Assign to' to pandaqa pandaqa"
                ,"Set 'Source name' to test"
                ,"Set 'Brand'"
                ,"Set 'PO Box'"
                ,"Set 'City' to Berlin"
                ,"Set 'State'"
                ,"Scroll Up"
                ,"Click 'Save'"
                ,"Lead was created"
                ,"Go to lead's details view"
                ,"Verify 'First Name' is '***'"
                ,"Verify 'Last Name' is '***'"
                ,"Verify 'Mobile' is '***'"
                ,"Verify 'Fax' is '***'"
                ,"Verify 'Email' is 'pandaqa+***@pandats.com'"
                ,"Verify 'Secondary Email' is 'pandaqa+***@pandats.com'"
                ,"Verify 'Source Name is Test"
                ,"Verify 'Panda Partner ID' exists"
                ,"Verify 'Referral' exists"
                ,"Verify 'Street' is Street test"
                ,"Verify 'Postal Code' is '***'"
                ,"Verify 'Country' is 'Germany'"
                ,"Verify 'Description' is 'Description test'"
                ,"Verify 'Phone Number' is '***'"
                ,"Verify 'Title' is 'Title test'"
                ,"Verify 'Conference' is 'Conference test'"
                ,"Verify 'Status' is 'R - New'"
                ,"Verfiy 'Languge' is 'English'"
                ,"Verify 'PO Box' is '***'"
                ,"Verify 'City' is 'Berlin'"
                ,"Verify 'State' is '***'"
                ,"Click the 'Edit' button"
                ,"Change 'First Name' to 'Sam'"
                ,"Change 'Last Name' to 'White'"
                ,"Change 'Mobile' to '***'"
                ,"Change 'Fax' to '***'"
                ,"Change 'Email' to 'pandaqa+***@pandats.com'"
                ,"Change 'Secondary Email' to 'pandaqa+***@pandats.com'"
                ,"Change 'Languge' to 'Hebrew'"
                ,"Change 'Panda Partner ID' to '***'"
                ,"Change 'Referral' to '***'"
                ,"Change 'Street' to 'Second Street test'"
                ,"Change 'Postal Code' to '***'"
                ,"Change 'Country' to 'United States'"
                ,"Change 'Description' to 'Second Description test'"
                ,"Change 'Phone Number' to '***'"
                ,"Change 'Title' to 'Second Title test'"
                ,"Change 'Conference' to 'Second Conference test'"
                ,"Change 'Status' to 'B - No interest'"
                ,"Change 'Assign to' to pandadev"
                ,"Change 'Source Name' to 'Second SN Test'"
                ,"Change 'PO Box' to '***'"
                ,"Change 'City' to 'New York'"
                ,"Change 'State' to 'NY'"
                ,"Scroll Up"
                ,"Click 'Save'"
                ,"Go to lead's details view"
                ,"Verify 'First Name' is 'Sam'"
                ,"Verify 'Last Name' is 'White'"
                ,"Verify 'Mobile' is '***'"
                ,"Verify 'Fax' is '***'"
                ,"Verify 'Email' is 'pandaqa+***@pandats.com'"
                ,"Verify 'Secondary Email' is 'pandaqa+***@pandats.com'"
                ,"Verify 'Referral' is '***'"
                ,"Verify 'Street' is Second Street test'"
                ,"Verify 'Postal Code' is '***'"
                ,"Verify 'Country' is 'United States'"
                ,"Verify 'Description' is 'Second Description test'"
                ,"Verify 'Phone Number' is '***'"
                ,"Verify 'Title' is 'Second Title test'"
                ,"Verify 'Conference' is 'Second Conference test'"
                ,"Verify 'Status' is 'B - No interest'"
                ,"Verfiy 'Languge' is 'English'"
                ,"Verify 'PO Box' is '***'"
                ,"Verify 'City' is 'New York'"
                ,"Verify 'State' is 'NY'"]

        if self.get_test_pretty_name_new(test) == "LeadModuleTest: test perform convert lead":
            step_suit = ["Open CRM"
                , "Enter Username"
                , "Enter Password"
                , "Click Login"
                , "No OTP"
                , "'What's new' popup isn't displayed"
                ,"Go to Leads module"
                ,"Click Create Lead"
                ,"Set 'First Name' to ***"
                ,"Set 'Last Name' to ***"
                ,"Set 'Mobile'"
                ,"Set 'Fax'"
                ,"Set 'Email' to pandaqa+***@pandats.com"
                ,"Set 'Secondary Email'"
                ,"Set 'Language' to English"
                ,"Set 'Street' to test"
                ,"Set 'Postal Code' to ***"
                ,"Set 'Country' to Germany"
                ,"Set 'Description' to test"
                ,"Set 'Phone Number'"
                ,"Set 'Title' to test"
                ,"Set 'Conference'"
                ,"Set 'Lead Status' to R - New"
                ,"Set 'Assign to' to pandaqa pandaqa"
                ,"Set 'Source name' to test"
                ,"Set 'Brand'"
                ,"Set 'PO Box'"
                ,"Set 'City' to Berlin"
                ,"Set 'State'"
                ,"Scroll Up"
                ,"Click 'Save'"
                ,"Lead was created"
                ,"Side bar is not present"
                ,"Go to lead's details view"
                ,"Click 'Convert Lead'"
                ,"Verify 'First Name' is ***"
                ,"Verify 'Last Name' is ***"
                ,"Verify 'Email' is pandaqa+***@pandats.com"
                ,"Verify 'Phone Number' is ***"
                ,"Set 'Birthday'"
                ,"Set 'Citizenship'"
                ,"Verify 'Address' is ***"
                ,"Verify 'Postal Code' is ***"
                ,"Verify 'City' is ***"
                ,"Verify 'Country' is ***"
                ,"Verify 'Password' is set"
                ,"Verify 'Currency' is set"
                ,"Verify 'Source Name' is set"
                ,"Verify 'Phone Area Code' is set"
                ,"Click 'Submit'"
                ,"Verify 'Account created successfully' message is shown"]

        if self.get_test_pretty_name_new(test) == "SearchingClientsTestCRM: test make searching client module":
            step_suit = ["Open CRM"
                , "Enter Username"
                , "Enter Password"
                , "Click Login"
                , "No OTP"
                , "'What's new' popup isn't displayed"
                ,"Click the filters dropdown"
                ,"Search for 'Test Clients'"
                ,"Choose the 'Test Clients' filter"
                ,"Set 'Email' to pandaqa+***@pandats.com"
                ,"Set 'Country' to ****"
                ,"Set 'First Name' to ***"
                ,"Click the 'Search' button"
                ,"Verify you found the correct client"
                , "Perform scroll up"
                , "Click user name by email :"
                , "Verify the first name"
                , "Verify the last name"
                , "Verify the email"]

        if self.get_test_pretty_name_new(test) == "AddInteraction: test add interaction":
            step_suit = ["Open CRM"
                , "Enter Username"
                , "Enter Password"
                , "Click Login"
                , "No OTP"
                , "'What's new' popup isn't displayed"
                , "Click the  drop down filter"
                , "Select Test Clients"
                , "Click the selected filter"
                , "Select client status"
                , "Set 'Email' to ***"
                , "Set 'Country' to ****"
                , "Click search button"
                , "Scroll up"
                , "Update page"
                , "Click user name by email :"
                , "Side bar is not present"
                , "Open event module"
                , "Set event status 'Not Started'"
                , "Set event type 'Meeting'"
                , "Set '30M'"
                , "Set time"
                , "Set date"
                , "Set  assign to 'pandaqa pandaqa'"
                , "Set priority 'Medium'"
                , "Set comments 'Event Description'"
                , "Set subject 'Test interaction'"
                , "Click the 'save' button"
                , "Verify a confirmation message: Interraction successfully created"
                , "The Ok button was clicked"
                , "Click 'ok' button"]

        if self.get_test_pretty_name_new(test) == "AddInteraction: test interaction search":
            step_suit = ["Open CRM"
                , "Enter Username"
                , "Enter Password"
                , "Click Login"
                , "No OTP"
                , "'What's new' popup isn't displayed"
                , "Open Task module"
                , "Open all tab"
                , "Set subject: Meeting"
                , "Search Meeting"
                , "Results found text: Meeting"
                , "Got search results"]

        if self.get_test_pretty_name_new(test) == "AddEventTaskModule: test add event":
            step_suit = ["Open CRM"
                , "Enter Username"
                , "Enter Password"
                , "Click Login"
                , "No OTP"
                , "'What's new' popup isn't displayed"
                , "Open Task module"
                , "Open event module"
                , "Set event status 'In Progress'"
                , "Set event type 'Meeting'"
                , "Set date"
                , "Set time"
                , "Set duration '30M'"
                , "Set priority 'Medium'"
                , "Set  assign to 'pandaqa pandaqa'"
                , "Set account name"
                , "Set subject 'Testing43434'"
                , "Set comments 'Description Add Event'"
                , "Click the 'save' button"
                , "Open all tab"
                , "Check event"]

        if self.get_test_pretty_name_new(test) == "AddEventTaskModule: test edit event":
            step_suit = ["Open CRM"
                , "Enter Username"
                , "Enter Password"
                , "Click Login"
                , "No OTP"
                , "'What's new' popup isn't displayed"
                , "Open Task module"
                , "Open all tab"
                , "Click Edit"
                , "Set event status 'Planned'"
                , "Set event type 'Call'"
                , "Set date"
                , "Set time"
                , "Set duration '15M'"
                , "Set priority 'High'"
                , "Set assign to 'Default User'"
                , "Set subject 'Testing'"
                , "Set comments 'Description Add Event'"
                , "Click the 'save' button"
                , "Text from 'Update' popup has been got: Task was updated"]

        if self.get_test_pretty_name_new(test) == "AddEventTaskModule: test delete interaction":
            step_suit = ["Open CRM"
                , "Enter Username"
                , "Enter Password"
                , "Click Login"
                , "No OTP"
                , "'What's new' popup isn't displayed"
                , "Click the  drop down filter"
                , "Select Test Clients"
                , "Click the selected filter"
                , "Set email of client"
                , "Click search button"
                , "Open client's details"
                , "Client's page contain events"
                , "Scroll to activities tab"
                , "Open Activities tab"
                , "Press Delete event button"
                , "Delete interaction message is verified"
                , "Delete interaction is confirmed"
                , "Interaction was deleted successfully"
                , "Client's page contain events"
                , "Scroll to activities tab"
                , "Open Activities tab"
                , "Press Delete event button"
                , "Delete interaction message is verified"
                , "Delete interaction is confirmed"
                , "Interaction was deleted successfully"
                , "Client's page does not contain events"]

        if self.get_test_pretty_name_new(test) == "TradingAccountCrmTest: test crm open trading account":
            step_suit = ["Open CRM"
                , "Enter Username"
                , "Enter Password"
                , "Click Login"
                , "No OTP"
                , "'What's new' popup isn't displayed"
                , "Click the  drop down filter"
                , "Select filter : Test Clients"
                , "Click the selected filter"
                , "Set the user's email in the email field"
                , "Click the search button"
                , "Click user email"
                , "Open mt4 actions"
                , "Trading account server was selected: demo"
                , "Trading account currency was selected: USD"
                , "Trading account group was selected: demoSOA-FIX_USD (USD)"
                , "Trading account leverage was selected: 1 : 100"
                , "The Save button was clicked"
                , "Returns a confirmation message: New User Account was created successfully"]

        if self.get_test_pretty_name_new(test) == "CheckPasswordTestCRM: test check client password crm":
            step_suit = ["Open CRM"
                , "Enter Username"
                , "Enter Password"
                , "Click Login"
                , "No OTP"
                , "'What's new' popup isn't displayed"
                , "Click the  drop down filter"
                , "Select filter: Test Clients"
                , "Click the selected filter"
                , "Set the user's email in the email field"
                , "Click the search button"
                , "Click user email"
                , "Perform scroll up"
                , "Open mt actions"
                , "The password to check is set to  Abcd"
                , "The Check button was clicked"
                , "Returns a confirmation message  The password that was entered is correct."
                , "The Ok button was clicked"
                , "Click 'ok' button"]

        if self.get_test_pretty_name_new(test) == "CheckPasswordTestCRM: test check mt4 password crm":
            step_suit = ["Open CRM"
                , "Enter Username"
                , "Enter Password"
                , "Click Login"
                , "No OTP"
                , "'What's new' popup isn't displayed"
                , "Click the  drop down filter"
                , "The field found is   Test Clients"
                , "Click the selected filter"
                , "Setting  the user's email"
                , "Click the search button"
                , "Click user email"
                , "Perform scroll down"
                , "Open the trading account tab"
                , "Perform scroll into view of the element"
                , "Returns the client_account  text"
                , "Perform scroll up"
                , "Open mt actions"
                , "Returns a confirmation message  Password was change successfully"
                , "The Ok button was clicked"
                , "Click 'ok' button"]

        if self.get_test_pretty_name_new(test) == "ChangePasswordTestCRM: test change client password from crm":
            step_suit = ["Open CRM"
                , "Enter Username"
                , "Enter Password"
                , "Click Login"
                , "No OTP"
                , "'What's new' popup isn't displayed"
                , "Click the  drop down filter"
                , "The field found is   Test Clients"
                , "Click the selected filter"
                , "Setting  the user's email in the email field"
                , "Click the search button"
                , "Click user email"
                , "Side bar is not present"
                , "The check client module was opened"
                , "The new password is set to"
                , "The Change button was clicked"
                , "Returns a confirmation message  Password changed succesfully"
                , "The Ok button was clicked"
                , "Click 'ok' button"]

        if self.get_test_pretty_name_new(test) == "ChangePasswordTestCRM: test change mt4 password from crm":
            step_suit = ["Open CRM"
                , "Enter Username"
                , "Enter Password"
                , "Click Login"
                , "No OTP"
                , "'What's new' popup isn't displayed"
                , "Click the  drop down filter "
                , "The field found is   Test Clients"
                , "Click the selected filter"
                , "Setting  the user's email in the email field"
                , "Click the search button "
                , "Click user email"
                , "Perform scroll down "
                , "Open the trading account tab "
                , "Perform scroll into view of the element "
                , "Returns the client account  text"
                , "Perform scroll up"
                , "Open mt actions "
                , "Returns a confirmation message  Password was change successfully"
                , "The Ok button was clicked"
                , "Click 'ok' button "
                , "The page is refreshed"
                , "Open mt actions"
                , "Returns a confirmation message  The password that was entered is correct"
                , "The Ok button was clicked "
                , "Click 'ok' button"
                , "The page is refreshed"
                , "Open mt actions "
                , "Returns a confirmation message  Password was change successfully"
                , "The Ok button was clicked"
                , "Click 'ok' butto"]

        if self.get_test_pretty_name_new(test) == "DepositTestCRM: test make deposit crm":
            step_suit = ["Open CRM"
                , "Enter Username"
                , "Enter Password"
                , "Click Login"
                , "No OTP"
                , "Whats new popup isnt displayed"
                , "The client module was opened"
                , "Click the  drop down filter"
                , "The field found is   Test Clients"
                , "Click the selected filter"
                , "Setting  the user's email in the email field"
                , "Click the search button"
                , "Click user email  "
                , "ClientProfilePage   Open mt actions"
                , "Trading account server was selected  real"
                , "Trading account currency was selected  USD"
                , "Trading account group was selected"
                , "Trading account leverage was selected"
                , "The Save button was clicked"
                , "The close button was clicked"
                , "Click 'close' button "
                , "Perform scroll down "
                , "Open the trading account tab"
                , "Perform scroll into view of the element"
                , "Returns the client_account  text "
                , "Perform scroll up "
                , "The payment method of deposit module was selected  Credit card"
                , "The account of deposit module was selected"
                , "The amount of deposit module was set"
                , "The  description of deposit module was set in the description field   Description Deposit"
                , "The create withdraw button of deposit module was clicked"
                , "Returns a confirmation message  Transaction created successfully"
                , "The Ok button was clicked"
                , "Click 'ok' button"
                , "The page is refreshed"
                , "Open the trading account tab"
                , "Returns the amount you placed on the deposit page"]

        if self.get_test_pretty_name_new(test) == "DepositTestCRM: test make deposit for client crm":
            step_suit = ["Open CRM"
                , "Enter Username"
                , "Enter Password"
                , "Click Login"
                , "No OTP"
                , "Whats new popup isnt displayed "
                , "Click the  drop down filter "
                , "The field found is   Test Clients"
                , "Click the selected filter"
                , "Setting  the users email in the email field  is"
                , "Click the search button "
                , "Click user email"
                , "Perform scroll down "
                , "Open the trading account tab"
                , "Perform scroll into view of the element"
                , "Returns the client_account  text "
                , "Return initial amount text"
                , "Perform scroll up "
                , "Deposit for client popup was opened"
                , "There is no accounts drop down list"
                , "Click OK in Client Deposit pop"]

        if self.get_test_pretty_name_new(test) == "CreditInTestCRM: test make credit in from crm":
            step_suit = ["Open CRM"
                , "Enter Username"
                , "Enter Password"
                , "Click Login"
                , "No OTP"
                , "Whats new popup isnt displayed "
                , "The client module was opened"
                , "Click the  drop down filter "
                , "The field found is   Test Clients"
                , "Click the selected filter"
                , "Setting  the user's email in the email field"
                , "Click the search button "
                , "Click user email"
                , "Open mt actions"
                , "Trading account server was selected  real"
                , "Trading account currency was selected  USD"
                , "Trading account group was selected  HFX_DIAMOND_USD (USD)"
                , "Trading account leverage was selected "
                , "The Save button was clicked"
                , "The close button was clicked "
                , "Click 'close' button "
                , "Perfor scroll down "
                , "Open the trading account tab "
                , "Perform scroll into view of the element"
                , "Returns the client_account  text "
                , "Perform scroll up"
                , "The account of deposit in module was selected"
                , "The amount of credit in module was set"
                , "The expire date of credit in module was set"
                , "The  description of credit in module was set in the description field   Credit in"
                , "The create withdraw button of deposit module was clicked"
                , "The Ok button was clicked "
                , "Click 'ok' button "
                , "The page is refreshed"
                , "The page is refreshed"
                , "he page is refreshed"
                , "Perform scroll down "
                , "Returns the amount you placed on the credit_in page"]

        if self.get_test_pretty_name_new(test) == "TradingAccountCrmTest: test crm edit trading account":
            step_suit = ["Open CRM"
                , "Enter Username"
                , "Enter Password"
                , "Click Login"
                , "No OTP"
                , "Whats new popup isnt displayed"
                , "Click the  drop down filter "
                , "The field found is   Test Clients"
                , "Click the selected filter"
                , "Setting  the user's email in the email field"
                , "Click the search button "
                , "Click user email "
                , "Open mt actions "
                , "Trading account server was selected  demo"
                , "Trading account currency was selected  USD"
                , "Trading account group was selected "
                , "Trading account leverage was selected"
                , "The Save button was clicked"
                , "The close button was clicked"
                , "Click 'close' button "
                , "The page is refreshed"
                , "The page is refreshed"
                , "Open mt actions"
                , "Trading account server was selected   (demo)   USD"
                , "Trading account group was selected  "
                , "Trading account leverage was selected"
                , "The Save button was clicked"
                , "Returns a confirmation message  User successfully update"]

        if self.get_test_pretty_name_new(test) == "AffiliateModule: test create affiliate":
            step_suit = ["Open CRM"
                , "Enter Username"
                , "Enter Password"
                , "Click Login"
                , "No OTP"
                , "What's new' popup isn't displayed"
                , "Open Affiliates module"
                , "Open 'Add new affiliate' popup"
                , "Enter partner name"
                , "Enter allowed IP"
                , "Click plus ip"
                , "Select allowed methods Create lead"
                , "Select blocked country Albania"
                , "Click Submit"
                , "Text from 'Update' popup has been got  Success"
                , "Search partner name and go to affiliate details page"
                , "Go to affiliate details page"
                , "Open Affiliates module"
                , "Open first tabs page"
                , "The Affiliates page was opened"
                , "Search partner name and go to affiliate details page"
                , "Delete button was clicked"
                , "Confirm delete button was clicked"
                , "Search partner name and go to affiliate details page"
                , "Data not found"]

        if self.get_test_pretty_name_new(test) == "CampaignsModuleTest: test create campaign":
            step_suit = ["Open CRM"
                , "Enter Username"
                , "Enter Password"
                , "Click Login"
                , "No OTP"
                , "What's new' popup isn't displayed"
                , "Open campaigns module"
                , "Open 'Add campaign' module"
                , "Set campaign name"
                , "Set assigned to"
                , "Set start date"
                , "Set end date"
                , "Set deal"
                , "Set rate"
                , "Set active check box"
                , "Click save button"
                , "Search by campaign_name"
                , "Verified campaign name"]

        if self.get_test_pretty_name_new(test) == "CampaignsModuleTest: test edit campaign":
            step_suit = ["Open CRM"
                , "Enter Username"
                , "Enter Password"
                , "Click Login"
                , "No OTP"
                , "What's new' popup isn't displayed"
                , "Open campaigns module"
                , "Select campaign name"
                , "Open campaign view"
                , "Set new start date"
                , "Set new end date"
                , "Click save button"
                , "Open campaign view"
                , "Current start date is updated"
                , "Current end date is updated"]

        if self.get_test_pretty_name_new(test) == "CampaignsModuleTest: test delete campaign":
            step_suit = ["Open CRM"
                , "Enter Username"
                , "Enter Password"
                , "Click Login"
                , "No OTP"
                , "What's new' popup isn't displayed"
                , "Open campaigns module"
                , "Select campaign name"
                , "Delete campaign"
                , "Click Confirmation button"
                , "Search deleted campaign"
                , "Deleted Campaign not found"]

        if self.get_test_pretty_name_new(test) == "TradingAccountCrmTest: test crm open live mt5":
            step_suit = ["Open CRM"
                , "Enter Username"
                , "Enter Password"
                , "Click Login"
                , "No OTP"
                , "'What's new' popup isn't displayed"
                , "Click the  drop down filter"
                , "The field found is : Test Clients"
                , "Click the selected filter"
                , "Set the user's email in the email field"
                , "Click the search button"
                , "Click user email"
                , "Open mt4 actions"
                , "Select trading account server: live"
                , "Select trading account currency"
                , "Select trading account group"
                , "Select trading account leverage"
                , "Click 'Save'"
                , "New MT5 Live Account was created successfully"]

        if self.get_test_pretty_name_new(test) == "TradingAccountCrmTest: test crm open demo mt5":
            step_suit = ["Open CRM"
                , "Enter Username"
                , "Enter Password"
                , "Click Login"
                , "No OTP"
                , "'What's new' popup isn't displayed"
                , "Click the drop down filter"
                , "Set name filter: Test Clients"
                , "Click the selected filter"
                , "Set the user's email in the email field"
                , "Click the search button"
                , "Click user email"
                , "Open mt4 actions"
                , "Select trading account server: live"
                , "Select trading account currency"
                , "Select trading account group"
                , "Select trading account leverage"
                , "Click 'Save'"
                , "New MT5 Demo Account was created successfully"]

        if self.get_test_pretty_name_new(test) == "WithdrawTest: test withdraw crm":
            step_suit = ["Open CRM"
                , "Enter Username"
                , "Enter Password"
                , "Click Login"
                , "No OTP"
                , "Whats new popup isn't displayed "
                , "The client module was opened"
                , "Click the  drop down filter "
                , "The field found is Test Clients"
                , "Click the selected filter"
                , "Setting the user's email in the email field"
                , "Click the search button "
                , "Click user email"
                , "Scroll to Financial Transactions section"
                , "Open the financial transactions tab"
                , "Get trading account number"
                , "Open mt4 actions"
                , "The payment method was selected"
                , "The account number was selected"
                , "The amount was set"
                , "The  description was set"
                , "The Create withdraw button was clicked"
                , "Scroll to trading account section"
                , "Open the trading account tab"
                , "Open the trading account page"
                , "Verify balance of account"]

        if self.get_test_pretty_name_new(test) == "CreditOutTestCRM: test make credit out crm":
            step_suit = ["Open CRM"
                , "Enter Username"
                , "Enter Password"
                , "Click Login"
                , "No OTP"
                , "Whats new popup isn't displayed "
                , "The client module was opened"
                , "Click the  drop down filter"
                , "The field found is Test Clients"
                , "Click the selected filter"
                , "Setting the user's email in the email field"
                , "Click the search button"
                , "Click user email"
                , "Open mt4 actions: Credit Out"
                , "The account for credit out was selected"
                , "The amount of credit out was set"
                , "The Granted by of credit out was set"
                , "The Comment of credit out was set"
                , "Create of credit out button was clicked"
                , "Scroll to trading account section"
                , "Open the trading account tab"
                , "Open the trading account page"
                , "Credit balance is verified"]

        return step_suit


