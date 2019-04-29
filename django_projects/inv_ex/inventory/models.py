from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse  # To generate URLS by reversing URL patterns

# Create Owners here.
class Owner(models.Model):
    """Model representing an author."""
    name = models.CharField(max_length=100)
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Account(models.Model):
    

    # Assigns an owner
    owner = models.ForeignKey('Owner', on_delete=models.SET_NULL, null=True)
    
    # Account info
    acct_num = models.CharField('Account Number', max_length=20, help_text='20 numeric number include dashes' )

    #STB information
    stbmodel = models.CharField(max_length=200, help_text='Enter a set top box model (e.g. Hopper 813)')
    rid = models.CharField('Receiver ID', max_length=10, help_text='10 numeric starting from R')
    sid = models.CharField('Smart Card ID', max_length=10, help_text='10 numeric starting from S')

    security_status = models.CharField(max_length=100, help_text='Type Secured or Unsecured')
        
        
    
    notes = models.TextField(max_length=1000, help_text='Notes')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.acct_num

    def get_absolute_url(self):
        """Returns the url to access a detail record for account."""
        return reverse('account-detail', args=[str(self.id)])
