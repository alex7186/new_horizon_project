app_name="new_horizon"

systemctl start ${app_name}_gunicorn.socket
systemctl start ${app_name}_gunicorn.service