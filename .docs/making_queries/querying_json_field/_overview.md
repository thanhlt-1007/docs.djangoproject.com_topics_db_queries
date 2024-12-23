# Querying JSONField

- Lookups implementation is different in **JSONField**, mainly due to the existence of key transformations. To demonstrate, we will use the following example model:

```python
from django.db import models

class Dog(models.Model):
    name = models.CharField(max_length=200)
    data = models.JSONField(null=True)
```
