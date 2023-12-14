from django.db import models

class Task(models.Model):
    
    PRODUCTIVITY_CHOICES = (
        ('Great' , 'great'),
        ('Good' , 'good'),
        ('Bad' , 'bad'),
    )
    CERTAINTY_CHOICES = (
        ('Confident' , 'confident'),
        ('Midst' , 'midst'),
        ('Vague' , 'vague'),
    )
    HEALTH_FEELING_CHOICES = (
    ('Perfect' , 'perfect'),
    ('Normal' , 'normal'),
    ('Weakness' , 'weakness'),
    )
    STAGE_CHOICES = (
        ('R&D','r&d'),
        ('Action(Doing Task)' , 'action_doing_task'),
        ('Cominucating' , 'cominucating'),
        ('Monitor' , 'monitor'),
        ('Setup Things' , 'setup_things'),
    )
    PROJECT = (
        ('All', 'all'),
        ('Retail', 'retail'),
        ('Promotion', 'promotion'),
        ('IESCO', 'iesco'),
        ('DR hajitaghi Web', 'dR_hajitaghi_web'),
        ('Baraye Iran', 'baraye_iran'),
        ('Branding', 'branding'),
        ('DR hajitaghi App', 'dR_hajitaghi_app'),
        ('Setup things','setup_things'),
    )

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    productivity = models.CharField(choices=PRODUCTIVITY_CHOICES, max_length=255)
    certainty = models.CharField(choices=CERTAINTY_CHOICES, max_length=255)
    health_feeling = models.CharField(choices=HEALTH_FEELING_CHOICES, max_length=255)
    stage = models.CharField(choices=STAGE_CHOICES, max_length=255)
    project = models.CharField(choices=PROJECT, max_length=255)
         
    def __str__(self):
        return self.name
    
    
    
    
   
    