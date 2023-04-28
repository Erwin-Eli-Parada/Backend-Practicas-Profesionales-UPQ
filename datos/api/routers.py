from rest_framework.routers import DefaultRouter
from .views.alumnoViews import AlumnoViewSet
from .views.datosViews import DatosViewSet
from .views.proyectoViews import proyectoViewSet

router = DefaultRouter()

router.register(r'alumno',AlumnoViewSet,basename = 'alumnos')
router.register(r'proyecto',proyectoViewSet,basename = 'proyectos')
# router.register(r'datos',DatosViewSet,basename = 'datos')

urlpatterns = router.urls