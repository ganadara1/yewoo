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

    # 맵 설명 리스트
    descriptions = [
        "6월 1일 망원한강공원",
        "6월 2일 올림픽공원 장미축제",
        "6월 6일 우리를 홀린 고양이 전시회",
        "6월 9일 조계사 방문",
        "6월 17일 선유도공원 산책",
        "6월 29일 낙산공원",
        "6월 30일 명동",
        "7월 6일 여의도 더현대",
        "7월 13일 해방촌",
        "7월 21일 용산미군기지",
        "7월 22일 신논현역",
        "8월 10일 종로 덕수궁 데이트"
    ]

    # 반복적으로 맵 생성 및 등록
    for i in range(1, len(descriptions) + 1):
        map_name = f"map{i}"
        background_path = f"assets/images/{map_name}_background.png"
        npc_image_path = f"assets/images/npc_{map_name}.png"
        interaction_image_path = f"assets/images/memory_{map_name}.png"

        # 포탈 설정
        portals = []
        if i > 1:  # 이전 맵으로 이동하는 포탈
            portals.append(Portal(50, 400, 50, 50, f"map{i - 1}"))
        if i < len(descriptions):  # 다음 맵으로 이동하는 포탈
            portals.append(Portal(900, 400, 50, 50, f"map{i + 1}"))

        # NPC 생성
        npcs = [NPC(512, 384, npc_image_path, scale=0.2)]

        # 맵 생성
        current_map = Map(background_path, portals, npcs, description=descriptions[i - 1])
        current_map.interaction_image = pygame.image.load(interaction_image_path)

        # 맵 등록
        scene_manager.add_scene(map_name, current_map)

    # 시작 맵 설정
    scene_manager.set_scene("map1")  # 첫 번째 맵에서 시작

    # 캐릭터 생성
    character = Character(100, 100, "assets/images/character.png", scale=0.2)

    # 캐릭터를 따라다니는 NPC 생성
    npc = NPC(200, 200, "assets/images/npc.png", scale=0.2)

    while True:
        keys = pygame.key.get_pressed()
        events = pygame.event.get()
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
        screen.fill((0, 0, 0))

        # 화면 그리기
        scene_manager.draw(screen)
        npc.draw(screen)
        character.draw(screen)

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        pygame.quit()
        raise e
