# COMP0035 Group coursework

The group coursework specification on Moodle lists a number of formats that you can use to present your work.

One of those options is to present your work as a static website using Flask.

This format allows the groups that want to try this to get a little experience with Flask before COMP0034.

You are not marked on the quality of the web app, only on the information it contains.

Feel free to copy and adapt this code for your group.

Do not reply on the pages in this repo as a checklist for what needs to be included however. Make sure you carefully read the spec on Moodle which states what needs to be included.

### To use this repository in Pycharm as a new repository
- Create a new project by cloning from VCS (copy and paste in the URL to this repo)
- Go to the settings/preferences in PyCharm, find the Project section and select Python interpreter. 
- Next to the Python Interpeter box click on the gear symbol and select Add. Add a new venv for the project.
- Open https://www.jetbrains.com/help/pycharm/managing-dependencies.html#apply_dependencies to see how to install the dependencies from requirements.txt. An alternative is to open the Terminal that is within Pycharm (View | Tool Windows | Terminal) and type: `pip install -r requirements.txt`
- Return to Settings/Preferences and find Project | Project Structure. Check that the `templates` directory is shown as a Template Folder (you can use the Mark as options to mark it if it isn't already highlighted).
- Still in Settings/Preferences, check Languages and Frameworks | Flask and make sure there is a tick in the box that says Flask integration (tick rather than a dash). Press OK if you make a change.
- Still in Settings/Preferences, check Languages and Frameworks | Template Languages and make sure that the Template Language box shows Jinja2 (use the drop down to select it if not then press OK).

### To merge this repository into your existing coursework repository
You will need to do this from a Terminal in PyCharm (at least I haven't found a way through the menu).

Enter `git remote add template https://github.com/nicholsons/comp0035_coursework_template.git`. This adds a way to use the remote repository and refer to it using the name `template`.

Enter `git fetch template`. This gets the files from the `template` repository.

Enter `git merge --allow-unrelated-histories template/master`. This merges the files from the `template` into your existing coursework repo.
 
At this point it will fail due to merge conflics on .gitignore, README.md and any other files that have the same name in both repositories.

In Pycharm the conflicted files will be highlighted a different colour (red in my colour scheme).

Right click on .gitignore and select Git - Resolve Conflicts. Keep your version of .gitignore.

Repeat this for all conflicts.

Enter `git remote rm template`.

Commit and push your changes to your coursework repo.

### To manually merge the files (i.e. not using Git)
If the above terrifies you then you could download the template repo as a zip and unzip to the files and manually copy them into your local directory for your coursework.

Since you don't care about tracking the history from my tempate repo this should be fine.

You will need to use Git | Add, Git | Commit and Git | Push the make sure all the new files you manually added are added, commited and pushed to your group repo.

### To edit the pages using HTML
Each page inherits the overall structure of the page from a file called `base.html` which is in the `templates` directory. This `base.html` includes the navigation bar, the Bootstrap css that is used to style the page, and defines a template area that can be edited for each of the other pages.

To edit the content of each page, find the relevant html page in the templates folder and open it.

You should see a section that starts and ends:

```jinja2
{% block content %}

{% endblock %}
```

Do not remove those lines as they are Jinja2 code that defines the start and end of the content section that will be displayed on the web page.

Everything between those tags is currently just HTML tags.

You can edit the HTML with the relevant details for your team's project.

HTML is pretty straightforward to use so hopefully you can work this out using a resource such as [w3schools](https://www.w3schools.com/html/).

There are examples in some of the pages for some of the common tasks such as hyperlinking a file (this involves a little Jinja2 so follow the example), including an image, using headings, lists and paragraphs.