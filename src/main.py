
from browser_operation import report_leave_school
from browser_operation import report_health_status
from util import get_user_config
from util import send_email
from util import merge_default_config
import sys


def single_person_action(user_config):
    config = merge_default_config(user_config)

    if config is None:
        print("Configuration error.")
        exit(0)
    else:
        print(config)

    email = config['email']
    try:
        report_health_status(config, 5)
        report_leave_school(config, timeout=8)
    except Exception as message:
        send_email(email, repr(message))
        return True
    else:
        send_email(email, '<h1>您已打卡成功</h1><p>感谢使用</p>')
        return False


if __name__ == '__main__':
    user_configs = get_user_config(sys.argv[1])
    flag = True
    for person in user_configs:
        while flag:
            flag = single_person_action(person)
