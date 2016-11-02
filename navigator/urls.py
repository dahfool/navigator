from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.core.urlresolvers import reverse_lazy


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', RedirectView.as_view(url=reverse_lazy('markets:home')), name="home"),
    url(r'^markets/', include('markets.urls'), name="markets"),
    url(r'^products/', include('products.urls'), name="products"),
    url(r'^geography/', include('geography.urls'), name="geography"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
