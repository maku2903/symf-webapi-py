from __future__ import annotations

from typing import Any, List
from datetime import datetime
from pydantic import TypeAdapter
from SymfWebAPI.operations import build_none_operation, build_raw_operation, build_typed_operation
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import Catalog
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import IncrementalSyncListElement
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import Kind
from SymfWebAPI.WebAPI.Interface.Common.ViewModels import Marker
from SymfWebAPI.WebAPI.Interface.ViewModels import Page
from SymfWebAPI.WebAPI.Interface.Products.ViewModels import Product
from SymfWebAPI.WebAPI.Interface.Products.ViewModels import ProductBarcodes
from SymfWebAPI.WebAPI.Interface.Products.ViewModels import ProductCriteriaFilter
from SymfWebAPI.WebAPI.Interface.Products.ViewModels import ProductFilterCriteria
from SymfWebAPI.WebAPI.Interface.Products.ViewModels import ProductListElement
from SymfWebAPI.WebAPI.Interface.Products.ViewModels import ProductListElementWithDimensions
from SymfWebAPI.WebAPI.Interface.Products.ViewModels import ProductListElementWithSalePrices
from SymfWebAPI.WebAPI.Interface.Products.ViewModels import ProductLogisticField
from SymfWebAPI.WebAPI.Interface.Enums import enumOrderByType

_ADAPTER_Get = TypeAdapter(Product)
OP_Get = build_typed_operation(method='GET', path='/api/Products', adapter=_ADAPTER_Get)
OP_Get_RAW = build_raw_operation(method='GET', path='/api/Products')

_ADAPTER_GetByCode = TypeAdapter(Product)
OP_GetByCode = build_typed_operation(method='GET', path='/api/Products', adapter=_ADAPTER_GetByCode)
OP_GetByCode_RAW = build_raw_operation(method='GET', path='/api/Products')

_ADAPTER_GetGet = TypeAdapter(List[ProductListElement])
OP_GetGet = build_typed_operation(method='GET', path='/api/Products', adapter=_ADAPTER_GetGet)
OP_GetGet_RAW = build_raw_operation(method='GET', path='/api/Products')

_ADAPTER_GetBySalePrices = TypeAdapter(List[ProductListElement])
OP_GetBySalePrices = build_typed_operation(method='GET', path='/api/Products', adapter=_ADAPTER_GetBySalePrices)
OP_GetBySalePrices_RAW = build_raw_operation(method='GET', path='/api/Products')

_ADAPTER_GetWithSalePrices = TypeAdapter(List[ProductListElementWithSalePrices])
OP_GetWithSalePrices = build_typed_operation(method='GET', path='/api/Products/WithSalePrices', adapter=_ADAPTER_GetWithSalePrices)
OP_GetWithSalePrices_RAW = build_raw_operation(method='GET', path='/api/Products/WithSalePrices')

_ADAPTER_GetWithDimensions = TypeAdapter(List[ProductListElementWithDimensions])
OP_GetWithDimensions = build_typed_operation(method='GET', path='/api/Products/WithDimensions', adapter=_ADAPTER_GetWithDimensions)
OP_GetWithDimensions_RAW = build_raw_operation(method='GET', path='/api/Products/WithDimensions')

_ADAPTER_Filter = TypeAdapter(List[ProductListElement])
OP_Filter = build_typed_operation(method='PATCH', path='/api/Products/Filter', adapter=_ADAPTER_Filter)
OP_Filter_RAW = build_raw_operation(method='PATCH', path='/api/Products/Filter')

_ADAPTER_FilterWithSalePrices = TypeAdapter(List[ProductListElementWithSalePrices])
OP_FilterWithSalePrices = build_typed_operation(method='PATCH', path='/api/Products/Filter/WithSalePrices', adapter=_ADAPTER_FilterWithSalePrices)
OP_FilterWithSalePrices_RAW = build_raw_operation(method='PATCH', path='/api/Products/Filter/WithSalePrices')

_ADAPTER_FilterWithDimensions = TypeAdapter(List[ProductListElementWithDimensions])
OP_FilterWithDimensions = build_typed_operation(method='PATCH', path='/api/Products/Filter/WithDimensions', adapter=_ADAPTER_FilterWithDimensions)
OP_FilterWithDimensions_RAW = build_raw_operation(method='PATCH', path='/api/Products/Filter/WithDimensions')

_ADAPTER_AddNew = TypeAdapter(Product)
OP_AddNew = build_typed_operation(method='POST', path='/api/Products/Create', adapter=_ADAPTER_AddNew)
OP_AddNew_RAW = build_raw_operation(method='POST', path='/api/Products/Create')

OP_Update = build_none_operation(method='PUT', path='/api/Products/Update')
OP_Update_RAW = build_raw_operation(method='PUT', path='/api/Products/Update')

_ADAPTER_GetMarkers = TypeAdapter(List[Marker])
OP_GetMarkers = build_typed_operation(method='GET', path='/api/Products/Markers', adapter=_ADAPTER_GetMarkers)
OP_GetMarkers_RAW = build_raw_operation(method='GET', path='/api/Products/Markers')

