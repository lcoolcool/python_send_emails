#!/usr/bin/ python2
#coding: utf-8  
import smtplib  
from email.mime.text import MIMEText  
from email.header import Header  
from email.mime.multipart import MIMEMultipart
  
sender = '1111111@qq.com'
receiver = ['******@hust.edu.cn']
smtpserver = 'smtp.qq.com' 
username = '1111111@qq.com'
password = '******'
  
# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
#message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message = MIMEMultipart()
message['From'] = Header("chifeng111", 'utf-8')
message['To'] =  Header("测试", 'utf-8')

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

#邮件正文内容
message.attach(MIMEText('带附件Python 邮件发送测试……', 'plain', 'utf-8'))

# 构造附件1，传送'/home/chifeng111/图片'目录下的red.jpg文件
att1 = MIMEText(open('/home/chifeng111/图片/red.jpg', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="red.jpg"'
message.attach(att1)

try:
	smtp = smtplib.SMTP()  
	smtp.connect(smtpserver)
	smtp.login(username, password)  
	smtp.sendmail(sender, receiver, message.as_string())
	smtp.quit()
	print '邮件发送成功'
except smtplib.SMTPException:
	print 'error:无法发送邮件'
