from django.db import models

class ProfileImage(models.Model):
	profile_picture = models.ImageField(upload_to='profile_images/')
	userId = models.CharField(max_length=255)


class Product(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField()
	image = models.ImageField(upload_to='products/')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	userId = models.CharField(max_length=255)
	likes = models.IntegerField(default=0)
	like_users = models.JSONField(default=list)
	dislikes = models.IntegerField(default=0)
	dislike_users = models.JSONField(default=list)
	comments = models.JSONField(default=list)


	def __str__(self):
		return self.name

	def edit(self, name, description, image):
		self.name = name
		self.description = description
		self.image = image
		self.save()


	def short_description(self):
		# Split the description into words
		words = self.description.split()
		if len(words) > 50:
			# Join the first 50 words and add "..." at the end
			return ' '.join(words[:30]) + '...'
		else:
			# If the description is already less than 50 words, return it as is
			return self.description
	
	def is_see_more(self):
		words = self.description.split()
		if len(words) > 50:
			return True
		else:
			return False
