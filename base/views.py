from django.shortcuts import render
from agriculture.models import *
from logistics.models import Expenses as ExpenseLog, Revenue as RevenueLog, SubcategoryLog
from merchandise.models import Expenses as ExpenseMer, Revenue as RevenueMer, SubcategoryMer
from django.http import HttpResponse
import json
from django.db.models import Sum
import datetime

# Create your views here.

def homepage(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def dashboard(request):
    now = datetime.datetime.now()

    # Agriculture expense filter
    total_expense_today = Expenses.objects.filter(
        date__day=now.day
    ).aggregate(total_expense_today=Sum('amount'))['total_expense_today']
    if total_expense_today == None:
        total_expense_today = 0

    total_expense_week = Expenses.objects.filter(
        date__week=now.today().isocalendar()[1], 
    ).aggregate(total_expense_week=Sum('amount'))['total_expense_week']
    if total_expense_week == None:
        total_expense_week = 0

    total_expense_month = Expenses.objects.filter(
        date__month=now.month, 
    ).aggregate(total_expense_month=Sum('amount'))['total_expense_month']
    if total_expense_month == None:
        total_expense_month = 0

    total_expense_year = Expenses.objects.filter(
        date__year=now.year, 
    ).aggregate(total_expense_year=Sum('amount'))['total_expense_year']
    if total_expense_year == None:
        total_expense_year = 0

    # Agriculture revenue filter
    total_revenue_today = Revenue.objects.filter(
        date__day=now.day
    ).aggregate(total_revenue_today=Sum('amount'))['total_revenue_today']
    if total_revenue_today == None:
        total_revenue_today = 0

    total_revenue_week = Revenue.objects.filter(
        date__week=now.today().isocalendar()[1], 
    ).aggregate(total_revenue_week=Sum('amount'))['total_revenue_week']
    if total_revenue_week == None:
        total_revenue_week = 0

    total_revenue_month = Revenue.objects.filter(
        date__month=now.month, 
    ).aggregate(total_revenue_month=Sum('amount'))['total_revenue_month']
    if total_revenue_month == None:
        total_revenue_month = 0

    total_revenue_year = Revenue.objects.filter(
        date__year=now.year, 
    ).aggregate(total_revenue_year=Sum('amount'))['total_revenue_year']
    if total_revenue_year == None:
        total_revenue_year = 0

    # Agriculture profit
    profit_today = total_revenue_today - total_expense_today
    profit_week = total_revenue_week - total_expense_week
    profit_month = total_revenue_month - total_expense_month
    profit_year = total_revenue_year - total_expense_year


    # Logistics expense filter
    total_expense_log_today = ExpenseLog.objects.filter(
        date__day=now.day
    ).aggregate(total_expense_log_today=Sum('amount'))['total_expense_log_today']
    if total_expense_log_today == None:
        total_expense_log_today = 0

    total_expense_log_week = ExpenseLog.objects.filter(
        date__week=now.today().isocalendar()[1], 
    ).aggregate(total_expense_log_week=Sum('amount'))['total_expense_log_week']
    if total_expense_log_week == None:
        total_expense_log_week = 0

    total_expense_log_month = ExpenseLog.objects.filter(
        date__month=now.month, 
    ).aggregate(total_expense_log_month=Sum('amount'))['total_expense_log_month']
    if total_expense_log_month == None:
        total_expense_log_month = 0

    total_expense_log_year = ExpenseLog.objects.filter(
        date__year=now.year, 
    ).aggregate(total_expense_log_year=Sum('amount'))['total_expense_log_year']
    if total_expense_log_year == None:
        total_expense_log_year = 0

    # Logistics revenue filter
    total_revenue_log_today = RevenueLog.objects.filter(
        date__day=now.day
    ).aggregate(total_revenue_log_today=Sum('amount'))['total_revenue_log_today']
    if total_revenue_log_today == None:
        total_revenue_log_today = 0

    total_revenue_log_week = RevenueLog.objects.filter(
        date__week=now.today().isocalendar()[1], 
    ).aggregate(total_revenue_log_week=Sum('amount'))['total_revenue_log_week']
    if total_revenue_log_week == None:
        total_revenue_log_week = 0

    total_revenue_log_month = RevenueLog.objects.filter(
        date__month=now.month, 
    ).aggregate(total_revenue_log_month=Sum('amount'))['total_revenue_log_month']
    if total_revenue_log_month == None:
        total_revenue_log_month = 0

    total_revenue_log_year = RevenueLog.objects.filter(
        date__year=now.year, 
    ).aggregate(total_revenue_log_year=Sum('amount'))['total_revenue_log_year']
    if total_revenue_log_year == None:
        total_revenue_log_year = 0

    # Logistics profit
    profit_log_today = total_revenue_log_today - total_expense_log_today
    profit_log_week = total_revenue_log_week - total_expense_log_week
    profit_log_month = total_revenue_log_month - total_expense_log_month
    profit_log_year = total_revenue_log_year - total_expense_log_year

    # Merchandise expense filter
    total_expense_mer_today = ExpenseMer.objects.filter(
        date__day=now.day
    ).aggregate(total_expense_mer_today=Sum('amount'))['total_expense_mer_today']
    if total_expense_mer_today == None:
        total_expense_mer_today = 0

    total_expense_mer_week = ExpenseMer.objects.filter(
        date__week=now.today().isocalendar()[1], 
    ).aggregate(total_expense_mer_week=Sum('amount'))['total_expense_mer_week']
    if total_expense_mer_week == None:
        total_expense_mer_week = 0

    total_expense_mer_month = ExpenseMer.objects.filter(
        date__month=now.month, 
    ).aggregate(total_expense_mer_month=Sum('amount'))['total_expense_mer_month']
    if total_expense_mer_month == None:
        total_expense_mer_month = 0

    total_expense_mer_year = ExpenseMer.objects.filter(
        date__year=now.year, 
    ).aggregate(total_expense_mer_year=Sum('amount'))['total_expense_mer_year']
    if total_expense_mer_year == None:
        total_expense_mer_year = 0

    # Merchandise revenue filter
    total_revenue_mer_today = RevenueMer.objects.filter(
        date__day=now.day
    ).aggregate(total_revenue_mer_today=Sum('amount'))['total_revenue_mer_today']
    if total_revenue_mer_today == None:
        total_revenue_mer_today = 0

    total_revenue_mer_week = RevenueMer.objects.filter(
        date__week=now.today().isocalendar()[1], 
    ).aggregate(total_revenue_mer_week=Sum('amount'))['total_revenue_mer_week']
    if total_revenue_mer_week == None:
        total_revenue_mer_week = 0

    total_revenue_mer_month = RevenueMer.objects.filter(
        date__month=now.month, 
    ).aggregate(total_revenue_mer_month=Sum('amount'))['total_revenue_mer_month']
    if total_revenue_mer_month == None:
        total_revenue_mer_month = 0

    total_revenue_mer_year = RevenueMer.objects.filter(
        date__year=now.year, 
    ).aggregate(total_revenue_mer_year=Sum('amount'))['total_revenue_mer_year']
    if total_revenue_mer_year == None:
        total_revenue_mer_year = 0

    # Merchandise profit
    profit_mer_today = total_revenue_mer_today - total_expense_mer_today
    profit_mer_week = total_revenue_mer_week - total_expense_mer_week
    profit_mer_month = total_revenue_mer_month - total_expense_mer_month
    profit_mer_year = total_revenue_mer_year - total_expense_mer_year

    context = {
        # Agriculture context
        'total_expense_today': total_expense_today,
        'total_expense_week': total_expense_week,
        'total_expense_month': total_expense_month,
        'total_expense_year': total_expense_year,

        'total_revenue_today': total_revenue_today,
        'total_revenue_week': total_revenue_week,
        'total_revenue_month': total_revenue_month,
        'total_revenue_year': total_revenue_year,

        'profit_today': profit_today,
        'profit_week': profit_week,
        'profit_month': profit_month,
        'profit_year': profit_year,

        # Logistics context
        'total_expense_log_today': total_expense_log_today,
        'total_expense_log_week': total_expense_log_week,
        'total_expense_log_month': total_expense_log_month,
        'total_expense_log_year': total_expense_log_year,

        'total_revenue_log_today': total_revenue_log_today,
        'total_revenue_log_week': total_revenue_log_week,
        'total_revenue_log_month': total_revenue_log_month,
        'total_revenue_log_year': total_revenue_log_year,

        'profit_log_today': profit_log_today,
        'profit_log_week': profit_log_week,
        'profit_log_month': profit_log_month,
        'profit_log_year': profit_log_year,

        # Merchandise context
        'total_expense_mer_today': total_expense_mer_today,
        'total_expense_mer_week': total_expense_mer_week,
        'total_expense_mer_month': total_expense_mer_month,
        'total_expense_mer_year': total_expense_mer_year,

        'total_revenue_mer_today': total_revenue_mer_today,
        'total_revenue_mer_week': total_revenue_mer_week,
        'total_revenue_mer_month': total_revenue_mer_month,
        'total_revenue_mer_year': total_revenue_mer_year,

        'profit_mer_today': profit_mer_today,
        'profit_mer_week': profit_mer_week,
        'profit_mer_month': profit_mer_month,
        'profit_mer_year': profit_mer_year,
    }
    return render(request, 'dashboard.html', context=context)

def get_subcategory_agric(request):
    id = request.GET.get('id', '')
    result = list(Subcategory.objects.filter(category_id=int(id)).values('id', 'name'))
    return HttpResponse(json.dumps(result), content_type='application/json')

def get_subcategory_log(request):
    id = request.GET.get('id', '')
    result = list(SubcategoryLog.objects.filter(category_id=int(id)).values('id', 'name'))
    return HttpResponse(json.dumps(result), content_type='application/json')

def get_subcategory_mer(request):
    id = request.GET.get('id', '')
    result = list(SubcategoryMer.objects.filter(category_id=int(id)).values('id', 'name'))
    return HttpResponse(json.dumps(result), content_type='application/json')