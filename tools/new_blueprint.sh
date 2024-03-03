#!/bin/bash

"""
This script helps creating the blueprint design pattern that I use in this project.
It creates the blueprint package (if not already existing), which functions as a blueprint loader, that dynamically
loads in all blueprints that are contained within the blueprint directory during flask create_app().

Please use this script with caution as it depends on the location it is launched in. If you leave it as is: myFlaskProject/tools as a 
sister directory to myFlaskProject/myFlaskApp, it works like a charm and will find the myFlaskApp directory!
"""


# Welcome message
echo -e "This script will help you create a new Flask-Blueprint by generating
the folderstructure and files according to best-practice.\n"

# make sure, app-directory is found to avoid messing up folder structure accidentally
found_app=false
while ! $found_app
do
	read -p "Please specify the name of the flask-project you wish to create the blueprint for: " app
	project_dir="$(dirname "$PWD")/$app"
	if ! [ -d $project_dir ]; then
        echo -e "Flask app \"$app\" not found. Make sure you are in the correct directory (/app/tools) have spelled everything correctly!"
    else
        found_app=true
    fi
done

# get list of blueprints to be added
read -p "Please specify the names of the blueprints you want to create. Note: To create multiple
blueprints at once, enter multiple names separated by blankspace: " names
read -a blueprints <<< "$names"

# init blueprints-package with bp-interface if it does not exist already
if ! [ -d $project_dir/blueprints ]; then
    cd $project_dir
    mkdir -p "blueprints" && cd $_
    touch __init__.py

    echo -e "from os import chdir, getcwd, listdir, path
from importlib import import_module

chdir(getcwd()+\"/happypants/blueprints\")
blueprints = [bp for bp in listdir() if path.isdir(bp) and bp != \"__pycache__\"]
chdir(\"..\")
chdir(\"..\")
liste = listdir(\"/home/happypants/Documents/PythonProjects/Flask/HP-first-website/happypants/blueprints\")
bps = []
for bp in blueprints:
    bps.append(import_module(\"happypants.blueprints.\"+bp))" > __init__.py
fi

# create all new blueprints, dont touch those, that already exist to avoid overwriting files
for i in "${blueprints[@]}"
do  
    cd $project_dir
    if [ -d "blueprints/$i" ]; then
        echo "Blueprint \"$i\" already exists, skipping..."
    else
        mkdir "blueprints/$i" && cd $_
        touch __init__.py
        echo "from .$i import bp" > __init__.py
        touch "$i.py"
        echo "from flask import Blueprint
bp = Blueprint(\"$i\", __name__, url_prefix=\"/$i\", static_folder=\"static\", template_folder=\"templates\")" > $i.py
        mkdir templates
        mkdir static && cd $_
        mkdir images
        mkdir styles
    fi
    
done
