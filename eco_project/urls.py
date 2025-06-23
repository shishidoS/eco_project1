
from django.contrib import admin
from django.urls import path, include
# eco_projectのURL設定
# このファイルはプロジェクト全体のURL設定を行います
# ここではDjangoの管理サイトとmain_appアプリケーションのURLを設定しています

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('main_app.urls')),# main_appアプリケーションのURLをインクルード
]
