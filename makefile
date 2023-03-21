_today =`date '+%Y-%m-%d  %H:%M:%S'`
_commit_name = "autocommit $(_today)"
app_name = new_horizon
_branch_name = main
_local_dir = $(CURDIR)

_common-service-path = /etc/systemd/system/

_black:
	@echo " 🧹 cleaning the code... "
	@python3 -m black .

push:
	@$(MAKE) --no-print-directory _black
	@$(MAKE) --no-print-directory _git_commit
	@echo " ⚙️  pushing as $(_commit_name) "
	@git push origin $(_branch_name)
	@echo "\n ✅  pushing done! "

push-force:
	@$(MAKE) --no-print-directory _black
	@$(MAKE) --no-print-directory _git_commit
	@echo " ⚙️  🚩FORCE🚩  pushing as $(_commit_name) "
	@git push --force origin $(_branch_name)
	@echo "\n ✅  🚩FORCE🚩 pushing done! "

_git_commit:
	@echo " ⚙️  pushing to git... "
	@git add .
	-@git commit -m $(_commit_name)


black:
	@echo " 🧹 cleaning the code... "
	@python3 -m black .

setup:
	@echo " ⚙️ installing pip dependencies "	
	@pip install -r misc/requirements.txt
	@echo "\n ✅  setup done! "

copy_service:
	@echo "\n⚙️  moving service from $(_local_dir)/service/ to $(_common-service-path)\n"
	@sudo cp $(_local_dir)/service/$(app_name).service $(_common-service-path)/$(app_name).service
	-@sudo systemctl daemon-reload
	-@sudo systemctl enable $(app_name)

start_service:
	@sudo systemctl restart $(app_name)
	@echo "\n ✅  service (re)started\n"

stop_service:
	@sudo systemctl stop $(app_name)
	@echo "\n ❌  service stopped\n"

status:
	@systemctl status new_horizon.service 




gunicorn_copy_service:
	@echo "\n⚙️  moving gunicorn services from $(_local_dir)/service/ to $(_common-service-path)\n"
	@sudo cp $(_local_dir)/service/$(app_name)_gunicorn.service $(_common-service-path)/$(app_name)_gunicorn.service
	@sudo cp $(_local_dir)/service/$(app_name)_gunicorn.socket $(_common-service-path)/$(app_name)_gunicorn.socket
	-@sudo systemctl daemon-reload
	-@sudo systemctl enable $(app_name)_gunicorn.socket
	-@sudo systemctl enable $(app_name)_gunicorn.service


gunicorn_start_service:
	-@sudo systemctl start $(app_name)_gunicorn.socket
	-@sudo systemctl start $(app_name)_gunicorn.service

gunicorn_stop_service:
	-@sudo systemctl stop $(app_name)_gunicorn.socket
	-@sudo systemctl stop $(app_name)_gunicorn.service

gunicorn_setup_nginx:
	@apt install nginx
	@cp $(_local_dir)/service/$(app_name)_nginx /etc/nginx/sites-enabled/new_horizon_project
	@sudo systemctl restart nginx
	@sudo ufw allow 'Nginx Full'

gunicorn_nginx_start:
	@$(MAKE) --no-print-directory gunicorn_copy_service
	@$(MAKE) --no-print-directory gunicorn_setup_nginx
	@$(MAKE) --no-print-directory gunicorn_start_service

