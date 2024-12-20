# Saving ForeignKey and ManyToManyField fields

- Updating a **ForeignKey** field works exactly the same way as saving a normal field - assign an object of the right type to the field in question. This example updates the **blog** attribute of an **Entry** instance **entry**, assuming appropriate instance of **Entry** and **Blog** are alerady saved to the database (so we can retrieve them below):

```python
from blog.models import Blog, Entry

entry = Entry.objects.get(pk=1)
cheese_blog = Blog.objects.get(name="Cheddar Talk")
entry.blog = cheese_blog
entry.save()
```

- Updating a **ManyToManyField** works a little differently - use the **add()** method on the field to add a record to the relation. This example adds the **Autho** instance **joe** to the **entry** object:

```python
from blog.models import Author

joe = Author.objects.create(name="Joe")
entry.authors.add(joe)
```

- To add multiple records to a **ManyToManyField** in one go, include multiple arguments in the call to **add()**, like this:

```python
john = Author.objects.create(name="John")
paul = Author.objects.create(name="Paul")
george = Author.objects.create(name="George")
ringo = Author.objects.create(name="Ringo")
entry.authors.add(john, paul, geogre, ringo)
```

- Django will complain if you try to assign or add an object of the wrong type.
