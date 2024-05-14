bl_info = {
    "name": "Blender Labor",
    "description": "一个集合多种便捷功能的工具箱",
    "author": "Vince",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "3D View > Right Pane > Blender Labor",
    "warning": "",  # used for warning icon and text in addons panel
    "wiki_url": "http://vinceofx.com/",
    "category": "3D View",
}

import bpy

from . import labor_blender
from . import panels

# 注册面板类和操作类
def register():
    labor_blender.register()
    panels.register()

# 取消注册面板类和操作类
def unregister():
    labor_blender.unregister()
    panels.unregister() 
    
# 主程序入口
if __name__ == "__main__":
    register()
