import sqlalchemy as sa

from .meta import Base

# TODO: understand this thing and move somewhere else
# I think I want to utilize transaction manager with pyramid_tm
# There is get_tm_session() in models.__init__. It looks nice.
from zope.sqlalchemy import ZopeTransactionExtension
DBSession = sa.orm.scoped_session(sa.orm.sessionmaker(extension=ZopeTransactionExtension()))



# base types - not for ORM purposes

# Any list have uid + name
class cBaseList():
    uid = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(255))

# Any document have uid + date
class cBaseDoc():
    uid = sa.Column(sa.Integer, primary_key=True)
    date = sa.Column(sa.DateTime)

# an item that can be bought
class cItem(Base, cBaseList):
    __tablename__ = 'items'

# a warehouse - just a reference to a physical vault
class cVault(Base, cBaseList):
    __tablename__ = 'vaults'

# defines a basic shipment
class cShipment(Base, cBaseDoc):
    __tablename__ = 'shipments'
    discriminator = sa.Column(sa.String(50))
    __mapper_args__ = {'polymorphic_identity': 'shipment', 'polymorphic_on': discriminator}
    vault_uid = sa.Column(sa.Integer, sa.ForeignKey('vaults.uid'))
    vault = sa.orm.relationship("cVault")

# defines a position within a shipment
class cShipmentPosition(Base):
    __tablename__ = 'shipment_position'
    uid = sa.Column(sa.Integer, primary_key=True)
    item_uid = sa.Column(sa.Integer, sa.ForeignKey('items.uid'))
    item = sa.orm.relationship("cItem")
    quantity = sa.Column(sa.Float(precision=3))

# a shipment from the supplier
class cShipmentIn(cShipment):
    __tablename__ = 'shipments_in'
    uid = sa.Column(sa.Integer, sa.ForeignKey('shipments.uid'), primary_key=True)
    __mapper_args__ = {'polymorphic_identity': 'shipmentin'}

# a shipment from the supplier
class cShipmentOut(cShipment):
    __tablename__ = 'shipments_out'
    uid = sa.Column(sa.Integer, sa.ForeignKey('shipments.uid'), primary_key=True)
    __mapper_args__ = {'polymorphic_identity': 'shipmentout'}