_ADAPTER_GetKinds = TypeAdapter(List[Kind])
OP_GetKinds = build_typed_operation(method='GET', path='/api/Products/Kinds', adapter=_ADAPTER_GetKinds)
OP_GetKinds_RAW = build_raw_operation(method='GET', path='/api/Products/Kinds')

_ADAPTER_GetCatalogs = TypeAdapter(List[Catalog])
OP_GetCatalogs = build_typed_operation(method='GET', path='/api/Products/Catalogs', adapter=_ADAPTER_GetCatalogs)
OP_GetCatalogs_RAW = build_raw_operation(method='GET', path='/api/Products/Catalogs')

_ADAPTER_IncrementalSync = TypeAdapter(List[IncrementalSyncListElement])
OP_IncrementalSync = build_typed_operation(method='GET', path='/api/Products/IncrementalSync', adapter=_ADAPTER_IncrementalSync)
OP_IncrementalSync_RAW = build_raw_operation(method='GET', path='/api/Products/IncrementalSync')

_ADAPTER_GetBarcodes = TypeAdapter(ProductBarcodes)
OP_GetBarcodes = build_typed_operation(method='GET', path='/api/Products/Barcodes', adapter=_ADAPTER_GetBarcodes)
OP_GetBarcodes_RAW = build_raw_operation(method='GET', path='/api/Products/Barcodes')

_ADAPTER_GetBarcodesByProductCode = TypeAdapter(ProductBarcodes)
OP_GetBarcodesByProductCode = build_typed_operation(method='GET', path='/api/Products/Barcodes', adapter=_ADAPTER_GetBarcodesByProductCode)
OP_GetBarcodesByProductCode_RAW = build_raw_operation(method='GET', path='/api/Products/Barcodes')

OP_UpdateBarcodes = build_none_operation(method='GET', path='/api/Products/UpdateBarcodes')
OP_UpdateBarcodes_RAW = build_raw_operation(method='GET', path='/api/Products/UpdateBarcodes')

OP_UpdateBarcodesByProductCode = build_none_operation(method='GET', path='/api/Products/UpdateBarcodes')
OP_UpdateBarcodesByProductCode_RAW = build_raw_operation(method='GET', path='/api/Products/UpdateBarcodes')

_ADAPTER_FilterSql = TypeAdapter(List[ProductListElement])
OP_FilterSql = build_typed_operation(method='PATCH', path='/api/Products/FilterSql', adapter=_ADAPTER_FilterSql)
OP_FilterSql_RAW = build_raw_operation(method='PATCH', path='/api/Products/FilterSql')

_ADAPTER_GetPagedDocument = TypeAdapter(Page)
OP_GetPagedDocument = build_typed_operation(method='GET', path='/api/Products/Page', adapter=_ADAPTER_GetPagedDocument)
OP_GetPagedDocument_RAW = build_raw_operation(method='GET', path='/api/Products/Page')

_ADAPTER_GetPageWithSalePrices = TypeAdapter(Page)
OP_GetPageWithSalePrices = build_typed_operation(method='GET', path='/api/Products/Page/WithSalePrices', adapter=_ADAPTER_GetPageWithSalePrices)
OP_GetPageWithSalePrices_RAW = build_raw_operation(method='GET', path='/api/Products/Page/WithSalePrices')

_ADAPTER_GetPageWithDimensions = TypeAdapter(Page)
OP_GetPageWithDimensions = build_typed_operation(method='GET', path='/api/Products/Page/WithDimensions', adapter=_ADAPTER_GetPageWithDimensions)
OP_GetPageWithDimensions_RAW = build_raw_operation(method='GET', path='/api/Products/Page/WithDimensions')

_ADAPTER_FilterSqlWthSalePrices = TypeAdapter(List[ProductListElementWithSalePrices])
OP_FilterSqlWthSalePrices = build_typed_operation(method='PATCH', path='/api/Products/FilterSql/WithSalePrices', adapter=_ADAPTER_FilterSqlWthSalePrices)
OP_FilterSqlWthSalePrices_RAW = build_raw_operation(method='PATCH', path='/api/Products/FilterSql/WithSalePrices')

_ADAPTER_FilterSqlWthDimensions = TypeAdapter(List[ProductListElementWithDimensions])
OP_FilterSqlWthDimensions = build_typed_operation(method='PATCH', path='/api/Products/FilterSql/WithDimensions', adapter=_ADAPTER_FilterSqlWthDimensions)
OP_FilterSqlWthDimensions_RAW = build_raw_operation(method='PATCH', path='/api/Products/FilterSql/WithDimensions')

_ADAPTER_GetLogisticFields = TypeAdapter(List[ProductLogisticField])
OP_GetLogisticFields = build_typed_operation(method='GET', path='/api/Products/LogisticFields', adapter=_ADAPTER_GetLogisticFields)
OP_GetLogisticFields_RAW = build_raw_operation(method='GET', path='/api/Products/LogisticFields')

_ADAPTER_GetLogisticFieldsByProductCode = TypeAdapter(List[ProductLogisticField])
OP_GetLogisticFieldsByProductCode = build_typed_operation(method='GET', path='/api/Products/LogisticFields', adapter=_ADAPTER_GetLogisticFieldsByProductCode)
OP_GetLogisticFieldsByProductCode_RAW = build_raw_operation(method='GET', path='/api/Products/LogisticFields')
