from django.db import models
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from sklearn.tree import DecisionTreeClassifier
import joblib
import os
from django.conf import settings

# Create your models here.

    # Assuming each value can range between -9999.99 and 9999.99 for example
min_value = -9999.99
max_value = 9999.99

class Input(models.Model):
    time = models.FloatField(blank=True, null=True, validators=[MinValueValidator(min_value), MaxValueValidator(max_value)])
    v1 = models.FloatField(blank=True, null=True, validators=[MinValueValidator(min_value), MaxValueValidator(max_value)])
    v2 = models.FloatField(blank=True, null=True, validators=[MinValueValidator(min_value), MaxValueValidator(max_value)])
    v3 = models.FloatField(blank=True, null=True, validators=[MinValueValidator(min_value), MaxValueValidator(max_value)])
    v4 = models.FloatField(blank=True, null=True, validators=[MinValueValidator(min_value), MaxValueValidator(max_value)])
    v5 = models.FloatField(blank=True, null=True, validators=[MinValueValidator(min_value), MaxValueValidator(max_value)])
    v6 = models.FloatField(blank=True, null=True, validators=[MinValueValidator(min_value), MaxValueValidator(max_value)])
    v7 = models.FloatField(blank=True, null=True, validators=[MinValueValidator(min_value), MaxValueValidator(max_value)])
    v8 = models.FloatField(blank=True, null=True, validators=[MinValueValidator(min_value), MaxValueValidator(max_value)])
    v9 = models.FloatField(blank=True, null=True, validators=[MinValueValidator(min_value), MaxValueValidator(max_value)])
    v10 = models.FloatField(blank=True, null=True, validators=[MinValueValidator(min_value), MaxValueValidator(max_value)])
    v11 = models.FloatField(blank=True, null=True, validators=[MinValueValidator(min_value), MaxValueValidator(max_value)])
    v12 = models.FloatField(blank=True, null=True, validators=[MinValueValidator(min_value), MaxValueValidator(max_value)])
    v13 = models.FloatField(blank=True, null=True, validators=[MinValueValidator(min_value), MaxValueValidator(max_value)])
    v14 = models.FloatField(blank=True, null=True, validators=[MinValueValidator(min_value), MaxValueValidator(max_value)])
    v15 = models.FloatField(blank=True, null=True, validators=[MinValueValidator(min_value), MaxValueValidator(max_value)])
    v16 = models.FloatField(blank=True, null=True, validators=[MinValueValidator(min_value), MaxValueValidator(max_value)])
    v17 = models.FloatField(blank=True, null=True, validators=[MinValueValidator(min_value), MaxValueValidator(max_value)])
    v18 = models.FloatField(blank=True, null=True, validators=[MinValueValidator(min_value), MaxValueValidator(max_value)])
    v19 = models.FloatField(blank=True, null=True, validators=[MinValueValidator(min_value), MaxValueValidator(max_value)])
    v20 = models.FloatField(blank=True, null=True, validators=[MinValueValidator(min_value), MaxValueValidator(max_value)])
    v21 = models.FloatField(blank=True, null=True, validators=[MinValueValidator(min_value), MaxValueValidator(max_value)])
    v22 = models.FloatField(blank=True, null=True, validators=[MinValueValidator(min_value), MaxValueValidator(max_value)])
    v23 = models.FloatField(blank=True, null=True, validators=[MinValueValidator(min_value), MaxValueValidator(max_value)])
    v24 = models.FloatField(blank=True, null=True, validators=[MinValueValidator(min_value), MaxValueValidator(max_value)])
    v25 = models.FloatField(blank=True, null=True, validators=[MinValueValidator(min_value), MaxValueValidator(max_value)])
    v26 = models.FloatField(blank=True, null=True, validators=[MinValueValidator(min_value), MaxValueValidator(max_value)])
    v27 = models.FloatField(blank=True, null=True, validators=[MinValueValidator(min_value), MaxValueValidator(max_value)])
    v28 = models.FloatField(blank=True, null=True, validators=[MinValueValidator(min_value), MaxValueValidator(max_value)])
    amount = models.FloatField(blank=True, null=True, validators=[MinValueValidator(min_value), MaxValueValidator(max_value)])
    predictions = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
        model_path = os.path.join(settings.BASE_DIR, 'DetectorApp', 'model.joblib')
        ml_model = joblib.load(model_path)
        # Assuming that your model takes in the 'time', 'v1' through 'v28', and 'amount' fields in this specific order
        self.predictions = ml_model.predict([[self.time, self.v1, self.v2, self.v3, self.v4, self.v5, self.v6, self.v7, self.v8, self.v9, self.v10, self.v11, self.v12, self.v13, self.v14, self.v15, self.v16, self.v17, self.v18, self.v19, self.v20, self.v21, self.v22, self.v23, self.v24, self.v25, self.v26, self.v27, self.v28, self.amount]])
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['time']

    
