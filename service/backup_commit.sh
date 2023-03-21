commit_name="\"backup autocommit $(date +'%Y-%m-%d %H:%M:%S')\""

backup_branch_name="backup"
main_branch_name="main"
BASE_DIR="/root/new_horizon_project"


# go to backup branch
#git branch $backup_branch_name
<<<<<<< HEAD
cd $BASE_DIR
=======
>>>>>>> 52d9433 ("backup autocommit 2023-03-21 17:37:39")
git checkout $backup_branch_name

# save changes to backup branch
git add .
git commit -m "${commit_name}"
git push --set-upstream origin $backup_branch_name


# go to main branch and push changes 
#git checkout $main_branch_name
#git merge $backup_branch_name

#git push origin $main_branch_name
