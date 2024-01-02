app_name = new_horizon
_local_dir = $(CURDIR)

_common-service-path = /etc/systemd/system/


setup:
	@echo " ⚙️ installing pip dependencies "	
	@pip install -r misc/requirements.txt

	@echo "\n⚙️  moving systemd services from $(_local_dir)/service/ to $(_common-service-path)\n"
	@sudo cp $(_local_dir)/service/$(app_name).service $(_common-service-path)/$(app_name).service
	@python3 manage.py collectstatic    
	
	@sudo systemctl daemon-reload
	@sudo systemctl enable $(app_name).service


	@echo "\n ✅  setup done "

start:
	-@sudo systemctl start $(app_name).service
	@echo "\n ✅  started "

stop:
	-@sudo systemctl stop $(app_name).service
	@echo "\n ❌  stopped "

status:
	-@sudo systemctl status $(app_name).service


makemigrations:
	

migrate:
	@python3 manage.py makemigrations
	@echo "\n ✅  migrations made "
	@python3 manage.py migrate
	@echo "\n ✅  migrations done "
	
cat-service:
	@systemctl cat $(app_name)

cat-log:
	@journalctl --unit=$(app_name)

