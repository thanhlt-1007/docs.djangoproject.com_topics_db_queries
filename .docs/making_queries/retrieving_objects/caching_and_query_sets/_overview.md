# Caching and QuerySets

- Each **QuerySet** contains a cache to minimize database access. Understanding how it works will allow you to write the mose efficient code.

- In a newly created **QuerySet**, the cache is empty. The first time a **QuerySet** is evaluated - and, hence, a database query happens - Django saves the query results in the **QuerySet**'s cache and returns the results that have been explicitly requested (e.g., the next element, if the **QuerySet** is being iterated over). Subsequent evaluations of the **QuerySet** reuse the cached results.

- Keep this caching behavior in mind, because it may bite you if you don't use your **QuerySet**s correctly. For example, the following will create two **QuerySet**s evaluate them, and throw them away:

```python
print([e.headline for e in Entry.objects.all()])
print([e.pub_date for e in Entry.objects.all()])
```

- That means the same database query will be executed twice, effectively doubling your database load. Also, there's a possibility the two lists may not include the same database records, because an **Entry** may have been added or deleted in the split second between the two requests.

- To avoid this problem, save the **QuerySet** abd reuse it:

```python
queryset = Entry.objects.all()
print([e.headline for e in queryset])
print([e.pub_date for e in queryset])
```
