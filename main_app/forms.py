# main_app/forms.py
from django import forms# フォームを作成するためのモジュールをインポート
from .models import DailyRecord# 日々のエコ行動を記録するモデルをインポート

class DailyRecordForm(forms.ModelForm):# 日々のエコ行動を記録するフォームを作成
    class Meta:
        model = DailyRecord
        # フォームに表示するフィールドを指定
        fields = ['gas_q1', 'gas_q2','gas_q3','water_q1','water_q2','water_q3', 'power_q1', 'power_q2', 'power_q3']
