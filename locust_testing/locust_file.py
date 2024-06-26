"""
site: https://locust.io/
git: https://github.com/locustio/locust
doc: http://docs.locust.io/en/stable/

run v1:
    locust --processes 4 --tags dj_sync_dummy_view
run v2:
    locust --headless -u 1000 -r 100 -t 60 --processes 4 --tags dj_sync_dummy_view
"""

from locust import FastHttpUser, task, tag


class LocustRPS(FastHttpUser):
    """LocustRPS"""

    """Django"""

    @tag("dj_sync_dummy_view")
    @task
    def dj_sync_dummy_view(self) -> None:
        """host = http://127.0.0.1:8000"""
        self.client.get(
            url="/dj_sync_dummy_view",
            timeout=(10, 10),
        )
        return None

    @tag("dj_async_dummy_view")
    @task
    def dj_async_dummy_view(self) -> None:
        """host = http://127.0.0.1:8001"""
        self.client.get(
            url="/dj_async_dummy_view",
            timeout=(10, 10),
        )
        return None

    @tag("dj_async_dummy_foo")
    @task
    def dj_async_dummy_foo(self) -> None:
        """host = http://127.0.0.1:8001"""
        self.client.get(
            url="/dj_async_dummy_foo",
            timeout=(10, 10),
        )
        return None

    @tag("dj_sync_user_view")
    @task
    def dj_sync_user_view(self) -> None:
        """host = http://127.0.0.1:8000"""
        self.client.get(
            url="/dj_sync_user_view",
            timeout=(10, 10),
        )
        return None

    @tag("dj_async_user_view")
    @task
    def dj_async_user_view(self) -> None:
        """host = http://127.0.0.1:8001"""
        self.client.get(
            url="/dj_async_user_view",
            timeout=(10, 10),
        )
        return None

    """FastAPI"""

    @tag("fa_sync_dummy_foo")
    @task
    def fa_sync_dummy_foo(self) -> None:
        """host = http://127.0.0.1:8002"""
        self.client.get(
            url="/fa_sync_dummy_foo",
            timeout=(10, 10),
        )
        return None

    @tag("fa_async_dummy_foo")
    @task
    def fa_async_dummy_foo(self) -> None:
        """host = http://127.0.0.1:8002"""
        self.client.get(
            url="/fa_async_dummy_foo",
            timeout=(10, 10),
        )
        return None

    @tag("fa_sync_user_foo")
    @task
    def fa_sync_user_foo(self) -> None:
        """host = http://127.0.0.1:8002"""
        self.client.get(
            url="/fa_sync_user_foo",
            timeout=(10, 10),
        )
        return None

    @tag("fa_async_user_foo")
    @task
    def fa_async_user_foo(self) -> None:
        """host = http://127.0.0.1:8002"""
        self.client.get(
            url="/fa_async_user_foo",
            timeout=(10, 10),
        )
        return None
