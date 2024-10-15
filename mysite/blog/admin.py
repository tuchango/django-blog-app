from django.contrib import admin

from .models import Post


# простейший вариант добавления таблицы в админ-панель
# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publish', 'status']  # добавить столбцы таблицы
    list_filter = ['publish', 'author', 'status']  # справа появится меню с фильтрами
    search_fields = ['title', 'body']  # поиск пройдет по этим полям
    prepopulated_fields = {'slug': ('title',)}  # слаг заполняется автоматом по заголовку, при создании поста
    date_hierarchy = 'publish'  # можно над таблицей выбирать дату
    raw_id_fields = ['author']  # по умолчанию автор выбирался из выпадашки, теперь через поле ввода, по id
    show_facets = admin.ShowFacets.ALWAYS  # по умолчанию показывать кол-во постов для каждого фильтра
