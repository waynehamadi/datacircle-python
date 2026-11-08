# datacircle

Find the best GTM APIs. We benchmark all the GTM APIs and we put the results on our website: https://datacircle.dev

A small Python client for the open Datacircle API (https://api.datacircle.dev/v1, no key). It has no dependencies.

```python
import datacircle

datacircle.apis()                      # every API on the sheet
datacircle.best("email-finder")        # who is best for one API
datacircle.plans(api="email-finder", limit=5)
datacircle.provider("hunter")          # one provider's ranks
```

The spec: https://api.datacircle.dev/v1/openapi.json. At most 60 calls a minute from one address.
