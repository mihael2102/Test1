class ParserDate(object):
    def __init__(self) -> None:
        super().__init__()

    def get_month_number(self, month):
        if month == "January":
            month = "01"
            return month
        if month == "February":
            month = "02"
            return month
        if month == "March":
            month = "03"
            return month
        if month == "April":
            month = "04"
            return month
        if month == "May":
            month = "05"
            return month
        if month == "June":
            month = "06"
            return month
        if month == "July":
            month = "07"
            return month
        if month == "August":
            month = "08"
            return month
        if month == "September":
            month = "09"
            return month
        if month == "October":
            month = "10"
            return month
        if month == "November":
            month = "11"
            return month
        if month == "December":
            month = "12"
            return month
