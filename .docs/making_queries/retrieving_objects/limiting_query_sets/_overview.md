# Limiting QuerySets

- Use a subset of Python's array-slicing synyax to limit your **QuerySet** to a certain number of results. This is the equivalent of SQL's **LIMIT** and **OFFSET** clauses.

- For example, this return the first 5 objects (**LIMIT 5**):

```python
Entry.objects.all()[:5]
```

- This returns the sixth through tenth objects (**OFFSET 5 LIMIT 5**):

```python
Entry.objects.all()[5:10]
```

- Negative indexing (i.e: **Entry.objects.all()[-1]**) is not supported.

- Generally, slicing a **QuerySet** returns a new **QuerySet** - it doesn't evaluate the query. An exception is if you use the "step" parameter of Python slice syntax. For example, this would actually execute the query in order to return a list of every second object of the first 10:

```python
Entry.objects.all()[:10:2]
```

- Further filtering or ordering of a sliced queryset is prohibited due to the ambiguous nature of how that might work.

- To retrieve a single object rather than a list (e.g. **SELECT foo FROM bar LIMIT 1**), use an index instead of a slice. For example, this returns the first **Entry** in the database, after ordering entries alphabetically by headline:

```python
Entry.objects.order_by("headline")[0]
```

- This is roughly equivalent to:

```python
Entry.objects.order_by("headline")[0:1].get()
```

- Note, however, that the first of these will raise **IndexError** while the **second** will raise **DoesNotExist** if no objects match the given criteria. See **get()** for more details.
