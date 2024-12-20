# Saving changes to obejct

- To save changes to an object that's already in the database, **use save().**

```python
b5.name = "New name"
b5.save()
```

- This perform an **UPDATE** SQL statement behind the scenes. Django doesn't hit the database until you explicitly call **save()**
