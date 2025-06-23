# main_app/urls.py
from django.urls import path# URLパターンを定義するためのモジュールをインポート
from . import views# ビュー関数をインポート

urlpatterns = [
    path('', views.home_view, name='home'),# ホームページのビュー関数を設定
    path('graph/', views.graph_view, name='graph'),# グラフ表示のビュー関数を設定
    path('result/', views.result_view, name='result'),# 結果表示のビュー関数を設定
]