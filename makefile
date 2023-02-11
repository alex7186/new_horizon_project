_today =`date '+%Y-%m-%d  %H:%M:%S'`
_commit_name = "autocommit $(_today)"
app_name = new_horizon
_branch_name = main
_local_dir = $(CURDIR)
_remote_dir = u1734296@31.31.196.21:www/xn-----dlccmbc8bcwbhe5aeehd9dxgi.xn--p1ai/

push:
	@$(MAKE) --no-print-directory _black
	@# @$(MAKE) --no-print-directory _touch_restart
	@$(MAKE) --no-print-directory _git_commit
	@echo " ⚙️  pushing as $(_commit_name) "
	@git push origin $(_branch_name)
	@echo " ✅  pushing done! "

push-force:
	@$(MAKE) --no-print-directory _black
	@# @$(MAKE) --no-print-directory _touch_restart
	@$(MAKE) --no-print-directory _git_commit
	@echo " ⚙️  🚩FORCE🚩  pushing as $(_commit_name) "
	@git push --force origin $(_branch_name)
	@echo " ✅  🚩FORCE🚩 pushing done! "

_black:
	@echo " 🧹 cleaning the code... "
	@python3 -m black .

_git_commit:
	@echo " ⚙️  pushing to git... "
	@git add .
	-@git commit -m $(_commit_name)

_touch_restart:
	@echo " ⚙️  creating '.restart-app' file... "
	@touch .restart-app

setup:
	@echo " ⚙️ installing pip dependencies "	
	@pip install -r misc/requirements.txt
	@echo " ✅  setup done! "

update_hosting:
	@$(MAKE) --no-print-directory _touch_restart
	@echo " ⚙️  pushing to hosting..."
	@echo " ⚙️  $(_local_dir) ➡️  $(_remote_dir)"
	@rsync -r $(_local_dir)/ $(_remote_dir)
	@echo " ✅  hosting update done! "

update_local:
	@echo " ⚙️  pushing to local..."
	@echo " ⚙️  $(_remote_dir) ➡️ $(_local_dir)"
	@rsync -r $(_remote_dir)/ $(_local_dir)
	@echo " ✅  local update done! "

runserver_local:
	@cd new_horizon; python3 manage.py runserver

migrate:
	@cd new_horizon; python3 manage.py makemigrations; python3 manage.py migrate

cat-logs:
	@python3 log_reader.py | less
