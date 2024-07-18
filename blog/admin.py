from django.contrib import admin
from .models import User, Post, Article, Vacancy, Case


class AllPostAdmin(admin.ModelAdmin):
    readonly_fields = ('type', )


admin.site.register(User)
admin.site.register(Post, AllPostAdmin)
admin.site.register(Article, AllPostAdmin)
admin.site.register(Vacancy, AllPostAdmin)
admin.site.register(Case, AllPostAdmin)
