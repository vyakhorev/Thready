import colander
import deform.widget

from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

#import transaction
from thready.models.allmodels import DBSession, cItem


class ItemPage(colander.MappingSchema):
    name = colander.SchemaNode(colander.String())


class cMainForm:
    def __init__(self, request):
        self.request = request

    @property
    def item_form(self):
        schema = ItemPage()
        return deform.Form(schema, buttons=('submit', 'cancel', 'delete',))

    # css / js - I do not undestand who use it
    @property
    def reqts(self):
        return self.item_form.get_widget_resources()

    @view_config(route_name='main', renderer='../templates/main.pt')
    def main_view(self):
        items = DBSession.query(cItem).order_by(cItem.name).all()
        return dict(title='Main View', items=items)

    @view_config(route_name='item_add', renderer='../templates/item_addedit.pt')
    def item_add(self):
        form = self.item_form.render()

        if 'submit' in self.request.params:
            controls = self.request.POST.items()
            try:
                appstruct = self.item_form.validate(controls)
            except deform.ValidationFailure as e:
                # Form is NOT valid
                return dict(form=e.render())

            # Add a new item to the DB
            new_name = appstruct['name']
            DBSession.add(cItem(name=new_name))

            # redirect to the main view
            url = self.request.route_url('main')
            return HTTPFound(url)

        if 'cancel' in self.request.params:
            url = self.request.route_url('main')
            return HTTPFound(url)

        return dict(form=form)

    @view_config(route_name='item_view', renderer='../templates/item_view.pt')
    def item_view(self):
        # # WTF?..
        # if self.request.matchdict['uid'] == 'favicon.ico': return dict(item=None)
        uid = int(self.request.matchdict['uid'])
        item = DBSession.query(cItem).filter_by(uid=uid).one()
        return dict(citem=item)

    @view_config(route_name='item_edit', renderer='../templates/item_addedit.pt')
    def item_edit(self):
        uid = int(self.request.matchdict['uid'])
        item = DBSession.query(cItem).filter_by(uid=uid).one()

        item_form = self.item_form

        if 'submit' in self.request.params:
            controls = self.request.POST.items()
            try:
                appstruct = item_form.validate(controls)
            except deform.ValidationFailure as e:
                return dict(item=item, form=e.render())

            # Change the content and redirect to the main view
            item.name = appstruct['name']
            url = self.request.route_url('main', uid=uid)
            return HTTPFound(url)

        if 'cancel' in self.request.params:
            url = self.request.route_url('main')
            return HTTPFound(url)

        form = self.item_form.render(dict(
            uid=item.uid, name=item.name)
        )

        return dict(item=item, form=form)