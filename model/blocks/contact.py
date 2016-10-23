import sqlalchemy as sa
from model.base import cBlock, BASE, abst_key
import model.view.base

class cBlockContact(cBlock, model.view.base.cViewBlock):
    __tablename__ = "blocks_contacts"
    rec_id = sa.Column(sa.Integer, sa.ForeignKey('blocks.rec_id'), primary_key=True)
    __mapper_args__ = {'polymorphic_identity': 'BlockContact'}
    name = sa.Column(sa.Unicode(255))
    job = sa.Column(sa.Unicode(255))
    is_person = sa.Column(sa.Boolean)
    additional_info = sa.Column(sa.UnicodeText)

# Internal table for cBlockContact
class cContactDetails(BASE, abst_key):
    __tablename__ = "blocks_contacts_details"
    contact_id = sa.Column(sa.Integer, sa.ForeignKey('blocks_contacts.rec_id'))
    contact = sa.orm.relationship("cBlockContact", backref=sa.orm.backref('details', cascade="all,delete"))
    cont_type = sa.Column(sa.Unicode(255))
    cont_value = sa.Column(sa.Unicode(255))
    is_type_fixed = sa.Column(sa.Boolean)

