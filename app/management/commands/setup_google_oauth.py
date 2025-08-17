from django.core.management.base import BaseCommand
from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialApp
from django.conf import settings


class Command(BaseCommand):
    help = 'Set up Google OAuth application for social login'

    def handle(self, *args, **options):
        # Get or create the default site
        site, created = Site.objects.get_or_create(
            id=settings.SITE_ID,
            defaults={
                'domain': '127.0.0.1:8000',
                'name': 'DjangoProject'
            }
        )
        
        if created:
            self.stdout.write(
                self.style.SUCCESS(f'Created site: {site.name} ({site.domain})')
            )
        else:
            self.stdout.write(
                self.style.SUCCESS(f'Using existing site: {site.name} ({site.domain})')
            )

        # Get or create Google social app
        google_app, created = SocialApp.objects.get_or_create(
            provider='google',
            defaults={
                'name': 'Google',
                'client_id': settings.GOOGLE_CLIENT_ID,
                'secret': settings.GOOGLE_CLIENT_SECRET,
            }
        )

        if created:
            self.stdout.write(
                self.style.SUCCESS('Created Google OAuth application')
            )
        else:
            # Update existing app with new credentials
            google_app.client_id = settings.GOOGLE_CLIENT_ID
            google_app.secret = settings.GOOGLE_CLIENT_SECRET
            google_app.save()
            self.stdout.write(
                self.style.SUCCESS('Updated Google OAuth application')
            )

        # Add site to the social app
        google_app.sites.add(site)
        
        self.stdout.write(
            self.style.SUCCESS('✅ Google OAuth setup completed successfully!')
        )
        self.stdout.write(
            self.style.WARNING('⚠️  Make sure your Google OAuth redirect URI is set to: http://127.0.0.1:8000/accounts/google/login/callback/')
        )
