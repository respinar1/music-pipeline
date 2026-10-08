(Date format dd/mm/yyyy)
------

# Date 07/10/2026
While attempting to create the initial environment for git and github repository, I came across my first issue. The .env file that will house my Spotify credentials was being tracked and pushed onto Github. My initial solution was to remove the .env from the .gitignore prior to deleting the file, then creating the .env folder again and posting the .env file back within the .gitignore. Although valid, the main issue was not the file being untracked, the main issue was the "git add ." command which ignores untracked restrictions and tracks every change present within git and previous commits.

Moving forward, now I know to not use 'git add .' or other credential files may appear on github. The best practice would be to include new files as they are generated using 'git add <foldername/filename>' and track commits with 'git commit -am "message"'.
