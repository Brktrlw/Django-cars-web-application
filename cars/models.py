from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField

class CarModel(models.Model):
    STATE_CHOICES = (
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('DC', 'District Of Columbia'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming'),
    )
    YEAR_CHOICES = [(year,year) for year in range(2000, (datetime.now().year+1))]
    FEATURES_CHOICES = (
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
    )
    DOOR_CHOICES = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )
    title        = models.CharField(verbose_name=_("Car Title"),max_length=100)
    city         = models.CharField(verbose_name=_("City"),max_length=100)
    state        = models.CharField(verbose_name=_("State"),max_length=100,choices=STATE_CHOICES)
    description  = RichTextField(verbose_name=_("Description"))
    year         = models.IntegerField(verbose_name=_("Year"),choices=YEAR_CHOICES)
    model        = models.CharField(verbose_name=_("Model"),max_length=100)
    condition    = models.CharField(verbose_name=_("Condition"),max_length=100)
    price        = models.FloatField(verbose_name=_("Price"))
    car_photo_1  = models.ImageField(verbose_name=_("Car Photo"),upload_to="cars/%Y/%m/%d/")
    car_photo_2  = models.ImageField(verbose_name=_("Car Photo"),upload_to="cars/%Y/%m/%d/",blank=True)
    car_photo_3  = models.ImageField(verbose_name=_("Car Photo"),upload_to="cars/%Y/%m/%d/",blank=True)
    car_photo_4  = models.ImageField(verbose_name=_("Car Photo"),upload_to="cars/%Y/%m/%d/",blank=True)
    car_photo_5  = models.ImageField(verbose_name=_("Car Photo"),upload_to="cars/%Y/%m/%d/",blank=True)
    features     = MultiSelectField(verbose_name=_("Features"),choices=FEATURES_CHOICES)
    body_style   = models.CharField(verbose_name=_("Body Style"),max_length=100)
    engine       = models.CharField(verbose_name=_("Engine"),max_length=50,default="")
    transmission = models.CharField(verbose_name=_("Transmission"),max_length=100)
    color        = models.CharField(verbose_name=_("Car Color"),max_length=50,default="")
    interior     = models.CharField(verbose_name=_("Interior"),max_length=100)
    miles        = models.IntegerField(verbose_name=_("Miles"))
    doors        = models.CharField(verbose_name=_("Doors"),max_length=10,choices=DOOR_CHOICES)
    vin_no       = models.CharField(verbose_name=_("Vin No"),max_length=100)
    milage       = models.IntegerField(verbose_name=_("Milage"))
    fuel_type    = models.CharField(verbose_name=_("Fuel Type"),max_length=100)
    no_of_owners = models.CharField(verbose_name=_("No Of Owners"),max_length=100)
    is_featured  = models.BooleanField(verbose_name=_("Is Featured"),default=False)
    created_date = models.DateTimeField(verbose_name=_("Created Date"),auto_now_add=True)
    passengers   = models.IntegerField(verbose_name=_("Passengers"))


    def __str__(self):
        return self.title

    class Meta:
        db_table            = "Cars"
        verbose_name        = _("Car")
        verbose_name_plural = _("Cars")

