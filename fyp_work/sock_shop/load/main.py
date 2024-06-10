from locust import SequentialTaskSet, HttpUser, constant, task, between
import random
import array


class MySeqTask(SequentialTaskSet):

    wait_time = between(1, 2)

    list_of_products = [
        "/detail.html?id=03fef6ac-1896-4ce8-bd69-b798f85c6e0b",
        "/detail.html?id=3395a43e-2d88-40de-b95f-e00e1502085b",
        "/detail.html?id=510a0d7e-8e83-4193-b483-e27e09ddc34d",
        "/detail.html?id=808a2de1-1aaa-4c25-a9b9-6612e8f29a38",
        "/detail.html?id=819e1fbf-8b7e-4f6d-811f-693534916a8b",
        "/detail.html?id=837ab141-399e-4c1f-9abc-bace40296bac"
    ]

    def add_to_wishlist(self):
        self.client.get("/basket.html")

    @task
    def visit_homepage(self):
        self.client.get("/index.html")
        from datetime import datetime
        current_time = datetime.now()
        current_hour = current_time.hour
        current_minute = current_time.minute
        if (current_hour==22 or current_hour==2)  and current_minute==55:
            self.cpu_intensive_calculation()
        elif (current_hour==22 or current_hour==6)  and current_minute==52:
            self.memory_intensive_operation()

    @task
    def visit_catalogue_page(self):
        self.client.get("/category.html")
        r= random.randint(2,5)
        for i in range(0,r):
            p = random.randint(0, 4)
            self.client.get(self.list_of_products[p])
            self.add_to_wishlist()
    

    def cpu_intensive_calculation(self):
        x = 0
        for i in range(100000000):
            x += i

    def memory_intensive_operation(self): 
        arr = array.array("L", [0] * (1024 * 1024))
        for i in range(len(arr)):
            arr[i] = i

    

class MyLoadTest(HttpUser):
    host = "http://192.168.49.2:30001/"
    tasks = [MySeqTask]


