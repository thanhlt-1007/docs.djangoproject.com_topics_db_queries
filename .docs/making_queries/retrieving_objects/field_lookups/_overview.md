# Field lookups

- Field lookups are how you specify the meat of an SQL **WHERE** clause. They're specified as keyword arguments to the **QuerySet** methods **filter()**, **exclude()**, and **get()**.

- Basic lookups keyword arguments take the form **field__lookuptype=value**. (That's double-underscore). For example:

```python
Entry.objects.filter(pub_date__lte="2006-01-01")
```

translates (roughy) into the following **SQL**:

```SQL
SELECT * FROM blog_entry WHERE pub_date <= '2006-01-01'
```

> [!Note] How this is possible
>
> Python has the ability to define functions that accept arbitrary name-value arguments whose names and values areevaluated at runtime. For more information, see **Keyword Arguments** in the official Python tutorial.

- The field specified in a lookup has to be the name of a model field. There's one exception though, in case of **ForeignKey** you can specify the field name suffixed with **_id**. In this case, the value parameter is expected to contain the raw value of the foreign models primary key. For example:

```python
Entry.objects.filter(blog_id=4)
```

- If you pass an invalid keywork argument, a lookup function will raise **TypeError**.

- The database API supports about two dozen lookup types; a complete reference can be found in the **field lookup reference**. To give you a taste of what's available, here's some of the more common lookups you'll probably use:

## exact:

- An "exact" match. For example:

```python
Entry.obejcts.get(headline__exact="Cat bites dog")
```

- Would generate SQL along these lines:

```SQL
SELECT ... WHERE headline = 'Cat bites dog';
```

- If you don't provide a lookup type - that is, if your keyword argument doesn't contain a double underscore - the lookup type is assumed to be **exact**.

- For example, the following two statements are equivalent:

```python
Blog.objects.get(id__exact=14)
Blog.objects.get(id=14)
```

- This is for convenience, because **exact** lookups are the common case.

## iexact

- A case-insensitive match. So, the query:

```python
Blog.objects.get(name__iexact="beatles blog")
```

- Would match a **Blog** titled **"Beatles Blog"**, **"beatles blog"**, or even **"BeAtlES blOG"**.

## contains

- Case-sensitive containment test. For example:

```python
Entry.objects.get(headline__contains="Lennon")
```

- Roughly translates to this SQL:

```python
SELECT ... WHERE headline LIKE '%Lennon%'
```

- Note this will match the headline **'Today Lennon honored'** but not **'today lennon honored'**.

- There's also a case-insensitive versions, **icontains**.

## startswith, endswith

- Starts-with and ends-with search, respectively. There are also case-insensitive versions called **istartswith** and **iendswith**.

- Again, this only scratches the surface. A complete reference can be found in the **field lookup reference**.
