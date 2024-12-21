# Lookups that span relationships

- Django offers a powerful and intuitive way to "follow" relationships in lookups, taking care of the SQL **JOIN**s for you automatically, behind the scenes. To span a relationship, use the field name of related fields across models, separated by double underscore, until you get to to teh field you want.

- This example retrieves all **Entry** objects with a **Blog** whise **name** is **'Beatles Blog'**:

```python
Entry.objects.filter(blog__name="Beatles Blog")
```

- This spanning can be as deep as you'd like.

- It works backwards, too. While it **can be customized** by default you refer to a "reverse" relationship in a lookup using the lowercase name of the model.

- This example retrieves all **Blog** objects which have at least one **Entry** whose **headline** contains **'Lennon'**:

```python
Blog.objects.filter(entry__headline__contains="Lennon")
```

- If you are filtering across multiple relationships and one of the intermediate models doesn't have a value that meets the filter condition, Django will treat it as if there is an empty (all values are **NULL**), but valid, object there. All this means is that no error will be raised. For example, in this filter:

```python
Blog.objects.filter(entry__authors__name="Lennon")
```

- (if there was a related **Author** model), if there was no **author** associated with an entry, it would be treated as if there was also no **name** attached, rather than raising an error because of the missing **author**. Usually this is exactly what you want to have happen. The only case where it might be confusing is if you are using **isnull**. Thus:

```python
Blog.objects.filter(entry__authors__name__isnull=True)
```

- will return **Blog** objects that have an empty **name** on the **author** and also those which have an empty **author** on the **entry**. If you don't want those latter objects, you could write:

```python
Blog.objects.filter(entry__authors__isnull=False, entry__authors__name__isnull=True)
```
