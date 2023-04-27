from rest_framework.routers import DefaultRouter
from .views.alumnoViews import AlumnoViewSet
from .views.datosViews import DatosViewSet

router = DefaultRouter()

router.register(r'alumno',AlumnoViewSet,basename = 'alumnos')
router.register(r'datos',DatosViewSet,basename = 'datos')

urlpatterns = router.urls