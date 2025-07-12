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
    gas_q1 = models.BooleanField(default=False, verbose_name="エコバッグを使った")# レジ袋を使わないことで石油使用量を減らした
    gas_q2 = models.BooleanField(default=False, verbose_name="近場に行くときは車を使用しなかった")# ガソリンを使わないことで石油使用量を減らした
    gas_q3 = models.BooleanField(default=False, verbose_name="食べ残しをしないことで食品ロスを減らした")# 食べ残しは可燃ごみなのでガスの発生源を減らした

    water_q1 = models.BooleanField(default=False, verbose_name="こまめに水を止めた")# 水の使用量を減らした
    water_q2 = models.BooleanField(default=False, verbose_name="洗い物はまとめて行った")# 水の使用量を減らした
    water_q3 = models.BooleanField(default=False, verbose_name="家族で風呂に入る時間を連続になるよう揃えた")# 水使用量の削減、追い炊きによるガス削減

    power_q1 = models.BooleanField(default=False, verbose_name="衣服で温度調整をした")# 電力削減
    power_q2 = models.BooleanField(default=False, verbose_name="換気を活用してエアコンの使用量を減らした")# 電力削減
    power_q3 = models.BooleanField(default=False, verbose_name="昼間は電気をつけず、自然光の明るさで過ごした") # 電力削減

    class Meta:
        # 同じ日に複数記録できないように制約を設定（重複登録などをできなくします）
        unique_together = ('character', 'record_date')

    def __str__(self):
        return f"{self.character.user.username} - {self.record_date}"
