
import datetime

class StatusContentValidator() :

    def validateTopicAndContent(self, topicOrContent):
        if topicOrContent == "":
            return True
        else:
            return False

    def startDateEndDateValidator(self, startDateOrEndDate):
        if startDateOrEndDate == "":
            print("Start Date or End Date Cant be empty...")
            return True
        else:
            return False

    def compareDate(self, startDateEndDate):
        todaysDate = datetime.datetime.strptime(datetime.datetime.today().strftime('%d/%m/%Y'), '%d/%m/%Y')
        if startDateEndDate > todaysDate:
            print("Future Date Is not allowed")
            return True
        else:
            return False

    def progressValidator(self, progress):
        progress = str(progress)
        if(progress != ""):
            progress = int(progress)
            while progress != 1 and progress != 2:
                print("Slect either 1 or 2")
                return "Please Enter Valid Input"
            if progress == 1:
                return "In Progress"
            elif progress == 2:
                return "Completed"
            else:
                return "Something Went Wrong"
        while progress == "":
            print("Progress cant be empty \n")
            return "Progress cant be empty"

    def validateConfidenceLevel(self , confidenceLevel):
        confidenceLevel = int(confidenceLevel)
        while confidenceLevel != 1 and confidenceLevel != 2 and confidenceLevel !=3:
            print("Slect either 1, 2 or 3")
            return "Please Enter Valid Input"
        if confidenceLevel == 1:
            return "High"
        elif confidenceLevel == 2:
            return "Medium"
        elif(confidenceLevel == 3):
            return "Low"
        else:
            print("Something Went Wrong")
        while confidenceLevel == "":
            print("Confidence Level cant be empty \n")
            return "Confidence cant be empty"

    def validateTeamMember(self, teamMember):
        if teamMember == "":
            print("Team Member Name cant be empty \n")
            return True
        else:
            return False

    def validateComments(self, comments):
        if comments == "":
            print("Comments cant be empty \n")
            return True
        else:
            return False




