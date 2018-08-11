
class ValidateCSVFile():
    def isCSVFileEmpty(self):
        statusReport = open('dailyStatusReport.csv', 'r')
        data = statusReport.read()
        if data == "":
            print(data)
            return True
        else:
            return False
