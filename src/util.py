
import json
import datetime
import random
import smtplib
from email.mime.text import MIMEText


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

        "date": (datetime.date.today() + datetime.timedelta(days=1)).strftime("%Y-%m-%d"),  # default: today + 1
        "reason": reason_pool[random.randint(0, len(reason_pool) - 1)],
        "campus": "将军路校区",
        # "assistant": "刘爽",
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


# 在发送成功后向用户发送通知邮件
def send_email(receiver, message):
    host = 'smtp.163.com'
    port = 465
    sender = 'auto_clockin_mail@163.com'
    pwd = 'LDEEKLCCPHAAIQJK'

    # body = '<h1>您已打卡成功</h1><p>感谢使用</p>'
    body = message
    msg = MIMEText(body, 'html')
    msg['subject'] = '打卡通知'
    msg['from'] = sender
    msg['to'] = receiver

    print(message)

    try:
        s = smtplib.SMTP_SSL(host)
        s.connect(host='smtp.163.com', port=port)
        s.login(sender, pwd)
        s.sendmail(sender, receiver, msg.as_string())
        print('Done. Send email success.')
    except smtplib.SMTPException as e:
        print('Error. Send email failed.')
        print('Error info: ' + e)
