import bpy

# 【01】对象分类集合操作符
class NestedCollectionOperator(bpy.types.Operator):
    bl_idname = "object.nested_collection"
    bl_label = "Move objects to a new collection"

    def execute(self, context):
        objects = bpy.context.selected_objects

        for obj in objects:
            collection = bpy.data.collections.new(obj.name)
            bpy.context.scene.collection.children.link(collection)

            obj_collection = obj.users_collection[0]
            obj_collection.objects.unlink(obj)
            collection.objects.link(obj)

        return {"FINISHED"}
    
# 【02】移动物体到原点    
class MoveToOriginOperator(bpy.types.Operator):
    bl_idname = "object.move_to_origin"
    bl_label = "Home Origin"

    def execute(self,context):
        # 获取选择的物体
        selected_objects = bpy.context.selected_objects

        # 遍历选中的物体并把它移动到原点
        for obj in selected_objects:
            obj.location = (0,0,0)
        
        return {"FINISHED"}

# 【03】重命名材质插槽操作符
class RenameMaterialOperator(bpy.types.Operator):
    bl_idname = "object.rename_material"
    bl_label = "Rename Material"

    def execute(self, context):
        # 获取当前选中的物体
        selected_objects = bpy.context.selected_objects

        for obj in selected_objects:
            # 获取物体上的所有材质槽
            material_slots = obj.material_slots

            # 对每个材质槽进行重命名
            for idx, slot in enumerate(material_slots):
                slot.material.name = f"{obj.name}_{idx}"

        return {"FINISHED"}

# 【04】替换材质插槽操作符
class ReplaceMaterialOperator(bpy.types.Operator):
    bl_idname = "object.replace_material"
    bl_label = "Replace Material"

    def execute(self, context):
        # 获取当前选中的物体
        selected_objects = bpy.context.selected_objects

        for obj in selected_objects:
            # 清除物体上的所有材质槽
            for material_slot in obj.material_slots:
                bpy.ops.object.material_slot_remove({'object': obj})

            # 在物体上添加一个新的材质槽
            bpy.ops.object.material_slot_add({'object': obj})

        return {"FINISHED"}
    
# 【05】清除空材质插槽操作符
class CleanMaterialSlotsOperator(bpy.types.Operator):
    bl_idname = "object.clean_material_slots"
    bl_label = "Clean Material Slots"

    def execute(self, context):
        # 获取当前选中的所有网格对象
        selected_objects = [obj for obj in context.selected_objects if obj.type == 'MESH']

        for obj in selected_objects:
            context.view_layer.objects.active = obj  # 激活当前对象
            # 反向迭代材质插槽，以便在移除时不会打乱索引
            for i in range(len(obj.material_slots) - 1, -1, -1):
                if not obj.material_slots[i].material:
                    obj.active_material_index = i
                    bpy.ops.object.material_slot_remove()

        return {"FINISHED"}
    
"""
import bpy
from mathutils import Vector

# 获取在场景中选中的物体
selected_objects = bpy.context.selected_objects

# 如果至少有一个物体被选中
if selected_objects and len(selected_objects) > 0:
    # 计算选中物体的坐标平均值
    avg_location = Vector()
    for obj in selected_objects:
        avg_location += obj.location
    avg_location /= len(selected_objects)

    # 在坐标平均值处创建一个空物体（Empty）
    bpy.ops.object.empty_add(location=avg_location)
    # 获取刚创建的空物体
    empty_obj = bpy.context.object
    # 使用首个所选物体的名字来命名新的空物体
    empty_obj.name = selected_objects[0].name + "_Group"

    # 遍历原来选中的物体，将它们设为新空物体的子物体
    for obj in selected_objects:
        # 在建立父子关系之前，保存当前物体的世界位置
        global_location = obj.matrix_world.translation.copy()

        # 设置父物体，这样设置后，子物体会与父物体相对位置保持一致
        obj.parent = empty_obj

        # 设置子物体的矩阵，以确保其在世界空间中的位置不改变
        obj.matrix_world.translation = global_location
"""

# 这是操作符模块的 register 和 unregister 函数
def register():
    bpy.utils.register_class(CleanMaterialSlotsOperator)
    bpy.utils.register_class(NestedCollectionOperator)
    bpy.utils.register_class(ReplaceMaterialOperator)
    bpy.utils.register_class(RenameMaterialOperator)
    bpy.utils.register_class(MoveToOriginOperator)

def unregister():
    bpy.utils.unregister_class(CleanMaterialSlotsOperator)
    bpy.utils.unregister_class(NestedCollectionOperator)
    bpy.utils.unregister_class(ReplaceMaterialOperator)
    bpy.utils.unregister_class(RenameMaterialOperator)
    bpy.utils.unregister_class(MoveToOriginOperator)