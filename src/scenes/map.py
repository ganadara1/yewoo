import pygame
import math

class Map:
    def __init__(self, background_path, portals, npcs=None, description=""):
        self.background = pygame.image.load(background_path)
        self.background = pygame.transform.scale(self.background, (1024, 768))
        self.portals = portals  # 포탈 리스트
        self.npcs = npcs if npcs else []  # NPC 리스트 (기본값은 빈 리스트)
        self.portal_cooldown = 0  # 포탈 이동 쿨다운 시간 (프레임 단위)
        self.interaction_image = None  # 출력할 이미지 (기본값 없음)
        self.interaction_start_time = None  # 상호작용 시작 시간 초기화
        self.current_dialogue = None  # 현재 출력 중인 대사
        self.dialogue_end_time = None  # 대사 출력 종료 시간
        self.font = pygame.font.Font("assets/fonts/NanumGothicBold.ttf", 28)  # 굵은 한글 폰트 설정
        self.description = description  # 맵 설명

    def update(self, character, scene_manager, keys, events):
        # 쿨다운 감소
        if self.portal_cooldown > 0:
            self.portal_cooldown -= 1

        # 포탈 충돌 처리
        for portal in self.portals:
            if character.rect.colliderect(portal.rect):
                for event in events:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and self.portal_cooldown == 0:
                        print(f"Moving from {scene_manager.current_scene} to {portal.target_map}")
                        scene_manager.set_scene(portal.target_map)
                        self.portal_cooldown = 30  # 30프레임 동안 추가 입력 무시
                        return

        # NPC와 상호작용 처리
        for npc in self.npcs:
            distance = ((character.rect.centerx - npc.rect.centerx) ** 2 +
                        (character.rect.centery - npc.rect.centery) ** 2) ** 0.5
            if distance < 50:  # NPC와의 상호작용 거리 (50 픽셀 이내)
                for event in events:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_a:  # A 키 입력
                        print(f"Interacting with NPC at ({npc.rect.centerx}, {npc.rect.centery})")
                        self.current_dialogue = "소중한 추억을 보여줄게"
                        self.interaction_start_time = pygame.time.get_ticks()  # 상호작용 시작 시간 기록
                        self.dialogue_end_time = pygame.time.get_ticks() + 2000  # 대사 출력 종료 시간 설정

    def draw(self, screen):
        screen.blit(self.background, (0, 0))  # 배경 그리기
        for portal in self.portals:
            portal.draw(screen)  # 포탈 그리기
        for npc in self.npcs:
            npc.draw(screen)  # NPC 그리기

        # 맵 설명 출력
        self.draw_description(screen)

        # 상호작용 이미지 출력
        if self.interaction_start_time:
            elapsed_time = pygame.time.get_ticks() - self.interaction_start_time
            if elapsed_time > 2000:  # 2초 후 이미지 출력
                scaled_image = pygame.transform.scale(self.interaction_image, (500, 375))  # 크기 조정
                screen.blit(scaled_image, (262, 196))  # 화면 중앙에 이미지 출력

        # 대사 출력
        if self.current_dialogue and pygame.time.get_ticks() < self.dialogue_end_time:
            self.draw_dialogue(screen)
        elif self.dialogue_end_time and pygame.time.get_ticks() >= self.dialogue_end_time:
            self.current_dialogue = None  # 대사 종료

    def draw_description(self, screen):
        # 맵 설명 텍스트 렌더링
        text_surface = self.font.render(self.description, True, (255, 255, 255))  # 하얀색 텍스트
        screen.blit(text_surface, (10, 10))  # 좌측 상단에 출력

    def draw_dialogue(self, screen):
        # 말풍선 배경 그리기
        dialogue_rect = pygame.Rect(300, 150, 424, 100)  # 말풍선 위치와 크기
        pygame.draw.rect(screen, (255, 255, 255), dialogue_rect)  # 흰색 배경
        pygame.draw.rect(screen, (0, 0, 0), dialogue_rect, 2)  # 검은색 테두리

        # 대사 텍스트 렌더링
        if self.current_dialogue:
            text_surface = self.font.render(self.current_dialogue, True, (0, 0, 0))  # 검은색 텍스트
            text_rect = text_surface.get_rect(center=dialogue_rect.center)
            screen.blit(text_surface, text_rect)