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


ABBREV = {
    'AMST': 'American Studies',
    'ARAB': 'Arabic',
    'ARTH': 'Art/History',
    'ARTM': 'Art/Media',
    'ARTS': 'Art/Studio',
    'BICH': 'Biochemistry',
    'BIO': 'Biology',
    'CHEM': 'Chemistry',
    'CHIN': 'Chinese',
    'COGS': 'Cognitive Science',
    'CSLC': 'Comparative Studies/Lit &amp; Cult',
    'COMP': 'Computer Science',
    'CTSJ': 'Critical Theory/Social Justice',
    'CSP': 'Cultural Studies Program',
    'DWA': 'Diplomacy and World Affairs',
    'ECON': 'Economics',
    'EDUC': 'Education',
    'ENGL': 'English',
    'FREN': 'French',
    'GEO': 'Geology',
    'GERM': 'German',
    'GRK': 'Greek',
    'HIST': 'History',
    'JAPN': 'Japanese',
    'KINE': 'Kinesiology',
    'LATN': 'Latin',
    'LLAS': 'Latino/a and Latin Amer Stud',
    'LING': 'Linguistics',
    'MATH': 'Mathematics',
    'MUSC': 'Music',
    'MUSA': 'Music Applied Study',
    'ABAR': 'Occidental-in-Argentina',
    'ABAU': 'Occidental-in-Australia',
    'ABAS': 'Occidental-in-Austria',
    'ABBO': 'Occidental-in-Bolivia',
    'ABBW': 'Occidental-in-Botswana',
    'ABBR': 'Occidental-in-Brazil',
    'ABCI': 'Occidental-in-Chile',
    'ABCH': 'Occidental-in-China',
    'ABCR': 'Occidental-in-Costa Rica',
    'ABCZ': 'Occidental-in-Czech Republic',
    'ABDE': 'Occidental-in-Denmark',
    'ABDR': 'Occidental-in-Dominican Repub',
    'ABFR': 'Occidental-in-France',
    'ABGE': 'Occidental-in-Germany',
    'ABHU': 'Occidental-in-Hungary',
    'ABIC': 'Occidental-in-Iceland',
    'ABIN': 'Occidental-in-India',
    'ABID': 'Occidental-in-Indonesia',
    'ABIR': 'Occidental-in-Ireland',
    'ABIT': 'Occidental-in-Italy',
    'ABJA': 'Occidental-in-Japan',
    'ABJO': 'Occidental-in-Jordan',
    'ABMO': 'Occidental-in-Morocco',
    'ABNZ': 'Occidental-in-New Zealand',
    'ABNI': 'Occidental-in-Nicaragua',
    'ABPE': 'Occidental-in-Peru',
    'ABRU': 'Occidental-in-Russia',
    'ABSM': 'Occidental-in-Samoa',
    'ABSE': 'Occidental-in-Senegal',
    'ABSA': 'Occidental-in-South Africa',
    'ABSP': 'Occidental-in-Spain',
    'ABSN': 'Occidental-in-Sweden',
    'ABSW': 'Occidental-in-Switzerland',
    'ABTN': 'Occidental-in-Taiwan',
    'ABNT': 'Occidental-in-the-Netherlands',
    'ABNA': 'Oxy-in-Netherlands Antilles',
    'ABUA': 'Oxy-in-United Arab Emirates',
    'ABUK': 'Oxy-in-the-United Kingdom',
    'PHIL': 'Philosophy',
    'PHAC': 'Physical Activities',
    'PHYS': 'Physics',
    'POLS': 'Politics',
    'PSYC': 'Psychology',
    'RELS': 'Religious Studies',
    'RUSN': 'Russian',
    'SOC': 'Sociology',
    'SPAN': 'Spanish',
    'OXAB': 'Study Abroad',
    'THEA': 'Theater',
    'UEP': 'Urban and Environmental Policy',
    'WRD': 'Writing and Rhetoric'}

class Course:
    def __init__(self, year, season, department, number, section, title, units, instructors, meetings, core, seats, \
                 enrolled, reserved, reserved_open, waitlisted):
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
    courseinfo = []
    with open('counts.tsv') as file:
        for line in file.read().splitlines():
            year, season, department, number, section, title, units, instructors, meetings, core, seats, \
            enrolled, reserved, reserved_open, waitlisted = line.split('\t')
            new_course = Course(year, season, department, number, section, title, units,
            instructors, meetings, core, seats, enrolled, reserved, reserved_open, waitlisted)
            courseinfo.append(new_course)
        return courseinfo


@app.route('/')
def view_alldepartment():
    listmajor = []
    for key, value in ABBREV.items():
        listmajor.append( (key, value) )
    return render_template('directformat.html', departments=listmajor)


@app.route('/<abbrev>')
def view_department(abbrev):
    allcourses = get_data()
    length = len(allcourses)
    offeredclasses = []
    for x in range(0, length):
        current = allcourses[x]
        if current.department == abbrev:

            offeredclasses.append(current)
    return render_template('classes.html', abbrev=offeredclasses, department=ABBREV[abbrev])


"""
@app.route('/season')
def view_season():
    listseason = get_data()
    return render_template('terms.html', courseinfo=listseason)


@app.route('/department/<depart:'')
def view_department(depart):
    departlist = get_data()
    length = len(departlist)
    for x in range(0, length):
        if departlist[x].department == depart:
            curdepart = departlist[x]
            index = x
    return render_template('department2.html', depart=curdepart)

@app.route('/core')
def view_core():
    return render_template('core.html')

@app.route('/all')
def view_all():
    course = get_data()
    return render_template('all.html', course_info=course)

@app.route('/actual')
def view_actual():
    return render_template('website.html')
"""

# The functions below lets you access files in the css, js, and images folders.
# You should not change them unless you know what you are doing.

@app.route('/images/<file>:')
def get_image(file):
    return send_from_directory('images', file)

@app.route('/css/<file>:')
def get_css(file):
    return send_from_directory('css', file)

@app.route('/js/<file>:')
def get_js(file):
    return send_from_directory('js', file)

if __name__ == '__main__':
    chdir(dirname(realpath(__file__)))
    app.run(debug=True)