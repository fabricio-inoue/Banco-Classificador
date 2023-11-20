category_mappings = {'decode':{
    'job': {
        0: 'admin.',
        2: 'entrepreneur',
        1: 'blue-collar',
        4: 'management',
        6: 'self-employed',
        5: 'retired',
        3: 'housemaid',
        8: 'student',
        7: 'services',
        9: 'technician',
        10: 'unemployed',
        11: None  # Represents missing data
    },
    'marital': {
        0: 'divorced',
        2: 'single',
        1: 'married',
        3: None
    },
    'education': {
        0: 'basic.4y',
        1: 'basic.6y',
        2: 'basic.9y',
        3: 'high.school',
        4: 'illiterate',
        5: 'professional.course',
        6: 'university.degree',
        7: None
    },
    'default': {
        0: 'no',
        1: 'yes',
        2: None
    },
    'housing': {
        0: 'no',
        1: 'yes',
        2: None
    },
    'loan': {
        0: 'no',
        1: 'yes',
        2: None
    },
    'contact': {
        0: 'cellular',
        1: 'telephone'
    },
    'month': {
        0: 'apr',
        1: 'aug',
        2: 'dec',
        3: 'jul',
        4: 'jun',
        5: 'mar',
        6: 'may',
        7: 'nov',
        8: 'oct',
        9: 'sep'
    },
    'day_of_week': {
        0: 'fri',
        1: 'mon',
        2: 'thu',
        3: 'tue',
        4: 'wed'
    },
    'poutcome': {
        0: 'failure',
        1: 'success',
        2: None
    },
    'y': {
        0: 'no',
        1: 'yes'
    }
},
'encode': {
    'job': {
        'admin.': 0,
        'entrepreneur': 2,
        'blue-collar': 1,
        'management': 4,
        'self-employed': 6,
        'retired': 5,
        'housemaid': 3,
        'student': 8,
        'services': 7,
        'technician': 9,
        'unemployed': 10,
        None: 11
    },
    'marital': {
        'divorced': 0,
        'single': 2,
        'married': 1,
        None: 3
    },
    'education': {
        'basic.4y': 0,
        'basic.6y': 1,
        'basic.9y': 2,
        'high.school': 3,
        'illiterate': 4,
        'professional.course': 5,
        'university.degree': 6,
        None: 7
    },
    'default': {
        'no': 0,
        'yes': 1,
        None: 2
    },
    'housing': {
        'no': 0,
        'yes': 1,
        None: 2
    },
    'loan': {
        'no': 0,
        'yes': 1,
        None: 2
    },
    'contact': {
        'cellular': 0,
        'telephone': 1
    },
    'month': {
        'apr': 0,
        'aug': 1,
        'dec': 2,
        'jul': 3,
        'jun': 4,
        'mar': 5,
        'may': 6,
        'nov': 7,
        'oct': 8,
        'sep': 9
    },
    'day_of_week': {
        'fri': 0,
        'mon': 1,
        'thu': 2,
        'tue': 3,
        'wed': 4
    },
    'poutcome': {
        'failure': 0,
        'success': 1,
        None: 2
    },
    'y': {
        'no': 0,
        'yes': 1
    }
}

}
