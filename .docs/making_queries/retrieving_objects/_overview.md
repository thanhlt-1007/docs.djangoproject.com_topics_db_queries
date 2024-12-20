# Retrieving objects

- To retrieve objects from your database, construct a  **QuerySet** via **Manager** on your model class.

- A **QuerySet** represents a collection of objects from your database. It can have zero, one or many filters. Filters narrow down the query results bases on the given parameters. In SQL terms, a QuerySet equates to a **SELECT** statement, and a filter is a limiting clause such as **WHERE** or **LIMIT**.

- You get a **QuerySet** by using your model's **Manager**. Each model has at least one **Manager** and it's called objects by default. Access it directly via the model class, like so:

```python
Blog.objects
# <django.db.models.manager.Manager object at ..>

b = Blog(name="Foo", tagline = "Bar")
# b.objects
# Traceback:
# ...
#  AttributeError: "Manager isn't accessible via Blog instances."
```

> [!Note]
>
> **Managers** are accessible only via model classes, rather than from model instances, to enforce a separation between "table-level" operations and "record-level" operations.

- The **Manager** is the main source if **QuerySet** for a model. For example, **Blog.objects.all()** returns a **QuerySet** that contains all **Blog** objects in the database.
