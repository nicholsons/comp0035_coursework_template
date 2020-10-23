# COMP0035 Group coursework

The group coursework specification on Moodle lists a number of formats that you can use to present your work.

One of those options is to present your work as a static website using Flask.

This format allows the groups that want to try this to get a little experience with Flask before COMP0034.

You are not marked on the quality of the web app, only on the information it contains.

Feel free to copy and adapt this code for your group.

Do not reply on the pages in this repo as a checklist for what needs to be included however. Make sure you carefully read the spec on Moodle which states what needs to be included.

### To use this in Pycharm
- Create a new project by cloning from VCS (copy and paste in the URL to this repo)
- Go to the settings/preferences in PyCharm, find the Project section and select Python interpreter. 
- Next to the Python Interpeter box click on the gear symbol and select Add. Add a new venv for the project.
- Open https://www.jetbrains.com/help/pycharm/managing-dependencies.html#apply_dependencies to see how to install the dependencies from requirements.txt. An alternative is to open the Terminal that is within Pycharm (View | Tool Windows | Terminal) and type: `pip install -r requirements.txt`
- Return to Settings/Preferences and find Project | Project Structure. Check that the `templates` directory is shown as a Template Folder (you can use the Mark as options to mark it if it isn't already highlighted).
- Still in Settings/Preferences, check Languages and Frameworks | Flask and make sure there is a tick in the box that says Flask integration (tick rather than a dash). Press OK if you make a change.
- Still in Settings/Preferences, check Languages and Frameworks | Template Languages and make sure that the Template Language box shows Jinja2 (use the drop down to select it if not then press OK).
