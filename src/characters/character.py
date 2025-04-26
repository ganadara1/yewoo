import pygame

class Character:
    def __init__(self, x, y, image_path, scale=0.2):  # 크기를 더 줄임
        self.image = pygame.image.load(image_path)
        original_width, original_height = self.image.get_size()
        new_width = int(original_width * scale)
        new_height = int(original_height * scale)
        self.image = pygame.transform.scale(self.image, (new_width, new_height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = 5  # 이동 속도

    def update(self, keys):
        if keys[pygame.K_UP]:  # 위쪽 화살표
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:  # 아래쪽 화살표
            self.rect.y += self.speed
        if keys[pygame.K_LEFT]:  # 왼쪽 화살표
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:  # 오른쪽 화살표
            self.rect.x += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)