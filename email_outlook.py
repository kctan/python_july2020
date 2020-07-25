import win32com.client


subject = 'From rp outlook'
body = '<html><body>' + 'test' + '</body></html>'
recipient = 'tkokchen@gmail.com'
attachments = ["D:\\Dropbox\\Modules\\PythonCET\\Past Runs\\Dec2019\\day2\\05. Email\\abc.txt"]

#Create and send email
olMailItem = 0x0
obj = win32com.client.Dispatch("Outlook.Application")
newMail = obj.CreateItem(olMailItem)
newMail.Subject = subject
newMail.HTMLBody = body
#newMail.Body = body
newMail.To = recipient

for location in attachments:
    newMail.Attachments.Add(Source=location)

#newMail.display()
newMail.Send()
