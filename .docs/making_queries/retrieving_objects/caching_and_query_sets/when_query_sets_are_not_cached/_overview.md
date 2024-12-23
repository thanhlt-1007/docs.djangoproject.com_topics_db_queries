# When QuerySets are not cached

- Querysets do not always cache their results. When evaluating only part of the queryset, the cache is checked, but if it is not populated then the items returned by the subsequent query are not cached. Specifically, this means that limiting the queryset using an array slice or an index will not populate the cache.

- For example, repeatedly getting a certain index in a queryset object will query the database each time:

```python
queryset = Entry.objects.all()
print(queryset[5]) # Query the database
print(queryset[5]) # Query the database again
```

- However, if the entire queryset has already been evaluated, the cache will be checked instead:

```python
queryset = Entry.objects.all()
[entry for entry in queryset] # Queries the database
queryset[5] # Use cache
queryset[5] # Use cache
```

- Here are some examples of other actions that will result in the entire queryset being evaluated and therefore populate the cache:

```python
[entry for entry in queryset]
bool(queryset)
entry in queryset
list(queryset)
```

> [!Note]
>
> Simply printing the queryset will not populate the cache. This is becase the call to **__repr__()** only return a slice of the entire queryset.
