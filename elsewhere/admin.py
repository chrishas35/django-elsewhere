from django.contrib import admin
from elsewhere import models

class ProfileAdmin(admin.ModelAdmin):
    raw_id_fields = ['user']

for model in (models.WebsiteProfile, models.InstantMessengerProfile,
        models.SocialNetworkProfile):
    admin.site.register(model, ProfileAdmin)