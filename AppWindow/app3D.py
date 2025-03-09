from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties, loadPrcFileData

class App3D:
    def __init__(self):
        self._initialized = False
        self._config = {}
        self._window_props = WindowProperties()
        self._bg_color = (0.1, 0.1, 0.1, 1)

    def setup(self):
        """必须调用的初始化方法"""
        if self._initialized:
            raise RuntimeError("App already initialized")
        
        # 应用PRC配置
        for key, value in self._config.items():
            loadPrcFileData("", f"{key} {value}")
        
        # 初始化Panda3D引擎
        self.base = ShowBase()
        
        # 应用窗口属性和背景色
        self.base.win.requestProperties(self._window_props)
        self.base.setBackgroundColor(*self._bg_color)
        
        self._initialized = True
        return self  # 支持链式调用

    @property
    def title(self):
        """窗口标题（支持初始化前后修改）"""
        return self._window_props.getTitle()

    @title.setter
    def title(self, value):
        if self._initialized:
            props = WindowProperties()
            props.setTitle(value)
            self.base.win.requestProperties(props)
        else:
            self._config['window-title'] = value
        self._window_props.setTitle(value)

    @property
    def size(self):
        """窗口尺寸（支持初始化前后修改）"""
        return self._window_props.getSize()

    @size.setter
    def size(self, value):
        w, h = value
        if self._initialized:
            props = WindowProperties()
            props.setSize(w, h)
            self.base.win.requestProperties(props)
        else:
            self._config['win-size'] = f"{w} {h}"
        self._window_props.setSize(w, h)

    @property
    def background_color(self):
        """背景颜色（初始化后修改立即生效）"""
        return self._bg_color

    @background_color.setter
    def background_color(self, value):
        self._bg_color = value
        if self._initialized:
            self.base.setBackgroundColor(*value)

    def run(self):
        """启动应用程序主循环"""
        if not self._initialized:
            raise RuntimeError("Must call setup() before run()")
        self.base.run()