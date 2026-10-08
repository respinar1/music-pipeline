(Date format dd/mm/yyyy)
------

# Date 07/10/2026

OBSTICLE DESCRIPTION:
>Git push kept pushing .env folder with credentials to Github

IN-DEPTH ANALYSIS:
>Git command "git add ." tracks all changes even those that fall within the .gitignore file.

SOLUTION:
>Initially I thought the issue was due to Git logging past changes and the .env file being present would stay until the .gitignore was updated. Doing a quick google search showed that the command "git add ." tracks all changes even the ones that fall within the .gitignore file. The solution was the stop using "git add ." and only use git add for new files that are created that git has yet to begin tracking. As of right now, the best command to use is "git commit -am "message"" as this will track changes and commit prior to pushing to github.
