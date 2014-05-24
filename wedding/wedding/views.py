from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from .models import Person, Invitation

class DotExpandedDict(dict):
    """
    A special dictionary constructor that takes a dictionary in which the keys
    may contain dots to specify inner dictionaries. It's confusing, but this
    example should make sense.

    >>> d = DotExpandedDict({'person.1.firstname': ['Simon'], \
            'person.1.lastname': ['Willison'], \
            'person.2.firstname': ['Adrian'], \
            'person.2.lastname': ['Holovaty']})
    >>> d
    {'person': {'1': {'lastname': ['Willison'], 'firstname': ['Simon']}, '2': {'lastname': ['Holovaty'], 'firstname': ['Adrian']}}}
    >>> d['person']
    {'1': {'lastname': ['Willison'], 'firstname': ['Simon']}, '2': {'lastname': ['Holovaty'], 'firstname': ['Adrian']}}
    >>> d['person']['1']
    {'lastname': ['Willison'], 'firstname': ['Simon']}

    # Gotcha: Results are unpredictable if the dots are "uneven":
    >>> DotExpandedDict({'c.1': 2, 'c.2': 3, 'c': 1})
    {'c': 1}
    """
    def __init__(self, key_to_list_mapping):
        for k, v in key_to_list_mapping.items():
            current = self
            bits = k.split('.')
            for bit in bits[:-1]:
                current = current.setdefault(bit, {})
            # Now assign value to current position
            try:
                current[bits[-1]] = v
            except TypeError: # Special-case if current isn't a dict.
                current = {bits[-1]: v}


def lookup(request):
    first_name = request.GET.get('first_name')
    last_name = request.GET.get('last_name')
    person = get_object_or_404(
        Person,
        first_name__iexact=first_name,
        last_name__iexact=last_name
    )

    context = {
        'invitation': person.invitation
    }

    if person.invitation.responded:
        template = 'responded.html'
    else:
        template = 'rsvp.html'

    return render_to_response(template, context, RequestContext(request))

def save(request):
    invitation = get_object_or_404(
        Invitation,
        id=request.POST['invitation_id']
    )

    persons = DotExpandedDict(request.POST)

    index = 0
    for person in invitation.people.all():
        def p_attr(name):
            "Closure to make getting attrs from persons easier"
            return persons['person'][str(index)][name]

        person.attending = True if p_attr('attending') == '1' else False
        person.first_name = p_attr('first_name')
        person.last_name = p_attr('last_name')
        person.dietary_restrictions = p_attr('dietary_restrictions')
        person.save()
        index += 1

    invitation.responded = True
    invitation.save()

    return render_to_response('thanks.html')
