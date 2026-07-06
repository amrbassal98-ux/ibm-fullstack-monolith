from datetime import date, timedelta
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from django.views import View
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.db.models import Count
from django.contrib.auth import login
from django.contrib.auth.models import Group
from .forms import AgentSignUpForm

from .models import Customer, Interaction
from .forms import CustomerForm, InteractionForm

class IndexView(View):
    """
    Handles the landing matrix context splitting. Unauthenticated traffic views 
    the public landing page; authenticated traffic views the customer collection.
    """
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return render(request, "landing.html")
        
        customers = Customer.objects.all()
        return render(request, "index.html", {"customers": customers})

class AgentSignUpView(CreateView):
    """
    Renders the sign-up form and automatically provisions the registered 
    user with 'Agent' group permissions upon validation.
    """
    form_class = AgentSignUpForm
    template_name = "signup.html"
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        # Save the new user record
        user = form.save()
        
        # Atomically resolve and append the user to the Agents group
        try:
            agent_group = Group.objects.get(name="Agents")
            user.groups.add(agent_group)
        except Group.DoesNotExist:
            # Fallback if the group hasn't been created via Admin yet
            messages.warning(self.request, "Account created, but 'Agents' group not found. Contact Admin for permission provisioning.")
        
        # Establish an active session for the user immediately
        login(self.request, user)
        messages.success(self.request, "Registration successful. Welcome to the Agent Portal.")
        return redirect(self.success_url)


class CustomerCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """
    Enforces authorization to restrict customer initialization to Managers.
    """
    model = Customer
    form_class = CustomerForm
    template_name = "add.html"
    success_url = reverse_lazy("index")
    permission_required = "customer360.can_manage_customers"
    raise_exception = True

    def form_valid(self, form):
        messages.success(self.request, "Customer profile successfully initialized.")
        return super().form_valid(form)


class InteractionCreateView(LoginRequiredMixin, PermissionRequiredMixin, View):
    """
    Processes customer touchpoint interactions. Restricted to Agents.
    """
    permission_required = "customer360.can_log_interactions"
    raise_exception = True

    def get(self, request, cid, *args, **kwargs):
        customer = get_object_or_404(Customer, id=cid)
        form = InteractionForm()
        return render(request, "interact.html", {
            "form": form,
            "customer": customer,
            "channels": Interaction.ChannelChoices.choices,
            "directions": Interaction.DirectionChoices.choices
        })

    def post(self, request, cid, *args, **kwargs):
        customer = get_object_or_404(Customer, id=cid)
        form = InteractionForm(request.POST)
        if form.is_valid():
            interaction = form.save(commit=False)
            interaction.customer = customer
            interaction.save()
            messages.success(request, f"Logged interaction for {customer.name}.")
            return redirect("index")
        
        return render(request, "interact.html", {
            "form": form,
            "customer": customer,
            "channels": Interaction.ChannelChoices.choices,
            "directions": Interaction.DirectionChoices.choices
        })


class SummaryView(LoginRequiredMixin, View):
    """
    Generates rolling 30-day transactional metrics aggregated directly in-database.
    """
    def get(self, request, *args, **kwargs):
        time_threshold = date.today() - timedelta(days=30)
        interactions_queryset = Interaction.objects.filter(interaction_date__gte=time_threshold)
        total_count = interactions_queryset.count()
        
        metrics = (
            interactions_queryset.values("channel", "direction")
            .annotate(count=Count("id"))
            .order_by("channel")
        )
        
        channel_mapping = dict(Interaction.ChannelChoices.choices)
        direction_mapping = dict(Interaction.DirectionChoices.choices)
        
        for metric in metrics:
            metric['channel_display'] = channel_mapping.get(metric['channel'], metric['channel'])
            metric['direction_display'] = direction_mapping.get(metric['direction'], metric['direction'])

        return render(request, "summary.html", {
            "interactions": metrics,
            "count": total_count
        })


class CustomLoginView(LoginView):
    """
    Processes secure authentication requests.
    """
    template_name = "login.html"
    redirect_authenticated_user = True


class CustomLogoutView(LogoutView):
    """
    Flushes active user session configurations securely via POST requests.
    """
    next_page = reverse_lazy("index")

    def dispatch(self, request, *args, **kwargs):
        if request.method == "POST":
            messages.info(request, "You have been successfully logged out of the system.")
        return super().dispatch(request, *args, **kwargs)