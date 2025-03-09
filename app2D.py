from AppWindow import app2D

# 配置窗口参数
app2D.title = "简洁示例"
app2D.size = (1024, 768)
app2D.bg_color = (100, 150, 200)

# 定义绘制逻辑
def custom_draw(surface):
    # 使用框架的绘图方法
    app2D.draw_circle(surface, (255,0,0), (500, 300), 50)
    app2D.draw_rect(surface, (0,255,0), (100, 100, 200, 150), 3)

# 挂载绘制方法
app2D.draw = custom_draw

if __name__ == "__main__":
    app2D.setup().run()