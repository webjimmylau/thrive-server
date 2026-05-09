from pydantic import BaseModel, ConstrainedList, Field
from typing import Optional, Any


class CateQuery(BaseModel):
    page: Optional[int] = Field(default=1, description="第几页", ge=1)
    size: Optional[int] = Field(default=5, description="每页显示几个")


class CateBody(BaseModel):
    id: Optional[int]
    name: str = Field(default="大前端", description="分类名称")
    icon: str = Field(default="🎉", description="分类图标")
    url: str = Field(default="http://127.0.0.1:9003", description="分类跳转链接")
    mark: str = Field(default="dqd", description="分类标识，通常为名称的英文首字母缩写")
    level: int = Field(default=0, description="分类级别 一级：0 | 二级：一级分类的ID")
    # children: ConstrainedList[Any] = Field(default=[], description="该分类下的所有子分类")


class CateBodyId(BaseModel):
    ids: ConstrainedList[int] = Field(default=[1, 2, 3], description="ID列表")
