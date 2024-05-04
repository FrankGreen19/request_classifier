from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# Создаем базовый класс для объявления моделей
Base = declarative_base()


class RequestClass(Base):
    __tablename__ = 'request_classes'  # Имя таблицы в базе данных

    id = Column(Integer, primary_key=True)  # Первичный ключ
    title = Column(String(50), nullable=False)
    alias = Column(String(50), nullable=False)

    links = relationship('RequestClassLink')
    scenario = relationship('Scenario')


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
    possible_answers = Column(String(500), nullable=False)
    scenario_id = Column(Integer, ForeignKey('scenarios.id'))