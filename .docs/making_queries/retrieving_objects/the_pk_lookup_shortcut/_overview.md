# The pk lookup shortcut

- For convenience, Django provides a **pk** lookup shortcut, which stands for "primary key".

- In the example **Blog** model, the primary key is the **id** field, so these three statements are equivalent:

```python
Blog.objects.get(id__exact=14)
Blog.objects.get(id=14)
Blog.objects.get(pk=14)
```

- The use of **pk** isn't limited to **__exact** queries - any query term can be combined with **pk** to perform a query on the primary key of a model:

```python
Blog.objects.filter(id__in=[1, 4, 7])
Blog.objects.filter(pk__gt=14)
```

- **ok** lookups also work across joins. For example, these statements are equivalent:

```python
Entry.objects.filter(blog__id__exact=3)
Entry.objects.filter(blog__id=3)
Entry.objects.filter(blog__pk=3)
```
