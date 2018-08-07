from django.shortcuts import render
from django.views.generic import TemplateView

from manager.models import Worker


class WorkerListView(TemplateView):
    template_name = "worker_list.html"

    def get(self, request, *args, **keyword):
        context = super(WorkerListView, self).get_context_data(**keyword)

        workers = Worker.objects.all()
        context['workers'] = workers

        return render(self.request, self.template_name, context)
