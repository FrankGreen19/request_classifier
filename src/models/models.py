from sqlalchemy import Column, Integer, String, Table, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from src.dto.request_class_dto import RequestClassDTO
import ast

# Создаем базовый класс для объявления моделей
Base = declarative_base()

class RequestClass(Base):
    __tablename__ = 'request_classes'  # Имя таблицы в базе данных

    CLASS_DOCTOR_VISIT = 'doctor_visit'
    CLASS_GIBDD_PAYMENT = 'gibdd_payment'
    CLASS_NET_PAYMENT = 'net_payment'
    CLASS_SCHOOL_CLAIM = 'school_claim'
    CLASS_TAX_PAYMENT = 'tax_payment'

    classes_dict = {
        0: CLASS_DOCTOR_VISIT,
        1: CLASS_GIBDD_PAYMENT,
        2: CLASS_NET_PAYMENT,
        3: CLASS_SCHOOL_CLAIM,
        4: CLASS_TAX_PAYMENT,
    }

    id = Column(Integer, primary_key=True)  # Первичный ключ
    title = Column(String(50), nullable=False)
    alias = Column(String(50), nullable=False)

    links = relationship('RequestClassLink')
    scenario = relationship('Scenario')

    def to_dto(self):
        links = []
        for link in self.links:
            links.append({'url': link.link, 'title': link.title})

        scenario_steps = []
        for step in self.scenario[0].scenario_steps:
            print(step.possible_answers)
            if step.possible_answers is None:
                possible_answers = None
            else:
                possible_answers = ast.literal_eval(step.possible_answers)

            scenario_steps.append({
                'question': step.question,
                'possible_answers': possible_answers
            })

        return RequestClassDTO(
            request_class_title=self.title,
            links=links,
            scenario_activation_question=self.scenario[0].activation_question,
            scenario_steps=scenario_steps
        )


class RequestClassLink(Base):
    __tablename__ = 'request_class_links'  # Имя таблицы в базе данных

    id = Column(Integer, primary_key=True)  # Первичный ключ
    title = Column(String(50), nullable=False)
    link = Column(String(500), nullable=False)
    request_class_id = Column(Integer, ForeignKey('request_classes.id'))


class Scenario(Base):
    __tablename__ = 'scenarios'  # Имя таблицы в базе данных

    id = Column(Integer, primary_key=True)  # Первичный ключ
    activation_question = Column(String(100), nullable=False)
    request_class_id = Column(Integer, ForeignKey('request_classes.id'))

    scenario_steps = relationship('ScenarioStep')


class ScenarioStep(Base):
    __tablename__ = 'scenario_steps'  # Имя таблицы в базе данных

    id = Column(Integer, primary_key=True)  # Первичный ключ
    ordi = Column(Integer, nullable=False)
    question = Column(String(100), nullable=False)
    possible_answers = Column(String(500), nullable=True)
    scenario_id = Column(Integer, ForeignKey('scenarios.id'))