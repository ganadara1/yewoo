class SceneManager:
    def __init__(self):
        self.scenes = {}
        self.current_scene = None

    def add_scene(self, name, scene):
        self.scenes[name] = scene

    def set_scene(self, name):
        if name in self.scenes:
            self.current_scene = self.scenes[name]
            print(f"Scene changed to: {name}")
        else:
            print(f"Scene '{name}' not found!")

    def update(self, character, keys, events):
        if self.current_scene:
            self.current_scene.update(character, self, keys, events)

    def draw(self, screen):
        if self.current_scene:
            self.current_scene.draw(screen)