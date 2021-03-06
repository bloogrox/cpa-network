from django.urls import path
from .views.conversions import ConversionCreateView
from .views.offer import OfferCreateView
from .views.payout import PayoutCreateView
from .views.landing import LandingCreateView
from .views.offer_traffic_source import OfferTrafficSourceCreateView
from .views.advertiser import AdvertiserCreateAPIView

urlpatterns = [
    path(
        'conversions/',
        ConversionCreateView.as_view(), name='api-conversions'),
    path(
        'offers/',
        OfferCreateView.as_view(), name='api-offers'),
    path(
        'offers/<int:pk>/payouts/',
        PayoutCreateView.as_view(), name='api-payouts'),
    path(
        'offers/<int:pk>/landings/',
        LandingCreateView.as_view(), name='api-landings'),
    path(
        'offers/<int:pk>/traffic-sources/',
        OfferTrafficSourceCreateView.as_view(),
        name='api-offer-traffic-sources'),
    path(
        'advertisers/',
        AdvertiserCreateAPIView.as_view(), name='api-advertisers'),
]
