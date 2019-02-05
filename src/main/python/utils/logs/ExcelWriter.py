import xlsxwriter
from time import gmtime, strftime
from src.test.python.ui.automation.utils.postconditions.SendMail import Send_Email_XLS

class ExcelWriter:

    def write_test_results(self, brands, tests, results):
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
                ,"Verify 'Panda Partner ID' exists"
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
                ,"Verify 'Source Name is 'Second SN Test'"
                ,"Verify 'Panda Partner ID' is '***'"
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
                , "The field found is : Test Clients"
                , "Click the selected filter"
                , "The client status was selected "
                , "Email was entered "
                , "The country was entered"
                , "The search button was clicked"
                , "Perform scroll up"
                , "Perform scroll up"
                , "Click user name by email :"
                , "Side bar is not present"
                , "The event module was opened"
                , "The event status is set Not Started"
                , "The event type is set Meeting"
                , "The duration  is set 30M"
                , "The time is set "
                , "The date is set"
                , "The  assign to is set pandaqa pandaqa"
                , "The priority is set Medium"
                , "The comments is set Event Description"
                , "The subject is set to Test interaction:"
                , "Click the 'save' button"
                , "Returns a confirmation message: Interraction successfully created"
                , "The Ok button was clicked"
                , "Click 'ok' button"]

        if self.get_test_pretty_name_new(test) == "AddInteraction: test interaction search":
            step_suit = ["Open first tabs page"
                , "Setting the user name"
                , "Setting the user password"
                , "Click the login button"
                , "No OTP authentication is required"
                , "'What's new' popup isn't displayed"
                , "Task module is opened"
                , "The all tab was opened"
                , "The subject was set: Meeting"
                , "The subject was set: Meeting"
                , "Results found text:"
                , "Got search results"]

        if self.get_test_pretty_name_new(test) == "AddEventTaskModule: test add event":
            step_suit = ["Open first tabs page"
                , "Setting the user name"
                , "Setting the user password"
                , "Click the login button"
                , "No OTP authentication is required"
                , "'What's new' popup isn't displayed"
                , "Task module is opened"
                , "The event  module was opened"
                , "The event status was set In Progress"
                , "The event type is set Meeting"
                , "The date  was set"
                , "The time  was set"
                , "The duration  was set 30M"
                , "The priority was set Medium"
                , "The  assign to was set pandaqa pandaqa"
                , "The account was set"
                , "The subject was set Testing43434"
                , "The comments was set Description Add Event"
                , "Click the 'save' button"
                , "The all tab was opened"
                , "The all tab was opened and check event"]

        if self.get_test_pretty_name_new(test) == "AddEventTaskModule: test edit event":
            step_suit = ["Open first tabs page:"
                , "Setting the user name"
                , "Setting the user password"
                , "Click the login button"
                , "No OTP authentication is required"
                , "'What's new' popup isn't displayed"
                , "Task module is opened"
                , "The all tab was opened"
                , "Edit popup was opened"
                , "The event status was set Planned"
                , "The event type is set Call"
                , "The date  is set"
                , "The time  is set"
                , "The duration  is set 15M"
                , "The priority is set High"
                , "The assign to is set Default User"
                , "The subject is set Testing28246"
                , "The comments is set Description Add Event"
                , "Click the 'save' button"
                , "Text from 'Update' popup has been got: Task was updated"]

        if self.get_test_pretty_name_new(test) == "TradingAccountCrmTest: test crm open trading account":
            step_suit = ["Open first tabs page"
                , "Setting the user name"
                , "Setting the user password"
                , "Click the login button"
                , "No OTP authentication is required"
                , "'What's new' popup isn't displayed"
                , "Click the  drop down filter"
                , "The field found is : Test Clients"
                , "Click the selected filter"
                , "Setting  the user's email in the email field"
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
            step_suit = ["Open first tabs page"
                , "Setting the user name"
                , "Setting the user password"
                , "Click the login button"
                , "No OTP authentication is required"
                , "'What's new' popup isn't displayed"
                , "Click the  drop down filter"
                , "The field found is   Test Clients"
                , "Click the selected filter"
                , "Setting  the user's email in the email field"
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
            step_suit = ["Open first tabs page"
                , "Setting the user name in the field"
                , "Setting the user name in the password"
                , "Click the login button"
                , "No OTP authentication is required"
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
            step_suit = ["Open first tabs page"
                , "Setting the user name in the field"
                , "Setting the user name in the password"
                , "Click the login button"
                , "No OTP authentication is required"
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
            step_suit = ["Open first tabs page"
                , "Setting the user name in the field"
                , "Setting the user name in the password"
                , "Click the login button"
                , "No OTP authentication is required"
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
            step_suit = ["Open first tabs page"
                , "Setting the user name in the field"
                , "Setting the user name in the password"
                , "Click the login button"
                , "No OTP authentication is required"
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
            step_suit = ["Open first tabs page"
                , "Setting the user name in the field"
                , "Setting the user name in the password"
                , "Click the login button"
                , "No OTP authentication is required"
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
            step_suit = ["Open first tabs page"
                , "Setting the user name in the field"
                , "Setting the user name in the password"
                , "Click the login button"
                , "No OTP authentication is required"
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
            step_suit = ["Open first tabs page"
                , "Setting the user name in the field"
                , "Setting the user name in the password"
                , "Click the login button"
                , "No OTP authentication is required"
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
            step_suit = ["Open first tabs page"
                , "Setting the user name in the field "
                , "Setting the user name in the password"
                , "lick the login button"
                , "OTP authentication is required"
                , "What's new' popup isn't displayed"
                , "Affiliates page was opened"
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
                , "Affiliate details page"
                , "Open first tabs page"
                , "The Affiliates page was opened"
                , "Search partner name and go to affiliate details page"
                , "Delete button was clicked"
                , "Confirm delete button was clicked"
                , "Search partner name and go to affiliate details page"
                , "Data not found"]

        if self.get_test_pretty_name_new(test) == "CampaignsModuleTest: test create campaign":
            step_suit = ["Open first tabs page"
                , "Setting the user name in the field "
                , "Setting the user name in the password"
                , "lick the login button"
                , "OTP authentication is required"
                , "What's new' popup isn't displayed"
                , "The campaigns module was opened"
                , "The Add campaign module was opened"
                , "The campaign name was set"
                , "The assigned to was set"
                , "The start date was set"
                , "The end date was set"
                , "The deal was set"
                , "The rate was set"
                , "The active check box was set"
                , "The save button was clicked"
                , "The campaign_name was entered to search field"
                , "Campaign name verified"]

        if self.get_test_pretty_name_new(test) == "CampaignsModuleTest: test edit campaign":
            step_suit = ["Open first tabs page"
                , "Setting the user name in the field "
                , "Setting the user name in the password"
                , "lick the login button"
                , "OTP authentication is required"
                , "What's new' popup isn't displayed"
                , "The campaigns module was opened"
                , "The campaign_name was found"
                , "The campaign view was opened"
                , "The new start date was set"
                , "The new end date was set"
                , "The save button was clicked"
                , "The campaign view was opened"
                , "Current start date is updated"
                , "Current end date is updated"]

        if self.get_test_pretty_name_new(test) == "CampaignsModuleTest: test delete campaign":
            step_suit = ["Open first tabs page"
                , "Setting the user name in the field "
                , "Setting the user name in the password"
                , "lick the login button"
                , "OTP authentication is required"
                , "What's new' popup isn't displayed"
                , "The campaigns module was opened"
                , "The campaign_name was found"
                , "The campaign was deleted"
                , "The deleting confirmation button is clicked"
                , "The deleted campaign was searched"
                , "Deleted Campaign not found"]

        if self.get_test_pretty_name_new(test) == "TradingAccountCrmTest: test crm open live mt5":
            step_suit = ["Open first tabs page"
                , "Setting the user name"
                , "Setting the user password"
                , "Click the login button"
                , "No OTP authentication is required"
                , "'What's new' popup isn't displayed"
                , "Click the  drop down filter"
                , "The field found is : Test Clients"
                , "Click the selected filter"
                , "Setting  the user's email in the email field"
                , "Click the search button"
                , "Click user email"
                , "Open mt4 actions"
                , "Trading account server was selected: live"
                , "Trading account currency was selected"
                , "Trading account group was selected"
                , "Trading account leverage was selected"
                , "The Save button was clicked"
                , "New MT5 Live Account was created successfully"]

        if self.get_test_pretty_name_new(test) == "TradingAccountCrmTest: test crm open demo mt5":
            step_suit = ["Open first tabs page"
                , "Setting the user name"
                , "Setting the user password"
                , "Click the login button"
                , "No OTP authentication is required"
                , "'What's new' popup isn't displayed"
                , "Click the  drop down filter"
                , "The field found is : Test Clients"
                , "Click the selected filter"
                , "Setting  the user's email in the email field"
                , "Click the search button"
                , "Click user email"
                , "Open mt4 actions"
                , "Trading account server was selected: live"
                , "Trading account currency was selected"
                , "Trading account group was selected"
                , "Trading account leverage was selected"
                , "The Save button was clicked"
                , "New MT5 Demo Account was created successfully"]

        return step_suit


