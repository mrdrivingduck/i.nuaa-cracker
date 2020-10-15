
from browser_operator import report_leave_school
from browser_operator import health_clockin
from util import getuserinfo
from util import sendemail
from util import merge_default_config


def single_person_action(config):
    config = merge_default_config(config)
    email = config['email']
    flag = True
    if config is None:
        print("Configuration error.")
        exit(0)
    else:
        print(config)
    try:
        health_clockin(config, 5)
        report_leave_school(config, timeout=8)
    except Exception as message:
        flag = False
        sendemail(email, repr(message))
    body = '<h1>您已打卡成功</h1><p>感谢使用</p>'
    if flag is True:
        sendemail(email, body)


if __name__ == '__main__':
    config = getuserinfo("config/freedom.json")
    for person in config:
        single_person_action(person)
