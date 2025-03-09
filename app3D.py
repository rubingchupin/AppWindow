from AppWindow import app3D

# 初始化前配置
app3D.title = "自定义窗口标题"
app3D.size = (1024, 768)
app3D.background_color = (0.2, 0.3, 0.4, 1)  # RGBA颜色

# 执行初始化
app3D.setup()

# 初始化后配置（可选）
app3D.title = "运行时修改的标题"  # 实时更新

# 添加自定义初始化代码
app3D.base.disableMouse()  # 访问原始ShowBase实例
app3D.base.cam.setPos(0, -20, 5)

# 启动程序
app3D.run()