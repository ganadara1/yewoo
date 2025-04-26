import pygame

class Portal:
    def __init__(self, x, y, width, height, target_map, image_path="assets/images/portal.png"):
        self.rect = pygame.Rect(x, y, width, height)  # 포탈의 위치와 크기
        self.target_map = target_map  # 이동할 맵 이름

        # 이미지 로드 및 크기 조정
        try:
            self.image = pygame.image.load(image_path)
            self.image = pygame.transform.scale(self.image, (width, height))
            print(f"Portal image loaded successfully: {image_path}")
        except pygame.error as e:
            print(f"Error loading portal image: {e}")
            self.image = None

    def draw(self, screen):
        if self.image:
            screen.blit(self.image, self.rect.topleft)  # 이미지 그리기
        else:
            # 이미지가 없을 경우 기본 사각형으로 표시
            pygame.draw.rect(screen, (0, 255, 0), self.rect)