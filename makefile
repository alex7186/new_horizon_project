app_name = new_horizon
_local_dir = $(CURDIR)

_common-service-path = /etc/systemd/system/


setup:
	@echo " ⚙️ installing pip dependencies "	
	@pip install -r misc/requirements.txt

	@echo "\n⚙️  moving systemd services from $(_local_dir)/service/ to $(_common-service-path)\n"
	@sudo cp $(_local_dir)/service/$(app_name).service $(_common-service-path)/$(app_name).service
	
	@sudo systemctl daemon-reload
	@sudo systemctl enable $(app_name).service

	@ln -s -f $(_local_dir)/static $(_local_dir)/apps/main/static
	@echo " ✅  setup done "

start:
	-@sudo systemctl start $(app_name).service
	@echo " ✅  started "

stop:
	-@sudo systemctl stop $(app_name).service
	@echo " ❌  stopped "

status:
	-@sudo systemctl status $(app_name).service

cat-service:
	@systemctl cat $(app_name)

cat-log:
	@journalctl --unit=$(app_name)

