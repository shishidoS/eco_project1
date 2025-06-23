from django.db import models#基礎モデルに必要なモジュールをインポート
from django.contrib.auth.models import User # Django標準のユーザーモデル
from django.utils import timezone# 日時を扱うためのモジュール

class Character(models.Model):# キャラクター情報を管理するモデル
    user = models.OneToOneField(User, on_delete=models.CASCADE)# Django標準のUserモデルと1対1で連携
    total_points = models.IntegerField(default=0)# ユーザーが獲得した総ポイントを保存するフィールド
    
    def __str__(self):
        return f"{self.user.username}のキャラクター"

class DailyRecord(models.Model):# 日々のエコ行動を記録するモデル
    character = models.ForeignKey(Character, on_delete=models.CASCADE)# キャラクター情報と関連付けるための外部キー
    record_date = models.DateField(default=timezone.now)# 記録日を保存するフィールド。デフォルトは今日の日付
    points_earned = models.IntegerField(default=0)# 獲得したポイントを保存するフィールド
    
    # 質問項目を定義するフィールドです種類増やしたい場合ここを増やす
    gas_q1 = models.BooleanField(default=False, verbose_name="エコバッグを使った")
    water_q1 = models.BooleanField(default=False, verbose_name="こまめに水を止めた")
    power_q1 = models.BooleanField(default=False, verbose_name="衣服で温度調整をした")

    class Meta:
        # 同じ日に複数記録できないように制約を設定（重複登録などをできなくします）
        unique_together = ('character', 'record_date')

    def __str__(self):
        return f"{self.character.user.username} - {self.record_date}"