# Chaining filters

- The result of refining a **QuerySet** is itself a **QuerySet**, so it's possible to chain refinements together. For example:

```python
Entry
    .objects
    .filter(headline_startswith="What")
    .exclude(pub_date__gte=datetime.date.today())
    .filter(pub_date__gte=datetime.date(2005, 1, 30))
```

- This takes the initial **QuerySet** of all entries in the database, adds a filter, then an exclusion, then another filter. The final result is a **QuerySet** containing all entries with a headline that starts with "What", that were published between January 30, 2005, and the current day.
