from simpukka import filters
from functools import partial

def clean_url_filter(url: str) -> str:
    return filters.url_filter(url.replace("attachment://", ""))


class ImmutablePartial:
    """Creates more safe partial which doesn't expose information or allow any changing."""
    def __init__(self, func, *args, **kwargs):
        self._partial = partial(func, *args, **kwargs)

    def __call__(self, *args, **kwargs):
        return self._partial(*args, **kwargs)

    def __repr__(self):
        return "<simpukka.ImmutablePartial>"

    def __str__(self):
        return "<simpukka.ImmutablePartial>"