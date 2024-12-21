# QuerySets are lazy

- **QuerySet** are lazy - the act of creating a **QuerySet** doesn't involve any database activity. You can stack filters together all day along, and Django won't actually run the query until the **QuerySet** is evaluated. Take a look at this example:

```python
q = Entry.objects.filter(headline_startswith="What")
q = q.filter(pub_date__lte=datetime.date.today())
q = q.exclude(body_text__icontains="food")
print(q)
```

- Though this look like three database hits, in fact it hits the database only once, at the last line (**print(q)**). In general, the results of a **QuerySet** aren't fetched from the database until you "ask" for them. When you do, the **QuerySet** is evaluated by accessing the database. For more details on exactly when evaluation takes place, see **When QuerySets are evaluated**.
