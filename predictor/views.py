<<<<<<< HEAD
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
=======
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.core.files.storage import default_storage
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import timedelta

from .ml_engine import predict_image
from .models import Prediction

import os


# ---------------- HOME ----------------

@login_required
def home(request):
    return render(request, "home.html")


# Decorative public landing page (no login required)
def decor_view(request):
    return render(request, "decor.html")


# ---------------- PREDICT API ----------------

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def predict_api(request):

    image = request.FILES.get('image')

    if not image:
        return Response({"error": "No image uploaded"}, status=400)

    # Save temporary file
    path = default_storage.save("temp.jpg", image)
    full_path = os.path.join("media", path)

    # Run ML prediction
    result = predict_image(full_path)

    # 🔥 Auto delete predictions older than 30 days
    expiry_date = timezone.now() - timedelta(days=30)
    Prediction.objects.filter(created_at__lt=expiry_date).delete()

    # Save new prediction
    Prediction.objects.create(
        user=request.user,
        image_name=image.name,
        prediction=result["prediction"],
        confidence=result["confidence"]
    )

    # Delete temp file
    default_storage.delete(path)

    return Response(result)


# ---------------- SIGNUP ----------------

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, "signup.html", {"form": form})


# ---------------- HISTORY ----------------

@login_required
def history_view(request):
    predictions = Prediction.objects.filter(user=request.user).order_by('-created_at')
    return render(request, "history.html", {"predictions": predictions})

@login_required
def profile_view(request):
    return render(request, "profile.html")
>>>>>>> 009df0ffc57ddd5736de8738092067bf21f48c79
