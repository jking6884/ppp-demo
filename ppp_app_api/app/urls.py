from django.contrib import admin
from django.conf.urls import url, include

import core.urls
import forgiveness_request.urls
import loan.urls

urlpatterns = [
    url(r'admin/', admin.site.urls),

    url(r'^api/', include(core.urls)),
    url(r'^api/', include(forgiveness_request.urls)),
    url(r'^api/', include(loan.urls)),
]
