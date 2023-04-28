app_name = new_horizon
_local_dir = $(CURDIR)

_common-service-path = /etc/systemd/system/


setup:
	@echo " ⚙️ installing pip dependencies "	
	@pip install -r misc/requirements.txt

	@echo "\n⚙️  moving gunicorn services from $(_local_dir)/service/ to $(_common-service-path)\n"
	@cp $(_local_dir)/service/$(app_name)_gunicorn.service $(_common-service-path)/$(app_name)_gunicorn.service
	@cp $(_local_dir)/service/$(app_name)_gunicorn.socket $(_common-service-path)/$(app_name)_gunicorn.socket
	@python3 manage.py collectstatic    
	
	@systemctl daemon-reload
	@systemctl enable $(app_name)_gunicorn.socket
	@systemctl enable $(app_name)_gunicorn.service

	@echo " ⚙️ setting up nginx "	
	@apt install nginx
	@cp $(_local_dir)/service/$(app_name)_nginx.config /etc/nginx/sites-enabled/new_horizon_project
	@echo " ⚙️ enabling nginx service "	
	@systemctl restart nginx
	@ufw allow 'Nginx Full'

	@echo "\n ✅  setup done "


start:
	-@systemctl start $(app_name)_gunicorn.socket
	-@systemctl start $(app_name)_gunicorn.service
	@python3 manage.py migrate
	@echo "\n ✅  started "

stop:
	-@systemctl stop $(app_name)_gunicorn.socket
	-@systemctl stop $(app_name)_gunicorn.service
	@echo "\n ❌  stopped "


