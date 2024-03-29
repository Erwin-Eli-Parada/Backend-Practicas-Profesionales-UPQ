from rest_framework.routers import DefaultRouter
from .views.alumnoViews import AlumnoViewSet
from .views.datosViews import DatosViewSet
from .views.proyectoViews import proyectoViewSet
from .views.asesorExternoViews import AsesorExternoViewSet
from .views.asesorUPQViews import AsesorUPQViewSet
from .views.empresaViews import EmpresaViewSet
from .views.encuestaViews import EncuestaViewSet
from .views.estatusViews import EstatusViewSet
from .views.excelViews import ExcelViewSet
from .views.excelEncuestaViews import ExcelEncuestasViewSet
from .views.comentarioViews import ComentarioViewSet
from .views.excelComentarioViews import ExcelComentarioViewSet

router = DefaultRouter()

router.register(r'alumno',AlumnoViewSet,basename = 'alumnos')
router.register(r'proyecto',proyectoViewSet,basename = 'proyectos')
router.register(r'asesorExt',AsesorExternoViewSet,basename = 'asesorExt')
router.register(r'asesorUPQ',AsesorUPQViewSet,basename = 'asesorUPQ')
router.register(r'empresa',EmpresaViewSet,basename = 'empresa')
router.register(r'encuesta',EncuestaViewSet,basename = 'encuesta')
router.register(r'comentario',ComentarioViewSet,basename = 'comentario')
router.register(r'estatus',EstatusViewSet,basename = 'estatus')
router.register(r'archivo',ExcelViewSet,basename = 'archivo')
router.register(r'archivoEncuesta',ExcelEncuestasViewSet,basename = 'archivoEncuesta')
router.register(r'archivoComentario',ExcelComentarioViewSet,basename = 'archivoComentario')
# router.register(r'datos',DatosViewSet,basename = 'datos')

urlpatterns = router.urls