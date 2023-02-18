_today =`date '+%Y-%m-%d  %H:%M:%S'`
_commit_name = "autocommit $(_today)"
app_name = new_horizon
_branch_name = main
_local_dir = $(CURDIR)
_remote_dir = root@194.87.191.45:/root/new_horizon_project

_common-service-path = /etc/systemd/system/

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

_black:
	@echo " 🧹 cleaning the code... "
	@python3 -m black .

_git_commit:
	@echo " ⚙️  pushing to git... "
	@git add .
	-@git commit -m $(_commit_name)

setup:
	@echo " ⚙️ installing pip dependencies "	
	@pip install -r misc/requirements.txt
	@echo "\n ✅  setup done! "

update_hosting:
	@echo " ⚙️  pushing to hosting..."
	@echo " ⚙️  $(_local_dir) ➡️  $(_remote_dir)"
	@rsync -r $(_local_dir)/ $(_remote_dir)
	@echo "\n ✅  hosting update done! "

update_local:
	@echo " ⚙️  pushing to local..."
	@echo " ⚙️  $(_remote_dir) ➡️ $(_local_dir)"
	@rsync -r $(_remote_dir)/ $(_local_dir)
	@echo "\n ✅  local update done! "


migrate:
	@cd new_horizon; python3 manage.py makemigrations; python3 manage.py migrate


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