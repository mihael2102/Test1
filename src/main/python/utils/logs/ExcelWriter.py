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
        cell_format_fail = workbook.add_format({'align': 'center', 'bg_color': '#fbabab', 'text_wrap': True})
        cell_format_steps_to_fail = workbook.add_format({'align': 'center', 'bg_color': '#F1F2A2', 'text_wrap': True})
        cell_format_name_test = workbook.add_format({'align': 'center', 'bg_color': '#ffffff', 'bold': True})
        cell_format_test = workbook.add_format({'align': 'center', 'bg_color': '#ffffff'})
        # set column widths
        worksheet.set_default_row(20)
        worksheet.write(0, 0, "Brand \ Test")
        worksheet.set_column(0, 0, 60)
        worksheet.set_column(1, len(brands), 20)

        col = 1
        for brand in brands:
            row = 0
            worksheet.write(row, col, brand)
            for test in tests:
                row += 1
                test_result = results[brand][self.get_test_pretty_name(test)] \
                    if self.get_test_pretty_name(test) in results[brand] else ""
                
                s = "\n"

                if s in test_result:
                    new_row_data = test_result.split("\n")

                    while '' in new_row_data:
                        new_row_data.remove('')

                    while ' ' in new_row_data:
                        new_row_data.remove(' ')


                    for data in new_row_data:
                        if "Test create client filter is failed" in data:
                            worksheet.write(row, col, data, cell_format_fail)
                            create_filter_clients_module = "The client module was opened\n The filter pop-up is opened \n Tha name filter was set \n The first column was selected \n The second column was selected \n The third column was selected \n The fourth column was selected \n The fifth column was selected \n The sixth column was selected \n The seventh column was selected \n The eight column was selected \n The ninth column was selected \n The eleventh column was selected \n The eleventh column was selected \n The filter was created:  \n First column name  \n Second column name \n Third column name \n Fourth column name \n Fifth column name \n Sixth column name \n Seventh column name  \n Eighth column name \n Ninth  column name \n Tenth  column name \n Eleventh column name"
                            worksheet.write_comment(row, col, create_filter_clients_module, {'width': 250, 'height': 400})


                        elif "Test create documents filter is failed" in data:
                            worksheet.write(row, col, data, cell_format_fail)
                            create_filter_documents_module = "The document module was opened \n The filter pop-up is opened \n Tha name filter was set \n The first column was selected \n The second column was selected\nThe third column was selected\nThe fourth column was selected\nThe filter was crated: \nFirst column name\nSecond column name\nThird column name\nFourth column name"
                            worksheet.write_comment(row, col, create_filter_documents_module,
                                                    {'width': 250, 'height': 400})

                        elif "Test create lead filter is failed" in data:
                            worksheet.write(row, col, data, cell_format_fail)
                            create_filter_leads_module = "Leads module was opened \n The filter pop-up is opened \n Tha name filter was set \n The first column was selected \n The second column was selected \n The third column was selected \n The fourth column was selected\n The fifth column was selected\n The sixth column was selected\n The seventh column was selected\n The eight column was selected\n The filter was created: \n First column name\n Second column name\n Third column name\n Fourth column name\n Fifth column name\n Sixth column name\n Seventh column name\n Seventh column name"
                            worksheet.write_comment(row, col, create_filter_leads_module,
                                                    {'width': 250, 'height': 400})

                        elif "Test create help desk filter is failed" in data:
                            worksheet.write(row, col, data, cell_format_fail)
                            create_filter_help_desk_module = "Open  help desk modul\n  The filter pop-up is opened\n Tha name filter was set\n The first column was selected\n The second column was selected\n The third column was selected\n The fourth column was selected\n The fifth column was selected\n The sixth column was selected\n The seventh column was selected\n The eight column was selected\n The eleventh column was selected\n The eleventh column was selected\n The filter was created:\n First column name\n Second column name\n Third column name\n Fourth column name\n Fifth column name\n Sixth column name\n Seventh column name\n Eighth column name\n Tenth  column name\n Eleventh column name"
                            worksheet.write_comment(row, col, create_filter_help_desk_module,
                                                    {'width': 250, 'height': 400})

                        elif "Test create trading account filter is failed" in data:
                            worksheet.write(row, col, data, cell_format_fail)
                            create_filter_trading_account_module = "The client module was o\n  The filter pop-up is opened\n Tha name filter was set\n The first column was selected\n The second column was selected\n The third column was selected\n The fourth column was selected\n The fifth column was selected\n The sixth column was selected\n The seventh column was selected\n The eight column was selected\n The ninth column was selected\n The eleventh column was selected\n The eleventh column was selected\n The filter was created:\n First column name\n Second column name\n Third column name\n Fourth column name\n Fifth column name\n Sixth column name\n Seventh column name\n Eighth column name\n Ninth  column name\n Tenth  column name\n Eleventh  column name"
                            worksheet.write_comment(row, col, create_filter_trading_account_module,
                                                    {'width': 250, 'height': 400})

                        elif "Test searching lead modules is failed" in data:
                            worksheet.write(row, col, data, cell_format_fail)
                            searching_lead_modules = "Leads module was ope\n  Create leads module is opened\n First name was set\n last name was set\n Mobile was set: 8888888\n fax was set: 5555\n The first name was set\n The secondary email was set\n The language  was set\n The street name was set\n The postal code was set\n The country was set\n The description was set\n The phone number was set\n The tittle was set\n The lead source was set\n The lead status was set\n The lead status was set\n The source name was set\n Brand select box was not found\n The po box was set\n The city was set\n The state was set\n Perform scroll up\n The save button was clicked\n The lead was created\n The page is refreshed\n The client module was opened\n Leads module was opened\n Click the  drop down filter\n The field found is : Test Leads\n Click the selected filter\n The first name was entered\n The last name was entered\n The email was entered\n The search button was clicked"
                            worksheet.write_comment(row, col, searching_lead_modules,
                                                    {'width': 250, 'height': 500})

                        elif "Test create lead is failed" in data:
                            worksheet.write(row, col, data, cell_format_fail)
                            create_lead = "Create leads module is opened\n First name was set \n last name was set \n Mobile was set\n fax was set \n The first name was set\n The secondary email was set \n The language  was set \n The street name was set\n The postal code was set\n The country was set\n The description was set\n The phone number was set\n The tittle was set: tittle test\n The lead source was set\n The lead status was set\n The lead status was set\n The source name was set\n Brand select box\n The po box was set\n The city was set\n The state was set\n Perform scroll up \n The save button was clicked\n The lead was created\n Verifying lead data\n Returns the first name\n Returns the last_name\n Returns the mobile text\n Returns the fax text\n Returns the email text\n Returns the secondary email\n Returns the source name\n Returns the panda partner\n Returns the referral text\n Returns the street text\n Returns the postal code\n Returns the postal code\n Returns the description text\n Returns the lead status text\n Returns the language text\n Returns the language text\n Returns the language text"
                            worksheet.write_comment(row, col, create_lead,
                                                    {'width': 250, 'height': 500})

                        elif "Test edit lead is failed" in data:
                            worksheet.write(row, col, data, cell_format_fail)
                            edit_lead = "Leads module was opened\n Create leads module is open\n  First name was set\n last name was set\n Mobile was set\n fax was set\n The first name was set\n The secondary email was set\n The language  was set\n The street name was set\n The postal code was set\n The country was set\n The description was set\n The phone number was set\n The tittle was set\n The lead source was set\n The lead status was set\n The lead status was set\n The source name was set\n Brand select box was not found\n The po box was set: po box text\n The city was set\n The state was set\n Perform scroll up \n The save button was clicked:\n The lead was created:\n Verifying lead data\n Returns the first name\n Returns the last name\n Returns the mobile text\n Returns the fax text\n Returns the email text\n Returns the secondary email\n Returns the source name\n Returns the panda partner\n Returns the referral text\n Returns the street text\n Returns the postal code\n Returns the postal code\n Returns the description text\n Returns the description text\n Returns the description text\n Returns the description text\n Returns the lead status text\n Returns the language text\n Returns the language text\n Returns the language text:\n The delete pop-up is displayed\n First name was set\n last name was set\n Mobile was set\n fax was set\n The first email was set\n The secondary email was set\n The language  was set\n The panda partner id was set\n The referral was set\n The street name was set\n The postal code was set\n The country was set\n The description was set\n The phone number was set\n The tittle was set\n The lead source was set\n The lead status was set\n The assign to was set\n The source name was set\n The po box was set\n The city was set\n The state was set\n Perform scroll up\n The save button was clicked:\n Verifying lead data\n Returns the first name\n Returns the last_name\n Returns the mobile text\n Returns the fax text\n Returns the email text\n Returns the secondary email\n Returns the source name\n Returns the panda partner\n Returns the referral text\n Returns the street text\n Returns the postal code\n Returns the postal code\n Returns the description text\n Returns the lead status text \n Returns the language text"
                            worksheet.write_comment(row, col, edit_lead,
                                                    {'width': 250, 'height': 500})

                        elif "Test convert lead is failed" in data:
                            worksheet.write(row, col, data, cell_format_fail)
                            convert_lead = "Leads module was open\n  Create leads module is opened\n First name was set\n last name was set\n Mobile was set\n fax was set\n The first name was set\n The secondary email was set\n The language  was set\n The street name was set\n The postal code was set\n The country was set\n The description was set\n The phone number was set\n The tittle was set\n The lead source was set\n The lead status was set\n The lead status was set\n The source name was set\n Brand select box was not found\n The po box was set: po box text\n The city was set: Berlin\n The state was set:\n Perform scroll up\n The save button was clicked:\n The lead was created:\n Side bar is not present\n The convert lead module was opened\n First name was set\n last name was set\n The email was set\n The phone number was set\n Birthday input\n Citizenship input\n The address was set\n The postal code was set\n The city was set\n The country was set\n The password was set\n The currency was set\n Source input was not found\n The phone area code was set\n Click submit\n Lead convert message was not picked up\n Returns the exists text"
                            worksheet.write_comment(row, col, convert_lead,
                                                    {'width': 250, 'height': 500})

                        elif "Test searching client is failed" in data:
                            worksheet.write(row, col, data, cell_format_fail)
                            searching_client = "Click the  drop down fi\n  The field found is : Test Clients\n Click the selected filter\n The client status was selected \n Email was entered \n The country was entered \n The search button was clicked\n Perform scroll up\n Perform scroll up\n Click user name by email\n Returns the first name\n Returns the last name\n Returns the email"
                            worksheet.write_comment(row, col, searching_client,
                                                    {'width': 250, 'height': 300})

                        elif "Test add interaction is failed" in data:
                            worksheet.write(row, col, data, cell_format_fail)
                            add_interaction = "Click the  drop down fil\n The field found is : Test Clients\n Click the selected filter\n The client status was selected\n Email was entered\n The country was entered\n The search button was clicked\n Perform scroll up\n Perform scroll up\n Click user name by email\n Side bar is not present\n The event module was opened\n The event status is set Not Started\n The event type is set Meeting\n The duration  is set 30M\n The time is set \n The date is set\n The  assign to is set pandaqa pandaqa\n The priority is set Medium\n The comments is set Event Description\n The subject is set to Test interaction:\n Click the 'save' button\n Returns a confirmation message: Interraction successfully created\n The Ok button was clicked\n Click 'ok' button"
                            worksheet.write_comment(row, col, add_interaction,
                                                    {'width': 250, 'height': 400})

                        elif "Test interaction search is failed" in data:
                            worksheet.write(row, col, data, cell_format_fail)
                            interaction_search = "Task module is o\n  The all tab was opened\n The subject was set: Meeting\n Results found text:\n Got search results"
                            worksheet.write_comment(row, col, interaction_search,
                                                    {'width': 250, 'height': 400})

                        elif "Test add event is failed" in data:
                            worksheet.write(row, col, data, cell_format_fail)
                            add_event = "Task module is opened\n The event  module was op\n  The event status was set In Progress\n The event type is set Meeting\n The date  was set\n The time  was set\n The duration  was set 30M\n The priority was set Medium\n The  assign to was set pandaqa pandaqa\n The account was set\n The subject was set \n The comments was set Description Add Event\n Click the 'save' button\n The all tab was opened\n The all tab was opened and check event"
                            worksheet.write_comment(row, col, add_event,
                                                    {'width': 250, 'height': 400})

                        elif "Test edit event is failed" in data:
                            worksheet.write(row, col, data, cell_format_fail)
                            edit_event = "Task module is opened\n The all tab was opened\n Edit popup was opened\n The event status was set Planned\n The event type is set Call\n The date  is set\n The time  is set\n The duration  is set 15M\n The priority is set High\n The assign to is set Default User\n The subject is set Testing28246\n The comments is set Description Add Event\n Click the 'save' button\n Text from 'Update' popup has been got: Task was updated"
                            worksheet.write_comment(row, col, edit_event,
                                                    {'width': 250, 'height': 400})

                        elif "Test open trading account is failed" in data:
                            worksheet.write(row, col, data, cell_format_fail)
                            open_trading_account = "Click the  drop down filter\n The field found is : Test Clients\n Click the selected filter\n Setting  the user's email in the email field\n Click the search button\n Click user email\n Open mt4 actions\n Trading account server was selected: demo\n Trading account currency was selected: USD\n Trading account group was selected: demoSOA-FIX_USD (USD)\n Trading account leverage was selected: 1 : 100\n The Save button was clicked\n Returns a confirmation message: New User Account was created successfully"
                            worksheet.write_comment(row, col, open_trading_account,
                                                    {'width': 250, 'height': 400})

                        elif "Test check client password crm is failed" in data:
                            worksheet.write(row, col, data, cell_format_fail)
                            check_client_password = "Click the  drop down filter\n  The field found is   Test Clients\n Click the selected filter\n Setting  the user's email in the email field\n Click the search button\n Click user email\n Perform scroll up\n Open mt actions\n The password to check is set to \n The Check button was clicked\n Returns a confirmation message  The password that was entered is correct\n The Ok button was clicked\n Click 'ok' button"
                            worksheet.write_comment(row, col, check_client_password,
                                                    {'width': 250, 'height': 400})

                        elif "Test check mt4 password crm is failed" in data:
                            worksheet.write(row, col, data, cell_format_fail)
                            check_mt4_password = "Click the  drop down fil\n  The field found is   Test Clients\n Click the selected filter\n Setting  the user's email\n Click the search button\n Click user email\n Perform scroll down\n Open the trading account tab\n Perform scroll into view of the element\n Returns theient_account  text\n Perform scroll up\n Open mt actions\n Returns a confirmation message  Password was change successfully\n The Ok button was clicked\n Click 'ok' button"
                            worksheet.write_comment(row, col, check_mt4_password,
                                                    {'width': 250, 'height': 400})

                        elif "Test change client password crm is failed" in data:
                            worksheet.write(row, col, data, cell_format_fail)
                            change_client_password = "Click the  drop down fil\n  The field found is   Test Clients\n Click the selected filter\n Setting  the user's email in the email field\n Click the search button\n Click user email\n Side bar is not present\n The check client module was opened\n The new password is set to\n The Change button was clicked\n Returns a confirmation message  Password changed succesfully\n The Ok button was clicked\n Click 'ok' button"
                            worksheet.write_comment(row, col, change_client_password,
                                                    {'width': 250, 'height': 400})

                        elif "Test change mt4 password is failed" in data:
                            worksheet.write(row, col, data, cell_format_fail)
                            change_mt4_password = "Click the  drop down filter\n The field found is   Test Clients\n Click the selected filter\n Setting  the user's email in the email field\n Click the search button\n Click user email\n Perform scroll down \n Open the trading account tab \n Perform scroll into view of the element\n Returns the client account  text\n Perform scroll up\n Open mt actions \n Returns a confirmation message  Password was change successfully\n The Ok button was clicked\n Click 'ok' button \n The page is refreshed\n Open mt actions\n Returns a confirmation message  The password that was entered is correct\n The Ok button was clicked \n Click 'ok' button\n The page is refreshed\n Open mt actions \n Returns a confirmation message  Password was change successfully\n The Ok button was clicked\n Click 'ok' butto"
                            worksheet.write_comment(row, col, change_mt4_password,
                                                    {'width': 250, 'height': 400})


                        elif "Test create deposit is failed" in data:
                            worksheet.write(row, col, data, cell_format_fail)
                            create_deposit = "The client module was open\n  Click the  drop down filter\n The field found is   Test Clients\n Click the selected filter\n Setting  the user's email in the email field\n Click the search button\n Click user email \n ClientProfilePage   Open mt actions\n Trading account server was selected  real\n Trading account currency was selected  USD\n Trading account group was selected\n Trading account leverage was selected\n The Save button was clicked\n The close button was clicked\n Click 'close' button \n Perform scroll down \n Open the trading account tab\n Perform scroll into view of the element\n Returns the client_account  text \n Perform scroll up \n The payment method of deposit module was selected  Credit card\n The account of deposit module was selected\n The amount of deposit module was set\n The  description of deposit module was set in the description field   Description Deposit\n The create withdraw button of deposit module was clicked\n Returns a confirmation message  Transaction created successfully\n The Ok button was clicked\n Click 'ok' button\n The page is refreshed\n Open the trading account tab\n Returns the amount you placed on the deposit page"
                            worksheet.write_comment(row, col, create_deposit,
                                                    {'width': 250, 'height': 500})

                        elif "Test create deposit for client is failed" in data:
                            worksheet.write(row, col, data, cell_format_fail)
                            create_deposit_for_client = "Click the  drop down filt\n  The field found is   Test Clients\n Click the selected filter\n Setting  the users email in the email field  is\n Click the search button \n Click user email\n Perform scroll down \n Open the trading account tab\n Perform scroll into view of the element\n Returns the client_account  text \n Return initial amount text\n Perform scroll up \n Deposit for client popup was opened\n There is no accounts drop down list\n Click OK in Client Deposit pop"
                            worksheet.write_comment(row, col, create_deposit_for_client,
                                                    {'width': 250, 'height': 400})

                        elif "Test make credit in is failed" in data:
                            worksheet.write(row, col, data, cell_format_fail)
                            create_credit_in = "The client module was opened\n Click the  drop down filter \n The field found is   Test Clients\n Click the selected filter\n Setting  the user's email in the email field\n Click the search button \n Click user email\n Open mt actions\n Trading account server was selected  real\n Trading account currency was selected  USD\n Trading account group was selected  HFX_DIAMOND_USD (USD)\n Trading account leverage was selected \n The Save button was clicked\n The close button was clicked \n Click 'close' button \n Perfor scroll down\n Open the trading account tab \n Perform scroll into view of the element\n Returns the client_account  text \n Perform scroll up\n The account of deposit in module was selected\n The amount of credit in module was set\n The expire date of credit in module was set\n The  description of credit in module was set in the description field   Credit in\n The create withdraw button of deposit module was clicked\n The Ok button was clicked \n Click 'ok' button \n The page is refreshed\n The page is refreshed\n he page is refreshed\n Perform scroll down \n Returns the amount you placed on the credit_in page"
                            worksheet.write_comment(row, col, create_credit_in,
                                                    {'width': 250, 'height': 450})

                        elif "Test edit trading account in is failed" in data:
                            worksheet.write(row, col, data, cell_format_fail)
                            edit_trading_account = "Click the  drop down filter\n The field found is   Test Clients\n Click the selected filter\n Setting  the user's email in the email field\n Click the search button \n Click user email \n Open mt actions \n Trading account server was selected  demo\n Trading account currency was selected  USD\n Trading account group was selected \n Trading account leverage was selected\n The Save button was clicked\n The close button was clicked\n Click 'close' button \n The page is refreshed\n The page is refreshed\n Open mt actions\n Trading account server was selected   (demo)   USD\n Trading account group was selected \n Trading account leverage was selected\n The Save button was clicked\n Returns a confirmation message  User successfully update"
                            worksheet.write_comment(row, col, edit_trading_account,
                                                    {'width': 250, 'height': 400})

                        elif "Test create affiliate is failed" in data:
                            worksheet.write(row, col, data, cell_format_fail)
                            create_affiliate = "Affiliates page was o\n  Open 'Add new affiliate' popup\n Enter partner name\n Enter allowed IP\n Click plus ip\n Select allowed methods Create lead\n Select blocked country Albania\n Click Submit\n Text from 'Update' popup has been got  Success\n The page is refreshed\n Search partner name and go to affiliate details page\n Affiliate details page"
                            worksheet.write_comment(row, col, create_affiliate,
                                                    {'width': 250, 'height': 400})

                        elif "Test create task in calendar view is failed" in data:
                            worksheet.write(row, col, data, cell_format_fail)
                            create_task = "Go to Task module\n Go to Calendar View\n Click Add Event\n Set 'Status' to 'In Progress'\n Set 'Event Type' to 'Meeting'\n Set 'Date'\n Set 'Time'\n Set 'Duration' to M\n Set 'Priority' to Medium\n Set 'Assign to' to pandaqa pandaqa\n Set 'Account Name'\n Set 'Subject'\n Set 'Comment'\n Click 'Save'\n Task was created' message is shown\n Verify subject is correct"
                            worksheet.write_comment(row, col, create_task,
                                                    {'width': 250, 'height': 400})

                        elif "Test check day tab is failed" in data:
                            worksheet.write(row, col, data, cell_format_fail)
                            day_tab = "Go to Task module\n  Go to Calendar View\n Go to 'Day' tab\n Verify date is correct"
                            worksheet.write_comment(row, col, day_tab,
                                                    {'width': 250, 'height': 200})

                        elif "Test check week tab is failed" in data:
                            worksheet.write(row, col, data, cell_format_fail)
                            week_tab = "Go to Task module\n Go to Calendar View\n Go to 'Week' tab"
                            worksheet.write_comment(row, col, week_tab,
                                                    {'width': 250, 'height': 200})

                        elif "Test check month tab is failed" in data:
                            worksheet.write(row, col, data, cell_format_fail)
                            month_tab = "Go to Task module\n Go to Calendar View\n  Go to 'Month' tab\n Verify first column is 'Sun'\n Verify second column is 'Mon'\n Verify third column is 'Tue'\n Verify fourth column is 'Wed'\n Verify fifth column is 'Thu'\n Verify sixth column is 'Fri'\n Verify seventh column is 'Sat'"
                            worksheet.write_comment(row, col, month_tab,
                                                    {'width': 250, 'height': 200})


                        elif "Test check all tab FT is failed" in data:
                            worksheet.write(row, col, data, cell_format_fail)
                            check_all_tab_FT = "The financial_transactions_module was selected\n Returns the tab name All\n Returns the tab name Credit In\n Returns the tab name Credit Out\n Returns the tab name Demo Accounts Transactions\n Returns the tab name Deposits\n Returns the tab name Withdraw"
                            worksheet.write_comment(row, col, check_all_tab_FT,
                                                    {'width': 250, 'height': 200})

                        elif "Test check search by column FT is failed" in data:
                            worksheet.write(row, col, data, cell_format_fail)
                            by_column_FT = "The financial transactions module was selected \n In filter the transaction number was entered \n In filter the client name was entered \n In filter the transaction_type was entered \n In filter the modified_time was entered \n The search button was clicked \n Perform scroll into view of the element \n First financial transaction in search results was opened\n Returns the transaction number"
                            worksheet.write_comment(row, col, by_column_FT,
                                                    {'width': 250, 'height': 200})

                        elif "Test check search via button FT is failed" in data:
                            worksheet.write(row, col, data, cell_format_fail)
                            via_button_FT = "The financial transactions module was selected\n Search form was opened\n Searching for transaction ID:\n Searching for client name\n Searching for transaction type\n Searching for modified time\n looking for created/modified time\n Time from the page list\n Correct time has been found\n Searching for trading account"
                            worksheet.write_comment(row, col, via_button_FT,
                                                    {'width': 250, 'height': 200})


                        elif "Create client filter" in data:
                            worksheet.write(row, 0, data, cell_format_name_test)

                        elif "Create documents filter" in data:
                            worksheet.write(row, 0, data, cell_format_name_test)

                        elif "Create lead filter" in data:
                            worksheet.write(row, 0, data, cell_format_name_test)

                        elif "Create help desk filter" in data:
                            worksheet.write(row, 0, data, cell_format_name_test)

                        elif "Create trading account filter" in data:
                            worksheet.write(row, 0, data, cell_format_name_test)

                        elif "Searching lead modules" in data:
                            worksheet.write(row, 0, data, cell_format_name_test)

                        elif "Create lead" in data:
                            worksheet.write(row, 0, data, cell_format_name_test)

                        elif "Edit lead" in data:
                            worksheet.write(row, 0, data, cell_format_name_test)

                        elif "Convert lead" in data:
                            worksheet.write(row, 0, data, cell_format_name_test)

                        elif "Searching client" in data:
                            worksheet.write(row, 0, data, cell_format_name_test)

                        elif "Add interaction" in data:
                            worksheet.write(row, 0, data, cell_format_name_test)

                        elif "Interaction search" in data:
                            worksheet.write(row, 0, data, cell_format_name_test)

                        elif "Add event" in data:
                            worksheet.write(row, 0, data, cell_format_name_test)

                        elif "Edit event" in data:
                            worksheet.write(row, 0, data, cell_format_name_test)

                        elif "Open trading account" in data:
                            worksheet.write(row, 0, data, cell_format_name_test)

                        elif "Check client password crm" in data:
                            worksheet.write(row, 0, data, cell_format_name_test)

                        elif "Check mt password crm" in data:
                            worksheet.write(row, 0, data, cell_format_name_test)

                        elif "Change client password crm" in data:
                            worksheet.write(row, 0, data, cell_format_name_test)

                        elif "Change mt password"  in data:
                            worksheet.write(row, 0, data, cell_format_name_test)

                        elif "Create deposit" in data:
                            worksheet.write(row, 0, data, cell_format_name_test)

                        elif "Create deposit for client" in data:
                            worksheet.write(row, 0, data, cell_format_name_test)

                        elif "Make credit in" in data:
                            worksheet.write(row, 0, data, cell_format_name_test)

                        elif "Edit trading account"  in data:
                            worksheet.write(row, 0, data, cell_format_name_test)

                        elif "Create affiliate"  in data:
                            worksheet.write(row, 0, data, cell_format_name_test)

                        elif "Create task in calendar view" in data:
                            worksheet.write(row, 0, data, cell_format_name_test)

                        elif "Check day tab"  in data:
                            worksheet.write(row, 0, data, cell_format_name_test)

                        elif "Check month tab"  in data:
                            worksheet.write(row, 0, data, cell_format_name_test)

                        elif "Check week tab"  in data:
                            worksheet.write(row, 0, data, cell_format_name_test)

                        elif "Check all tab FT" in data:
                            worksheet.write(row, 0, data, cell_format_name_test)

                        elif "Check search by column FT" in data:
                            worksheet.write(row, 0, data, cell_format_name_test)

                        elif "Check search via button FT" in data:
                            worksheet.write(row, 0, data, cell_format_name_test)


                        else:
                            worksheet.write(row, col, data, cell_format_pass)

                        row += 1


            col += 1

        workbook.close()

        # Send_Email_XLS(filepath)

    @staticmethod
    def get_test_pretty_name(test):
        return test['class'] + '.' + test['method']

    @staticmethod
    def get_test_pretty_name_new(test):
        return test['class'] + ': ' + test['method'].replace('_', ' ')

