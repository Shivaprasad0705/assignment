from django.shortcuts import render



from django.http import HttpResponseBadRequest

def index(request):
    return render(request, 'factorial/index.html')

def calculate_factorial(request):
    if request.method == 'POST':
        try:
            number = int(request.POST.get('number'))
            if 1 <= number <= 10:
                factorial = 1
                for i in range(2, number + 1):
                    factorial *= i
                return render(request, 'factorial/result.html', {'number': number, 'factorial': factorial})
            else:
                return HttpResponseBadRequest('Number must be between 1 and 10.')
        except ValueError:
            return HttpResponseBadRequest('Invalid input.')
    else:
        return HttpResponseBadRequest('Method not allowed.')
