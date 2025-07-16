from sqlalchemy import Column, Integer, Float, String
from app.database.session import Base

class Calculation(Base):
    __tablename__ = "calculations"

    id = Column(Integer, primary_key=True, index=True)
    a = Column(Float, nullable=False)
    b = Column(Float, nullable=False)
    type = Column(String, nullable=False)
    result = Column(Float, nullable=True)
    user_id = Column(Integer, nullable=True)  # Included per assignment, but no ForeignKey
