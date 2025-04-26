import pygame
import sys
from scenes.scene_manager import SceneManager
from scenes.map import Map
from objects.portal import Portal
from characters.character import Character
from characters.npc import NPC

def main():
    pygame.init()
    screen = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption("데이트 게임")
    
    clock = pygame.time.Clock()
    scene_manager = SceneManager()

    # 첫 번째 맵 생성 (map1)
    npc_map1 = NPC(512, 384, "assets/images/npc_map1.png", scale=0.2)  # map1의 중앙에 위치한 NPC
    portal_to_map2 = Portal(900, 400, 50, 50, "map2")  # map1에서 map2로 이동
    map1 = Map("assets/images/map1_background.png", [portal_to_map2], [npc_map1], description="6월 1일 망원한강공원")
    map1.interaction_image = pygame.image.load("assets/images/memory_map1.png")  # map1의 이미지

    # 두 번째 맵 생성 (map2)
    npc_map2 = NPC(512, 384, "assets/images/npc_map2.png", scale=0.2)  # map2의 중앙에 위치한 NPC
    portal_to_map1 = Portal(50, 400, 50, 50, "map1")  # map2에서 map1로 이동
    portal_to_map3 = Portal(900, 400, 50, 50, "map3")  # map2에서 map3로 이동
    map2 = Map("assets/images/map2_background.png", [portal_to_map1, portal_to_map3], [npc_map2], description="6월 2일 올림픽공원 장미축제")
    map2.interaction_image = pygame.image.load("assets/images/memory_map2.png")  # map2의 이미지

    # 세 번째 맵 생성 (map3)
    npc_map3 = NPC(512, 384, "assets/images/npc_map3.png", scale=0.2)  # map3의 중앙에 위치한 NPC
    portal_to_map2 = Portal(50, 400, 50, 50, "map2")  # map3에서 map2로 이동
    portal_to_map4 = Portal(900, 400, 50, 50, "map4")  # map3에서 map4로 이동
    map3 = Map("assets/images/map3_background.png", [portal_to_map2, portal_to_map4], [npc_map3], description="6월 6일 우리를 홀린 고양이 전시회")
    map3.interaction_image = pygame.image.load("assets/images/memory_map3.png")  # map3의 이미지

    # 네 번째 맵 생성 (map4)
    npc_map4 = NPC(512, 384, "assets/images/npc_map4.png", scale=0.2)  # map4의 중앙에 위치한 NPC
    portal_to_map3 = Portal(50, 400, 50, 50, "map3")  # map4에서 map3로 이동
    portal_to_map5 = Portal(900, 400, 50, 50, "map5")  # map4에서 map5로 이동
    map4 = Map("assets/images/map4_background.png", [portal_to_map3, portal_to_map5], [npc_map4], description="6월 9일 조계사 방문")
    map4.interaction_image = pygame.image.load("assets/images/memory_map4.png")  # map4의 이미지

    # 다섯 번째 맵 생성 (map5)
    npc_map5 = NPC(512, 384, "assets/images/npc_map5.png", scale=0.2)  # map5의 중앙에 위치한 NPC
    portal_to_map4 = Portal(50, 400, 50, 50, "map4")  # map5에서 map4로 이동
    portal_to_map6 = Portal(900, 400, 50, 50, "map6")  # map5에서 map6로 이동
    map5 = Map("assets/images/map5_background.png", [portal_to_map4, portal_to_map6], [npc_map5], description="6월 17일 선유도공원 산책")
    map5.interaction_image = pygame.image.load("assets/images/memory_map5.png")  # map5의 이미지

    # 여섯 번째 맵 생성 (map6)
    npc_map6 = NPC(512, 384, "assets/images/npc_map6.png", scale=0.2)  # map6의 중앙에 위치한 NPC
    portal_to_map5 = Portal(50, 400, 50, 50, "map5")  # map6에서 map5로 이동
    portal_to_map7 = Portal(900, 400, 50, 50, "map7")  # map6에서 map7로 이동
    map6 = Map("assets/images/map6_background.png", [portal_to_map5, portal_to_map7], [npc_map6], description="6월 29일 낙산공원")
    map6.interaction_image = pygame.image.load("assets/images/memory_map6.png")  # map6의 이미지

    # 일곱 번째 맵 생성 (map7)
    npc_map7 = NPC(512, 384, "assets/images/npc_map7.png", scale=0.2)  # map7의 중앙에 위치한 NPC
    portal_to_map6 = Portal(50, 400, 50, 50, "map6")  # map7에서 map6로 이동
    portal_to_map8 = Portal(900, 400, 50, 50, "map8")  # map7에서 map8로 이동
    map7 = Map("assets/images/map7_background.png", [portal_to_map6, portal_to_map8], [npc_map7], description="6월 30일 명동")
    map7.interaction_image = pygame.image.load("assets/images/memory_map7.png")  # map7의 이미지

    # 여덟 번째 맵 생성 (map8)
    npc_map8 = NPC(512, 384, "assets/images/npc_map8.png", scale=0.2)  # map8의 중앙에 위치한 NPC
    portal_to_map7 = Portal(50, 400, 50, 50, "map7")  # map8에서 map7로 이동
    portal_to_map9 = Portal(900, 400, 50, 50, "map9")  # map8에서 map9로 이동
    map8 = Map("assets/images/map8_background.png", [portal_to_map7, portal_to_map9], [npc_map8], description="7월 6일 여의도 더현대")
    map8.interaction_image = pygame.image.load("assets/images/memory_map8.png")  # map8의 이미지

    # 아홉 번째 맵 생성 (map9)
    npc_map9 = NPC(512, 384, "assets/images/npc_map9.png", scale=0.2)  # map9의 중앙에 위치한 NPC
    portal_to_map8 = Portal(50, 400, 50, 50, "map8")  # map9에서 map8로 이동
    portal_to_map10 = Portal(900, 400, 50, 50, "map10")  # map9에서 map10로 이동
    map9 = Map("assets/images/map9_background.png", [portal_to_map8, portal_to_map10], [npc_map9], description="7월 13일 해방촌")
    map9.interaction_image = pygame.image.load("assets/images/memory_map9.png")  # map9의 이미지

    # 열 번째 맵 생성 (map10)
    npc_map10 = NPC(512, 384, "assets/images/npc_map10.png", scale=0.2)  # map10의 중앙에 위치한 NPC
    portal_to_map9 = Portal(50, 400, 50, 50, "map9")  # map10에서 map9로 이동
    map10 = Map("assets/images/map10_background.png", [portal_to_map9], [npc_map10], description="7월 21일 용산미군기지")
    map10.interaction_image = pygame.image.load("assets/images/memory_map10.png")  # map10의 이미지

    # 추가된 맵 등록
    scene_manager.add_scene("map6", map6)
    scene_manager.add_scene("map7", map7)
    scene_manager.add_scene("map8", map8)
    scene_manager.add_scene("map9", map9)
    scene_manager.add_scene("map10", map10)

    # 맵 등록
    scene_manager.add_scene("map1", map1)
    scene_manager.add_scene("map2", map2)
    scene_manager.add_scene("map3", map3)
    scene_manager.add_scene("map4", map4)
    scene_manager.add_scene("map5", map5)
    scene_manager.set_scene("map1")  # map1에서 시작

    # 캐릭터 생성
    character = Character(100, 100, "assets/images/character.png", scale=0.2)  # 기존 캐릭터 이미지 사용

    # 캐릭터를 따라다니는 NPC 생성
    npc = NPC(200, 200, "assets/images/npc.png", scale=0.2)

    while True:
        keys = pygame.key.get_pressed()  # 키 입력 상태 확인
        events = pygame.event.get()  # 이벤트 가져오기
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # 현재 맵 업데이트
        scene_manager.update(character, keys, events)

        # NPC 업데이트 (캐릭터를 따라다니도록 설정)
        npc.update(character.rect)

        # 캐릭터 업데이트
        character.update(keys)

        # 화면 초기화
        screen.fill((0, 0, 0))  # 검은색으로 화면 초기화

        # 화면 그리기
        scene_manager.draw(screen)
        npc.draw(screen)  # NPC 그리기
        character.draw(screen)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        pygame.quit()
        raise e