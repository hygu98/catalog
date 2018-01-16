from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


class PantryAddress(Base):
    __tablename__ = 'pantry_address'

    id = Column(Integer, primary_key=True)
    address = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'address': self.address,
            'id': self.id,
        }


class PantryItem(Base):
    __tablename__ = 'pantry_item'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    price = Column(String(8))
    foodGroup = Column(String(250))
    PantryAddress_id = Column(Integer, ForeignKey('pantry_address.id'))
    PantryAddress = relationship(PantryAddress)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'price': self.price,
            'foodGroup': self.foodGroup,
        }


engine = create_engine('sqlite:///pantry.db')


Base.metadata.create_all(engine)
