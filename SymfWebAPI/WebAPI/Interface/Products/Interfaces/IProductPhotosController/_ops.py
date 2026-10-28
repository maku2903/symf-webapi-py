from __future__ import annotations

from typing import Any, List
from pydantic import TypeAdapter
from SymfWebAPI.operations import build_none_operation, build_raw_operation, build_typed_operation
from SymfWebAPI.WebAPI.Interface.Products.ViewModels import ProductPhoto
from SymfWebAPI.WebAPI.Interface.Products.ViewModels import ProductPhotoListElement
from SymfWebAPI.WebAPI.Interface.Enums import enumPhotoQuality

_ADAPTER_Get = TypeAdapter(List[ProductPhotoListElement])
OP_Get = build_typed_operation(method='GET', path='/api/ProductPhotos', adapter=_ADAPTER_Get)
OP_Get_RAW = build_raw_operation(method='GET', path='/api/ProductPhotos')

_ADAPTER_GetByProductCode = TypeAdapter(List[ProductPhotoListElement])
OP_GetByProductCode = build_typed_operation(method='GET', path='/api/ProductPhotos', adapter=_ADAPTER_GetByProductCode)
OP_GetByProductCode_RAW = build_raw_operation(method='GET', path='/api/ProductPhotos')

_ADAPTER_GetByPhotoIdQuality = TypeAdapter(ProductPhoto)
OP_GetByPhotoIdQuality = build_typed_operation(method='GET', path='/api/ProductPhotos', adapter=_ADAPTER_GetByPhotoIdQuality)
OP_GetByPhotoIdQuality_RAW = build_raw_operation(method='GET', path='/api/ProductPhotos')
