from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from blog.models import Incident
from users.forms import IncidentForm, IncidentUpdateForm
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    DeleteView
)

def home(request):
    context = {
        'incidents': Incident.objects.all(),
    }
    return render(request, 'blog/home.html', context)

def natural_disasters(request):
    # Add any context data you want to pass to the template
    return render(request, 'blog/natural_disasters.html')

def incident_list(request):
    search_query = request.GET.get('q')
    if search_query:
        # Filter the incidents based on the search query
        incidents = Incident.objects.filter(
            Q(title__icontains=search_query) |  # Filter by title (case-insensitive)
            Q(description__icontains=search_query)  # Filter by description (case-insensitive)
        ).order_by('-date_reported')
    else:
        # If no search query, display all incidents
        incidents = Incident.objects.order_by('-date_reported')

    return render(request, 'blog/incident_list.html', {'incidents': incidents})

@login_required
def report_incident(request):
    if request.method == 'POST':
        form = IncidentForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            print("Incident created:", form.instance)  # Add this line to check
            return redirect('incident_list')
    else:
        form = IncidentForm()
    return render(request, 'blog/incident_report.html', {'form': form})

class PostListView(ListView):
    model = Incident
    template_name = 'blog/incident_list.html'
    context_object_name = 'incidents'
    ordering = ['-date_reported']
    paginate_by = 5

class UserPostListView(ListView):
    model = Incident
    template_name = 'blog/user_incident_list.html'
    context_object_name = 'incidents'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Incident.objects.filter(author=user).order_by('-date_reported')

class PostDetailView(DetailView):
    model = Incident

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Incident
    form_class = IncidentUpdateForm
    template_name = 'blog/update_incident_report.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        # Store the initial picture in the form_kwargs dictionary
        kwargs['initial_picture'] = self.object.pictures
        return kwargs

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    def get_success_url(self):
        return reverse('incident_list')

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Incident
    template_name = 'blog/post_confirm_delete.html'  # Specify the template name
    success_url = reverse_lazy('incident_list')  # Update this to your desired URL name for the incident list page

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
