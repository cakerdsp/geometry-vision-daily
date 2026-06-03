import requests

from scripts.update_papers import ArxivClient, is_arxiv_rate_limit_error


def test_arxiv_client_honors_retry_after_for_429() -> None:
    client = ArxivClient(_config())
    response = requests.Response()
    response.status_code = 429
    response.headers["Retry-After"] = "75"
    error = requests.HTTPError("rate limited", response=response)

    assert client._sleep_seconds_for_error(error, attempt=1) == 75


def test_arxiv_client_uses_long_backoff_for_429_without_retry_after() -> None:
    client = ArxivClient(_config())
    response = requests.Response()
    response.status_code = 429
    error = requests.HTTPError("rate limited", response=response)

    assert client._sleep_seconds_for_error(error, attempt=2) == 120


def test_arxiv_rate_limit_error_detection_walks_exception_chain() -> None:
    response = requests.Response()
    response.status_code = 429
    http_error = requests.HTTPError("Temporary arXiv HTTP status 429", response=response)
    wrapped = RuntimeError("arXiv query failed after 3 attempts")
    wrapped.__cause__ = http_error

    assert is_arxiv_rate_limit_error(wrapped)


def _config() -> dict:
    return {
        "arxiv": {
            "base_url": "http://export.arxiv.org/api/query",
            "timeout_seconds": 30,
            "max_retries": 3,
            "request_interval_seconds": 10,
            "retry_429_seconds": 60,
            "retry_5xx_seconds": 10,
            "user_agent": "geometry-vision-daily/1.0 test",
        }
    }
