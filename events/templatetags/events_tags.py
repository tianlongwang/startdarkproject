from django import template
from events.models import Attendance

register = template.Library()


def event(context, e):
    to_return = {
        'event' : e,
        #'request' : context['request']
    }
    if context['user'].is_authenticated():
        try:
            Attendance.objects.get(event=event,user=context['user'])
            attending = True
        except Attendance.DoesNotExist:
            attending = False
        to_return.update({
            'attending' : attending,
            'authenticated' : True,
        })
    else:
        to_return['authenticted'] = False
    return to_return

register.inclusion_tag('events/event.html', takes_context=True)(event)
