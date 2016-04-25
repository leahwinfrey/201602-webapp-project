from os import chdir
from os.path import dirname, realpath

from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# https://course-counts.herokuapp.com/ <-- heroku webb app

DEPART_ABBREV = {
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

CORE_ABBREV = {
    'CPAF': 'Core Africa & The Middle East',
    'CPAS': 'Core Central/South/East Asia',
    'CPEU': 'Core Europe',
    'CPFA': 'Core Fine Arts',
    'CFAP': 'Core Fine Arts Partial',
    'CPGC': 'Core Global Connections',
    'CPIC': 'Core Intercultural',
    'CPLS': 'Core Labratory Science',
    'CPLA': 'Core Latin America',
    'CMSP': 'Core Mathematics/Science Partial',
    'CPMS': 'Core Mathematics/Science',
    'CPPE': 'Core Pre-1800',
    'CPRF': 'Core Regional Focus',
    'CPUS': 'Core United States',
    'CPUD': 'Core United States Partial'}

YEAR_ABBREV = {
    '2010': '2010',
    '2011': '2011',
    '2012': '2012',
    '2013': '2013',
    '2014': '2014',
    '2015': '2015',
    '2016': '2016',
    '2017': '2017'}

SEASONS = {
    'spring': 'spring',
    'fall': 'fall',
    'summer': 'summer'
}


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
def view_homepage():
    return render_template('base2.html')
# this will be a list of links where they can click to sort by departments or core or time

@app.route('/department')
def view_alldepartment():
    listmajor = []
    for key, value in DEPART_ABBREV.items():
        listmajor.append((key, value))
    listmajor.sort(key=lambda x: x[1])
    return render_template('department2.html', departments=listmajor)


@app.route('/department/<abbrev>')
def view_department(abbrev):
    allcourses = get_data()
    length = len(allcourses)
    offeredclasses = []
    for x in range(0, length):
        current = allcourses[x]
        if current.department == abbrev:
            offeredclasses.append(current)
    return render_template('classes.html', abbrev=offeredclasses, department=DEPART_ABBREV[abbrev])

""" #Core classes aren't listed in TSV file
@app.route('/core')
def view_core():
    listcore = []
    for key,value in CORE_ABBREV.items():
        listcore.append((key, value))
    return render_template('core.html', core=sorted(listcore))

@app.route('/core/<abbrevcore>')
def view_core2(abbrevcore):
    allcourses2 = get_data()
    length = len(allcourses2)
    offered = []
    for x in range(0, length):
        current = allcourses2[x]
        if current.core == abbrevcore:
            offered.append(current)
    return render_template('coreclasses.html', abrevcore=offered, core=CORE_ABBREV[abbrevcore])
"""


@app.route('/year')
def view_year():
    listyear = []
    for key,value in YEAR_ABBREV.items():
        listyear.append((key, value))
    return render_template('year2.html', year=sorted(listyear))


@app.route('/year/<specyear>')
def view_year2(specyear):
    allcourses = get_data()
    length = len(allcourses)
    yearclass = []
    for x in range(0, length):
        current = allcourses[x]
        if current.year == specyear:
            yearclass.append(current)
    return render_template('specyear.html', specyear=yearclass, years=YEAR_ABBREV[specyear])


@app.route('/year/<specyear>/<semester>')
def view_year3(specyear, semester):
    allcourses = get_data()
    length = len(allcourses)
    yearsem = []
    for x in range(0, length):
        current = allcourses[x]
        if current.year == specyear and current.season == semester:
            yearsem.append(current)
    return render_template('semester.html', cursem=yearsem, years=YEAR_ABBREV[specyear], season=SEASONS[semester])

@app.route('/year/<specyear>/all')
def view_year4(specyear):
    allcourses = get_data()
    length = len(allcourses)
    allyear = []
    for x in range(0, length):
        current = allcourses[x]
        if current.year == specyear:
            allyear.append(current)
    return render_template('allyear.html', cursem=allyear, years=YEAR_ABBREV[specyear])



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