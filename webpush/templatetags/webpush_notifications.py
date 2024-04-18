from django import template

from webpush.utils import get_templatetag_context

register = template.Library()


@register.filter
@register.inclusion_tag('webpush_header.html', takes_context=True)
def webpush_header(context):
    template_context = get_templatetag_context(context)
    return template_context


@register.filter
@register.inclusion_tag('webpush_button.html', takes_context=True)
def webpush_button(
    context,
    with_subscribe_label="Subscribe",
    with_unsubscribe_label="Unsubscribe",
    with_success_label="Success",
    with_class=None
):
    template_context = get_templatetag_context(context)
    if with_class:
        template_context['class'] = with_class
    template_context["subscribe_label"] = with_subscribe_label
    template_context["unsubscribe_label"] = with_unsubscribe_label
    template_context["success_label"] = with_success_label
    return template_context
