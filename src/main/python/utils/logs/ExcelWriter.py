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


        workbook.close()

        # Send_Email_XLS(filepath)

    @staticmethod
    def get_test_pretty_name(test):
        return test['class'] + '.' + test['method']

    @staticmethod
    def get_test_pretty_name_new(test):
        return test['class'] + ': ' + test['method'].replace('_', ' ')

    def steps_for_test(self, test):

        if self.get_test_pretty_name_new(test) == "UpdateCustomer: test update customer":
            step_suit = ["Open CRM"
                , "Setting the user name in the field : "

                , " Setting the user name in the password: "

                , " Click the login button"

                , "No OTP authentication is required"

                , "'What's new' popup isn't displayed ", "Affiliates page was opened",""
                ,"Enter partner ID 3898"
                ,"Click edit affiliate"
                ,"Check selected methods"
                ,"Select all methods and click submit"
                ,"Check selected methods"
                ,"Copy key"
                ,"Get link API"
                , "Open api"
                , "Enter Secret Key"
                , "Open Authorization module"
                , "Enter partnerId"
                , "Generate time"
                , "Generate accessKey"
                , "Click send"
                , "Check token"
                , "Open update customer module"
                , "Enter email"
                , "Change first name"
                , "Change postal code"
                , "Change phone"
                , "Click Send"
                , "Check token read customers details"
                , "Open first tabs page: "
                , "Click the  drop down filter"
                , "The field found is : Test Clients"
                , "Click the selected filter"
                , "Setting  the user's email in the email field"
                , "Click the search button"
                , "Click user email"
                , "Verified the client email"
                , "Verified the first name: test"
                , "Verified the phone: +352 3233"
                , "Click Custom Information"
                , "Verified the code: 777"]

        if self.get_test_pretty_name_new(test) == "LoginToken: test login token":
            step_suit = ["Open CRM"
                , "Setting the user name in the field : "

                , " Setting the user name in the password: "

                , " Click the login button"

                , "No OTP authentication is required"

                , "'What's new' popup isn't displayed ", "Affiliates page was opened",""
                ,"Enter partner ID 3898"
                ,"Click edit affiliate"
                ,"Check selected methods"
                ,"Select all methods and click submit"
                ,"Check selected methods"
                ,"Copy key"
                ,"Get link API"
                , "Open api"
                , "Enter Secret Key"
                , "Open Authorization module"
                , "Enter partnerId"
                , "Generate time"
                , "Generate accessKey"
                , "Click send"
                , "Check token"
                , "Open login token module"
                , "Enter email"
                , "Click Send"
                , "Check login token"
                , "Open first tabs page"
                , "Check login token"]
        if self.get_test_pretty_name_new(test) == "ReadLeads: test read leads api":
            step_suit = ["Open CRM"
                , "Setting the user name in the field : "

                , " Setting the user name in the password: "

                , " Click the login button"

                , "No OTP authentication is required"

                , "'What's new' popup isn't displayed ", "Affiliates page was opened",""
                ,"Enter partner ID 3898"
                ,"Click edit affiliate"
                ,"Check selected methods"
                ,"Select all methods and click submit"
                ,"Check selected methods"
                ,"Copy key"
                ,"Get link API"
                , "Open api"
                , "Enter Secret Key"
                , "Open Authorization module"
                , "Enter partnerId"
                , "Generate time"
                , "Generate accessKey"
                , "Click send"
                , "Check token"
                , "Open read leads module"
                , "Enter page"
                , "Enter limit"
                , "Click Send"
                , "Check token read leads details"]

        if self.get_test_pretty_name_new(test) == "CreateLead: test create lead api":
            step_suit = ["Open CRM"
                , "Setting the user name in the field : "

                , " Setting the user name in the password: "

                , " Click the login button"

                , "No OTP authentication is required"

                , "'What's new' popup isn't displayed ", "Affiliates page was opened",""
                ,"Enter partner ID 3898"
                ,"Click edit affiliate"
                ,"Check selected methods"
                ,"Select all methods and click submit"
                ,"Check selected methods"
                ,"Copy key"
                ,"Get link API"
                , "Open api"
                , "Enter Secret Key"
                , "Open Authorization module"
                , "Enter partnerId"
                , "Generate time"
                , "Generate accessKey"
                , "Click send"
                , "Check token"
                , "Open create lead module"
                , "Enter email"
                , "Enter first name"
                , "Enter last name"
                , "Enter phone"
                , "Click Send"
                , "Check token read customers details"
                , "Open first tabs page"
                , "Leads module was opened"
                , "Click the  drop down filter"
                , "The field found is : Test Leads"
                , "Click the selected filter"
                , "The first name was entered : LeadFName"
                , "The last name was entered : LeadLName"
                , "The email was entered : pandaqa+20190128152425@pandats.com"
                , "The search button was clicked"
                , "Go to personal details lead"
                , "Verified the lead email: pandaqa+20190128152425@pandats.com"
                , "Verified the lead first name: LeadFName"
                , "Verified the lead last name: LeadLName"
                , "Verified the lead phone: +352 3233"]

        if self.get_test_pretty_name_new(test) == "ReadCustomersDetails: test read customers details":
            step_suit = ["Open CRM"
                , "Setting the user name in the field : "

                , " Setting the user name in the password: "

                , " Click the login button"

                , "No OTP authentication is required"

                , "'What's new' popup isn't displayed ", "Affiliates page was opened",""
                ,"Enter partner ID 3898"
                ,"Click edit affiliate"
                ,"Check selected methods"
                ,"Select all methods and click submit"
                ,"Check selected methods"
                ,"Copy key"
                ,"Get link API"
                , "Open api"
                , "Enter Secret Key"
                , "Open Authorization module"
                , "Enter partnerId"
                , "Generate time"
                , "Generate accessKey"
                , "Click send"
                , "Check token"
                , "Open read customers module"
                , "Enter page"
                , "Enter page"
                , "Click Send"
                , "Check token read customers details"]

        if self.get_test_pretty_name_new(test) == "ReadCustomerDetails: test read customer details":
            step_suit = ["Open CRM"
                , "Setting the user name in the field : "

                , " Setting the user name in the password: "

                , " Click the login button"

                , "No OTP authentication is required"

                , "'What's new' popup isn't displayed ", "Affiliates page was opened",""
                ,"Enter partner ID 3898"
                ,"Click edit affiliate"
                ,"Check selected methods"
                ,"Select all methods and click submit"
                ,"Check selected methods"
                ,"Copy key"
                ,"Get link API"
                , "Open api"
                , "Enter Secret Key"
                , "Open Authorization module"
                , "Enter partnerId"
                , "Generate time"
                , "Generate accessKey"
                , "Click send"
                , "Check token"
                , "Open read customer module"
                , "Enter email"
                , "Click Send"
                , "Check token read customer details"]

        if self.get_test_pretty_name_new(test) == "AutorizationProcess: test autorization process":
            step_suit = ["Open CRM"
                , "Setting the user name in the field : "

                , " Setting the user name in the password: "

                , " Click the login button"

                , "No OTP authentication is required"

                , "'What's new' popup isn't displayed ", "Affiliates page was opened",""
                ,"Enter partner ID 3898"
                ,"Click edit affiliate"
                ,"Check selected methods"
                ,"Select all methods and click submit"
                ,"Check selected methods"
                ,"Copy key"
                ,"Get link API"
                , "Open api"
                , "Enter Secret Key"
                , "Open Authorization module"
                , "Enter partnerId"
                , "Generate time"
                , "Generate accessKey"
                , "Click send"
                , "Check token"]

        if self.get_test_pretty_name_new(test) == "CreateNewCustomer: test create new customer":
            step_suit = ["Open CRM"
                , "Setting the user name in the field : "

                , " Setting the user name in the password: "

                , " Click the login button"

                , "No OTP authentication is required"

                , "'What's new' popup isn't displayed ", "Affiliates page was opened",""
                ,"Enter partner ID 3898"
                ,"Click edit affiliate"
                ,"Check selected methods"
                ,"Select all methods and click submit"
                ,"Check selected methods"
                ,"Copy key"
                ,"Get link API"
                , "Open api"
                , "Enter Secret Key"
                , "Open Authorization module"
                , "Enter partnerId"
                , "Generate time"
                , "Generate accessKey"
                , "Click send"
                , "Check token"
                , "Open customer module"
                , "Enter email"
                , "Enter password"
                , "Enter country"
                , "Enter firstName"
                , "Enter lastName"
                , "Enter phone"
                , "Enter refferal"
                , "Click send"
                , "Check token"
                , "Open CRM,"
                , "Click the  drop down filter "
                , "The field found is : Test Clients"
                , "Click the selected filter"
                , "Setting  the user's email in the email field"
                , "Click the search button"
                , "Click user email: pandaqa+20190128152425@pandats.com"
                , "Verified the client email: pandaqa+20190128152425@pandats.com"
                , "Verified the client country: Germany"
                , "Verified the first name: testqaYNXVJB"
                , "Verified the last name: testAPI"
                , "Verified the phone: +34 53453"
                , "Click Custom Information"
                , "Verified the client email: langref=hebrew"]

        # CalendarView

        if self.get_test_pretty_name_new(test) == "CalendarView: test check add tasks calendar view":
            step_suit = ["Open CRM"
                        ,"Enter Username"
                        ,"Enter Password"
                        ,"Click Login"
                        ,"No OTP"
                        ,"No What's new"
                        ,"Go to Task module"
                        ,"Go to Calendar View"
                        ,"Click Add Event"
                        ,"Set 'Status' to 'In Progress'"
                        ,"Set 'Event Type' to 'Meeting'"
                        ,"Set 'Date'"
                        ,"Set 'Time'"
                        ,"Set 'Duration' to M"
                        ,"Set 'Priority' to Medium"
                        ,"Set 'Assign to' to pandaqa pandaqa"
                        ,"Set 'Account Name'"
                        ,"Set 'Subject'"
                        ,"Set 'Comment'"
                        ,"Click 'Save'"
                        ,"Task was created' message is shown"
                        ,"Verify subject is correct"]

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
                ,"Go to Task module"
                , "Go to Calendar View"
                , "Go to 'Month' tab"
                , "Verify first column is 'Sun'"
                ,"Verify second column is 'Mon'"
                , "Verify third column is 'Tue'"
                , "Verify fourth column is 'Wed'"
                ,"Verify fifth column is 'Thu'"
                , "Verify sixth column is 'Fri'"
                , "Verify seventh column is 'Sat'"]

        if self.get_test_pretty_name_new(test) == "CalendarView: test check week tab":
            step_suit = ["Open CRM"
                , "Enter Username"
                , "Enter Password"
                , "Click Login"
                , "No OTP"
                , "No What's new"
                , "Go to Task module"
                , "Go to Calendar View"
                , "Go to 'Week' tab"]

        # TabFinancialTransaction

        if self.get_test_pretty_name_new(test) == "TabFinancialTransaction: test check searching by column":
            step_suit = ["Open first tabs page"
                , "Setting the user name"
                , "Setting the user password"
                , "Click the login button"
                , "No OTP authentication"
                , "'What's new' popup"
                ,"The financial transactions module was selected"
                , "In filter the transaction number was entered"
                , "In filter the client name was entered:"
                ,"In filter the transaction_type was entered"
                , "In filter the modified_time was entered"
                , "The search button was clicked"
                , "Perform scroll into view of the element"
                , "First financial transaction in search results was opened"
                , "Returns the transaction number"]

        if self.get_test_pretty_name_new(test) == "TabFinancialTransaction: test check all tab from financial transactions":
            step_suit = ["Open first tabs page"
                , "Setting the user name"
                , "Setting the user password"
                , "Click the login button"
                , "No OTP authentication"
                , "'What's new' popup"
                , "The financial_transactions_module was selected"
                , "Returns the tab name All"
                , "Returns the tab name Credit In"
                , "Returns the tab name Credit Out"
                , "Returns the tab name Demo Accounts Transactions"
                , "Returns the tab name Deposits"
                , "Returns the tab name Withdraw"]

        if self.get_test_pretty_name_new(test) == "TabFinancialTransaction: test check search via button":
            step_suit = ["Open first tabs page"
                , "Setting the user name"
                , "Setting the user password"
                , "Click the login button"
                , "No OTP authentication"
                , "'What's new' popup"
                , "The financial transactions module was selected"
                , "Search form was opened"
                , "Searching for transaction ID:"
                , "Searching for client name"
                ,"Searching for transaction type"
                , "Searching for modified time"
                , "looking for created/modified time"
                , "Time from the page list"
                , "Correct time has been found"
                , "Searching for trading account"]


        # FilterModulesTest

        if self.get_test_pretty_name_new(test) == "FilterModulesTest: test create filter clients module":
            step_suit = ["Open first tabs page"
                , "Setting the user name"
                , "Setting the user password"
                , "Click the login button"
                , "No OTP authentication"
                , "'What's new' popup"
                , "The client module was opened"
                , "The filter pop-up is opened"
                , "Tha name filter was set"
                , "The first column was selected"
                , "The second column was selected"
                , "The third column was selected"
                ,"The fourth column was selected"
                ,"The fifth column was selected"
                ,"The sixth column was selected"
                ,"The seventh column was selected"
                ,"The eight column was selected"
                ,"The ninth column was selected"
                ,"The eleventh column was selected"
                ,"The eleventh column was selected"
                ,"The filter was created: "
                ,"First column name "
                ,"Second column name"
                ,"Third column name"
                ,"Fourth column name"
                ,"Fifth column name"
                ,"Sixth column name"
                ,"Seventh column name "
                ,"Eighth column name"
                ,"Ninth  column name"
                ,"Tenth  column name"
                ,"Eleventh column name"]

        if self.get_test_pretty_name_new(test) == "FilterModulesTest: test create filter documents module":
            step_suit = ["Open first tabs page"
                , "Setting the user name"
                , "Setting the user password"
                , "Click the login button"
                , "No OTP authentication"
                , "'What's new' popup"
                ,"The document module was opened"
                , " The filter pop-up is opened"
                , "Tha name filter was set"
                , "The first column was selected"
                , "The second column was selected"
                , "The third column was selected"
                , "The fourth column was selected"
                , "The filter was crated: "
                , "First column name"
                , "Second column name"
                , "Third column name"
                ,"Fourth column name"]

        if self.get_test_pretty_name_new(test) == "FilterModulesTest: test create filter leads module":
            step_suit = ["Open first tabs page"
                ,"Setting the user name in the field"
                , "Setting the user name in the password"
                ,"Click the login button"
                ,"No OTP authentication is required"
                ,"'What's new' popup isn't displayed"
                ,"Leads module was opened"
                ,"The filter pop-up is opened"
                ,"Tha name filter was set"
                ,"The first column was selected"
                ,"The second column was selected"
                ,"The third column was selected"
                ,"The fourth column was selected"
                ,"The fifth column was selected"
                ,"The sixth column was selected"
                ,"The seventh column was selected"
                ,"The eight column was selected"
                ,"The filter was created: "
                ,"First column name"
                ,"Second column name"
                ,"Third column name"
                ,"Fourth column name"
                ,"Fifth column name"
                ,"Sixth column name"
                ,"Seventh column name"
                ,"Seventh column name"]


        if self.get_test_pretty_name_new(test) == "FilterModulesTest: test create filter help desk":
            step_suit = ["Open first tabs page:"
                ,"Setting the user name"
                ,"Setting the user password"
                ,"Click the login button"
                ,"No OTP authentication"
                ,"'What's new' popup isn't displayed"
                ,"Open  help desk module"
                , "The filter pop-up is opened"
                ,"Tha name filter was set"
                ,"The first column was selected"
                ,"The second column was selected"
                ,"The third column was selected"
                ,"The fourth column was selected"
                ,"The fifth column was selected"
                ,"The sixth column was selected"
                ,"The seventh column was selected"
                ,"The eight column was selected"
                ,"The eleventh column was selected"
                ,"The eleventh column was selected"
                ,"The filter was created:"
                ,"First column name"
                ,"Second column name"
                ,"Third column name"
                , "Fourth column name"
                ,"Fifth column name"
                ,"Sixth column name"
                ,"Seventh column name"
                ,"Eighth column name"
                ,"Tenth  column name"
                ,"Eleventh column name"]

        if self.get_test_pretty_name_new(test) == "FilterModulesTest: test create filter trading account module":
            step_suit = ["Open first tabs page"
                ,"Setting the user name"
                ,"Setting the user password"
                ,"Click the login button"
                ,"OTP authentication"
                ,"'What's new' popup isn't displayed"
                ,"The client module was opened"
                ,"The filter pop-up is opened"
                ,"Tha name filter was set"
                ,"The first column was selected"
                ,"The second column was selected"
                , "The third column was selected"
                ,"The fourth column was selected"
                ,"The fifth column was selected"
                ,"The sixth column was selected"
                ,"The seventh column was selected"
                ,"The eight column was selected"
                ,"The ninth column was selected"
                ,"The eleventh column was selected"
                ,"The eleventh column was selected"
                ,"The filter was created:"
                ,"First column name"
                ,"Second column name"
                ,"Third column name"
                ,"Fourth column name"
                ,"Fifth column name"
                ,"Sixth column name"
                ,"Seventh column name"
                ,"Eighth column name"
                ,"Ninth  column name"
                ,"Tenth  column name"
                ,"Eleventh  column name"]

        #LeadsModuleTest

        if self.get_test_pretty_name_new(test) == "TabLeadsModuleCRM: test searching lead modules":
            step_suit = [ "Open first tabs page"
                ,"Setting the user name"
                ,"Setting the user password"
                ,"Click the login button"
                ,"OTP authentication"
                ,"'What's new' popup isn't displayed"
                , "Leads module was opened"
                ,"Create leads module is opened"
                ,"First name was set"
                ,"last name was set"
                ,"Mobile was set: 8888888"
                ,"fax was set: 5555"
                ,"The first name was set"
                ,"The secondary email was set"
                ,"The language  was set"
                ,"The street name was set"
                ,"The postal code was set"
                ,"The country was set"
                ,"The description was set"
                ,"The phone number was set"
                ,"The tittle was set"
                ,"The lead source was set"
                ,"The lead status was set"
                ,"The lead status was set"
                ,"The source name was set"
                ,"Brand select box was not found"
                , "The po box was set"
                ,"The city was set"
                ,"The state was set: "
                ,"Perform scroll up "
                ,"The save button was clicked:"
                , "The lead was created: "
                ,"The page is refreshed"
                ,"The client module was opened"
                ,"Leads module was opened"
                ,"Click the  drop down filter "
                ,"The field found is : Test Leads"
                ,"Click the selected filter"
                ,"The first name was entered"
                ,"The last name was entered"
                ,"The email was entered"
                ,"The search button was clicked"]

        if self.get_test_pretty_name_new(test) == "LeadModuleTest: test create lead":
            step_suit = [ "Open first tabs page"
                ,"Setting the user name"
                ,"Setting the user name"
                ,"Click the login button"
                ,"OTP authentication"
                ,"'What's new' popup isn't displayed"
                ,"Leads module was opened"
                ,"Create leads module is opened"
                ,"First name was set "
                ,"last name was set "
                ,"Mobile was set"
                ,"fax was set "
                ,"The first name was set"
                ,"The secondary email was set "
                ,"The language  was set "
                ,"The street name was set"
                ,"The postal code was set"
                ,"The country was set"
                ,"The description was set"
                ,"The phone number was set"
                ,"The tittle was set: tittle test"
                ,"The lead source was set"
                ,"The lead status was set"
                ,"The lead status was set"
                ,"The source name was set"
                , "Brand select box"
                ,"The po box was set"
                , "The city was set"
                ,"The state was set"
                ,"Perform scroll up "
                ,"The save button was clicked"
                , "The lead was created"
                , "Verifying lead data"
                ,"Returns the first name"
                ,"Returns the last_name"
                ,"Returns the mobile text"
                ,"Returns the fax text"
                ,"Returns the email text"
                ,"Returns the secondary email"
                ,"Returns the source name"
                ,"Returns the panda partner"
                ,"Returns the referral text"
                ,"Returns the street text"
                ,"Returns the postal code"
                ,"Returns the postal code"
                ,"Returns the description text"
                ,"Returns the description text"
                ,"Returns the description text"
                ,"Returns the description text"
                ,"Returns the lead status text"
                ,"Returns the language text"
                ,"Returns the language text"
                ,"Returns the language text"]

        if self.get_test_pretty_name_new(test) == "LeadModuleTest: test edit lead":
            step_suit = ["Open first tabs page"
                ,"Setting the user name"
                ,"Setting the user name"
                ,"Click the login button"
                ,"OTP authentication"
                ,"'What's new' popup isn't displayed"
                ,"Leads module was opened"
                ,"Create leads module is opened"
                ,"First name was set"
                ,"last name was set"
                ,"Mobile was set"
                , "fax was set"
                ,"The first name was set"
                , "The secondary email was set"
                ,"The language  was set"
                ,"The street name was set"
                , "The postal code was set"
                ,"The country was set"
                ,"The description was set"
                ,"The phone number was set"
                ,"The tittle was set"
                ,"The lead source was set"
                ,"The lead status was set"
                ,"The lead status was set"
                ,"The source name was set"
                , "Brand select box was not found"
                ,"The po box was set: po box text"
                , "The city was set"
                ,"The state was set"
                ,"Perform scroll up "
                ,"The save button was clicked:"
                , "The lead was created:"
                ,"Verifying lead data"
                ,"Returns the first name"
                ,"Returns the last name"
                ,"Returns the mobile text"
                ,"Returns the fax text"
                ,"Returns the email text"
                ,"Returns the secondary email"
                ,"Returns the source name"
                ,"Returns the panda partner"
                ,"Returns the referral text"
                ,"Returns the street text"
                ,"Returns the postal code"
                ,"Returns the postal code"
                ,"Returns the description text"
                ,"Returns the description text"
                ,"Returns the description text"
                ,"Returns the description text"
                ,"Returns the lead status text"
                ,"Returns the language text"
                ,"Returns the language text"
                ,"Returns the language text:"
                ,"The delete pop-up is displayed"
                ,"First name was set"
                ,"last name was set"
                ,"Mobile was set"
                ,"fax was set"
                ,"The first email was set"
                ,"The secondary email was set"
                ,"The language  was set"
                ,"The panda partner id was set"
                ,"The referral was set"
                ,"The street name was set"
                ,"The postal code was set"
                ,"The country was set"
                ,"The description was set"
                ,"The phone number was set"
                ,"The tittle was set"
                ,"The lead source was set"
                ,"The lead status was set"
                ,"The assign to was set"
                ,"The source name was set"
                ,"The po box was set"
                ,"The city was set"
                ,"The state was set"
                ,"Perform scroll up"
                ,"The save button was clicked:"
                ,"Verifying lead data"
                ,"Returns the first name"
                ,"Returns the last_name"
                ,"Returns the mobile text"
                ,"Returns the fax text"
                ,"Returns the email text"
                ,"Returns the secondary email"
                ,"Returns the source name"
                ,"Returns the panda partner"
                ,"Returns the referral text"
                ,"Returns the street text"
                ,"Returns the postal code"
                ,"Returns the postal code"
                ,"Returns the description text"
                ,"Returns the description text"
                ,"Returns the description text"
                ,"Returns the description text"
                ,"Returns the lead status text"
                ,"Returns the language text"
                ,"Returns the language text"
                ,"Returns the language text"]

        if self.get_test_pretty_name_new(test) == "LeadModuleTest: test perform convert lead":
            step_suit = ["Open first tabs page"
                            ,"Setting the user name"
                            ,"Setting the user password"
                            ,"Click the login button"
                            ,"No OTP authentication is required"
                            ,"'What's new' popup isn't displayed"
                            ,"Leads module was opened"
                            ,"Create leads module is opened"
                            ,"First name was set"
                            ,"last name was set"
                            ,"Mobile was set"
                            ,"fax was set"
                            ,"The first name was set"
                            ,"The secondary email was set"
                            ,"The language  was set"
                            ,"The street name was set"
                            ,"The postal code was set"
                            ,"The country was set"
                            ,"The description was set"
                            ,"The phone number was set"
                            ,"The tittle was set"
                            ,"The lead source was set"
                            ,"The lead status was set"
                            ,"The lead status was set"
                            ,"The source name was set"
                            ,"Brand select box was not found"
                            ,"The po box was set: po box text"
                            ,"The city was set: Berlin"
                            ,"The state was set:"
                            ,"Perform scroll up"
                            ,"The save button was clicked:"
                            ,"The lead was created:"
                            ,"Side bar is not present"
                            ,"The convert lead module was opened"
                            ,"First name was set"
                            ,"last name was set"
                            ,"The email was set"
                            ,"The phone number was set"
                            ,"Birthday input"
                            ,"Citizenship input"
                            ,"The address was set"
                            ,"The postal code was set"
                            ,"The city was set"
                            ,"The country was set"
                            ,"The password was set"
                            ,"The currency was set"
                            ,"Source input was not found"
                            ,"The phone area code was set"
                            ,"Click submit"
                            ,"Lead convert message was not picked up"
                            ,"Returns the exists text" ]


        if self.get_test_pretty_name_new(test) == "SearchingClientsTestCRM: test make searching client module":
            step_suit = ["Open first tabs page:"
                        ,"Setting the user name in the field"
                        ,"Setting the user name in the password"
                        ,"Click the login button"
                        ,"No OTP authentication is required"
                        ,"'What's new' popup isn't displayed"
                        ,"Click the  drop down filter"
                        ,"The field found is : Test Clients"
                        ,"Click the selected filter"
                        ,"The client status was selected "
                        ,"Email was entered "
                        ,"The country was entered "
                        ,"The search button was clicked"
                        ,"Perform scroll up"
                        ,"Perform scroll up"
                        ,"Click user name by email :"
                        ,"Returns the first name"
                        ,"Returns the last name"
                        ,"Returns the email"]

        if self.get_test_pretty_name_new(test) == "AddInteraction: test add interaction":
            step_suit = ["Open first tabs page"
                        ,"Setting the user name in the field"
                        ,"Setting the user name in the password"

                        ,"Click the login button"

                        ,"No OTP authentication is required"

                        ,"'What's new' popup isn't displayed"
                        ,"Click the  drop down filter"
                        ,"The field found is : Test Clients"
                        ,"Click the selected filter"
                        ,"The client status was selected "
                        ,"Email was entered "
                        ,"The country was entered"
                        ,"The search button was clicked"
                        ,"Perform scroll up"
                        ,"Perform scroll up"
                        ,"Click user name by email :"
                        ,"Side bar is not present"
                        ,"The event module was opened"
                        ,"The event status is set Not Started"
                        ,"The event type is set Meeting"
                        ,"The duration  is set 30M"
                        ,"The time is set "
                        ,"The date is set"
                        ,"The  assign to is set pandaqa pandaqa"
                        ,"The priority is set Medium"
                        ,"The comments is set Event Description"
                        ,"The subject is set to Test interaction:"
                        ,"Click the 'save' button"
                        ,"Returns a confirmation message: Interraction successfully created"
                        ,"The Ok button was clicked"
                        ,"Click 'ok' button"]

        if self.get_test_pretty_name_new(test) == "AddInteraction: test interaction search":
            step_suit = ["Open first tabs page"
                        ,"Setting the user name"
                        ,"Setting the user password"
                        ,"Click the login button"
                        ,"No OTP authentication is required"
                        ,"'What's new' popup isn't displayed"
                        ,"Task module is opened"
                        ,"The all tab was opened"
                        ,"The subject was set: Meeting"
                        ,"The subject was set: Meeting"
                        ,"Results found text:"
                        ,"Got search results"]

        if self.get_test_pretty_name_new(test) == "AddEventTaskModule: test add event":
            step_suit = ["Open first tabs page"
                        ,"Setting the user name"
                        ,"Setting the user password"
                        ,"Click the login button"
                        ,"No OTP authentication is required"
                        ,"'What's new' popup isn't displayed"
                        ,"Task module is opened"
                        ,"The event  module was opened"
                        ,"The event status was set In Progress"
                        ,"The event type is set Meeting"
                        ,"The date  was set"
                        ,"The time  was set"
                        ,"The duration  was set 30M"
                        ,"The priority was set Medium"
                        ,"The  assign to was set pandaqa pandaqa"
                        ,"The account was set"
                        ,"The subject was set Testing43434"
                        ,"The comments was set Description Add Event"
                        ,"Click the 'save' button"
                        ,"The all tab was opened"
                        ,"The all tab was opened and check event"]

        if self.get_test_pretty_name_new(test) == "AddEventTaskModule: test edit event":
            step_suit = ["Open first tabs page:"
                        ,"Setting the user name"
                        ,"Setting the user password"
                        ,"Click the login button"
                        ,"No OTP authentication is required"
                        ,"'What's new' popup isn't displayed"
                        ,"Task module is opened"
                        ,"The all tab was opened"
                        ,"Edit popup was opened"
                        ,"The event status was set Planned"
                        ,"The event type is set Call"
                        ,"The date  is set"
                        ,"The time  is set"
                        ,"The duration  is set 15M"
                        ,"The priority is set High"
                        ,"The assign to is set Default User"
                        ,"The subject is set Testing28246"
                        ,"The comments is set Description Add Event"
                        ,"Click the 'save' button"
                        ,"Text from 'Update' popup has been got: Task was updated"]

        if self.get_test_pretty_name_new(test) == "TradingAccountCrmTest: test crm open trading account":
            step_suit = ["Open first tabs page"
                        ,"Setting the user name"
                        ,"Setting the user password"
                        ,"Click the login button"
                        ,"No OTP authentication is required"
                        ,"'What's new' popup isn't displayed"
                        ,"Click the  drop down filter"
                        ,"The field found is : Test Clients"
                        ,"Click the selected filter"
                        ,"Setting  the user's email in the email field"
                        ,"Click the search button"
                        ,"Click user email"
                        ,"Open mt4 actions"
                        ,"Trading account server was selected: demo"
                        ,"Trading account currency was selected: USD"
                        ,"Trading account group was selected: demoSOA-FIX_USD (USD)"
                        ,"Trading account leverage was selected: 1 : 100"
                        ,"The Save button was clicked"
                        ,"Returns a confirmation message: New User Account was created successfully"]


        if self.get_test_pretty_name_new(test) == "CheckPasswordTestCRM: test check client password crm":
            step_suit = ["Open first tabs page"
                        ,"Setting the user name"
                        ,"Setting the user password"
                        ,"Click the login button"
                        ,"No OTP authentication is required"
                        ,"'What's new' popup isn't displayed"
                        ,"Click the  drop down filter"
                        ,"The field found is   Test Clients"
                        ,"Click the selected filter"
                        ,"Setting  the user's email in the email field"
                        ,"Click the search button"
                        ,"Click user email"
                        ,"Perform scroll up"
                        ,"Open mt actions"
                        ,"The password to check is set to  Abcd"
                        ,"The Check button was clicked"
                        ,"Returns a confirmation message  The password that was entered is correct."
                        ,"The Ok button was clicked"
                        ,"Click 'ok' button"]

        if self.get_test_pretty_name_new(test) == "CheckPasswordTestCRM: test check mt4 password crm":
            step_suit = [ "Open first tabs page"
                            ,"Setting the user name in the field"
                            ,"Setting the user name in the password"
                            ,"Click the login button"
                            ,"No OTP authentication is required"
                            ,"'What's new' popup isn't displayed"
                            ,"Click the  drop down filter"
                            ,"The field found is   Test Clients"
                            ,"Click the selected filter"
                            ,"Setting  the user's email"
                            ,"Click the search button"
                            ,"Click user email"
                            ,"Perform scroll down"
                            ,"Open the trading account tab"
                            ,"Perform scroll into view of the element"
                            ,"Returns the client_account  text"
                            ,"Perform scroll up"
                            ,"Open mt actions"
                            ,"Returns a confirmation message  Password was change successfully"
                            ,"The Ok button was clicked"
                            ,"Click 'ok' button"]

        if self.get_test_pretty_name_new(test) == "ChangePasswordTestCRM: test change client password from crm":
            step_suit = [ "Open first tabs page"
                        ,"Setting the user name in the field"
                        ,"Setting the user name in the password"
                        ,"Click the login button"
                        ,"No OTP authentication is required"
                        ,"'What's new' popup isn't displayed"
                        ,"Click the  drop down filter"
                        ,"The field found is   Test Clients"
                        ,"Click the selected filter"
                        ,"Setting  the user's email in the email field"
                        ,"Click the search button"
                        ,"Click user email"
                        ,"Side bar is not present"
                        ,"The check client module was opened"
                        ,"The new password is set to"
                        ,"The Change button was clicked"
                        ,"Returns a confirmation message  Password changed succesfully"
                        ,"The Ok button was clicked"
                        ,"Click 'ok' button" ]

        if self.get_test_pretty_name_new(test) == "ChangePasswordTestCRM: test change mt4 password from crm":
            step_suit = ["Open first tabs page"
                        ,"Setting the user name in the field"
                        ,"Setting the user name in the password"
                        ,"Click the login button"
                        ,"No OTP authentication is required"
                        ,"'What's new' popup isn't displayed"
                        ,"Click the  drop down filter "
                        ,"The field found is   Test Clients"
                        ,"Click the selected filter"
                        ,"Setting  the user's email in the email field"
                        ,"Click the search button "
                        ,"Click user email"
                        ,"Perform scroll down "
                        ,"Open the trading account tab "
                        ,"Perform scroll into view of the element "
                        ,"Returns the client account  text"
                        ,"Perform scroll up"
                        ,"Open mt actions "
                        ,"Returns a confirmation message  Password was change successfully"
                        ,"The Ok button was clicked"
                        ,"Click 'ok' button "
                        ,"The page is refreshed"
                        ,"Open mt actions"
                        ,"Returns a confirmation message  The password that was entered is correct"
                        ,"The Ok button was clicked "
                        ,"Click 'ok' button"
                        ,"The page is refreshed"
                        ,"Open mt actions "
                        ,"Returns a confirmation message  Password was change successfully"
                        ,"The Ok button was clicked"
                        ,"Click 'ok' butto"]

        if self.get_test_pretty_name_new(test) == "DepositTestCRM: test make deposit crm":
            step_suit = ["Open first tabs page"
                        ,"Setting the user name in the field"
                        ,"Setting the user name in the password"
                        ,"Click the login button"
                        ,"No OTP authentication is required"
                        ,"Whats new popup isnt displayed"
                        ,"The client module was opened"
                        ,"Click the  drop down filter"
                        ,"The field found is   Test Clients"
                        ,"Click the selected filter"
                        ,"Setting  the user's email in the email field"
                        ,"Click the search button"
                        ,"Click user email  "
                        ,"ClientProfilePage   Open mt actions"
                        ,"Trading account server was selected  real"
                        ,"Trading account currency was selected  USD"
                        ,"Trading account group was selected"
                        ,"Trading account leverage was selected"
                        ,"The Save button was clicked"
                        ,"The close button was clicked"
                        ,"Click 'close' button "
                        ,"Perform scroll down "
                        ,"Open the trading account tab"
                        ,"Perform scroll into view of the element"
                        ,"Returns the client_account  text "
                        ,"Perform scroll up "
                        ,"The payment method of deposit module was selected  Credit card"
                        ,"The account of deposit module was selected"
                        ,"The amount of deposit module was set"
                        ,"The  description of deposit module was set in the description field   Description Deposit"
                        ,"The create withdraw button of deposit module was clicked"
                        ,"Returns a confirmation message  Transaction created successfully"
                        ,"The Ok button was clicked"
                        ,"Click 'ok' button"
                        ,"The page is refreshed"
                        ,"Open the trading account tab"
                        ,"Returns the amount you placed on the deposit page" ]

        if self.get_test_pretty_name_new(test) == "DepositTestCRM: test make deposit for client crm":
            step_suit = [ "Open first tabs page"
                        ,"Setting the user name in the field"
                        ,"Setting the user name in the password"
                        ,"Click the login button"
                        ,"No OTP authentication is required"
                        ,"Whats new popup isnt displayed "
                        ,"Click the  drop down filter "
                        ,"The field found is   Test Clients"
                        ,"Click the selected filter"
                        ,"Setting  the users email in the email field  is"
                        ,"Click the search button "
                        ,"Click user email"
                        ,"Perform scroll down "
                        ,"Open the trading account tab"
                        ,"Perform scroll into view of the element"
                        ,"Returns the client_account  text "
                        ,"Return initial amount text"
                        ,"Perform scroll up "
                        ,"Deposit for client popup was opened"
                        ,"There is no accounts drop down list"
                        ,"Click OK in Client Deposit pop"]

        if self.get_test_pretty_name_new(test) == "CreditInTestCRM: test make credit in from crm":
            step_suit = ["Open first tabs page"
                        ,"Setting the user name in the field"
                        ,"Setting the user name in the password"
                        ,"Click the login button"
                        ,"No OTP authentication is required"
                        ,"Whats new popup isnt displayed "
                        ,"The client module was opened"
                        ,"Click the  drop down filter "
                        ,"The field found is   Test Clients"
                        ,"Click the selected filter"
                        ,"Setting  the user's email in the email field"
                        ,"Click the search button "
                        ,"Click user email"
                        ,"Open mt actions"
                        ,"Trading account server was selected  real"
                        ,"Trading account currency was selected  USD"
                        ,"Trading account group was selected  HFX_DIAMOND_USD (USD)"
                        ,"Trading account leverage was selected "
                        ,"The Save button was clicked"
                        ,"The close button was clicked "
                        ,"Click 'close' button "
                        ,"Perfor scroll down "
                        ,"Open the trading account tab "
                        ,"Perform scroll into view of the element"
                        ,"Returns the client_account  text "
                        ,"Perform scroll up"
                        ,"The account of deposit in module was selected"
                        ,"The amount of credit in module was set"
                        ,"The expire date of credit in module was set"
                        ,"The  description of credit in module was set in the description field   Credit in"
                        ,"The create withdraw button of deposit module was clicked"
                        ,"The Ok button was clicked "
                        ,"Click 'ok' button "
                        ,"The page is refreshed"
                        ,"The page is refreshed"
                        ,"he page is refreshed"
                        ,"Perform scroll down "
                        ,"Returns the amount you placed on the credit_in page" ]

        if self.get_test_pretty_name_new(test) == "TradingAccountCrmTest: test crm edit trading account":
            step_suit = ["Open first tabs page"
                        ,"Setting the user name in the field"
                        ,"Setting the user name in the password"
                        ,"Click the login button"
                        ,"No OTP authentication is required"
                        ,"Whats new popup isnt displayed"
                        ,"Click the  drop down filter "
                        ,"The field found is   Test Clients"
                        ,"Click the selected filter"
                        ,"Setting  the user's email in the email field"
                        ,"Click the search button "
                        ,"Click user email "
                        ,"Open mt actions "
                        ,"Trading account server was selected  demo"
                        ,"Trading account currency was selected  USD"
                        ,"Trading account group was selected "
                        ,"Trading account leverage was selected"
                        ,"The Save button was clicked"
                        ,"The close button was clicked"
                        ,"Click 'close' button "
                        ,"The page is refreshed"
                        ,"The page is refreshed"
                        ,"Open mt actions"
                        ,"Trading account server was selected   (demo)   USD"
                        ,"Trading account group was selected  "
                        ,"Trading account leverage was selected"
                        ,"The Save button was clicked"
                        ,"Returns a confirmation message  User successfully update"]

        if self.get_test_pretty_name_new(test) == "AffiliateModule: test create affiliate":
            step_suit = ["Open first tabs page"
                            ,"Setting the user name in the field "
                            ,"Setting the user name in the password"
                            ,"lick the login button"
                            ,"OTP authentication is required"
                            ,"What's new' popup isn't displayed"
                            ,"Affiliates page was opened"
                            ,"Open 'Add new affiliate' popup"
                            ,"Enter partner name"
                            ,"Enter allowed IP"
                            ,"Click plus ip"
                            ,"Select allowed methods Create lead"
                            ,"Select blocked country Albania"
                            ,"Click Submit"
                            ,"Text from 'Update' popup has been got  Success"
                            ,"Search partner name and go to affiliate details page"
                            ,"Affiliate details page"
                            ,"Delete affiliate"
                            ,"Affiliates page was opened"
                            ,"Search partner name and go to affiliate details page"
                            ,"Delete button was clicked"
                            ,"Confirm delete button was clicked"
                            ,"Search partner name and go to affiliate details page"
                            ,"Data not found"]

        return step_suit


