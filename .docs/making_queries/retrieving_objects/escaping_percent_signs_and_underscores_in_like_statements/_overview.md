# Escaping percent signs and underscores in LIKE statements

- The field lookups that equate to **LIKE** SQL statements (**iexact**, **contains**, **icontains**, **startswith**, **endswith** and **iendswith**) will automatically escape the two special characters used in **LIKE** statement, the percent sign and the underscore.  (In a **LIKE** statement, the percent sign signifies a multiple-character wildcard and the underscore signifies a single-character wildcard.)

- This means things should work intuitively, so the abstraction doesn't leak. For example, to retrieve all the entries that contain a percent sign, use the percent sign as any other character:

```python
Entry.objects.filter(headline__contains="%")
```

- Django takes care of the quoting for you; the resulting SQL will look something like this:

```SQL
SELECT ... WHERE headline LIKE '%\%%';
```

- Same goes for underscores. Both percentage signs and underscores are handled for you transparently.
