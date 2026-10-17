(Date format dd/mm/yyyy)
------

# Date 07/10/2026

OBSTACLE DESCRIPTION:
>Git push kept pushing .env file with credentials to Github

IN-DEPTH ANALYSIS:
>Git command "git add ." re-adds files to Git's index even if they are listed in .gitignore, specifically when those files were previously tracked by Git. Once a file has been committed even once, "git add ." will pick that file up even if they are within the .gitignore list.

SOLUTION:
>Initially I thought the issue was due to Git logging past changes and the .env file being present would stay until the .gitignore was updated. Doing a quick google search showed that the command "git add ." tracks all changes even the ones that fall within the .gitignore file. The solution was the stop using "git add ." and only use git add for new files that are created that git has yet to begin tracking. As of right now, the best command to use is "git commit -am "message"" as this will track changes and commit prior to pushing to github. For future reference, I should focus on the .gitignore list first to ensure that necessary files dont get tracked and committed due to a previous indexing.

OBSTACLE DESCRIPTION:
>Docker-Compose file issues

IN-DEPTH ANALYSIS:
>The encoder assosicated with the docker-compose was UTF-16 when the standard is UTF-8. Additionally, all docker related files can not have any comments or started with "echo "" > path_location" as the echo adds a "hidden" values at line 1 1.

SOLUTION:
>Moving forward, create new files with command "code <filename.extension>" and work from there. Any additional comments must be saved separately as a .example file.

# Date 17/10/2026

OBSTACLE DESCRIPTION:
>File not found in build context

IN-DEPTH ANALYSIS:
>"COPY failed: file not found in bould context: stat bronze_layer_ingestion.py: file does not exist" error popped up which indicates a missing file

SOLUTION:
>The Dockerfile had "COPY bronze_layer_ingestion.py" but the file is in the scripts folder so had to update to "COPY scripts/bronze_layer_ingestion.py"

OBSTACLE DESCRIPTION:
>Failed to push commit to GitHub

IN-DEPTH ANALYSIS:
>Error message returned that GitHub fell out of sync.

SOLUTION:
>The local repository and the host repository were out of sync, so had to pull the GitHub repo to update the local one prior to pushing.