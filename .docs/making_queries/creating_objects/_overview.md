# Creating objects

- To represent database-table data in Python objects, Django uses an intuitive system: A model class represent a database table, and an instance of that class represent a particular record in the database table.
<br>

- To create an object, instantiate it using keywork arguments to the model class, then call **[save()](https://docs.djangoproject.com/en/5.1/ref/models/instances/#django.db.models.Model.save)** to save it to the database.
<br>

- Assuming models live in a **models.py** file inside a **blog** Django app, here is an example:


```python
from blog.models import Blog

b = Blog(name="Beatles Blog", tagline="All the latest Beatles news.")
b.save()
```

- This performs an **INSERT** SQL statement behind the scene. Django doesn't hit the database until you explicitly call **save()**.
<br>

- The **save()** nethod has no return value.

> [!Note]
>
> **save()** takes a number of advanced options not described here. See the document for **[save()](https://docs.djangoproject.com/en/5.1/ref/models/instances/#django.db.models.Model.save)** for complete details. To create and save an object in a single step, use the **[create()](https://docs.djangoproject.com/en/5.1/ref/models/querysets/#django.db.models.query.QuerySet.create)** method.
