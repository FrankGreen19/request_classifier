"""add some data

Revision ID: f43cc77d7505
Revises: 47883de1bc46
Create Date: 2024-05-04 16:47:25.471946

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f43cc77d7505'
down_revision: Union[str, None] = '47883de1bc46'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.execute("""
        insert into request_classes (title, alias) values 
        ('Посещение врача', 'doctor_visit'),
        ('Оплата ГИБДД', 'gibdd_payment'),
        ('Оплата интернета', 'net_payment'),
        ('Заявление в школу', 'school_claim'),
        ('Оплата налогов', 'tax_payment')
    """)

    op.execute("""
            insert into request_class_links (title, link, request_class_id) values 
            ('Запись к врачу', 'https://uslugi.tatarstan.ru/mis/tatarstan/authenticate?callback_url=https%3A%2F%2Fuslugi'
                       '.tatarstan.ru%2Fmis%2Ftatarstan%2Finit%3Fglobalsid'
                       '%3D3e9b7076058b19640df10a67efa5abd8661d834e0d304&globalsid'
                       '=3e9b7076058b19640df10a67efa5abd8661d834e0d304', (select id from request_classes where alias = 'doctor_visit')),
            ('Стать донором', 'https://donorsearch.org/', (select id from request_classes where alias = 'doctor_visit')),
            ('Дежурные аптеки', 'https://farm.tatarstan.ru/24hourrharmacy.htm', (select id from request_classes where alias = 'doctor_visit'))
    """)

    op.execute("""
            insert into scenarios (request_class_id, activation_question) values 
            ((select id from request_classes where alias = 'doctor_visit'), 'Желаете записаться к врачу прямо сейчас?') 
    """)

    op.execute("""
                insert into scenario_steps (ordi, question, possible_answers, scenario_id) values 
                (1, 'Укажите Ваше имя, фамилию, отчество (при наличии)', '', (select id from scenarios where activation_question = 'Желаете записаться к врачу прямо сейчас?')),
                (2, 'Выберете медицинское учреждение', '["Городская больница 1", "Городская больница 2", "Городская больница 3"]', (select id from scenarios where activation_question = 'Желаете записаться к врачу прямо сейчас?')),
                (3, 'Выберете дату/время визита', '["2024-04-04 11:00", "2024-04-05 12:00", "2024-04-06 13:00"]', (select id from scenarios where activation_question = 'Желаете записаться к врачу прямо сейчас?')) 
    """)


def downgrade() -> None:
    op.execute('delete from scenario_steps')
    op.execute('delete from scenarios')
    op.execute('delete from request_class_links')
    op.execute('delete from request_classes')
