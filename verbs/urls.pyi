from . import views as views
from .main import choices as choices, export as export, index as index
from _typeshed import Incomplete

handler404 = views.error_404
handler500 = views.error_500
urlpatterns: Incomplete
