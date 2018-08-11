

class MailGenerate():

    def generateMailBody(self, statusReport):
        print(type(statusReport))
        statusReport = dict(statusReport)
        headers = statusReport.keys()
        values = statusReport.values()
        print(headers)
        print(values)
        commonContent = """<!DOCTYPE html>
<html>
<head>
<style>
table {
    font-family: arial, sans-serif;
    border-collapse: collapse;
    width: 100%;
}

td, th {
    border: 1px solid #dddddd;
    text-align: left;
    padding: 8px;
}

tr:nth-child(even) {
    background-color: #dddddd;
}
</style>
</head>
<body>

<center><h2>Daily Status Report</h2></center>
"""
        commonContent += "<table><tr>"
        for header in headers:
            commonContent += "<th>"+str(header)+"</th>"
        commonContent += "</tr><tr>"
        for value in values:
            commonContent += "<td>"+str(value)+"</td>"

        finalBody = commonContent+"</tr></table>"
        print(finalBody)
        return  finalBody
