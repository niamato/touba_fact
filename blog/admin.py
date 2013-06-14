#-*-coding:utf-8-*
from django.contrib import admin
from blog.models import Article, Categorie


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'apercu_contenu', 'date')
    list_filter = ('auteur','categorie',)
    date_hierarchy = 'date'
    ordering = ('-date', )
    search_fields = ('titre', 'contenu')
    fieldsets = (
        # Fieldset 1 : Meta-info (titre, auteur...)
        ('Général', {
            'classes': ['collapse',],
            'fields': ('titre', 'auteur', 'categorie')
        }),
        # Fieldset 2 : Contenu de l'article
        ('Contenu de l\'article', {
            'description': 'Le formulaire accepte les balises HTML. Utilisez-les à bon escient !', 'fields': ('contenu', 'source' )
    }),)

    def apercu_contenu(self, article):
        """
        Retourne les 40 premiers caractères du contenu de l'article. Si il
        y a plus de 40 caractères, on rajoute des points de suspension
        """
        text = article.contenu[0:40]
        if len(article.contenu) > 40:
            return '%s...' % text
        else:
            return text

    apercu_contenu.short_description = 'Aperçu du contenu'



admin.site.register(Article, ArticleAdmin)
admin.site.register(Categorie)
