# coding=utf-8
from flask.ext.babelex import lazy_gettext
from app.views.base import ModelViewWithAccess


class EnumValuesAdmin(ModelViewWithAccess):
    column_list = ('id', 'code', 'display', 'type')

    page_size = 50

    column_editable_list = ['display']
    column_searchable_list = ['code', 'display', 'type.display', 'type.code']
    column_filters = ('code', 'display', 'type.display')

    column_sortable_list = ('id', 'code', 'display', ('type', 'type.id'))

    column_details_list = ['id', 'code', 'display', 'type', 'type_values']

    column_labels = {
        'id': lazy_gettext('id'),
        'type': lazy_gettext('Type'),
        'code': lazy_gettext('Code'),
        'display': lazy_gettext('Display'),
        'type_values': lazy_gettext('Type Values'),
        'type.display': lazy_gettext('Type'),
    }
