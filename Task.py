from sqlalchemy.orm import relationship
from api import db

class Task(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    task_text = db.Column(db.String(150), index=True) 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    uu = relationship("User", uselist=False, back_populates="tt")