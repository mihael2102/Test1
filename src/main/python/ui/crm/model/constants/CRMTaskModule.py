import random


class CRMTaskModuleConstants(object):
    DESCRIPTION_SEND_SMS = "Hello from task module"
    MESSAGE_TASK_WAS_UPDATED = "Task was updated"
    MESSAGE_TASK_WERE_UPDATED = "Tasks were updated"
    MESSAGE_TASK_WAS_DELETED = "Tasks were deleted"
    TASK_MODULE = "TasksModule"
    FIRST_TAB = "first_tab"
    SECOND_TAB = "second_tab"
    THIRD_TAB = "third_tab"
    FOURTH_TAB = "fourth_tab"
    FIFTH_TAB = "fifth_tab"
    FIRST_DURATION = "30M"
    SECOND_DURATION = "15M"
    THIRD_DURATION = "45M"
    FIRST_EVENT_TYPE = "Meeting"
    SECOND_EVENT_TYPE = "Call"
    THIRD_EVENT_TYPE = "Task"
    FIRST_EVENT_STATUS = "In Progress"
    SECOND_EVENT_STATUS = "Planned"
    THIRD_EVENT_STATUS = "Deferred"
    FIRST_ASSIGN_TO = "Default User"
    SECOND_ASSIGN_TO = "pandaqa pandaqa"
    THIRD_ASSIGN_TO = "testuser"
    FIRST_ACCOUNT_NAME = "alena"
    SECOND_ACCOUNT_NAME = "evgen"
    THIRD_ACCOUNT_NAME = "dima"
    FIRST_SUBJECT = "QATest1" + str(random.randrange(1, 10000))
    SECOND_SUBJECT = "ATest1" + str(random.randrange(1, 10000))
    THIRD_SUBJECT = "WTest1" + str(random.randrange(1, 10000))
    FIRST_PRIORITY = "Medium"
    SECOND_PRIORITY = "High"
    THIRD_PRIORITY = "Low"
    DESCRIPTION_ADD_EVENT = "Description Add Event"
    MESSAGE_CREATE_EVENT = "Task was created"
    MESSAGE_SMS_SUCCESSFULLY = "Sending SMS to 3 phone numbers from 3 persons"
    SECOND_MESSAGE_SMS_SUCCESSFULLY = "Sending SMS to Alena TestQA"
    SUNDAY = "Sun"
    MONDAY = "Mon"
    TUESDAY = "Tue"
    WEDNESDAY = "Wed"
    THURSDAY = "Thu"
    FRIDAY = "Fri"
    SATURDAY = "Sat"
    FIRST_CALL_OUTCOME = "first_call_outcome"
    SECOND_CALL_OUTCOME = "second_call_outcome"
    FIRST_POSITIVE_OUTCOME = "first_call_outcome"
    SECOND_POSITIVE_OUTCOME = "second_positive_outcome"
    THIRD_CALL_OUTCOME = "third_positive_outcome"
    FIRST_NEGATIVE_OUTCOME = "first_negative_outcome"
    SECOND_NEGATIVE_OUTCOME = "second_negative_outcome"
    THIRD_NEGATIVE_OUTCOME = "third_negative_outcome"
    FOURTH_NEGATIVE_OUTCOME = "third_negative_outcome"
    COMMENTS_CALL_PHONE = "test call phone"
