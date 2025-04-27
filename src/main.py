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
    portal_to_map11 = Portal(900, 400, 50, 50, "map11")  # map10에서 map11로 이동 추가
    map10 = Map("assets/images/map10_background.png", [portal_to_map9, portal_to_map11], [npc_map10], description="7월 21일 용산미군기지")
    map10.interaction_image = pygame.image.load("assets/images/memory_map10.png")  # map10의 이미지

    # 열한 번째 맵 생성 (map11)
    npc_map11 = NPC(512, 384, "assets/images/npc_map11.png", scale=0.2)
    portal_to_map10 = Portal(50, 400, 50, 50, "map10")
    portal_to_map12 = Portal(900, 400, 50, 50, "map12")
    map11 = Map("assets/images/map11_background.png", [portal_to_map10, portal_to_map12], [npc_map11], description="7월 22일 신논현역")
    map11.interaction_image = pygame.image.load("assets/images/memory_map11.png")

    # 열두 번째 맵 생성 (map12)
    npc_map12 = NPC(512, 384, "assets/images/npc_map12.png", scale=0.2)
    portal_to_map11 = Portal(50, 400, 50, 50, "map11")
    portal_to_map13 = Portal(900, 400, 50, 50, "map13")
    map12 = Map("assets/images/map12_background.png", [portal_to_map11, portal_to_map13], [npc_map12], description="8월 10일 종로 덕수궁")
    map12.interaction_image = pygame.image.load("assets/images/memory_map12.png")

    # 열세 번째 맵 생성 (map13)
    npc_map13 = NPC(512, 384, "assets/images/npc_map13.png", scale=0.2)
    portal_to_map12 = Portal(50, 400, 50, 50, "map12")
    portal_to_map14 = Portal(900, 400, 50, 50, "map14")
    map13 = Map("assets/images/map13_background.png", [portal_to_map12, portal_to_map14], [npc_map13], description="8월 15일 여의도 더현대, 여의도 한강공원")
    map13.interaction_image = pygame.image.load("assets/images/memory_map13.png")

    # 열네 번째 맵 생성 (map14)
    npc_map14 = NPC(512, 384, "assets/images/npc_map14.png", scale=0.2)
    portal_to_map13 = Portal(50, 400, 50, 50, "map13")
    portal_to_map15 = Portal(900, 400, 50, 50, "map15")
    map14 = Map("assets/images/map14_background.png", [portal_to_map13, portal_to_map15], [npc_map14], description="8월 18일 속초여행")
    map14.interaction_image = pygame.image.load("assets/images/memory_map14.png")

    # 열다섯 번째 맵 생성 (map15)
    npc_map15 = NPC(512, 384, "assets/images/npc_map15.png", scale=0.2)
    portal_to_map14 = Portal(50, 400, 50, 50, "map14")
    portal_to_map16 = Portal(900, 400, 50, 50, "map16")
    map15 = Map("assets/images/map15_background.png", [portal_to_map14, portal_to_map16], [npc_map15], description="8월 18일 속초여행2")
    map15.interaction_image = pygame.image.load("assets/images/memory_map15.png")

    # 열여섯 번째 맵 생성 (map16)
    npc_map16 = NPC(512, 384, "assets/images/npc_map16.png", scale=0.2)
    portal_to_map15 = Portal(50, 400, 50, 50, "map15")
    portal_to_map17 = Portal(900, 400, 50, 50, "map17")
    map16 = Map("assets/images/map16_background.png", [portal_to_map15, portal_to_map17], [npc_map16], description="8월 18일 속초여행3")
    map16.interaction_image = pygame.image.load("assets/images/memory_map16.png")

    # 열일곱 번째 맵 생성 (map17)
    npc_map17 = NPC(512, 384, "assets/images/npc_map17.png", scale=0.2)
    portal_to_map16 = Portal(50, 400, 50, 50, "map16")
    portal_to_map18 = Portal(900, 400, 50, 50, "map18")
    map17 = Map("assets/images/map17_background.png", [portal_to_map16, portal_to_map18], [npc_map17], description="8월 20일 신논현역")
    map17.interaction_image = pygame.image.load("assets/images/memory_map17.png")

    # 열여덟 번째 맵 생성 (map18)
    npc_map18 = NPC(512, 384, "assets/images/npc_map18.png", scale=0.2)
    portal_to_map17 = Portal(50, 400, 50, 50, "map17")
    portal_to_map19 = Portal(900, 400, 50, 50, "map19")
    map18 = Map("assets/images/map18_background.png", [portal_to_map17, portal_to_map19], [npc_map18], description="8월 25일 망원")
    map18.interaction_image = pygame.image.load("assets/images/memory_map18.png")

    # 열아홉 번째 맵 생성 (map19)
    npc_map19 = NPC(512, 384, "assets/images/npc_map19.png", scale=0.2)
    portal_to_map18 = Portal(50, 400, 50, 50, "map18")
    portal_to_map20 = Portal(900, 400, 50, 50, "map20")
    map19 = Map("assets/images/map19_background.png", [portal_to_map18, portal_to_map20], [npc_map19], description="8월 31일 국제전자센터")
    map19.interaction_image = pygame.image.load("assets/images/memory_map19.png")

    # 스무 번째 맵 생성 (map20)
    npc_map20 = NPC(512, 384, "assets/images/npc_map20.png", scale=0.2)
    portal_to_map19 = Portal(50, 400, 50, 50, "map19")
    portal_to_map21 = Portal(900, 400, 50, 50, "map21")
    map20 = Map("assets/images/map20_background.png", [portal_to_map19, portal_to_map21], [npc_map20], description="9월 11일 이대 놀숲")
    map20.interaction_image = pygame.image.load("assets/images/memory_map20.png")

    # 스물한 번째 맵 생성 (map21)
    npc_map21 = NPC(512, 384, "assets/images/npc_map21.png", scale=0.2)
    portal_to_map20 = Portal(50, 400, 50, 50, "map20")
    portal_to_map22 = Portal(900, 400, 50, 50, "map22")
    map21 = Map("assets/images/map21_background.png", [portal_to_map20, portal_to_map22], [npc_map21], description="9월 14일 나가노마켓")
    map21.interaction_image = pygame.image.load("assets/images/memory_map21.png")

    # 스물두 번째 맵 생성 (map22)
    npc_map22 = NPC(512, 384, "assets/images/npc_map22.png", scale=0.2)
    portal_to_map21 = Portal(50, 400, 50, 50, "map21")
    portal_to_map23 = Portal(900, 400, 50, 50, "map23")
    map22 = Map("assets/images/map22_background.png", [portal_to_map21, portal_to_map23], [npc_map22], description="9월 28일 채그로")
    map22.interaction_image = pygame.image.load("assets/images/memory_map22.png")

    # 스물세 번째 맵 생성 (map23)
    npc_map23 = NPC(512, 384, "assets/images/npc_map23.png", scale=0.2)
    portal_to_map22 = Portal(50, 400, 50, 50, "map22")
    portal_to_map24 = Portal(900, 400, 50, 50, "map24")
    map23 = Map("assets/images/map23_background.png", [portal_to_map22, portal_to_map24], [npc_map23], description="10월 5일 채그로2")
    map23.interaction_image = pygame.image.load("assets/images/memory_map23.png")

    # 스물네 번째 맵 생성 (map24)
    npc_map24 = NPC(512, 384, "assets/images/npc_map24.png", scale=0.2)
    portal_to_map23 = Portal(50, 400, 50, 50, "map23")  # map24에서 map23로 이동
    portal_to_map25 = Portal(900, 400, 50, 50, "map25")  # map24에서 map25로 이동 추가
    map24 = Map("assets/images/map24_background.png", [portal_to_map23, portal_to_map25], [npc_map24], description="10월 9일 몽마르뜨 공원")
    map24.interaction_image = pygame.image.load("assets/images/memory_map24.png")

    # 스물다섯 번째 맵 생성 (map25)
    npc_map25 = NPC(512, 384, "assets/images/npc_map25.png", scale=0.2)
    portal_to_map24 = Portal(50, 400, 50, 50, "map24")  # map25에서 map24로 이동
    portal_to_map26 = Portal(900, 400, 50, 50, "map26")  # map25에서 map26로 이동
    map25 = Map("assets/images/map25_background.png", [portal_to_map24, portal_to_map26], [npc_map25], description="10월 15일 서울숲")
    map25.interaction_image = pygame.image.load("assets/images/memory_map25.png")

    # 스물여섯 번째 맵 생성 (map26)
    npc_map26 = NPC(512, 384, "assets/images/npc_map26.png", scale=0.2)
    portal_to_map25 = Portal(50, 400, 50, 50, "map25")  # map26에서 map25로 이동
    portal_to_map27 = Portal(900, 400, 50, 50, "map27")  # map26에서 map27로 이동
    map26 = Map("assets/images/map26_background.png", [portal_to_map25, portal_to_map27], [npc_map26], description="10월 20일 남산타워")
    map26.interaction_image = pygame.image.load("assets/images/memory_map26.png")

    # 스물일곱 번째 맵 생성 (map27)
    npc_map27 = NPC(512, 384, "assets/images/npc_map27.png", scale=0.2)
    portal_to_map26 = Portal(50, 400, 50, 50, "map26")  # map27에서 map26로 이동
    portal_to_map28 = Portal(900, 400, 50, 50, "map28")  # map27에서 map28로 이동
    map27 = Map("assets/images/map27_background.png", [portal_to_map26, portal_to_map28], [npc_map27], description="10월 25일 한강공원")
    map27.interaction_image = pygame.image.load("assets/images/memory_map27.png")

    # 스물여덟 번째 맵 생성 (map28)
    npc_map28 = NPC(512, 384, "assets/images/npc_map28.png", scale=0.2)
    portal_to_map27 = Portal(50, 400, 50, 50, "map27")  # map28에서 map27로 이동
    portal_to_map29 = Portal(900, 400, 50, 50, "map29")  # map28에서 map29로 이동
    map28 = Map("assets/images/map28_background.png", [portal_to_map27, portal_to_map29], [npc_map28], description="10월 30일 홍대거리")
    map28.interaction_image = pygame.image.load("assets/images/memory_map28.png")

    # 스물아홉 번째 맵 생성 (map29)
    npc_map29 = NPC(512, 384, "assets/images/npc_map29.png", scale=0.2)
    portal_to_map28 = Portal(50, 400, 50, 50, "map28")  # map29에서 map28로 이동
    portal_to_map30 = Portal(900, 400, 50, 50, "map30")  # map29에서 map30로 이동
    map29 = Map("assets/images/map29_background.png", [portal_to_map28, portal_to_map30], [npc_map29], description="11월 5일 대학로")
    map29.interaction_image = pygame.image.load("assets/images/memory_map29.png")

    # 서른 번째 맵 생성 (map30)
    npc_map30 = NPC(512, 384, "assets/images/npc_map30.png", scale=0.2)
    portal_to_map29 = Portal(50, 400, 50, 50, "map29")  # map30에서 map29로 이동
    portal_to_map31 = Portal(900, 400, 50, 50, "map31")  # map30에서 map31로 이동
    map30 = Map("assets/images/map30_background.png", [portal_to_map29, portal_to_map31], [npc_map30], description="11월 10일 서촌")
    map30.interaction_image = pygame.image.load("assets/images/memory_map30.png")

    # 서른한 번째 맵 생성 (map31)
    npc_map31 = NPC(512, 384, "assets/images/npc_map31.png", scale=0.2)
    portal_to_map30 = Portal(50, 400, 50, 50, "map30")  # map31에서 map30로 이동
    portal_to_map32 = Portal(900, 400, 50, 50, "map32")  # map31에서 map32로 이동
    map31 = Map("assets/images/map31_background.png", [portal_to_map30, portal_to_map32], [npc_map31], description="11월 15일 이태원")
    map31.interaction_image = pygame.image.load("assets/images/memory_map31.png")

    # 서른두 번째 맵 생성 (map32)
    npc_map32 = NPC(512, 384, "assets/images/npc_map32.png", scale=0.2)
    portal_to_map31 = Portal(50, 400, 50, 50, "map31")  # map32에서 map31로 이동
    portal_to_map33 = Portal(900, 400, 50, 50, "map33")  # map32에서 map33로 이동
    map32 = Map("assets/images/map32_background.png", [portal_to_map31, portal_to_map33], [npc_map32], description="11월 20일 명동")
    map32.interaction_image = pygame.image.load("assets/images/memory_map32.png")

    # 서른세 번째 맵 생성 (map33)
    npc_map33 = NPC(512, 384, "assets/images/npc_map33.png", scale=0.2)
    portal_to_map32 = Portal(50, 400, 50, 50, "map32")  # map33에서 map32로 이동
    portal_to_map34 = Portal(900, 400, 50, 50, "map34")  # map33에서 map34로 이동
    map33 = Map("assets/images/map33_background.png", [portal_to_map32, portal_to_map34], [npc_map33], description="11월 25일 낙산공원")
    map33.interaction_image = pygame.image.load("assets/images/memory_map33.png")

    # 서른네 번째 맵 생성 (map34)
    npc_map34 = NPC(512, 384, "assets/images/npc_map34.png", scale=0.2)
    portal_to_map33 = Portal(50, 400, 50, 50, "map33")  # map34에서 map33로 이동
    map34 = Map("assets/images/map34_background.png", [portal_to_map33], [npc_map34], description="11월 30일 한강 야경")
    map34.interaction_image = pygame.image.load("assets/images/memory_map34.png")

    # 모든 맵 등록
    scene_manager.add_scene("map1", map1)  # map1 등록 추가
    scene_manager.add_scene("map2", map2)
    scene_manager.add_scene("map3", map3)
    scene_manager.add_scene("map4", map4)
    scene_manager.add_scene("map5", map5)
    scene_manager.add_scene("map6", map6)
    scene_manager.add_scene("map7", map7)
    scene_manager.add_scene("map8", map8)
    scene_manager.add_scene("map9", map9)
    scene_manager.add_scene("map10", map10)
    scene_manager.add_scene("map11", map11)
    scene_manager.add_scene("map12", map12)
    scene_manager.add_scene("map13", map13)
    scene_manager.add_scene("map14", map14)
    scene_manager.add_scene("map15", map15)
    scene_manager.add_scene("map16", map16)
    scene_manager.add_scene("map17", map17)
    scene_manager.add_scene("map18", map18)
    scene_manager.add_scene("map19", map19)
    scene_manager.add_scene("map20", map20)
    scene_manager.add_scene("map21", map21)
    scene_manager.add_scene("map22", map22)
    scene_manager.add_scene("map23", map23)
    scene_manager.add_scene("map24", map24)
    scene_manager.add_scene("map25", map25)
    scene_manager.add_scene("map26", map26)
    scene_manager.add_scene("map27", map27)
    scene_manager.add_scene("map28", map28)
    scene_manager.add_scene("map29", map29)
    scene_manager.add_scene("map30", map30)
    scene_manager.add_scene("map31", map31)
    scene_manager.add_scene("map32", map32)
    scene_manager.add_scene("map33", map33)
    scene_manager.add_scene("map34", map34)

    # 시작 맵 설정
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