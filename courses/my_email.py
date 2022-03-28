import smtplib

server = smtplib.SMTP(host="localhost", port=7777)

message = """
A

message

on multiple lines!
"""

server.sendmail(
    from_addr="kameran@localhost.com",
    to_addrs=["kameranhajabdo1@gmail.com"],
    msg=message,
)