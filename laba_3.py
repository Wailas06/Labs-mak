import copy

class MediaTemplate:
    def __init__(self, name, data):
        self.name = name
        self.data = data

    def clone(self):
        return copy.deepcopy(self)

    def display(self):
        raise NotImplementedError("Subclasses must implement this method")

class VideoFile(MediaTemplate):
    def __init__(self, name, data, resolution):
        super().__init__(name, data)
        self.resolution = resolution

    def display(self):
        print(f"VideoFile:\n Name: {self.name}\n Resolution: {self.resolution}\n Data: {self.data}\n")

class ImageFile(MediaTemplate):
    def __init__(self, name, data, format_type):
        super().__init__(name, data)
        self.format_type = format_type

    def display(self):
        print(f"ImageFile:\n Name: {self.name}\n Format: {self.format_type}\n Data: {self.data}\n")

def run_demo():
    print("== Створення шаблонів медіа ==")
    video_template = VideoFile("Презентація", "Відео презентації продукту", "1080p")
    image_template = ImageFile("Логотип", "Файл логотипу компанії", "PNG")

    video_template.display()
    image_template.display()

    print("== Клонування шаблонів ==")
    video_clone = video_template.clone()
    image_clone = image_template.clone()

    video_clone.name = "Оновлена презентація"
    video_clone.data = "Оновлене відео"
    video_clone.resolution = "4K"

    image_clone.name = "Логотип 2025"
    image_clone.format_type = "SVG"

    print("Оригінали:")
    video_template.display()
    image_template.display()

    print("Копії:")
    video_clone.display()
    image_clone.display()

if __name__ == "__main__":
    run_demo()
