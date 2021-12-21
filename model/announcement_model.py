from DB.alchemy_setup import ORM, engine
from sqlalchemy import Column, DateTime, Integer, String, select
from sqlalchemy.orm import Session

Base = ORM()
engine = engine() 

class AnnouncementModel(Base):

    __tablename__ = "announcements"

    announce_id       = Column(Integer, primary_key=True)
    announcement_title = Column(String)
    announcer         = Column(String)
    message           = Column(String)
    announce_datetime = Column(DateTime)
    last_edit         = Column(DateTime)

    def __init__(self, announce_id, announcer, message, announce_datetime, last_edit):
        self.announce_id = announce_id
        self.announcer = announcer
        self.message = message
        self.announce_datetime = announce_datetime
        self.last_edit = last_edit
    
    def create_announcement(self):
        pass

    def update_announcement(self):
        pass

    def delete_book(self):
        pass

    @classmethod
    def get_all_announcements(cls):
        result = Session(engine).execute(select(cls.announce_id, cls.announcement_title, cls.announcer, cls.message, cls.announce_datetime, cls.last_edit))
        return result
