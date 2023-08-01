from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
	def create_user(self, email, password, **kw):
		if not email:
			raise ValueError("Email must be set")
		
		email = self.normalize_email(email)
		user = self.model(email=email, password=password, **kw)
		user.set_password(password)
		user.save()
		return user
	
	def create_superuser(self, email, password, **kw):
		user = self.create_user(email=email, password=password, **kw)
		user.is_admin = True
		user.save()
		return user
