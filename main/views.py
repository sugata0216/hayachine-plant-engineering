from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, "main/top.html")
def news_list_view(request):
    # ダミーデータ
    dummy_news = [
        {'category': 'event', 'category_name': 'イベント', 'date': '2025年10月26日', 'title': 'お仕事体験の様子のご紹介'},
        {'category': 'info', 'category_name': 'お知らせ', 'date': '2025年10月25日', 'title': '新しいパンフレットの発刊'},
        {'category': 'urgent', 'category_name': '重要', 'date': '2025年10月22日', 'title': '工事の範囲拡大について'},
        {'category': 'info', 'category_name': 'お知らせ', 'date': '2025年10月22日', 'title': '職業体験開始について'},
        {'category': 'info', 'category_name': 'お知らせ', 'date': '2025年10月22日', 'title': 'ホームページ開設'},
    ]
    
    return render(request, 'main/news.html', {'news_list': dummy_news})
def news_detail(request):
    # 実際にはデータベースから取得
    context = {
        'title': 'お仕事体験の様子のご紹介',
        'date': '2025.10.22',
        'content': 'お仕事体験にご参加いただきありがとうございました。',
        'image': 'news-detail-1.jpg'
    }
    return render(request, 'main/news_details.html', context)

def recruitment(request):
    return render(request, "main/recruit_ment.html")

def business_activities(request):
    return render(request, "main/business_activities.html")

def company_information(request):
    return render(request, "main/company_information.html")
 
def inquiry_view(request):
    return render(request, "main/inquiry.html")
