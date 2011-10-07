from django.conf.urls.defaults import patterns
from django.views.generic.simple import direct_to_template
from django.views.generic.create_update import update_object, delete_object

from apps.wiki.models import WikiItem


urlpatterns = patterns('apps.wiki.views',
    (r'^$', 'show_all_wiki_items'),
    (r'^novo_item/$', 'add_wiki_item'),
    (r'^item_editado_com_sucesso/$',
        direct_to_template, {'template': 'wiki_item_successfully_updated.html'}
    ),
    (r'^item_excluido_com_sucesso/$',
        direct_to_template, {'template': 'wiki_item_successfully_deleted.html'}
    ),
    (r'^novo_item/adicionado_com_sucesso/$',
        direct_to_template, {'template': 'wiki_item_successfully_added.html'}
    ),
    (r'^(?P<wiki_item_slug>[\w_-]+)/$', 'view_wiki_item'),
    (r'^(?P<slug>[\w_-]+)/editar/$', update_object,
        {'model': WikiItem, 'template_name': 'edit_wiki_item.html',
        'post_save_redirect': '/wiki/item_editado_com_sucesso/',
        'login_required': True}
    ),
    (r'^(?P<slug>[\w_-]+)/excluir/$', delete_object,
        {'model': WikiItem, 'template_name': 'delete_wiki_item.html',
        'post_delete_redirect': '/wiki/item_excluido_com_sucesso/',
        'login_required': True}
    ),
)
