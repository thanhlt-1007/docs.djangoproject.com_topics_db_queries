# Spanning multi-valued relationships

- When spanning a **ManyToManyField** or a reverse **ForeignKey** (such as from **Blog** to **Entry**), filtering on multiple attributes raises the question of whether to require each attribute to coincide in the same related object. We might seek blogs that have an entry from 2008 with "Lennon" in its headline, or we might seek blogs that merely have any entry from 2008 as well as some newer or older entry with "Lennon" in its headline.

- To select all blogs containing at least one entry from 2008 having "Lennon" in its headline (the same entry satisfying both conditions), we would write:

```python
Blog.objects.filter(entry__headline__contains="Lennon", entry__pub_date__year=2008)
```

- Otherwise, to perform a more permissive query selecting any blogs with merely some entry with "Lennon" in its headline and some entry from 2008, we would write:

```python
Blog.objects.filter(entry__headline__contains="Lennon")
    .filter(entry__pub_date__year=2008)
```

- Suppose there is only one blog that has both entries containing "Lennon" and entries from 2008, but that none of the entries from 2008 contained "Lennon". The first query would not return any blogs but the second query would return that one blog. (This is because the entries selected by the second filter may or may not be the same as the entries in the first filter. We are filtering the **Blog** items with each filter statement, not the **Entry** items.) In short, if each condition needs to match the same related object, then each should be contained in a single **filter()** call.

> [!Note]
>
> As the second (more permissive) query chains multiple filters, it performs multiple joins to the primary model, potentially yielding duplicates.

```python
from datetime import date

beatles = Blog.objects.create(name="Beatles Blog")
pop = Blog.objects.create(name="Pop Music Blog")

Entry.objects.create(
    blog=beatles,
    headline="New Lennon Biography",
    pub_date=date(2008, 6, 1),
)
Entry.objects.create(
    blog=beatles,
    headline="New Lennon Biography in Paperback",
    pub_date=date(2009, 6, 1),
)
Entry.objects.create(
    blog=pop,
    headline="Best Albums of 2008",
    pub_date=date(2008, 12, 15),
)
Entry.objects.create(
    blog=pop,
    headline="Lennon Would Have Loved Hip Hop",
    pub_date=date(2020, 4, 1),
)
Blog.objects.filter(
    entry__headline__contains="Lennon",
    entry__pub_date__year=2008,
)
# <QuerySet [<Blog: Beatles Blogs>]>
Blog.objects.filter(
    entry__headline__contains="Lennon",
).filter(
    entry__pub_date__year=2008,
)
# <QuerySet [<Blog: Beatles Blogs>], [<Blog: Beatles Blogs>], [<Blog: Pop Music Blog>]>
```

> [!Note]
>
> The behavior of **filter()** for queries that span multi-value relationships, as described above, is not implemented equivalently for **exclude()**. Instead, the conditions in a single **exclude()** call will not necessarily refer to the same item.
>
> For example, the following query would exclude blogs that contain both entries with "Lennon" in headline and entries published in 2008:
>
>```python
>Blog.objects.exclude(
>    entry__headline__contains="Lennon",
>    entry__pub_date__year=2008,
>)
>```
>
> However, unlike the behavior when using **filter()**, this will not limit blogs based on entries that satisfy both conditions. In order to do that, i.e. to select all blogs that do not contain entries published with "Lemon" that were published in 2008, you need to make two queries:
>
>```python
>Blog.objects.exclude(
>    entry__in=Entry.objects.filter(
>        headline__contains="Lennon",
>        pub_date__year=2008,
>),
>```
