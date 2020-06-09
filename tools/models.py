from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.utils.text import slugify
from django.contrib.contenttypes.models import ContentType
from django.utils.safestring import mark_safe
from urllib.parse import urlparse
from tinymce.models import HTMLField
from urllib.parse import parse_qs

# Not just pages but also text fragements used throughout the site

class Person(models.Model):
	slug = models.SlugField(null=True, blank=True, default='')
	name = models.CharField(max_length=100)
	preamble = HTMLField(default='', null=True, blank=True)
	image_url = models.URLField(max_length=250, null=True, default='', blank=True)
	youtube = models.URLField(max_length=250, null=True, default='', blank=True)

	text = HTMLField(null=True, blank=True, default='')
		#Can make upload folders personal
	image = models.ImageField(upload_to ='', 
			height_field=None, width_field=None, max_length=250,
			blank=True, default=None, null=True)


class Page(models.Model):
	slug = models.SlugField(null=True, blank=True, default='')
	name = models.CharField(max_length=100)
	preamble = HTMLField(default='', null=True, blank=True)
	image_url = models.URLField(max_length=250, null=True, default='', blank=True)
	youtube = models.URLField(max_length=250, null=True, default='', blank=True)

	text = HTMLField(null=True, blank=True, default='')
		#Can make upload folders personal
	image = models.ImageField(upload_to ='', 
			height_field=None, width_field=None, max_length=250,
			blank=True, default=None, null=True)

	
	

	class Meta:
		ordering = ['name',]

	def __str__(self):
		return self.name


class Tag(models.Model):
	slug = models.SlugField(null=True, blank=True, default='')
	name = models.CharField(max_length=100)
	about = models.TextField(null=True, blank=True, default='')
	#content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name="type")
	#object_id = models.PositiveIntegerField()
	#content_object = GenericForeignKey('content_type', 'object_id')
	
	class Meta:
		ordering = ['name',]

	def ltype(self):
		return self.__class__.__name__.lower()

	def __str__(self):
		return self.name

	def tools_count(self):
		tagC = Tool.objects.filter(tags=self).count()
		resC = Resource.objects.filter(tags=self).count()
		inspC = Inspiration.objects.filter(tags=self).count()
		return tagC + resC + inspC

	def font_size(self):
		return translate(self.tools_count(), 0, 100, 18, 54 )

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Tag, self).save(*args, **kwargs)

class Category(models.Model):
	class Meta:
		ordering = ['name']

	name = models.CharField(max_length=100)
	#owner = models.ForeignKey(User, on_delete=models.CASCADE)
	text = models.TextField(blank=True)

	def __str__(self):
		return self.name

class Level(models.Model):
	class Meta:
		ordering = ['order']

	name = models.CharField(max_length=100)
	order = models.IntegerField(null=False, default=0)
	text = HTMLField(blank=True)

	def __str__(self):
		return self.name



class ScreenCastVideo(models.Model):
	name = models.CharField(max_length=255, null=True, default='')
	url = models.URLField(max_length=250, null=True, default='')
	image_url = models.CharField(max_length=250, null=True, default='', blank=True)

	about = HTMLField(default='', null=True, blank=True)
	tags = models.ManyToManyField(Tag, blank=True,  )
	created_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(auto_now=True)

	def _get_linked_thumbnail(self):
		img = format_html(u'<img src="{}" width="100"/></a>', self.image_url)
		linked_img = format_html('<a href="{}" target="_blank">' + img + "</a>", self.url)
		return linked_img
	_get_linked_thumbnail.allow_tags = True

	def embed_url(self):
		''
		print("screencast:",self.id)
		#https://www.youtube.com/embed/UTAMfolxyD0
		if "https://www.youtube.com/watch?v" in self.url:
			qs = self.url.split('?')
			video_id = parse_qs(qs[1])['v'][0]
			print(video_id)
			return "https://www.youtube.com/embed/" + video_id
		elif  "youtu.be" in self.url:
			video_id = self.url.replace("https://youtu.be/", "")
			return "https://www.youtube.com/embed/" + video_id
		else:
			return self.id

	def __str__(self):
		return self.name + ": " + self.url

	def save(self, *args, **kwargs):
		if "https://www.youtube.com/watch?v" in self.url:
			url = self.url
			url = url.replace("&feature=youtu.be", "")
			qs = url.split('?')
			video_id = parse_qs(qs[1])['v'][0]
			self.image_url = "http://img.youtube.com/vi/%s/0.jpg" % video_id
			self.url = url
		elif "youtu.be" in self.url:#https://youtu.be/VSX_M_YDW34
			url = self.url
			video_id = url.replace("https://youtu.be/", "")
			self.image_url = "http://img.youtube.com/vi/%s/0.jpg" % video_id
			self.url = url
		super(ScreenCastVideo, self).save(*args, **kwargs)

	class Meta:
		''
		ordering = ('-id',)

