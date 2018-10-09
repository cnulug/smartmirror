smartmirror
===========

Software repository for smart-mirror build. Application and feature development will be based out of this branch.

## CNU LUG BOARD
 - President: Eric Miers, eric.miers.15@cnu.edu
 - Vice President: Avery Gibson, avery.gibson.16@cnu.edu
 - Secretary: Logan O'Leary, logan.oleary.16@cnu.edu
 - Treasurer: Benjamin Marshall, benjamin.marshall.16@cnu.edu
 - Faculty Sponsor: Dr.David Gore, david.gore@cnu.edu
 
## Collaboration
Join us on slack at `cnulinuxusersgroup.slack.com`
 
View our Kanban board of tasks at `https://tree.taiga.io/project/ejmiers-cnu-lug-smart-mirror/`
   -To be a project member on Taiga Kanban, email president at contact listed above
 
## Pull requests

Please keep pull requests to this repo short and concise. Pull requests should focus on one feature, and changes that are
part of a pull request should be split into separate commits, according to logical groups of changes.

### Set up local environment

Before beginning development, ensure your local environment is adequately set up to begin contributing:

1. Fork this repository if you have not already done so
4. `cd smartmirror`
5. Setup your upstream repository
  - `git remote add upstream https://github.com/cnulug/smartmirror`
6. Ensure the output of the command `git remote -v` is as follows:
  - origin `<url to your fork of this repo>` (fetch)
  - origin `<url to your fork of this repo>` (push)
  - upstream https://github.com/cnulug/smartmirror (fetch)
  - upstream https://github.com/cnulug/smartmirror (push)

### Opening a pull request

Any time you begin working on a new contribution, make sure your master branch is up to date with the latest changes:

1. `git checkout master`
2. `git pull upstream master`

**Remember to _not_ use your `master` branch for development. Always try to begin making your changes in a new feature branch:

1. `git checkout -b smartmirror-my-new-contribution`

Once you have committed your changes locally, and are ready to open a pull request, push your branch's changes to your fork of the repo (if you have followed the above steps, `origin` should point to it):

1. `git push origin smartmirror-my-new-contribution` (replace `smartmirror-my-new-contribution` with the actual name you gave your branch).
2. You can now open a pull request by going to https://github.com/cnulug/smartmirror and clicking on the `New pull request` button.
3. Make your pull request against the `master` branch of the upstream repository.
4. Your pull request will be reviewed by members of the board to ensure quality and functionality of code. Your pull request may not go through until certain criteria is met. We will let you know of any changes that need to be changed before your branch can be merged.

If you have any questions, or need help setting up your local environment, don't hesitate to ask in our Slack channel or reach out directly to any of the board or club members.

Happy Coding!



