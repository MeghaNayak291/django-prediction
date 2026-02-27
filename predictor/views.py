from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
from .models import Prediction
from .forms import PredictionForm
import random


class HomeView(View):
    def get(self, request):
        predictions = Prediction.objects.all()[:5]
        context = {
            'predictions': predictions,
            'total_predictions': Prediction.objects.count(),
            'diseases': dict(Prediction.DISEASE_CHOICES)
        }
        return render(request, 'predictor/home.html', context)


class PredictView(View):
    def get(self, request):
        form = PredictionForm()
        return render(request, 'predictor/predict.html', {'form': form})

    def post(self, request):
        form = PredictionForm(request.POST, request.FILES)
        if form.is_valid():
            # Simulated ML prediction (replace with actual ML model)
            diseases = ['healthy', 'leaf_scorch', 'powdery_mildew', 'angular_leaf']
            disease = random.choice(diseases)
            confidence = random.uniform(85, 99)

            prediction = form.save(commit=False)
            prediction.disease_type = disease
            prediction.confidence = confidence
            prediction.save()

            return redirect('predictor:result', pk=prediction.id)
        return render(request, 'predictor/predict.html', {'form': form})


class ResultView(View):
    def get(self, request, pk):
        try:
            prediction = Prediction.objects.get(id=pk)
            return render(request, 'predictor/result.html', {'prediction': prediction})
        except Prediction.DoesNotExist:
            return redirect('predictor:home')


class HistoryView(View):
    def get(self, request):
        predictions = Prediction.objects.all()
        return render(request, 'predictor/history.html', {'predictions': predictions})
