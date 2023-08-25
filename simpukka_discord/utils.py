from simpukka import filters


def clean_url_filter(url: str) -> str:
    return filters.url_filter(url.replace("attachment://", ""))