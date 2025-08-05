from .models import Sale
from django.db.models import Sum
from django.db.models.functions import TruncMonth
import pandas as pd
from django.shortcuts import render
import json
from django.contrib.auth.decorators import login_required
@login_required
def chart_view(request):
    # Group sales by month
    sales_data = (
        Sale.objects
        .annotate(month=TruncMonth('date'))
        .values('month')
        .annotate(total=Sum('amount'))
        .order_by('month')
    )

    labels = [s['month'].strftime('%b %Y') for s in sales_data]
    data = [s['total'] for s in sales_data]

    context = {
        'labels': json.dumps(labels),
        'data': json.dumps(data)
    }
    return render(request, 'dashboard/chart.html', context)

@login_required
def excel_chart_view(request):
    # Load Excel file
    excel_path = 'dashboard/static/sales.xlsx'
    df = pd.read_excel(excel_path, engine='openpyxl')

    # Convert date column to datetime
    df['Date'] = pd.to_datetime(df['Date'])

    # Group by month
    monthly_sales = df.groupby(df['Date'].dt.to_period('M'))['Amount'].sum().reset_index()
    monthly_sales['Date'] = monthly_sales['Date'].dt.strftime('%b %Y')

    labels = monthly_sales['Date'].tolist()
    data = monthly_sales['Amount'].tolist()

    return render(request, 'dashboard/chart_excel.html', {
        'labels': json.dumps(labels),
        'data': json.dumps(data)
    })