import pygame
import sys
import os

def resource_path(relative_path):
    """获取资源文件的绝对路径"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# 初始化 Pygame
pygame.init()

# 设置屏幕
screen = pygame.display.set_mode((1320, 720))  # 1321 726
pygame.display.set_caption("COMPLICT")

# 加载并播放背景音乐
pygame.mixer.init()
try:
    bgmusic_path = resource_path(os.path.join("sounds", "bgmusic.mp3"))
    pygame.mixer.music.load(bgmusic_path)
    pygame.mixer.music.play(-1, fade_ms=2000)  # -1 表示循环播放，fade_ms=2000 表示淡入时间为 2000 毫秒
except pygame.error as e:
    print(f"Error loading background music: {e}")
    sys.exit(1)

# 加载图像
try:
    icon = pygame.image.load(resource_path(os.path.join("images", "ic.png")))
    bkImg1 = pygame.image.load(resource_path(os.path.join("images", "first.png")))
    bkImg2 = pygame.image.load(resource_path(os.path.join("images", "sec.png")))
    bkImg3 = pygame.image.load(resource_path(os.path.join("images", "a.png")))
    bkImg4 = pygame.image.load(resource_path(os.path.join("images", "m.png")))
    bkImg5 = pygame.image.load(resource_path(os.path.join("images", "n.png")))
except pygame.error as e:
    print(f"Error loading images: {e}")
    sys.exit(1)

# 设置图标
pygame.display.set_icon(icon)

# 裁剪图像为相同大小
target_size = (1320, 720)
bkImg1 = pygame.transform.scale(bkImg1, target_size)
bkImg2 = pygame.transform.scale(bkImg2, target_size)
bkImg3 = pygame.transform.scale(bkImg3, target_size)
bkImg4 = pygame.transform.scale(bkImg4, target_size)
bkImg5 = pygame.transform.scale(bkImg5, target_size)

# 初始背景图像
backgrounds = [bkImg1, bkImg2, bkImg3, bkImg4, bkImg5]
current_bkImg_index = 0
current_bkImg = backgrounds[current_bkImg_index]
next_bkImg = None
alpha = 0

# 主循环
running = True
clock = pygame.time.Clock()

try:
    while running:
        # 处理事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 切换背景图片
                if next_bkImg is None:
                    current_bkImg_index = (current_bkImg_index + 1) % len(backgrounds)
                    next_bkImg = backgrounds[current_bkImg_index]
                    alpha = 0

        # 画背景
        if next_bkImg:
            temp_img = next_bkImg.copy()
            temp_img.set_alpha(alpha)
            screen.blit(current_bkImg, (0, 0))
            screen.blit(temp_img, (0, 0))
            alpha += 5
            if alpha >= 255:
                current_bkImg = next_bkImg
                next_bkImg = None
        else:
            screen.blit(current_bkImg, (0, 0))

        # 更新显示
        pygame.display.update()

        # 控制帧率
        clock.tick(60)
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    pygame.quit()
    sys.exit()