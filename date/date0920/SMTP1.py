#coding=utf-8
from email.mime.text import MIMEText
mag=MIMEText('这是测试邮件','plain','utf-8')
from_addr=raw_input('From:')
password=raw_input('Password:')
smtp_server=raw_input('STMP server:')
to_addr=raw_input('To:')
import smtplib
server=smtplib.SMTP(smtp_server,465)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()
