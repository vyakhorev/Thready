"""
The simpliest possible block to test the idea
"""

import sqlalchemy as sa
from model.base import cBlock, BASE, abst_key
import model.view.base

class cBlockNote(cBlock, model.view.base.cViewBlock):
    __tablename__ = "blocks_notes"
    rec_id = sa.Column(sa.Integer, sa.ForeignKey('blocks.rec_id'), primary_key=True)
    __mapper_args__ = {'polymorphic_identity': 'BlockNote'}
    text = sa.Column(sa.Unicode(255))

