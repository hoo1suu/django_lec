from django.contrib import admin
from .models import MainContent, Comment


class MainContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'image')  # 관리자 페이지에서 표시할 필드
    search_fields = ('title', 'content')  # 검색 기능에 사용할 필드
    list_filter = ('pub_date',)  # 필터 옵션에 사용할 필드


class CommentAdmin(admin.ModelAdmin):
    list_display = ('content_list', 'author', 'content', 'create_date', 'modify_date')
    search_fields = ('content', 'author__username')  # 사용자 이름으로 검색 가능
    list_filter = ('create_date', 'modify_date')  # 필터 옵션에 사용할 필드


admin.site.register(MainContent, MainContentAdmin)
admin.site.register(Comment, CommentAdmin)
