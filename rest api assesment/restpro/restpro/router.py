from myapi.viewsets import userapiviews
from rest_framework import routers

router = routers.DefaultRouter()
router.register('user', userapiviews)