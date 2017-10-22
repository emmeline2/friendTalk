#!/web/cs2041/bin/python3.6.3
#Emmeline Pearson - z5178618

import os
import re
from flask import Flask, render_template, session

students_dir = "dataset-medium"; #change this value to switch datasets 

app = Flask(__name__)

# Show unformatted details for student "n"
# Increment n and store it in the session cookie

@app.route('/', methods=['GET','POST'])
@app.route('/start', methods=['GET','POST'])
def start():
    studentDict = {}
    n = session.get('n', 0)
    students = sorted(os.listdir(students_dir))
    student_to_show = students[n % len(students)]
    details_filename = os.path.join(students_dir, student_to_show, "student.txt")
    with open(details_filename) as f:
        details = f.read()
    #print(details)
    lines = details.split('\n')
    #return render_template('start.html',student_details=lines)
    for index, line in enumerate(lines): 
        if re.match(r'^program: ',lines[index]):
            program = line
        elif re.match(r'^full_name: ',lines[index]):
            name = line;
        elif re.match(r'^birthday: ',lines[index]):
            birthday = line
        elif re.match(r'^zid: ',lines[index]):
            zid = line
        elif re.match(r'^courses: ',lines[index]):
            courses = line
        elif re.match(r'^password: ', lines[index]): 
            password = line
    #complete text:       
    infoToShare = name + '\n' + program + '\n' + birthday + '\n' + zid + '\n' + courses

    #get image
    details_imagename = os.path.join(students_dir, student_to_show, "image.jpg")

    #get posts
    #alltextfiles = os.path.join(students_dir,student_to_show).endswith('.txt'); 
    max = 3;
    allPosts = ""
    for n in range(max,0,-1):
        filename = str(n)
        filename +='.txt'
        details_posts = os.path.join(students_dir, student_to_show, filename)
        with open(details_posts) as file:
            post = file.read()
            allPosts = allPosts + post + '\n'
            
    session['n'] = n + 1 #infoToShare
    return render_template('start.html',student_details=details_imagename,image_filename= details_imagename, posts=allPosts)

if __name__ == '__main__':
    app.secret_key = os.urandom(12) #12
    app.run(debug=True)





