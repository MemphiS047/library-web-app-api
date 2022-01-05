from DB.alchemy_setup import ORM, engine
from sqlalchemy import Column, DateTime, Integer, String, select
from sqlalchemy.orm import Session

Base = ORM()
engine = engine() 

class PositionModel(Base):
    __tablename__ = "jobs"

    job_id              = Column(Integer, primary_key=True)
    job_title           = Column(String)
    Job_description     = Column(String)
    payment             = Column(Integer)
    job_type            = Column(String)

    def __init__(self, job_title, Job_description, payment, job_type):
        self.job_title = job_title
        self.Job_description = Job_description 
        self.payment = payment
        self.job_type = job_type

    def create_position(self):
        with Session(engine) as session:
            session.add(self)
            session.commit()

    def update_position(self, new_salary):
        with Session(engine) as session:
            session.query(self.__class__).filter(self.__class__.name == self.payment).update({'payment': new_salary})
            session.commit()

    def delete_position(self):
        with Session(engine) as session:
            session.delete(self)
            session.commit()

    @classmethod
    def get_all_positions(cls):
        with Session(engine) as session:
            result = session.execute(select(cls.job_id, cls.job_title, cls.Job_description, cls.payment, cls.job_type))
            return result

class JobApplicationModel(Base):
    __tablename__ = "job_applications"

    job_id  = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    respond = Column(String)


    def __init__(self, job_id, user_id, respond):
        self.job_id = job_id
        self.user_id = user_id
        self.respond = respond 

    def create_application(self):
        with Session(engine) as session:
            session.add(self)
            session.commit()

    @classmethod
    def get_job_application_by_user_id(cls, user_id):
        with Session(engine) as session:
            result = session.query(cls).filter_by(user_id=user_id).first()
            return result
