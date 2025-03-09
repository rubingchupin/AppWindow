import pygame
import sys
from pygame.locals import *

class App2D:
    # 事件类型
    EVENT_QUIT = 0
    EVENT_KEY_DOWN = 1
    EVENT_KEY_UP = 2
    EVENT_MOUSE_MOTION = 3

    # 按键编码
    KEY_ESCAPE = 27
    KEY_SPACE = 32
    KEY_W = 119
    KEY_A = 97
    KEY_S = 115
    KEY_D = 100

    def __init__(self):
        self._screen = None
        self._clock = None
        self._running = False
        self._event_handlers = []
        
        # 窗口配置
        self.title = "AppWindow2D"
        self.size = (800, 600)
        self.bg_color = (32, 32, 32)
        self.fps = 60
        
        # 输入状态
        self.mouse_pos = (0, 0)
        self.keys_down = set()

    def setup(self):
        """初始化显示系统"""
        pygame.init()
        self._screen = pygame.display.set_mode(self.size, pygame.RESIZABLE)
        pygame.display.set_caption(self.title)
        self._clock = pygame.time.Clock()
        return self

    def run(self):
        """启动主循环"""
        self._running = True
        while self._running:
            self._process_events()
            self.update()
            self._draw_frame()
            self._clock.tick(self.fps)
        pygame.quit()

    def _process_events(self):
        """处理系统事件"""
        self.mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
                self.trigger_event(self.EVENT_QUIT)
                
            elif event.type == pygame.KEYDOWN:
                code = self._translate_key(event.key)
                self.keys_down.add(code)
                self.trigger_event(self.EVENT_KEY_DOWN, code)
                
            elif event.type == pygame.KEYUP:
                code = self._translate_key(event.key)
                self.keys_down.discard(code)
                self.trigger_event(self.EVENT_KEY_UP, code)
                
            elif event.type == pygame.MOUSEMOTION:
                self.trigger_event(self.EVENT_MOUSE_MOTION, self.mouse_pos)

    def _translate_key(self, key_code):
        """转换按键编码"""
        return key_code if key_code < 256 else 0

    def _draw_frame(self):
        """绘制单帧"""
        self._screen.fill(self.bg_color)
        self.draw(self._screen)
        pygame.display.flip()

    # 用户可重写方法
    def update(self):
        """每帧更新逻辑"""
        pass

    def draw(self, surface):
        """自定义绘制"""
        pass

    # 事件系统
    def trigger_event(self, event_type, data=None):
        """触发事件"""
        for handler in self._event_handlers:
            handler(event_type, data)

    def on_event(self, func):
        """事件监听装饰器"""
        self._event_handlers.append(func)
        return func

    # 绘图API
    def draw_circle(self, surface, color, position, radius):
        """绘制圆形"""
        pygame.draw.circle(surface, color, position, radius)

    def draw_rect(self, surface, color, rect, width=0):
        """绘制矩形"""
        pygame.draw.rect(surface, color, rect, width)

    def draw_text(self, text, position, size=24, color=(255,255,255)):
        """绘制文本"""
        font = pygame.font.SysFont(None, size)
        text_surface = font.render(text, True, color)
        self._screen.blit(text_surface, position)

# 全局实例
app = App2D()