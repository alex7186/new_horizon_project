import os

from settings import LOG_FILENAME, LOG_FILEPATH
from datetime import datetime


def register_user_activity(function):
    def wrapper(*args, **kwargs):
        request = args[0]

        # getting api
        adress = request.META.get("HTTP_X_FORWARDED_FOR")
        if adress:
            user_ip = adress.split(",")[-1].strip()
        else:
            user_ip = request.META.get("REMOTE_ADDR")

        # getting browser
        user_agent = request.META.get("HTTP_USER_AGENT")

        # getting opened_page
        opened = request.path

        # appending log file
        message = (
            "\t".join(
                [
                    datetime.now().strftime("%Y.%m.%d %H:%M:%S"),
                    f"{user_ip}\t{user_agent}\t{opened}",
                ]
            )
            + "\n"
        )

        flag_skip_local_usage = False
        # loacal data is not interested
        if str(user_ip) in ("127.0.0.1", "192.168.0.17", "10.8.0.8"):
            flag_skip_local_usage = True

        if not flag_skip_local_usage:
            with open(os.path.join(LOG_FILEPATH, LOG_FILENAME), "a") as file:
                file.write(message)

        return function(*args, **kwargs)

    return wrapper
