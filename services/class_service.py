import classes

classes_data = {
    classes.CLASS_DOCTOR_VISIT: {
        'links': [
            {
                'url': 'https://uslugi.tatarstan.ru/mis/tatarstan/authenticate?callback_url=https%3A%2F%2Fuslugi'
                       '.tatarstan.ru%2Fmis%2Ftatarstan%2Finit%3Fglobalsid'
                       '%3D3e9b7076058b19640df10a67efa5abd8661d834e0d304&globalsid'
                       '=3e9b7076058b19640df10a67efa5abd8661d834e0d304',
                'title': 'Запись к врачу'
            },
            {
                'url': 'https://donorsearch.org/',
                'title': 'Стать донором'
            },
            {
                'url': 'https://farm.tatarstan.ru/24hourrharmacy.htm',
                'title': 'Дежурные аптеки'
            }
        ],
        'scenario_activation_question': 'Желаете записаться к врачу прямо сейчас?',
        'scenario_steps': [
            {
                'question': 'Укажите Ваше имя, фамилию, отчество (при наличии)'
            },
            {
                'question': 'Выберете медицинское учреждение',
                'possible_answers': [
                    'Городская больница 1',
                    'Городская больница 2',
                    'Городская больница 3',
                ]
            },
            {
                'question': 'Выберете дату/время визита',
                'possible_answers': [
                    '2024-04-04 11:00',
                    '2024-04-05 12:00',
                    '2024-04-06 13:00',
                ]
            }
        ],
    },
    classes.CLASS_SCHOOL_CLAIM: {
        'answers': [
            {
                'url': 'https://uslugi.tatarstan.ru/education/school',
                'title': 'Подача заявления на прием в школу'
            }
        ],
        'scenario_activation_question': None,
        'scenario_steps': None,
    }
}