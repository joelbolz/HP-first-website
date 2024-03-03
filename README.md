# Installation

## Virtual environment

Create and activate the Virtual Environment
```bash
python3 -m venv .venv && source .venv/bin/activate
```
Install dependencies
```bash
pip install flask flask_sqlalchemy flask_login flask_wtf flask_bcrypt wtforms
```

# Running the Flask App
To run the Website, first make sure you are in the **project directory** (```HP-first-website```), **not** the **app directory** (```HP-first-website/happypants```). Then run the App with flask run:
```bash
flask --app happypants run --debug
```
 Note that the ```--debug``` tag is optional and enables live-updating as well as other debug features

 # Creating new Blueprints
I have choosen to make loading in Blueprints dynamic, without the need to add them manually to the create_app() function. To make this work, and follow the best-practice-pattern, I have created a small bash-script that sets up everything for you.

Make sure, that you are in the **tools-directory** (```HP-first-website/tools```) and run the script:
```bash
bash new_blueprint.sh
```
The script will prompt you to specify the Flask App name and the names of the Blueprints you would like to add. You can add multiple Blueprints at once, if you like. Existing Blueprints will be detected and not altered.