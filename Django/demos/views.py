from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'demos/index.html')

def cal(request):
  num1 = request.GET.get('num1')
  num2 = request.GET.get('num2')
  operators = request.GET.get('operators')
  
  # 2. 계산
  if operators == '+':
    result = int(num1) + int(num2)
  elif operators == '-':
    result = int(num1) - int(num2)
  elif operators == '*':
    result = int(num1) * int(num2)
  elif operators == '/':
    result = int(num1) / int(num2)
  else:
    result = 0
    
  # 3. 응답
  return render(request, 'demos/cal.html', {'result': result})