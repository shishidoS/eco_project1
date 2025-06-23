# main_app/views.py
from django.shortcuts import render, redirect # レンダリングとリダイレクトのためのモジュールをインポート
from django.contrib.auth.decorators import login_required # ログイン必須にするデコレーターをインポート
from .models import Character, DailyRecord # キャラクターと日々の記録を管理するためのモデルをインポート
from .forms import DailyRecordForm # 日々のエコ行動を記録するフォームをインポート
from django.utils import timezone # 日時を扱うためのモジュールをインポート

@login_required # ログイン必須にする
def home_view(request):
    character, created = Character.objects.get_or_create(user=request.user)

    # 今日の日付で既に記録があるかチェック
    today = timezone.now().date()
    record_exists = DailyRecord.objects.filter(character=character, record_date=today).exists()

    if request.method == 'POST':# POSTリクエストが送信,つまりデータが送信されたら場合に動作
        form = DailyRecordForm(request.POST)
        if form.is_valid() and not record_exists:
            # === ここからが改造する部分 ===================================================================
            # TODO: ポイント計算ロジックを実装する
            points = 0
            if form.cleaned_data.get('gas_q1'): points += 10
            if form.cleaned_data.get('water_q1'): points += 10
            if form.cleaned_data.get('power_q1'): points += 10
            # === ここまで ===

            # データベースに保存
            record = form.save(commit=False)# フォームのデータを保存するが、まだデータベースには保存しない
            record.character = character# キャラクター情報を関連付ける
            record.record_date = today# 今日の日付を設定
            record.points_earned = points#  獲得したポイントを設定
            record.save()

            # キャラクターのポイントを更新
            character.total_points += points# 獲得したポイントをキャラクターの総ポイントに加算
            character.save()

            return redirect('result')# 結果表示ページにリダイレクト(移動する)
    else:
        form = DailyRecordForm()# フォームのインスタンスを作成(データ送信するフォーム)

    context = {# コンテキストデータを定義(web側に渡すデータ)
        'character': character,
        'form': form,
        'record_exists': record_exists,
    }
    return render(request, 'main_app/home.html', context)# レンダリングしてホームページを表示

@login_required# ログイン必須にする
def graph_view(request):# グラフ表示ページのビュー関数
    # ユーザーのキャラクター情報を取得
    character = Character.objects.get(user=request.user)
    records = DailyRecord.objects.filter(character=character).order_by('record_date')
    context = {'records': records}
    return render(request, 'main_app/graph.html', context)

def result_view(request):
    return render(request, 'main_app/result.html')