commit_name="autocommit $(date +'%Y-%m-%d %H:%M:%S')"

backup_branch_name="backup"
main_branch_name="main"


# go to backup branch
git branch $backup_branch_name
git checkout $backup_branch_name

# save changes to backup branch
git add .
git commit $commit_name
git push --set-upstream origin $backup_branch_name


# go to main branch and push changes 
git checkout $main_branch_name
git merge $backup_branch_name

git push origin $main_branch_name
