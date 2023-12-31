from django.db import models

class Task(models.Model):
    
    PRODUCTIVITY_CHOICES = (
        ('great' , 'Great'),
        ('good' , 'Good'),
        ('bad' , 'Bad'),
    )
    CERTAINTY_CHOICES = (
        ('confident' , 'Confident'),
        ('midst' , 'Midst'),
        ('vague' , 'Vague'),
    )
    HEALTH_FEELING_CHOICES = (
    ('perfect' , 'Perfect'),
    ('normal' , 'Normal'),
    ('weakness' , 'Weakness'),
    )
    STAGE_CHOICES = (
        ('r&d','R&D'),
        ('action_doing_task' , 'Action(Doing Task)'),
        ('cominucating' , 'Cominucating'),
        ('monitor' , 'Monitor'),
        ('setup_things' , 'Setup Things'),
    )
    PROJECT = (
        ('all', 'All'),
        ('retail', 'Retail'),
        ('promotion', 'Promotion'),
        ('iesco', 'IESCO'),
        ('dR_hajitaghi_web', 'DR hajitaghi Web'),
        ('baraye_iran', 'Baraye Iran'),
        ('branding', 'Branding'),
        ('dR_hajitaghi_app', 'DR hajitaghi App'),
        ('setup_things','Setup things'),
        
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
    
    
    
    
   
    