# Retrieving specific objects with filters

- The **QuerySet** returned by **all()** describes all objects in the database table. Usually, though, you'll need to select only a subset of the complete set of objects.

- To create such as subset, you refine the initial **QuerySet**, adding filter conditions. The two most common ways to refine a **QuerySet** are:

## filter(**kwargs)

- Returns a new **QuerySet** containing objects that match the given lookup parameters.

## exclude(**kwargs)

- Returns a new **QuerySet** containing objects that do not match the given lookup parameters.

- The lookup parameters (****kwargs** in the above function definitions) should be in the format described in **Field lookups** below.

- For example, to get a **QuerySet** of blog entries from the year 2006, use **filter()** like so:

```python
Entry.objects.filter(pub_date__year=2006)
```

- With the default manager class, it is the same as:

```python
Entry.obejcts.all().filter(pub_date__year=2006)
```
