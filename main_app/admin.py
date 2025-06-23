# main_app/admin.py
from django.contrib import admin
from .models import Character, DailyRecord #モデルをインポートしキャラクターと日々の記録を管理するためのモデルを登録

admin.site.register(Character) # キャラクター情報を管理するモデルを登録
admin.site.register(DailyRecord)# 日々のエコ行動を記録するモデルを登録