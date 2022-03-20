import yagmail

yag = yagmail.SMTP("mail...", "password..")

reciver = "mail.."
subject = "financial data"
body = "This is a message!"
attach = yagmail.inline("..\my_finance\stock\diagram")

yag.send(to=reciver, subject=subject, content=[body, attach])