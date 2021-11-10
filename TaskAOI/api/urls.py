from django.conf.urls import url
from django.urls import path,include

#views
from django.db import router

#viewsets
from rest_framework.routers import SimpleRouter

#JWT
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import HomiyDetail, Homiylist, TalabaDetail, TalabaList,HomiyViewset,TalabaViewset
router = SimpleRouter()
router.register("Homiylar",HomiyViewset,basename='homiylar')
router.register('Talabalar',TalabaViewset,basename='talabalar')


# from rest_framework.schemas import get_schema_view #schima va dokumentla
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

#dokumitatsiya
schema_view = get_schema_view(
    openapi.Info(
        title='UIC API',
        description="Firdavs Dev ",
        default_version='v1',
        terms_of_service='https://www.google.com/policies/terms/',
        contact=openapi.Contact(email="xackercoder@gmail.com"),
        license=openapi.License(name='API lisensiyasi')
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)

urlpatterns = [
    #post
    path('homiy/',Homiylist.as_view(),name='homiy'),
    path('homiy/<int:pk>/',HomiyDetail.as_view(),name='homiy_id'),
    #login register ...
    path('api-auth/', include('rest_framework.urls')),
    
    #JWT
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    #user
    path('talaba/',TalabaList.as_view(),name='talaba'),
    path('talaba/<int:pk>/',TalabaDetail.as_view(),name='talaba_id'),
    
                    #schema and documentatsiya
    #swaggger
    # path('swagger/',schema_view.with_ui(
    #     'swagger',cache_timeout=0
    # ),name='schema-swagger-ui'),

    #redoc
    # path('redoc/',schema_view.with_ui(
    #     'redoc',cache_timeout=0
    # ),name='schema-redoc'),

    path('dj_rest_auth/',include('dj_rest_auth.urls')),

    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   
]
#coonect to viewset
urlpatterns += router.urls