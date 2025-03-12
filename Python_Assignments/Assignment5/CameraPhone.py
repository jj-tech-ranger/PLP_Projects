from Python_Assignments.Assignment5.SmartPhone import Smartphone


class CameraPhone(Smartphone):
    def __init__(self, brand, model, battery_life, camera_megapixels):
        super().__init__(brand, model, battery_life)
        self.camera_megapixels = camera_megapixels

    def take_photo(self):
        if self.is_on:
            print(f"Taking a photo with {self.camera_megapixels} MP camera.")
        else:
            print("Please turn on the phone first.")

my_camera_phone = CameraPhone("Samsung", "Galaxy S21", 18, 108)
my_camera_phone.display_info()
my_camera_phone.turn_on()
my_camera_phone.take_photo()
my_camera_phone.turn_off()