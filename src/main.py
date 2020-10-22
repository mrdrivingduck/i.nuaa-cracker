from browser_operation import report_leave_school
from browser_operation import report_health_status
from util import get_user_config
from util import send_email, build_mail_content
from util import merge_default_config
import sys
import json


def single_person_action(user_config):
    config = merge_default_config(user_config)

    if config is None:
        print("Configuration error.")
        exit(0)
    else:
        print(config)

    email_address = config['email']

    try:
        report_health_status(config, 15)
        report_leave_school(config, timeout=15)
    except Exception as message:
        html = build_mail_content(repr(message), True)
        send_email(email_address, html)
        return True
    else:
        config.pop('password')
        html = build_mail_content(json.dumps(config), False)
        send_email(email_address, html)
        return False


if __name__ == '__main__':
    user_configs = get_user_config(sys.argv[1])
    for person in user_configs:
        redo = True
        while redo:
            redo = single_person_action(person)
