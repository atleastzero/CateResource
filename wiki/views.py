from django.shortcuts import render
from django.views.generic.list import ListView

class WikiPageListView(ListView):
    """ Renders a list of all available WikiPages """
    model = WikiPage

    def get(self, request):
        """ GET a list of WikiPages. """
        wiki_pages = self.get_queryset().all()
        return render(request, 'wiki_page_list.html', {
            wiki_pages
        })