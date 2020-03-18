import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from  email.mime.multipart import MIMEMultipart

username = '1193723749@qq.com'
password = 'umeblcelhkajfjbi'
rec = '838214651@qq.com'
file = './test.mp4'
content = '多情自古空余恨'
title = 'this is test title'

class send_email():
    def __init__(self,username,password,rec,title,content,file=''):
        self.connect_server = smtplib.SMTP_SSL('smtp.qq.com',465)
        self.connect_server.login(username,password)
        self.username = username
        self.rec = rec
        self.title = title
        self.content = content
        self.file = file

    def send_msg(self):
        try:
            msg = MIMEText(self.content,'plain','utf-8')

            # form 可以是列表形式
            msg['From'] = username

            # 接受人
            msg['To'] = self.rec

            # subject: 邮件主题
            msg['Subject'] = self.title

            # 发送信息
            self.connect_server.sendmail(self.username,self.rec,msg.as_string())
            print('发送普通成功')
        except Exception as e:
            raise e
            print('发送普通失败')

    def send_file(self):
        try:

            msg = MIMEMultipart()
            if self.file:
            # 加附件
                file_read = open(self.file,'rb').read()
                file_msg = MIMEApplication(file_read)
                file_msg.add_header('content-disposition','attachment',filename=self.file.split('/')[-1])
                msg.attach(file_msg)

            # 加文本
            text_msg = MIMEText(self.content,'plain','utf-8')
            msg.attach(text_msg)

            msg['From'] = self.username
            msg['To'] = self.rec
            msg['Subject'] = self.title
            self.connect_server.send_message(msg,from_addr=self.username,to_addrs=self.rec)
            print('发送成功')
        except Exception as e:
            raise e
            print('发送失败')


if __name__ =='__main__':
    m = send_email(
        username,password,rec,title,content,file
    )
    m.send_msg()
    m.send_file()




