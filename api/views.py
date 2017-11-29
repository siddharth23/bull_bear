from django.shortcuts import render
from django.http import JsonResponse
from django.core.exceptions import *
from nsepy import get_history
from .serializers import shareSerializer
from datetime import date,datetime
from rest_framework import status
from .models import Share,Stock
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
@api_view(['GET'])
def get(request,symbol):
    start_date=request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    if(start_date==None):
        return JsonResponse({'status':'false','message':'start_date is empty'}, status=405)
    if (end_date == None):
        return JsonResponse({'status': 'false', 'message': 'end_date is empty'}, status=405)
    try:
        startdate = map(int, start_date.split('-'))
        enddate = map(int, end_date.split('-'))
        df=get_history(symbol,date(*startdate),date(*enddate))
        df.reset_index(level=0, inplace=True)
        df_records = df.to_dict('records')
        Stock.objects.get_or_create(symbol=symbol)
        new_stock=list(Stock.objects.filter(symbol=symbol))
        for record in df_records:
            Share.objects.get_or_create(
            symbol=new_stock[0], series=record['Series'], date=record['Date'], prev_close=record['Prev Close'],
            open=record['Open'], high=record['High'], low=record['Low'], last=record['Last'], close=record['Close'],
            vwap=record['VWAP'],
            volume=record['Volume'], turnover=record['Turnover'], trades=record['Trades'],
            deliverable_volume=record['Deliverable Volume'],
            percentage_deliverable=record['%Deliverble'])
        return Response(df.to_json())
    except TypeError as e:
        return JsonResponse({'status': 'false', 'message': e.__str__()}, status=405)

@api_view(['GET'])
def get_MFI(request,symbol):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    if (start_date == None):
        return JsonResponse({'status': 'false', 'message': 'start_date is empty'}, status=405)
    if (end_date == None):
        return JsonResponse({'status': 'false', 'message': 'end_date is empty'}, status=405)
    shares=list(Share.objects.filter(symbol=Stock(symbol)).all())
    serialized=shareSerializer(shares,many=True)
    return Response(serialized.data)

