from urls.custom_urls import url_paths


def resolved_url(url_path):
    return url_paths.get(url_path)
