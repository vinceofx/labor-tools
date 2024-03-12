import bpy

# 在视窗创建插件面板按钮
class ObjectPanel(bpy.types.Panel):
    bl_idname = "CUSTOM_PT_simple_panel"
    bl_label = "便捷工具"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Blender Labor"

    def draw(self, context):
        layout = self.layout

         # 创建一个分组框
        box = layout.box()
        box.label(text="物体操作")

        # 在分组框中添加移动到集合按钮
        nested_collection_box = box.box()
        nested_collection_box.operator("object.nested_collection", text="移动到新集合")

        # 创建移动物体到原点按钮
        move_to_origin_box = box.box()
        move_to_origin_box.operator("object.move_to_origin",text="移动到原点")
        
        # 创建一个分组框
        box = layout.box()
        box.label(text="材质操作")

         # 在分组框中添加材质重命名按钮
        rename_material_box = box.box()
        rename_material_box.operator("object.rename_material", text="材质重命名")

        # 在分组框中添加替换材质按钮
        replace_material_box = box.box()
        replace_material_box.operator("object.replace_material", text="替换材质")

        # 再分组框中添加删除空材质插槽按钮
        clean_material_slots_box = box.box()
        clean_material_slots_box.operator("object.clean_material_slots",text="删除空插槽")

# 这里定义 panels 模块的 register() 函数
def register():
    bpy.utils.register_class(ObjectPanel)

# 这里定义 panels 模块的 unregister() 函数
def unregister():
    bpy.utils.unregister_class(ObjectPanel)
