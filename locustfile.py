from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    wait_time = between(1, 3)  # Espera entre 1 e 3 segundos entre requisições

    @task
    def get_root(self):
        self.client.get("/")
