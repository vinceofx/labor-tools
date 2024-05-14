''' 函数方法库，适用于3ds Max 2020版本及以上版本 '''

# -*- coding: utf-8 -*-
import random
import MaxPlus # type: ignore
import pymxs # type: ignore

from pymxs import runtime as rt # type: ignore
from PySide2 import QtWidgets, QtCore # type: ignore

# 这定义了一个名为 MyFloatingPanel 的类，它继承自 QtWidgets.QWidget，意味着它是一个Qt窗口部件
class MyFloatingPanel(QtWidgets.QWidget): 
    def __init__(self, parent=None): # 这是类的初始化方法，它会在创建类的实例时被调用。parent=None 表示父级部件默认为空。
        super(MyFloatingPanel, self).__init__(parent)
        self.setWindowTitle("3DsMax Labor Tools")
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.Window)
        self.setFixedSize(800, 600)
        
        layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(layout)

        # 创建一个组框架
        group_box = QtWidgets.QGroupBox("Buttons Group", self)
        group_layout = QtWidgets.QVBoxLayout(group_box)
        group_box.setLayout(group_layout)

        # 创建按钮1
        button1 = QtWidgets.QPushButton("随机线框颜色", self)
        button1.setFixedSize(125, 25)
        button1.clicked.connect(self.on_button1_clicked)
        layout.addWidget(button1)

        # 创建按钮2
        button2 = QtWidgets.QPushButton("基于线框创建材质", self)
        button2.setFixedSize(125, 25)
        button2.clicked.connect(self.on_button2_clicked)
        layout.addWidget(button2)

        # 将组框架添加到主布局中
        layout.addWidget(group_box)

    """ 随机创建线框颜色 """
    def random_wirecolor(self):
        #获取当前选中对象
        selected_objects = MaxPlus.SelectionManager.Nodes

        # 循环遍历选中对象，并为每个对象设置随机线框颜色
        for obj in selected_objects:
            # 随机生成一个颜色
            random_color = MaxPlus.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            
            # 设置随机线框颜色
            obj.SetWireColor(random_color)

    """ 基于线框颜色创建标准材质球 """
    def wirecolor_material(self):
        selected_objects = rt.selection # 获取当前选中对象

        # 循环遍历选中对象，并为每个对象设置随机颜色和材质
        for obj in selected_objects: 
            random_color = rt.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) # 随机生成一个颜色
            obj.wirecolor = random_color # 设置随机颜色
            
            # 创建材质
            material = rt.standardMaterial()
            material_name = obj.name + "_Material"
            material.name = material_name
            material.diffuse = random_color
            material.ambient = random_color
        
        obj.material = material # 将材质应用于对象

    # 槽函数，点击对应按钮就可以触发不同功能
    def on_button1_clicked(self):
        self.random_wirecolor()
        self.repaint()

    def on_button2_clicked(self):
        self.wirecolor_material()

""" 这是一个主函数，用于创建并显示浮动面板 """
def main():
    main_window = MaxPlus.GetQMaxMainWindow()
    floating_panel = MyFloatingPanel(parent=main_window)
    floating_panel.show()

""" 这行代码检查脚本是否直接运行（而不是被导入到其他模块中）。如果是，则调用主函数 main() """
if __name__ == '__main__':
    main()