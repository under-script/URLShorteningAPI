from rest_framework import viewsets

from URLShorteningAPI import settings
from .models import Shorten
from .serializers import ShortenSerializer
from django.shortcuts import redirect


class ShortenViewSet(viewsets.ModelViewSet):
    queryset = Shorten.objects.all()
    serializer_class = ShortenSerializer


def my_redirect_view(request, code):
    # Extracted code is available in the 'code' variable
    print(f"Extracted code: {code}")
    shorten_obj = Shorten.objects.filter(short_code=code).only('long_url').first()
    if shorten_obj:
        return redirect(shorten_obj.long_url)
    else:
        # Handle the case where the short code does not exist
        return redirect('/')