class Tool(models.Model):
	name = models.CharField(max_length=255, null=True, default='')
	
	url = models.URLField(max_length=250, null=True, default='')
	image_url = models.CharField(max_length=250, null=True, default='', blank=True)
	about = HTMLField(default='', null=True, blank=True)
	#HTMLField
	tags = models.ManyToManyField(Tag, blank=True,  )
	category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True,null=True, related_name="category1")
	altcategory = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True,null=True, related_name="category2")
	web_based = models.BooleanField(null=True, blank=True, default=True)
	desktop = models.BooleanField(null=True, blank=True, default=False)
	mobile = models.BooleanField(null=True, blank=True, default=False)
	requires_registration = models.BooleanField(null=True, blank=True, default=True)
	level = models.ForeignKey(Level, on_delete=models.CASCADE, blank=True,null=True, related_name="level")
	learnings = models.ManyToManyField( 'Learning', blank=True, )
	created_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(auto_now=True)

	class Meta:
		''
		ordering = ('-modified_date',)

	def ltype(self):
		return self.__class__.__name__.lower()

	def tags_as_list(self):
		# Children query
		s = ''
		for g in self.tags.all():
			s = s + str(g.name) + " , "
		return str(    s   )

	def save(self, *args, **kwargs):
		#self.slug = slugify(self.name)
		super(Tool, self).save(*args, **kwargs)


	def _get_thumbnail(self):
		return format_html(u'<img src="{}" width="150"/>', self.image_url)
	_get_thumbnail.allow_tags = True

	def _get_link(self):
		short_url = "".join(self.url.split("/")[2:4])
		short_url = urlparse(self.url)[1]
		return mark_safe(format_html(u'<a href="{}" target="_blank"/>{}</a>', self.url, short_url))
	_get_link.allow_tags = True

	def _get_linked_thumbnail(self):
		return format_html(u'<img src="{}" width="100"/>_', self.image_url)
	_get_linked_thumbnail.allow_tags = True

	def __str__(self):
		return self.name + ": " + self.url

class Resource(models.Model):
	name = models.CharField(max_length=255, null=True, default='')
	
	url = models.URLField(max_length=250, null=True, default='')
	image_url = models.CharField(max_length=250, null=True, default='', blank=True)
	about = HTMLField(default='', null=True, blank=True)
	tags = models.ManyToManyField(Tag, blank=True, )
	category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True,null=True, related_name="rcategory1")
	altcategory = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True,null=True, related_name="rcategory2")

	def ltype(self):
		return self.__class__.__name__.lower()

	def get_thumbnail(self):
		return format_html(u'<img src="{}" width="150"/>', self.image_url)
	get_thumbnail.allow_tags = True

	def _get_link(self):
		return format_html(u'<a href="{}" target="_blank"/>{}</a>', self.url, self.url)
	_get_link.allow_tags = True

	def _get_linked_thumbnail(self):
		return format_html(u'<img src="{}" width="100"/>', self.image_url)
	_get_linked_thumbnail.allow_tags = True




	def __str__(self):
		return self.name + ": " + self.url

class Inspiration(models.Model):
	name = models.CharField(max_length=255, null=True, default='')
	
	url = models.URLField(max_length=250, null=True, default='')
	image_url = models.CharField(max_length=250, null=True, default='', blank=True)
	about = HTMLField(default='', null=True, blank=True)
	tags = models.ManyToManyField(Tag, blank=True,)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True,null=True, related_name="icategory1")
	altcategory = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True,null=True, related_name="icategory2")

	def ltype(self):
		return self.__class__.__name__.lower()

	def _get_thumbnail(self):
		return format_html(u'<img src="{}" width="150"/>', self.image_url)
	_get_thumbnail.allow_tags = True

	def _get_edit_link(self):
		return format_html(u'<a href="/admin/tools/inspiration/{}/change/" target="_blank"/>{}</a>', self.id, "view")
	_get_edit_link.allow_tags = True

	def _get_link(self):
		
		return format_html(u'<a href="{}" target="_blank"/>{}</a>', self.url, "view")
	_get_link.allow_tags = True

	def _get_linked_thumbnail(self):
		return format_html(u'<img src="{}" width="100"/>', self.image_url)
	_get_linked_thumbnail.allow_tags = True

	def __str__(self):
		return self.name + ": " + self.url
	
	def save(self, *args, **kwargs):
		if "https://www.youtube.com/watch?v" in self.url:
			qs = self.url.split('?')
			video_id = parse_qs(qs[1])['v'][0]
			self.image_url = "http://img.youtube.com/vi/%s/0.jpg" % video_id


		super(Inspiration, self).save(*args, **kwargs)

	def tags_as_list(self):
		# Children query
		s = ''
		for g in self.tags.all():
			s = s + str(g.name) + " , "
		return str(    s   )

