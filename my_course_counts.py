from os import chdir
from os.path import dirname, realpath

from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# FIXME write your app below
# https://course-counts.herokuapp.com/ <-- heroku webb app
# Need a code to read in file

# Need @app.route links that separate counts '/professor'
# Need @app.route links that separate counts by '/major'
# HTML links to Oxy professor page


class Courses:
    def __init__(self, year, season, department, number, section, title, units, instructors, meetings, core, seats, enrolled, reserved, reserved_open, waitlisted):
        self.year = year
        self.season = season
        self.department = department
        self.number = number
        self.section = section
        self.title = title
        self.unit = units
        self.instructors = instructors
        self.meetings = meetings
        self.core = core
        self.seats = seats
        self.enrolled = enrolled
        self.reserved = reserved
        self.reserved_open = reserved_open
        self.waitlisted = waitlisted


def get_data():
    course_info = []
    with open('counts.tsv') as file:
        for line in file.read().splitlines():
            year, season, department, number, section, title, units, instructors, meetings, core, seats, enrolled, reserved, reserved_open, waitlisted = line.split('\t')
            course_info.append(Courses(year, season, department, number, section, title, units, instructors, meetings, core, seats, enrolled, reserved, reserved_open, waitlisted))
        return course_info


@app.route('/')
def view_root():
    return render_template('base.html')

# The functions below lets you access files in the css, js, and images folders.
# You should not change them unless you know what you are doing.

@app.route('/images/<file>')
def get_image(file):
    return send_from_directory('images', file)

@app.route('/css/<file>')
def get_css(file):
    return send_from_directory('css', file)

@app.route('/js/<file>')
def get_js(file):
    return send_from_directory('js', file)

if __name__ == '__main__':
    chdir(dirname(realpath(__file__)))
    app.run(debug=True)
