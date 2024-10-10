from locust import HttpUser, task, wait_time, between

class HelloWorldUser(HttpUser):
    jwt_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2NzA0ZDU1YjRhYzI3Nzc2OGQxODUyOGQiLCJleHAiOjE3Mjg1MzEyOTAsImlhdCI6MTcyODUzMDM5MCwic2Vuc2l0aXZlIjpmYWxzZSwidHdvZmFfb2siOmZhbHNlfQ.WFBE6lf-HtRW-Ut4cxkVxPGh2wXk3fHQR7iiDAIxmhc"
        
    headers = {
        "Authorization": f"Bearer {jwt_token}"
    }

    wait_time = between(15,15)

    # @task
    # def health(self):
    #     self.client.get("/")

    @task
    def me(self):
        self.client.get("/api/v1/auth/me", headers=self.headers)
    
    @task
    def companies(self):
        self.client.get("/api/v1/analytics/companies", headers=self.headers)
    
    @task
    def analytics_me(self):
        self.client.get("/api/v1/analytics/me", headers=self.headers)