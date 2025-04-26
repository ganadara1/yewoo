import pygame
import math

class NPC:
    def __init__(self, x, y, image_path, scale=0.2):  # 크기를 더 줄임
        self.image = pygame.image.load(image_path)
        original_width, original_height = self.image.get_size()
        new_width = int(original_width * scale)
        new_height = int(original_height * scale)
        self.image = pygame.transform.scale(self.image, (new_width, new_height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = 2  # NPC 이동 속도
        self.min_distance = 30  # 캐릭터와 최소 거리 (픽셀 단위)

    def update(self, target_rect):
        # NPC와 캐릭터 사이의 거리 계산
        distance_x = target_rect.x - self.rect.x
        distance_y = target_rect.y - self.rect.y
        distance = math.sqrt(distance_x**2 + distance_y**2)

        # 최소 거리 이상일 때만 움직임
        if distance > self.min_distance:
            if self.rect.x < target_rect.x:
                self.rect.x += self.speed
            elif self.rect.x > target_rect.x:
                self.rect.x -= self.speed

            if self.rect.y < target_rect.y:
                self.rect.y += self.speed
            elif self.rect.y > target_rect.y:
                self.rect.y -= self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)