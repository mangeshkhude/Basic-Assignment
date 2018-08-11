from validateAndWriteCSV import WriteToCSV
from dailyStatus import InputsFromUser
from mailReporting import MailReport

class DailyStatus():

    def dailyStatus(self):

        #User Entered Inputs
        getUserInputs = InputsFromUser.InputsFromUser().userInputs()
        WriteToCSV.WriteToCSV().writeToFile(getUserInputs)
        MailReport.Report_Mailer().send_mail(getUserInputs)

dailyStatus = DailyStatus()
dailyStatus.dailyStatus()