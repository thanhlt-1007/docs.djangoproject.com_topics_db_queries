# Retrieving all objects

- The simplest way to retrieve objects from a table is to get all of them. To do this, use the **all()** method on a **Manager**:

```python
all_entries = Entry.objects.all()
```

- The **all()** method returns a **QuerySet** of all the objects in the database.
