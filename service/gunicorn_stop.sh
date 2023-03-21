app_name="new_horizon"

systemctl stop ${app_name}_gunicorn.socket
systemctl stop ${app_name}_gunicorn.service