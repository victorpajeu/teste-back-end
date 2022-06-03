from rest_framework import routers

# viewsets
from students.api.viewsets import StudentViewSet

router = routers.DefaultRouter()

router.register('students', StudentViewSet)


default_routers = router.urls
