from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect


class RedirectIfNotFoundMiddleware(object):
    def process_exception(self, _request, exception):
        if isinstance(exception, Http404):
            return HttpResponseRedirect(reverse('polls:index'))
