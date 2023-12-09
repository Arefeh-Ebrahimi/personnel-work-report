from django.db import models

class Post(models.Model):
    
    PRODUCTIVITY_CHOICES = (
        ('Great' , 'Great'),
        ('Good' , 'Good'),
        ('Bad' , 'Bad'),
    )
    CERTAINTY_CHOICES = (
        ('Confident' , 'Confident'),
        ('Midst' , 'Midst'),
        ('Vague' , 'Vague'),
    )
    HEALTH_FEELING_CHOICES = (
    ('Perfect' , 'Perfect'),
    ('Normal' , 'Normal'),
    ('Weakness' , 'Weakness'),
    )
    STAGE_CHOICES = (
        ('R&D','R&D'),
        ('Actin(Doing Task)' , 'Actin(Doing Task)'),
        ('Cominucating' , 'Cominucating'),
        ('Monitor' , 'Monitor'),
        ('Setup Things' , 'Setup Things'),
    )

    text = models.CharField(max_length=100)
    datatime_created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)
    project = models.BooleanField(default=True) 
    Productivity = models.CharField(choices=PRODUCTIVITY_CHOICES, max_length=50)
    Certainty = models.CharField(choices=CERTAINTY_CHOICES, max_length=50)
    Health_Feeling = models.CharField(choices=HEALTH_FEELING_CHOICES, max_length=50)
    Stage = models.CharField(choices=STAGE_CHOICES, max_length=50)
      
    def __str__(self):
        return self.name