class Camera:

    megapixels = 12

    def __init__(self, producer_name=None, amount_of_memory_in_mb=None,
                 zoom_ratio=None, image_format=None, memory_card_type=None, resolution=None):
        self.producer_name = producer_name
        self.amount_of_memory_in_mb = amount_of_memory_in_mb
        self.zoom_ratio = zoom_ratio
        self.image_format = image_format
        self.memory_card_type = memory_card_type
        self.resolution = resolution

    def __del__(self):
        pass

    def __str__(self):
        return "Producer name is: " + str(self.producer_name) + "\n" + \
                "Amount of memory in mb is: " + str(self.amount_of_memory_in_mb) + "\n" + \
                "Zoom ratio is: " + str(self.zoom_ratio) + "\n" + \
                "Image format is: " + str(self.image_format) + "\n" + \
                "Memory card type is: " + str(self.memory_card_type) + "\n" + \
                "Resolution is: " + str(self.resolution) + "\n"

    @staticmethod
    def get_megapixels():
        return Camera.megapixels


if __name__ == '__main_':
    first_camera = Camera()
    second_camera = Camera("Canon", 1024, 15)
    third_camera = Camera("Sony", 16384, 20, "JPEG", "SD-card", 1080)
    cameras = [first_camera, second_camera, third_camera]
    for camera in cameras:
        print(camera)