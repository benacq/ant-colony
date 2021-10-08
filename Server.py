from Device import Device


class Server:
    devices = [Device(1, 2, 3), Device(2, 4, 5), Device(3, 5, 1), Device(4, 6, 7), Device(5, 5, 4)]

    def __init__(self, job):
        self.job = job

    def assign_job(self):
        new_devices = sorted(self.devices, key=lambda x: x.pheromone_level, reverse=True)
        return new_devices[0]

    def get_assigned_device(self):
        assigned_device = self.assign_job()
        assigned_device.increase_tasks()
        print(
            f'Job {self.job} assigned to {assigned_device.device_id} with Pheromone level {assigned_device.pheromone_level}')
