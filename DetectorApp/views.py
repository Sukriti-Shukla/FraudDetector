from django.shortcuts import render

# Create your views here.

from .forms import InputForm
from sklearn.preprocessing import StandardScaler
from joblib import load
import numpy as np
import os
from .models import Input
from django.http import JsonResponse


# Get the directory where this file (views.py) is located
views_dir = os.path.dirname(__file__)

# Get the path to model.joblib inside this directory

# Load the model
# def index(request):
#     if request.method == 'POST':
#         form = InputForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return render(request, 'result.html')

#     else:
#         form = InputForm()

#     return render(request, 'index.html', {'form': form})
# def index(request):
#     if request.method == 'POST':
#         form = InputForm(request.POST)
#         if form.is_valid():
#             instance = form.save() 
#             model_path = os.path.join(views_dir, 'model.joblib')
#             ml_model = load(model_path)
#             # Create a feature vector from your instance fields
#             features = [getattr(instance, f'v{i}') for i in range(1, 29)]
#             features += [instance.time, instance.amount]
#             prediction = ml_model.predict([features])[0]
#             # Now pass this prediction to your template
#             return render(request, 'result.html', {'result': prediction})

#     else:
#         form = InputForm()

#     return render(request, 'index.html', {'form': form})

def index(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            instance = form.save() 
            model_path = os.path.join(views_dir, 'model.joblib')
            ml_model = load(model_path)
            # Create a feature vector from your instance fields
            features = [getattr(instance, f'v{i}') for i in range(1, 29)]
            features += [instance.time, instance.amount]
            prediction = int(ml_model.predict([features])[0]) # Convert to Python int
            # Now pass this prediction to your template
            return JsonResponse({'prediction': prediction})
    else:
        form = InputForm()
    return render(request, 'index.html', {'form': form})
def result(request):
    result = Input.objects.all()
    return render(request, 'result.html', {'result': result})