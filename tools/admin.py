from django.contrib import admin
from django.contrib.contenttypes.admin import  GenericTabularInline
from django.contrib.admin.widgets import FilteredSelectMultiple

from django.utils.html import format_html_join
from django.utils.safestring import mark_safe

from .models import Tool, Category, Tag, Resource, Level, Inspiration, Activity, Learning

from django.contrib import admin

admin.site.site_header = "DIGITAL CREATIVITY"
admin.site.site_title = "DC Admin"
admin.site.index_title = "Welcome to DC Admin"



class LevelInline(admin.StackedInline):
	model = Level


class ToolInline(admin.StackedInline):
	model = Tool.tags.through
	extra = 3

class TagAdmin(admin.ModelAdmin):
	model = Tool
	list_display = ('name', "slug", "tools_count")
	#inlines = [ToolInline,]

class CategoryAdmin(admin.ModelAdmin):
	model = Category
	list_display = ('name', )


class LevelAdmin(admin.ModelAdmin):
	model = Level
	list_display = ('name', )   


class CategoryInline(admin.TabularInline):
	model = Tool


class ResourceAdmin(admin.ModelAdmin):
	#fields = ('name', )
   
	list_display = ('name','_get_link', "get_thumbnail" )
	list_filter = ('tags',)
	search_fields = ['name', "about"]
	filter_horizontal = ('tags',)
	exclude = ['category', 'altcategory',]






class ToolAdmin(admin.ModelAdmin):

	exclude = ('category', 'altcategory')
	list_display = ( '_get_linked_thumbnail' ,'name', 'tags_as_list','_get_link',)
	list_filter = ('web_based','desktop','level','tags',)
	search_fields = ['name', "about"]
	filter_horizontal = ('tags','learnings')
	actions = ['make_fun',]



	def make_fun(modeladmin, request, queryset):
		level = Level.objects.filter(name="Anyone/Fun").first()
		print(level)
		queryset.update(level=level)
	make_fun.short_description = "Mark as Anyone or Fun"

class InspirationAdmin(admin.ModelAdmin):
	#fields = ('name', )
   
	list_display = ('name','_get_link', "_get_thumbnail" )
	list_filter = ('tags',)
	search_fields = ['name', "about"]
	filter_horizontal = ('tags',)
	exclude = ['category', 'altcategory',]


class LearningAdmin(admin.ModelAdmin):
	#fields = ('name', )
	exclude = ['category', 'altcategory',]

	list_display = ('name','_get_link', "_get_thumbnail" )
	list_filter = ('tags',)
	search_fields = ['name', "about"]
	filter_horizontal = ('tags',)

admin.site.register(Learning, LearningAdmin)
admin.site.register(Tag, TagAdmin)
#admin.site.register(Category, CategoryAdmin)
admin.site.register(Resource, ResourceAdmin)
admin.site.register(Tool, ToolAdmin)
admin.site.register(Inspiration, InspirationAdmin)
admin.site.register(Level, LevelAdmin)

#https://djangotricks.blogspot.com/2016/12/django-administration-inlines-for-inlines.html
def get_picture_preview(obj):
	if obj.pk:  # if object has already been saved and has a primary key, show picture preview
		return """<a href="{src}" target="_blank"><img src="{src}" alt="{title}" style="max-width: 200px; max-height: 200px;" /></a>""".format(
			src=obj.image.url,
			title=obj.name,
		)
	return _("(choose a picture and save and continue editing to see the preview)")
get_picture_preview.allow_tags = True
get_picture_preview.short_description = "Picture Preview"



class ActivityAdmin(admin.ModelAdmin):
	exclude =      ('slug', )
	list_display = (  'name', 'tags_as_list','is_published', '_get_link')
	list_filter =  ('is_published','level','tags',)
	search_fields = ['name', "preamble", "inspiration_text","resource_text", "tool_text"]
	filter_horizontal = ('tags','inspirations','resources','tools', "learnings")
	readonly_fields = [ "preview_image", ]
	actions = ['publish',]

	def preview_image(self, obj):
		return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
			url = obj.image.url,
			width=350,
			height=250,
			)
	)
	def publish(modeladmin, request, queryset):
		queryset.update(is_published=True)
	publish.short_description = "Publish"

admin.site.register(Activity, ActivityAdmin)