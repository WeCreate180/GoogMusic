# GoogMusic
A Google Music Alexa Skill

## Setup
1) Fork this repository.

2) Create an account at http://heroku.com

3) Create an app. Go to Settings, then reveal config vars

3b) add a config var called email, and insert your google music email.

3c) add a config var called password, and insert your google music password.

3d) add a config var called android_id, and insert your authorized device id. To find it: go to 3e

3e) Go to the google music website, and then go to settings, youll find authorized devices. Inspect element and find something like "id" ignore the 0x and copy the rest, this is your id.

4) Go to deploy, link your github account. Select this forked repo. Click "Deploy"

5) Setup your alexa skill. Use the same tutorial from the origian repo with the files from this repo.
