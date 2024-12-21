# Retrieving a single object with get()

- **filter()** will always give you a **QuerySet**, even if only a single object matches the query - in this case, it will be a **QuerySet** containing a single element.

- If you know there is only one object that matches your query, you can use the **get()** method on a **Manaber** which returns the object directly:

```python
one_entry = Entry.objects.get(pk=1)
```

- You can use any query expression with **get()**, just like with **filter()** - again, see **Field lookups** below.

- Note that there is a difference between using **get()**, and using **filter()** with a slice of **[0]**. If there no results that match the query, **get()** will raise a **DoesNotExist** exception. This exception is an attribute of the model class that the query is being performed on - so in the code above, if there is no Entry object with a primary key of 1, Django will raise **Entry.DoesNotExist**.

- Similarly, Django will complain if more than one item matches the **get()** query. In this case, it will raise **MultipleObjectsReturned**, which again is an attribute of the model class itself.
