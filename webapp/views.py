# modules for creating class and getting database object
from django.views import generic
from .models import MasterIn, IssueIn, ConsumIn, WhouseIn, ItemIn
# to render a template & to
from django.shortcuts import render
# to use login_required
from django.contrib.auth.decorators import login_required #for fuction view
from django.contrib.auth.mixins import LoginRequiredMixin # for class based view
# to create ,update ,delete
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# to run coustom sql queries
from django.db import connection
# Create your views here.

# about view as function
def about(request):
    return render(request, 'webapp/about.html', {'dict_content':['Credits: ','Elon Musk']})
# index page
def index(request):
    template_name = 'webapp/index.html' #which template should i use to return?
    return render(request, template_name, {})

# class based views
# home view
class HomeView(LoginRequiredMixin, generic.ListView):
    login_url = '/login/'  # what is the login_url
    redirect_field_name = '/login/'
    template_name = 'webapp/home.html' #which template should i use to return?
    #context_object_name = 'all_items' # for List it return object_list to change it to our name object use this
    def get_queryset(self):
        return MasterIn.objects.all()

class MasterInAdd(CreateView):
    model = MasterIn
    fields = ['item_code', 'item_name', 'item_qty', 'item_rate', 'item_bal_qty', 'item_new_rate', 'whouse_code' ]
# product detail view
class DetailView(LoginRequiredMixin, generic.DetailView):
    login_url = '/login/'
    redirect_field_name = '/login/'
    model = MasterIn
    template_name = 'webapp/details.html'


class ConsumInView(LoginRequiredMixin, generic.ListView):
    login_url = '/login/'  # what is the login_url
    redirect_field_name = '/login/'
    template_name = 'webapp/consum.html' #which template should i use to return?
    #context_object_name = 'all_items' # for List it return object_list to change it to our name object use this
    def get_queryset(self):
        return ConsumIn.objects.all()

# to create a new ConsumIn --> buying something into Inventory
class ConsumInAdd(CreateView):
    model = ConsumIn
    fields = ['item_code', 'date_consum', 'item_consum_qty', 'item_consum_rate' ]

class IssueInView(LoginRequiredMixin, generic.ListView):
    login_url = '/login/'  # what is the login_url
    redirect_field_name = '/login/'
    template_name = 'webapp/issue.html' #which template should i use to return?
    #context_object_name = 'all_items' # for List it return object_list to change it to our name object use this
    def get_queryset(self):
        return IssueIn.objects.all()

# to create a new ConsumIn --> buying something into Inventory
class IssueInAdd(CreateView):
    model = IssueIn
    fields = ['item_code', 'date_issue', 'item_issue_qty', 'item_issue_rate' ]

class ItemInView(LoginRequiredMixin, generic.ListView):
    login_url = '/login/'  # what is the login_url
    redirect_field_name = '/login/'
    template_name = 'webapp/item.html' #which template should i use to return?
    #context_object_name = 'all_items' # for List it return object_list to change it to our name object use this
    def get_queryset(self):
        return ItemIn.objects.all()

class WhouseInView(LoginRequiredMixin, generic.ListView):
    login_url = '/login/'  # what is the login_url
    redirect_field_name = '/login/'
    template_name = 'webapp/whouse.html' #which template should i use to return?
    #context_object_name = 'all_items' # for List it return object_list to change it to our name object use this
    def get_queryset(self):
        return WhouseIn.objects.all()

# to add whouse
class WhouseInAdd(CreateView):
    model = WhouseIn
    fields = ['whouse_code', 'whouse_name', 'whouse_address', 'whouse_location', 'whouse_city',
            'whouse_phone', 'whouse_mobile', 'whouse_head_name', 'whouse_pincode' ]

class WhouseInUpdate(UpdateView):
    model = WhouseIn
    fields = ['whouse_code', 'whouse_name', 'whouse_address', 'whouse_location', 'whouse_city',
            'whouse_phone', 'whouse_mobile', 'whouse_head_name', 'whouse_pincode' ]

class WhouseInDelete(DeleteView):
    model = WhouseIn
    success_url = reverse_lazy('webapp:whouse')

def update_master(request):
    template_name = 'webapp/home.html' #which template should i use to return?
    with connection.cursor() as cursor:
        cursor.execute("DROP VIEW IF EXISTS `item_consume_list`;")
        cursor.execute("DROP VIEW IF EXISTS `item_wise_issued_list`;")
        cursor.execute("create VIEW `item_wise_issued_list` AS (select `issue_in`.`item_code` AS `item_code`,sum(`issue_in`.`Item_issue_qty`) AS `item_total_issues` \
        from `issue_in` group by `issue_in`.`item_code`);")
        cursor.execute("create VIEW `item_consume_list` AS select `consum_in`.`item_code` AS `item_code`,sum(`consum_in`.`Item_consum_qty`) AS `item_total_consum` \
        from `consum_in` group by `consum_in`.`item_code`;")
        cursor.execute("Update master_in a,item_wise_issued_list b \
        Set a.item_bal_qty = a.item_bal_qty +b.item_total_issues  Where a.item_code=b.item_code ;")
        cursor.execute("update master_in a,item_consume_list b set a.item_bal_qty=a.item_bal_qty - b.item_total_consum \
        where a.item_code=b.item_code;")
    return render(request, template_name, {})
