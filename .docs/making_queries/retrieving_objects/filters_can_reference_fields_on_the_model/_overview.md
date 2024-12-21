# Filters can reference fields on the model

- In the examples given so far, we have constructed filters that compare the value of a model field with a constant. But what if you want to compare the value of a model field with another field on the same model?

- Django provides **F expressions** to allow such comparisons. Instance of **F()** act as a reference to a model field within a query. These references can then be used in query filters to compare the values of two different fields on the same model instance.

- For example, to find a list of all blog entries that have had more comments than pingbacks, we construct an **F()** object to reference the pingback count, and use that **F()** object in the query:

```python
from django.db.models import F

Entry.objects.filter(number_of_comments__gt=F("number_of_pingbacks"))
```

- Django supports the use of addition, subtraction, multiplication, division, modulo, and power arithmetic with **F()** objects, both with constants and with other **F()** objects. To find all the blog entries with more than twice as many comments as pingbacks, we modify the query:

```python
Entry.objects.filter(number_of_comments__gt=F("number_of_pingbacks") * 2)
```

- To find all the entries where the rating of the entry is less than the sum of the pingback count and comment count, we would issue the query:

```python
Entry.objects.filter(rating__lt=F("number_of_comments") + F("number_of_pingbacks"))
```

- You can also use the double underscore notation to span relationships in an **F()** object. An **F()** object with a double underscore will introduce any joins needed to access the related object. For example, to retrieve all the entries where the author's name is the same as the blog name, we could issue the query:

```python
Entry.objects.filter(author__name=F("blog__name))
```

- For date and date/time fields, you can add or subtract a **timedelta** object. The following would return all entries that were modified more than 3 days after they were published:

```python
from datetime import timedelta

Entry.objects.filter(mod_date__gt=F("pub_date") + timedelta(days=3))
```

- The **F()** objects support bitwise operations by **.bitand()**, **.bitor()**, **.bitxor()**, **.bitrightshift()**, and **.bitleftshift()**. For example:

```python
F("somefield").bitand(16)
```
