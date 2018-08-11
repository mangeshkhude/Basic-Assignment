
import datetime
from customValidatord import CustomValidator

class InputsFromUser():
    statusReport = {}

    def userInputs(self):
        todaysDate = datetime.datetime.strptime(datetime.datetime.today().strftime('%d/%m/%Y'), '%d/%m/%Y')
        print(todaysDate)
        while True:
            topic = input("Enter Topic :\n")[:255]
            self.statusReport['Topic'] = topic
            while CustomValidator.StatusContentValidator().validateTopicAndContent(topic):
                topic = input("Enter Topic : \n")[:255]
                self.statusReport['Topic'] = topic

            content = input("Enter Content : \n")[:255]
            self.statusReport['Content'] = content
            while CustomValidator.StatusContentValidator().validateTopicAndContent(content):
                print("Content cant be empty \n")
                content = input("Enter Content : \n")[:255]
                self.statusReport['Content'] = content

            enteredStartDate = input("Enter Start Date ('DD/MM/YYYY') : \n")
            while CustomValidator.StatusContentValidator.startDateEndDateValidator(self, enteredStartDate):
                enteredStartDate = input("Enter Start Date ('DD/MM/YYYY') : \n")
            formatedStartDate = datetime.datetime.strptime(enteredStartDate, "%d/%m/%Y")
            self.statusReport['Start Date'] = str(formatedStartDate.day)+"/"+str(formatedStartDate.month)+"/"+str(formatedStartDate.year)
            while CustomValidator.StatusContentValidator.compareDate(self, formatedStartDate):
                enteredStartDate = input("Enter Start Date ('DD/MM/YYYY') : \n")
                while CustomValidator.StatusContentValidator.startDateEndDateValidator(self, enteredStartDate):
                    enteredStartDate = input("Enter Start Date ('DD/MM/YYYY') : \n")
                formatedStartDate = datetime.datetime.strptime(enteredStartDate, "%d/%m/%Y")
                self.statusReport['Start Date'] = str(formatedStartDate.day)+"/"+str(formatedStartDate.month)+"/"+str(formatedStartDate.year)
                print(formatedStartDate)

            enteredEndDate = input("Enter End Date ('DD/MM/YYYY') : \n")
            while CustomValidator.StatusContentValidator.startDateEndDateValidator(self, enteredEndDate):
                enteredEndDate = input("Enter End Date ('DD/MM/YYYY') : \n")

            formatedEndDate = datetime.datetime.strptime(enteredEndDate, "%d/%m/%Y")
            self.statusReport['End Date'] = str(formatedEndDate.day) + "/" + str(formatedEndDate.month) + "/" + str(formatedEndDate.year)
            while CustomValidator.StatusContentValidator.compareDate(self, formatedEndDate):
                enteredEndDate = input("Enter End Date ('DD/MM/YYYY') : \n")
                while CustomValidator.StatusContentValidator.startDateEndDateValidator(self, enteredEndDate):
                    enteredEndDate = input("Enter End Date ('DD/MM/YYYY') : \n")
                formatedEndDate = datetime.datetime.strptime(enteredEndDate, "%d/%m/%Y")
                self.statusReport['End Date'] = str(formatedEndDate.day) + "/" + str(formatedEndDate.month) + "/" + str(formatedEndDate.year)
                print(formatedEndDate)

            progress = (input("Progress\n 1.In Progress\n 2.Completed :\n"))
            self.statusReport['Progress'] =CustomValidator.StatusContentValidator.progressValidator(self, progress)
            while self.statusReport['Progress'] == "Please Enter Valid Input":
                print(self.statusReport['Progress'])
                progress = int(input("Progress\n 1.In Progress\n 2.Completed : \n"))
                self.statusReport['Progress'] = CustomValidator.StatusContentValidator.progressValidator(self, progress)
                if self.statusReport['Progress'] == "Something Went Wrong":
                    break
            while self.statusReport['Progress'] == "Progress cant be empty":
                print(self.statusReport['Progress'])
                progress = (input("Progress\n 1.In Progress\n 2.Completed :\n"))
                self.statusReport['Progress'] = CustomValidator.StatusContentValidator.progressValidator(self, progress)
                if self.statusReport['Progress'] == "Something Went Wrong":
                    break

            confidenceLevel = int(input("Confidence Level :\n 1.High – Ready to work on deliverables \n 2.Medium – Understood but have some queries'\n 3.Low – No confidence \n"))
            self.statusReport['Confidence Level'] =CustomValidator.StatusContentValidator.validateConfidenceLevel(self, confidenceLevel)
            while self.statusReport['Confidence Level'] == "Please Enter Valid Input":
                print(self.statusReport['Confidence Level'])
                confidenceLevel = int(input("Confidence Level :\n 1.High – Ready to work on deliverables \n 2.Medium – Understood but have some queries'\n 3.Low – No confidence \n"))
                self.statusReport['Confidence Level'] = CustomValidator.StatusContentValidator.validateConfidenceLevel(self, confidenceLevel)

            while self.statusReport['Confidence Level'] == "Confidence cant be empty":
                print(self.statusReport['Confidence Level'])
                confidenceLevel = input("Progress\n 1.In Progress \n 2.Completed') : \n")
                self.statusReport['Confidence Level'] = CustomValidator.StatusContentValidator.validateConfidenceLevel(self, confidenceLevel)
                if self.statusReport['Confidence Level'] == "Something Went Wrong":
                    break

            teamMember = input("Enter Team Member Name : \n")[:100]
            self.statusReport['Team Member'] = teamMember
            while CustomValidator.StatusContentValidator.validateTeamMember(self, teamMember):
                teamMember = input("Enter Team Member Name : \n")
                self.statusReport['Team Member'] = teamMember

            comments = input("Enter Comments : \n")[:1024]
            self.statusReport['Comments'] = comments
            while CustomValidator.StatusContentValidator.validateComments(self, comments):
                comments = input("Enter Comments : \n")
                self.statusReport['Comments'] = comments

            anotherResponse = input("Want to submit another response : \n 1. Yes \n 2. No \n")
            if anotherResponse == "2":
                break
        print(self.statusReport)
        return self.statusReport