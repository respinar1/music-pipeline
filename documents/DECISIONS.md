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

# Date 19/10/2026

OBSTACLE DESCRIPTION:
>Passing .env file to bronze_layer_ingestion script

IN-DEPTH ANALYSIS:
>Three possible options for passing the .env file into the script: using the dotenv library with either load_dotenv() or dotenv_values(), or using the env_file developed within Docker. 
>1. load_dotenv() would work well as it is the standard in this case. Seeing as I am the owner and I know the values within the file, I can freely load and alter the file as needed. So having it readily available within the system environment would be best for when I create a new script that may need said credentials. However, in a production environment where there are other people involved, load_dotenv() may not be best as others may use said credentials without visibility of usage.
>2. dotenv_values() would also work well as it give me access to the data within the .env file. However, having to constantly refer to the config variable whenever access is needed may become tedious. In a production environment, using the dotenv_values() function removes the caveat associated with the load_dotenv() function.
>3. using the docker env_file would also work similar to the load_dotenv() just on the container level, which is good for an organization or team.

SOLUTION:
>Going with option 1 as Spotifys API, and most APIs, can read System Environments automatically, making the process of accessing the API calls smoother vs pushing the credentials manually.

# Date 20/10/2026

OBSTACLE DESCRIPTION:
>Docker container not reflecting script changes without rebuilding

IN-DEPTH ANALYSIS:
>The pipeline container was running the script from /app/bronze_layer_ingestion.py which is the initial Dockerfile copy came from. However, scripts are being saved within the /app/scripts/ directory. The Path mismatch caused docker to not read new changes to the script thus updating the encoder and saving the file with the new utf-8 was not being registered by Docker unless a full rebuild of the image was done. 

SOLUTION:
>To circumvent this, I decided to mount a volume on the docker-compose.yml that points to app/scripts inside the container and update the Dockerfile's CMD to ./app/scripts/bronze_layer_ingestion.py which aligns paths allowing for seamless update and save from script to docker.