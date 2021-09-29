# xujuan
#coding: UTF-8
import smtplib
from email.header import Header
from email.mime.text import MIMEText
msg_from='2100974138@qq.com'
passwd='delrmlbrgkoqcahd'
msg_to='57820042@qq.com'
subject="2019144144 徐娟"
content="校园网：10.128.66.75 ,ip.cn查询 39.129.40.50 ； 本机：10.171.21.150, ip.cn查询 172.69.35.47"
msg=MIMEText(content)
msg['Subject']=subject
msg['From']=msg_from
msg['To']=msg_to
try:
	s=smtplib.SMTP_SSL("smtp.qq.com",465)
	s.login(msg_from,passwd)
	s.sendmail(msg_from,msg_to,msg.as_string())
	print("发送成功")
except Exception as e:
	print("发送失败",e)
finally:
 s.quit()
