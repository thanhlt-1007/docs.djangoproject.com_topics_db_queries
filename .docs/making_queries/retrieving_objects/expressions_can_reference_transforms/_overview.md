# Expressions can reference transforms

- Django supports using transforms in expressions.

- For example, to find all **Entry** objects published in the same year as they were last modified:

```python
from django.db.models import F

Entry.objects.filter(pub_date__year=F("mode_date__year"))
```

- To find the earliest year an entry was published, we can issue the query:

```python
from django.db.models import Min

Entry.objects.aggregate(first_published_year=Min("pub_date__year"))
```

- This example finds the value of the highest rated entry and the total number of comments on all entries for each year:

```python
from django.db.models import OuterRef, Subquery, Sum

Entry.objects
    .values("pub_date__year")
    .annotate(
        top_rating=Subquery(
            Entry.objects.filter(pub_date__year=OuterRef("pub_date__year"),)
                .order_by("-ratings")
                .values("ratings")[:1]
        ),
        total_comments=Sum("number_of_comments"),
    )
```
