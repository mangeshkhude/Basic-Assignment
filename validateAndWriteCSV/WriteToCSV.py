from configuration import Configuration
from validateAndWriteCSV import ValidateCSVFile

class WriteToCSV():

    def writeToFile(self, userInputs):
        statusReport = open('dailyStatusReport.csv', 'a')
        statusReportHeader = userInputs.keys()
        statusReportValues = userInputs.values()
        if ValidateCSVFile.ValidateCSVFile().isCSVFileEmpty():
            for header in statusReportHeader:
                statusReport.writelines('%s,' % header)
            statusReport.write('\n')
            print("Writing Completed...")
            for value in statusReportValues:
                statusReport.writelines('%s,' % value)
        elif not ValidateCSVFile.ValidateCSVFile().isCSVFileEmpty():
            for content in statusReportValues:
                statusReport.writelines('%s,' % content)
            statusReport.write('\n')
        statusReport.close()
