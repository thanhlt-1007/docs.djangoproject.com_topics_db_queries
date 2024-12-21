# Filtered QuerySets are unique

- Each time you refine a **QuerySet**, you get a brand-new **QuerySet** that is in no way bound to the previous **QuerySet**. Each refinement creates a separate and distinct **QuerySet** that can be stored, used and reused.

- Example:

```python
q1 = Entry.objects.filter(headline__startswith="What")
q2 = q1.exclude(pub_date__gte=datetime.date.today())
q2 = q1.filter(pub_date__gte=datetime.date.today())
```

- These three **QuerySet** are separate. The first is base **QuerySet** containing all entries that contain a headline starting with "What". The second is a subset of the first, with an additional criteria that excludes records whose **pub_date** is today or in the future. The initial **QuerySet (q1)** is unaffected by the refinement process.