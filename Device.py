class Device:

    def __init__(self, device_id=0, processing_power=0, task_assigned=0):
        self.device_id = device_id
        self.processing_power = processing_power
        self.task_assigned = task_assigned
        self.pheromone_level = self.processing_power / (1 + self.task_assigned)

    def increase_tasks(self):
        self.task_assigned += 1

    def details(self):
        return "ID: ", self.device_id, "\n Processing power", self.processing_power, "\n Task assigned", self.task_assigned, "\n"
