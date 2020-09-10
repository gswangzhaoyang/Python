# @ProjectFile:pyStudy_2_mail.py
# @Discription:
# @Author:zy.w
# @Time:2020/9/7 9:39


import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
import re, time, os
import socket, socks


# 读取配置文件信息
def ReadSettingInformation():
    '''
    读取配置文件信息，将配置转换成dict格式，并返回
    :return:setting_dict
    '''
    setting_dict = {}
    with open(r'.\conf\setting.conf', 'r', encoding='utf-8') as f:
        detail = f.read()
        match = '([a-zA-Z_]+)=(\S+)\s*'
        info = re.findall(match, detail)
        for item in info:
            setting_dict[item[0]] = item[1]
            pass
        pass
    return setting_dict
    pass


# 读取收件人邮箱
def ReceiversList():
    '''
    读取收件人邮箱，将收件人转换为list，并返回
    :return: Receivers_list
    '''
    Receivers_df = pd.read_csv(r'.\conf\receivers.csv', encoding='utf-8')
    MReceivers_list = Receivers_df['M_ReceiversList'].values
    Receivers_list = [MReceivers_list]
    return Receivers_list
    pass


# 创建邮件
class create_mail():
    def __init__(self):
        '''
        初始化函数，
        self.email_src：邮件内容路径
        self.email_filename：邮件附件名称
        self.dateTime：当前日期及时间
        '''
        setting = ReadSettingInformation()
        self.email_src = setting["mail_src"]
        self.email_filename = setting["mail_filename"]
        self.dateTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        pass

    def title(self):
        '''
        邮件主题
        :return:
        '''
        title = '{} 的邮件'.format(self.dateTime)
        return title

    def content(self):
        '''
        邮件正文
        :return:
        '''
        with open(r'{}\{}'.format(self.email_src, self.email_filename), 'r', encoding='utf-8') as f:
            fcontent = f.read()
            pass
        content = """
        <p>{}</p>
        <p><img src="cid:io"></p>
        """.format(fcontent)
        return content
        # print(content)

    def image(self):
        '''
        邮件正文图片
        :return:
        '''
        image = r'.\conf\22.png'
        return image

    pass


# 插入图片函数，参数1：图片路径，参数2：图片id
def addimg(src, imgid):
    fp = open(src, 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    # 指定图片文件的Content-ID
    msgImage.add_header('Content-ID', imgid)
    return msgImage
    pass


# 构造自动发送邮件模块
def send_mail(title, content, image):
    # 读取用户信息
    setting = ReadSettingInformation()
    email_src = setting["mail_src"]
    email_filename = setting["mail_filename"]
    proxy = setting["proxy"]
    proxy_ip = setting["proxy_ip"]
    proxy_port = setting["proxy_port"]
    if proxy == 'on':
        socks.set_default_proxy(socks.HTTP, proxy_ip, proxy_port)
        socket.socket = socks.socksocket
        # print(proxy, proxy_ip, proxy_port)
        pass
    username = setting["mail_user"]
    password = setting["mail_passwd"]
    # 加载第三SMTP服务器设置
    SSL_Host = setting["smtp_server"]
    SSL_Port = setting["smtp_port"]
    # 加载收件人邮箱
    Mreceivers = ReceiversList()[0]

    # 创建MIMEMultipart对象，采用related定义内嵌资源的有简体
    msg = MIMEMultipart('related')
    msgtext = MIMEText(content, 'html', 'utf-8')
    msg.attach(msgtext)
    msg.attach(addimg(image, content[content.find('io'):content.find('io') + 2]))
    # 设置邮件附件
    file = r'{}\{}'.format(email_src, email_filename)
    part = MIMEApplication(open(file, 'rb').read())
    fname = os.path.split(file)[1]
    part.add_header('Content-Disposition', 'attachment', filename=fname)
    msg.attach(part)

    msg['Subject'] = title  # 主题
    msg['From'] = username  # 发件人
    msg['To'] = ','.join(Mreceivers)  # 收件人

    try:
        # 邮件服务器及端口号
        server = smtplib.SMTP_SSL(SSL_Host, SSL_Port)
        # 登录smtp服务器
        print('开始登录smtp服务器...')
        server.login(username, password)
        print('开始发送邮件...')
        # 发邮件  as_string()将MIMEText对象转换成str
        server.sendmail(username, Mreceivers, msg.as_string())
        print('发送成功')
        pass
    except:
        print('发送失败')
        pass
    pass


if __name__ == '__main__':
    qqmail = create_mail()
    title = qqmail.title()
    content = qqmail.content()
    image = qqmail.image()
    send_mail(title, content, image)
    pass
