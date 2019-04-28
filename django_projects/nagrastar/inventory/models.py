from django.db import models

# Create your models here.
class STBModel(models.Model):
    """Model representing a book genre."""
    stbmodel = models.CharField(max_length=200, help_text='Enter a set top box model (e.g. Hopper 813)')

    rid = models.CharField('Receiver ID', max_length=10, help_text='10 numeric starting from R')
    sid = models.CharField('Smart Card ID', max_length=10, help_text='10 numeric starting from S')
    
    def __str__(stbmodel):
        """String for representing the Model object."""
        return self.stbmodel


from django.urls import reverse # Used to generate URLs by reversing the URL patterns

class Account(models.Model):
    

    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file
    owner = models.ForeignKey('Owner', on_delete=models.SET_NULL, null=True)
    notes = models.TextField(max_length=1000, help_text='Notes')
    
    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    stbmodel = models.ManyToManyField(STBModel, help_text='Select a receiver')
    acct_num = models.CharField('Account Number', max_length=20, help_text='20 numeric number include dashes' )
    
    def __str__(self):
        """String for representing the Model object."""
        return self.title
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for account."""
        return reverse('account-detail', args=[str(self.id)])

import uuid # Required for unique book instances

class AccountInstance(models.Model):
    """Model representing a specific copy of a book (i.e. that can be borrowed from the library)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book across whole library')
    account = models.ForeignKey('Account', on_delete=models.SET_NULL, null=True) 
    

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.book.title})'

class Owner(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'