class Learning(models.Model):
	name = models.CharField(max_length=255, null=True, default='')
	
	url = models.URLField(max_length=250, null=True, default='', help_text="If this is a Youtube URL, the video's thumbnail will be automatically used.")
	image_url = models.CharField(max_length=250, null=True, default='', blank=True)
	#youtube_url = models.URLField(max_length=250, null=True, default='', blank=True)

	about =HTMLField(default='', null=True, blank=True)
	tags = models.ManyToManyField(Tag)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True,null=True, related_name="lcategory1")
	altcategory = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True,null=True, related_name="lcategory2")

	def ltype(self):
		return self.__class__.__name__.lower()

	def _get_thumbnail(self):
		return format_html(u'<img src="{}" width="150"/>', self.image_url)
	_get_thumbnail.allow_tags = True

	def _get_link(self):
		return format_html(u'<a href="{}" target="_blank"/>{}</a>', self.url, self.url)
	_get_link.allow_tags = True

	def _get_linked_thumbnail(self):
		return format_html(u'<img src="{}" width="100"/>', self.image_url)
	_get_linked_thumbnail.allow_tags = True

	def __str__(self):
		return self.name + ": " + self.url
	
	def save(self, *args, **kwargs):
		if "https://www.youtube.com/watch?v" in self.url:
			qs = self.url.split('?')
			video_id = parse_qs(qs[1])['v'][0]
			self.image_url = "http://img.youtube.com/vi/%s/0.jpg" % video_id


		super(Learning, self).save(*args, **kwargs)



##################

class Activity(models.Model):
	name = models.CharField(max_length=255, null=True, default='')
	slug = models.SlugField(null=True, blank=True, default='')

	
	#Can make upload folders personal
	image = models.ImageField(upload_to ='', 
			height_field=None, width_field=None, max_length=250,
			blank=True, default=None, null=True)

	youtube = models.URLField(max_length=250, null=True, default='', blank=True)
	
	screencasts = models.ManyToManyField(ScreenCastVideo,blank=True)
	preamble = HTMLField(default='', null=True, blank=True)

	level = models.ForeignKey(Level, on_delete=models.CASCADE, blank=True,null=True, related_name="alevel")
	
	tags = models.ManyToManyField(Tag,blank=True)
	
	inspiration_text = HTMLField(default='', null=True, blank=True)
	inspirations = models.ManyToManyField(Inspiration,blank=True)

	resource_text = HTMLField(default='', null=True, blank=True)
	resources = models.ManyToManyField( Resource,blank=True )

	tool_text = HTMLField(default='', null=True, blank=True)
	tools = models.ManyToManyField( Tool, blank=True )

	learning_text = HTMLField(default='',  blank=True)
	learnings = models.ManyToManyField( Learning, blank=True, default=None )

	conclusion = HTMLField(default='', null=True, blank=True)
	is_published = models.BooleanField(null=True, blank=True, default=False)

	created_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(auto_now=True)

	class Meta:
		''
		ordering = ('-modified_date',)

	def ltype(self):
		return self.__class__.__name__.lower()

	def screencasts_count(self):
		return self.screencasts.count()

	def tags_as_list(self):
		# Children query
		s = ''
		for g in self.tags.all():
			s = s + str(g.name) + " , "
		return str(    s   )

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Activity, self).save(*args, **kwargs)

	def url(self):
		return "/activities/view/" + self.slug

	def _get_thumbnail(self):
		return format_html(u'<img src="{}" width="150"/>', self.image_url)
	_get_thumbnail.allow_tags = True

	def _get_link(self):
		#short_url = "".join(self.url.split("/")[2:4])
		#short_url = urlparse(self.url)[1]
		slug = self.slug
		return mark_safe(f'<a href="/activities/view/{slug}" target="_blank"/>view</a>')
	_get_link.allow_tags = True

	def _get_linked_thumbnail(self):

		return format_html(u'<img src="{}" width="100"/>', self.image_url)
	_get_linked_thumbnail.allow_tags = True

	def __str__(self):
		return self.name 


def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)