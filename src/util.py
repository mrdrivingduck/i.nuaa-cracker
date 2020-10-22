import json
import random
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# 读取用户的配置文件 (JSON 格式)
def get_user_config(path):
    with open(path, "r", encoding="utf-8") as file:
        config = json.loads(file.read())
    return config


# 将用户自定义的配置文件与默认的配置文件合并
def merge_default_config(config):
    reason_pool = ['吃饭', '去超市', '干洗店取衣服', '买杯咖啡', '打球']

    default = {
        # username (needed)
        # password (needed)
        # email (needed)
        # assistant (optional)
        # supervisor (optional)

        # default: today + 2
        "date": (datetime.date.today() + datetime.timedelta(days=2)).strftime("%Y-%m-%d"),
        "reason": reason_pool[random.randint(0, len(reason_pool) - 1)],
        "campus": "将军路校区",
        "driver": "Chrome"
    }

    necessary_list = ["username", "password", "email"]
    optional_list = ["assistant", "supervisor",
                     "date", "reason", "campus", "driver"]

    # error if necessary parameter is missing
    for key in necessary_list:
        if key not in config:
            print("Necessary parameter '%s' is missing." % key)
            return None
        default[key] = config[key]

    # override default parameter
    for key in optional_list:
        if key in config:
            default[key] = config[key]

    return default


def build_mail_content(content, failed):
    result = '<h1>i.NUAA-cracker Notification</h1>'
    if failed is True:
        result += '<h3>Operation Failed!</h3>'\
                  + '<p>Check the reason and report to <a href="mailto:mrdrivingduck@gmail.com">us</a></p>'\
                  + '<p>' + content + '</p>'
    else:
        result += '<h3>Operation Success!</h3>' + '<p>' + content + '</p>'
    # print(result)
    result += '<p>Completed at: ' + datetime.datetime.now().strftime("%a %b %d %H:%M:%S %Y") + '</p>'
    return result


# 在发送成功后向用户发送通知邮件
def send_email(receiver, message):
    host = 'smtp.163.com'
    port = 465
    sender = 'i.NUAA-crack-bot <auto_clockin_mail@163.com>'
    l_sender = 'auto_clockin_mail@163.com'
    pwd = 'PZCVFQNUMFNKCIKV'

    to_receiver = [receiver, sender]
    # cc_receiver = [sender]
    receiver = to_receiver
    msg = MIMEMultipart()
    msg.attach(MIMEText(message, 'html', 'utf-8'))
    msg['subject'] = 'i.NUAA-cracker Notification'
    msg['from'] = sender
    msg['to'] = ";".join(to_receiver)
    # msg['Cc'] = ";".join(cc_receiver)

    try:
        s = smtplib.SMTP_SSL(host)
        s.connect(host='smtp.163.com', port=port)
        s.login('auto_clockin_mail@163.com', pwd)
        s.sendmail(l_sender, receiver, msg.as_string())
        print('Done. Send email success.')
    except smtplib.SMTPException as e:
        print('Error. Send email failed.')
        print('Error info: ' + repr(e))
