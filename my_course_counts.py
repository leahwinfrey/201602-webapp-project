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
    'CSLC': 'Comparative Studies/Lit & Culture',
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

DEPART_FULL = {
    'AMST': 'AMST',
    'ARAB': 'ARAB',
    'ARTH': 'ARTH',
    'ARTM': 'ARTM',
    'ARTS': 'ARTS',
    'BICH': 'BICH',
    'BIO': 'BIO',
    'CHEM': 'CHEM',
    'CHIN': 'CHIN',
    'COGS': 'COGS',
    'CSLC': 'CSLC',
    'COMP': 'COMP',
    'CTSJ': 'CTSJ',
    'CSP': 'CSP',
    'DWA': 'DWA',
    'ECON': 'ECON',
    'EDUC': 'EDUC',
    'ENGL': 'ENGL',
    'FREN': 'FREN',
    'GEO': 'GEO',
    'GERM': 'GERM',
    'GRK': 'GRK',
    'HIST': 'HIST',
    'JAPN': 'JAPN',
    'KINE': 'KINE',
    'LATN': 'LATN',
    'LLAS': 'LLAS',
    'LING': 'LING',
    'MATH': 'MATH',
    'MUSC': 'MUSC',
    'MUSA': 'MUSA',
    'ABAR': 'ABAR',
    'ABAU': 'ABAU',
    'ABAS': 'ABAS',
    'ABBO': 'ABBO',
    'ABBW': 'ABBW',
    'ABBR': 'ABBR',
    'ABCI': 'ABCI',
    'ABCH': 'ABCH',
    'ABCR': 'ABCR',
    'ABCZ': 'ABCZ',
    'ABDE': 'ABDE',
    'ABDR': 'ABDR',
    'ABFR': 'ABFR',
    'ABGE': 'ABGE',
    'ABHU': 'ABHU',
    'ABIC': 'ABIC',
    'ABIN': 'ABIN',
    'ABID': 'ABID',
    'ABIR': 'ABIR',
    'ABIT': 'ABIT',
    'ABJA': 'ABJA',
    'ABJO': 'ABJO',
    'ABMO': 'ABMO',
    'ABNZ': 'ABNZ',
    'ABNI': 'ABNI',
    'ABPE': 'ABPE',
    'ABRU': 'ABRU',
    'ABSM': 'ABSM',
    'ABSE': 'ABSE',
    'ABSA': 'ABSA',
    'ABSP': 'ABSP',
    'ABSN': 'ABSN',
    'ABSW': 'ABSW',
    'ABTN': 'ABTN',
    'ABNT': 'ABNT',
    'ABNA': 'ABNA',
    'ABUA': 'ABUA',
    'ABUK': 'ABUK',
    'PHIL': 'PHIL',
    'PHAC': 'PHAC',
    'PHYS': 'PHYS',
    'POLS': 'POLS',
    'PSYC': 'PSYC',
    'RELS': 'RELS',
    'RUSN': 'RUSN',
    'SOC': 'SOC',
    'SPAN': 'SPAN',
    'OXAB': 'OXAB',
    'THEA': 'THEA',
    'UEP': 'UEP',
    'WRD': 'WRD'}

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
    'summer': 'summer'}


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
    return render_template('homepage.html')

# List of all departments
@app.route('/department')
def view_alldepartment():
    listmajor = []
    for key, value in DEPART_ABBREV.items():
        listmajor.append((key, value))
    listmajor.sort(key=lambda x: x[1])
    return render_template('listalldeparts.html', departments=listmajor)


# List of all classes offered in specific department
@app.route('/department/<abbrev>')
def view_department(abbrev):
    allcourses = get_data()
    length = len(allcourses)
    offeredclasses = []
    for x in range(0, length):
        current = allcourses[x]
        if current.department == abbrev:
            offeredclasses.append(current)
    return render_template('listdepartmentclasses.html', abbrev=offeredclasses, department=DEPART_ABBREV[abbrev],
                           full=DEPART_FULL[abbrev])


# List of all classes offered in specific department by year
@app.route('/department/<abbrev>/<specyear>')
def view_classesperyear(abbrev, specyear):
    allcourses = get_data()
    length = len(allcourses)
    departyear = []
    for x in range(0, length):
        current = allcourses[x]
        if current.year == specyear and current.department == abbrev:
            departyear.append(current)
    return render_template('listdepartmentbyear.html', cursem=departyear, years=YEAR_ABBREV[specyear],
                           depart=DEPART_ABBREV[abbrev], full=DEPART_FULL[abbrev])

# List of all classes offered in specific department by year and semester
@app.route('/department/<specdepart>/<specyear>/<specsem>')
def view_classessemyear(specdepart, specyear, specsem):
    allcourses = get_data()
    length = len(allcourses)
    departyearsem = []
    for x in range(0, length):
        current = allcourses[x]
        if current.year == specyear and current.department == specdepart and current.season == specsem:
            departyearsem.append(current)
    return render_template('listdepartmentsbyearsem.html', cursem=departyearsem, years=YEAR_ABBREV[specyear],
    depart=DEPART_ABBREV[specdepart], specsem=SEASONS[specsem])

# List of years
@app.route('/year')
def view_year():
    listyear = []
    for key,value in YEAR_ABBREV.items():
        listyear.append((key, value))
    return render_template('listyears.html', year=sorted(listyear))

# List of years with option to choose semester
@app.route('/year/<specyear>')
def view_year2(specyear):
    allcourses = get_data()
    length = len(allcourses)
    yearclass = []
    for x in range(0, length):
        current = allcourses[x]
        if current.year == specyear:
            yearclass.append(current)
    return render_template('listyearsemoption.html', specyear=yearclass, years=YEAR_ABBREV[specyear])


# List of all classes offered that year
@app.route('/year/<specyear>/all')
def view_year4(specyear):
    allcourses = get_data()
    length = len(allcourses)
    allyear = []
    for x in range(0, length):
        current = allcourses[x]
        if current.year == specyear:
            allyear.append(current)
    return render_template('allofferedbyear.html', cursem=allyear, years=YEAR_ABBREV[specyear])


# List of all classes offered in semester of that year
@app.route('/year/<specyear>/<semester>')
def view_year3(specyear, semester):
    allcourses = get_data()
    length = len(allcourses)
    yearsem = []
    for x in range(0, length):
        current = allcourses[x]
        if current.year == specyear and current.season == semester:
            yearsem.append(current)
    return render_template('listofferedbysemester.html', cursem=yearsem, years=YEAR_ABBREV[specyear], season=SEASONS[semester])


# List of classes ex: 2011 fall AMST
@app.route('/year/<specyear>/<specsem>/<specdepart>')
def view_yeardepartsem(specyear, specsem, specdepart):
    allcourses = get_data()
    length = len(allcourses)
    yeardepsem = []
    for x in range(0, length):
        current = allcourses[x]
        if current.year == specyear and current.department == specdepart and current.season == specsem:
            yeardepsem.append(current)
    return render_template('listyearsemesterdepartment.html', cursem=yeardepsem, years=YEAR_ABBREV[specyear],
                           depart=DEPART_ABBREV[specdepart], specsem=SEASONS[specsem])





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