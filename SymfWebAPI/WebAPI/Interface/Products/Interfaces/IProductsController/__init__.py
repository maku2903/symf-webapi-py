from __future__ import annotations

from typing import Any, List, overload
from datetime import datetime
from SymfWebAPI.operations import invoke_operation
from SymfWebAPI.protocols import (SyncInvokerProtocol, SyncRequestProtocol)
from SymfWebAPI.response import ResponseEnvelope
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
from ._common import (
    _prepare_Get,
    _prepare_GetByCode,
    _prepare_GetGet,
    _prepare_GetBySalePrices,
    _prepare_GetWithSalePrices,
    _prepare_GetWithDimensions,
    _prepare_Filter,
    _prepare_FilterWithSalePrices,
    _prepare_FilterWithDimensions,
    _prepare_AddNew,
    _prepare_Update,
    _prepare_GetMarkers,
    _prepare_GetKinds,
    _prepare_GetCatalogs,
    _prepare_IncrementalSync,
    _prepare_GetBarcodes,
    _prepare_GetBarcodesByProductCode,
    _prepare_UpdateBarcodes,
    _prepare_UpdateBarcodesByProductCode,
    _prepare_FilterSql,
    _prepare_GetPagedDocument,
    _prepare_GetPageWithSalePrices,
    _prepare_GetPageWithDimensions,
    _prepare_FilterSqlWthSalePrices,
    _prepare_FilterSqlWthDimensions,
    _prepare_GetLogisticFields,
    _prepare_GetLogisticFieldsByProductCode,
)
from ._ops import (
    OP_Get,
    OP_Get_RAW,
    OP_GetByCode,
    OP_GetByCode_RAW,
    OP_GetGet,
    OP_GetGet_RAW,
    OP_GetBySalePrices,
    OP_GetBySalePrices_RAW,
    OP_GetWithSalePrices,
    OP_GetWithSalePrices_RAW,
    OP_GetWithDimensions,
    OP_GetWithDimensions_RAW,
    OP_Filter,
    OP_Filter_RAW,
    OP_FilterWithSalePrices,
    OP_FilterWithSalePrices_RAW,
    OP_FilterWithDimensions,
    OP_FilterWithDimensions_RAW,
    OP_AddNew,
    OP_AddNew_RAW,
    OP_Update,
    OP_Update_RAW,
    OP_GetMarkers,
    OP_GetMarkers_RAW,
    OP_GetKinds,
    OP_GetKinds_RAW,
    OP_GetCatalogs,
    OP_GetCatalogs_RAW,
    OP_IncrementalSync,
    OP_IncrementalSync_RAW,
    OP_GetBarcodes,
    OP_GetBarcodes_RAW,
    OP_GetBarcodesByProductCode,
    OP_GetBarcodesByProductCode_RAW,
    OP_UpdateBarcodes,
    OP_UpdateBarcodes_RAW,
    OP_UpdateBarcodesByProductCode,
    OP_UpdateBarcodesByProductCode_RAW,
    OP_FilterSql,
    OP_FilterSql_RAW,
    OP_GetPagedDocument,
    OP_GetPagedDocument_RAW,
    OP_GetPageWithSalePrices,
    OP_GetPageWithSalePrices_RAW,
    OP_GetPageWithDimensions,
    OP_GetPageWithDimensions_RAW,
    OP_FilterSqlWthSalePrices,
    OP_FilterSqlWthSalePrices_RAW,
    OP_FilterSqlWthDimensions,
    OP_FilterSqlWthDimensions_RAW,
    OP_GetLogisticFields,
    OP_GetLogisticFields_RAW,
    OP_GetLogisticFieldsByProductCode,
    OP_GetLogisticFieldsByProductCode_RAW,
)

_UNSET = object()

@overload
def Get(api: SyncInvokerProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[Product]: ...
@overload
def Get(api: SyncRequestProtocol, id: int, *, validate: bool = True) -> ResponseEnvelope[Product]: ...
@overload
def Get(api: SyncInvokerProtocol, code: str, *, validate: bool = True) -> ResponseEnvelope[Product]: ...
@overload
def Get(api: SyncRequestProtocol, code: str, *, validate: bool = True) -> ResponseEnvelope[Product]: ...
@overload
def Get(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[ProductListElement]]: ...
@overload
def Get(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[ProductListElement]]: ...
@overload
def Get(api: SyncInvokerProtocol, salePrices: bool, *, validate: bool = True) -> ResponseEnvelope[List[ProductListElement]]: ...
@overload
def Get(api: SyncRequestProtocol, salePrices: bool, *, validate: bool = True) -> ResponseEnvelope[List[ProductListElement]]: ...
def Get(api: object, id: object = _UNSET, code: object = _UNSET, salePrices: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'id' if id is not _UNSET else None,
        'code' if code is not _UNSET else None,
        'salePrices' if salePrices is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'id'}:
        if exact_match_name is not None:
            raise TypeError("Get(): ambiguous overload for provided arguments")
        exact_match = 'Get'
        exact_match_name = 'Get'
    if provided_names == {'code'}:
        if exact_match_name is not None:
            raise TypeError("Get(): ambiguous overload for provided arguments")
        exact_match = 'GetByCode'
        exact_match_name = 'GetByCode'
    if provided_names == set():
        if exact_match_name is not None:
            raise TypeError("Get(): ambiguous overload for provided arguments")
        exact_match = 'GetGet'
        exact_match_name = 'GetGet'
    if provided_names == {'salePrices'}:
        if exact_match_name is not None:
            raise TypeError("Get(): ambiguous overload for provided arguments")
        exact_match = 'GetBySalePrices'
        exact_match_name = 'GetBySalePrices'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'id'}.issubset(provided_names) and provided_names.issubset({'id'}):
            candidates.append((1, -1, 'Get'))
        if {'code'}.issubset(provided_names) and provided_names.issubset({'code'}):
            candidates.append((1, -1, 'GetByCode'))
        if set().issubset(provided_names) and provided_names.issubset(set()):
            candidates.append((0, 0, 'GetGet'))
        if {'salePrices'}.issubset(provided_names) and provided_names.issubset({'salePrices'}):
            candidates.append((1, -1, 'GetBySalePrices'))
        if not candidates:
            raise TypeError("Get(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("Get(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'Get':
        params, data = _prepare_Get(id=id)
        return invoke_operation(api, OP_Get if validate else OP_Get_RAW, params=params, data=data)
    if selected == 'GetByCode':
        params, data = _prepare_GetByCode(code=code)
        return invoke_operation(api, OP_GetByCode if validate else OP_GetByCode_RAW, params=params, data=data)
    if selected == 'GetGet':
        params, data = _prepare_GetGet()
        return invoke_operation(api, OP_GetGet if validate else OP_GetGet_RAW, params=params, data=data)
    if selected == 'GetBySalePrices':
        params, data = _prepare_GetBySalePrices(salePrices=salePrices)
        return invoke_operation(api, OP_GetBySalePrices if validate else OP_GetBySalePrices_RAW, params=params, data=data)
    raise TypeError("Get(): internal overload dispatch failure")

@overload
def GetWithSalePrices(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[ProductListElementWithSalePrices]]: ...
@overload
def GetWithSalePrices(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[ProductListElementWithSalePrices]]: ...
def GetWithSalePrices(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetWithSalePrices()
    return invoke_operation(api, OP_GetWithSalePrices if validate else OP_GetWithSalePrices_RAW, params=params, data=data)

@overload
def GetWithDimensions(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[ProductListElementWithDimensions]]: ...
@overload
def GetWithDimensions(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[ProductListElementWithDimensions]]: ...
def GetWithDimensions(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetWithDimensions()
    return invoke_operation(api, OP_GetWithDimensions if validate else OP_GetWithDimensions_RAW, params=params, data=data)

@overload
def Filter(api: SyncInvokerProtocol, salePrices: bool, criteria: "ProductFilterCriteria", *, validate: bool = True) -> ResponseEnvelope[List[ProductListElement]]: ...
@overload
def Filter(api: SyncRequestProtocol, salePrices: bool, criteria: "ProductFilterCriteria", *, validate: bool = True) -> ResponseEnvelope[List[ProductListElement]]: ...
def Filter(api: object, salePrices: bool, criteria: "ProductFilterCriteria", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_Filter(validate=validate, salePrices=salePrices, criteria=criteria)
    return invoke_operation(api, OP_Filter if validate else OP_Filter_RAW, params=params, data=data)

@overload
def FilterWithSalePrices(api: SyncInvokerProtocol, criteria: "ProductFilterCriteria", *, validate: bool = True) -> ResponseEnvelope[List[ProductListElementWithSalePrices]]: ...
@overload
def FilterWithSalePrices(api: SyncRequestProtocol, criteria: "ProductFilterCriteria", *, validate: bool = True) -> ResponseEnvelope[List[ProductListElementWithSalePrices]]: ...
def FilterWithSalePrices(api: object, criteria: "ProductFilterCriteria", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_FilterWithSalePrices(validate=validate, criteria=criteria)
    return invoke_operation(api, OP_FilterWithSalePrices if validate else OP_FilterWithSalePrices_RAW, params=params, data=data)

@overload
def FilterWithDimensions(api: SyncInvokerProtocol, criteria: "ProductFilterCriteria", *, validate: bool = True) -> ResponseEnvelope[List[ProductListElementWithDimensions]]: ...
@overload
def FilterWithDimensions(api: SyncRequestProtocol, criteria: "ProductFilterCriteria", *, validate: bool = True) -> ResponseEnvelope[List[ProductListElementWithDimensions]]: ...
def FilterWithDimensions(api: object, criteria: "ProductFilterCriteria", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_FilterWithDimensions(validate=validate, criteria=criteria)
    return invoke_operation(api, OP_FilterWithDimensions if validate else OP_FilterWithDimensions_RAW, params=params, data=data)

@overload
def AddNew(api: SyncInvokerProtocol, product: "Product", *, validate: bool = True) -> ResponseEnvelope[Product]: ...
@overload
def AddNew(api: SyncRequestProtocol, product: "Product", *, validate: bool = True) -> ResponseEnvelope[Product]: ...
def AddNew(api: object, product: "Product", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_AddNew(validate=validate, product=product)
    return invoke_operation(api, OP_AddNew if validate else OP_AddNew_RAW, params=params, data=data)

@overload
def Update(api: SyncInvokerProtocol, product: "Product", *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def Update(api: SyncRequestProtocol, product: "Product", *, validate: bool = True) -> ResponseEnvelope[None]: ...
def Update(api: object, product: "Product", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_Update(validate=validate, product=product)
    return invoke_operation(api, OP_Update if validate else OP_Update_RAW, params=params, data=data)

@overload
def GetMarkers(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[Marker]]: ...
@overload
def GetMarkers(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[Marker]]: ...
def GetMarkers(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetMarkers()
    return invoke_operation(api, OP_GetMarkers if validate else OP_GetMarkers_RAW, params=params, data=data)

@overload
def GetKinds(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[Kind]]: ...
@overload
def GetKinds(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[Kind]]: ...
def GetKinds(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetKinds()
    return invoke_operation(api, OP_GetKinds if validate else OP_GetKinds_RAW, params=params, data=data)

@overload
def GetCatalogs(api: SyncInvokerProtocol, *, validate: bool = True) -> ResponseEnvelope[List[Catalog]]: ...
@overload
def GetCatalogs(api: SyncRequestProtocol, *, validate: bool = True) -> ResponseEnvelope[List[Catalog]]: ...
def GetCatalogs(api: object, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetCatalogs()
    return invoke_operation(api, OP_GetCatalogs if validate else OP_GetCatalogs_RAW, params=params, data=data)

@overload
def IncrementalSync(api: SyncInvokerProtocol, dateFrom: datetime, *, validate: bool = True) -> ResponseEnvelope[List[IncrementalSyncListElement]]: ...
@overload
def IncrementalSync(api: SyncRequestProtocol, dateFrom: datetime, *, validate: bool = True) -> ResponseEnvelope[List[IncrementalSyncListElement]]: ...
def IncrementalSync(api: object, dateFrom: datetime, *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_IncrementalSync(dateFrom=dateFrom)
    return invoke_operation(api, OP_IncrementalSync if validate else OP_IncrementalSync_RAW, params=params, data=data)

@overload
def GetBarcodes(api: SyncInvokerProtocol, productId: int, *, validate: bool = True) -> ResponseEnvelope[ProductBarcodes]: ...
@overload
def GetBarcodes(api: SyncRequestProtocol, productId: int, *, validate: bool = True) -> ResponseEnvelope[ProductBarcodes]: ...
@overload
def GetBarcodes(api: SyncInvokerProtocol, productCode: str, *, validate: bool = True) -> ResponseEnvelope[ProductBarcodes]: ...
@overload
def GetBarcodes(api: SyncRequestProtocol, productCode: str, *, validate: bool = True) -> ResponseEnvelope[ProductBarcodes]: ...
def GetBarcodes(api: object, productId: object = _UNSET, productCode: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'productId' if productId is not _UNSET else None,
        'productCode' if productCode is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'productId'}:
        if exact_match_name is not None:
            raise TypeError("GetBarcodes(): ambiguous overload for provided arguments")
        exact_match = 'GetBarcodes'
        exact_match_name = 'GetBarcodes'
    if provided_names == {'productCode'}:
        if exact_match_name is not None:
            raise TypeError("GetBarcodes(): ambiguous overload for provided arguments")
        exact_match = 'GetBarcodesByProductCode'
        exact_match_name = 'GetBarcodesByProductCode'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'productId'}.issubset(provided_names) and provided_names.issubset({'productId'}):
            candidates.append((1, -1, 'GetBarcodes'))
        if {'productCode'}.issubset(provided_names) and provided_names.issubset({'productCode'}):
            candidates.append((1, -1, 'GetBarcodesByProductCode'))
        if not candidates:
            raise TypeError("GetBarcodes(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("GetBarcodes(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'GetBarcodes':
        params, data = _prepare_GetBarcodes(productId=productId)
        return invoke_operation(api, OP_GetBarcodes if validate else OP_GetBarcodes_RAW, params=params, data=data)
    if selected == 'GetBarcodesByProductCode':
        params, data = _prepare_GetBarcodesByProductCode(productCode=productCode)
        return invoke_operation(api, OP_GetBarcodesByProductCode if validate else OP_GetBarcodesByProductCode_RAW, params=params, data=data)
    raise TypeError("GetBarcodes(): internal overload dispatch failure")

@overload
def UpdateBarcodes(api: SyncInvokerProtocol, productId: int, *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def UpdateBarcodes(api: SyncRequestProtocol, productId: int, *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def UpdateBarcodes(api: SyncInvokerProtocol, productCode: str, *, validate: bool = True) -> ResponseEnvelope[None]: ...
@overload
def UpdateBarcodes(api: SyncRequestProtocol, productCode: str, *, validate: bool = True) -> ResponseEnvelope[None]: ...
def UpdateBarcodes(api: object, productId: object = _UNSET, productCode: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'productId' if productId is not _UNSET else None,
        'productCode' if productCode is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'productId'}:
        if exact_match_name is not None:
            raise TypeError("UpdateBarcodes(): ambiguous overload for provided arguments")
        exact_match = 'UpdateBarcodes'
        exact_match_name = 'UpdateBarcodes'
    if provided_names == {'productCode'}:
        if exact_match_name is not None:
            raise TypeError("UpdateBarcodes(): ambiguous overload for provided arguments")
        exact_match = 'UpdateBarcodesByProductCode'
        exact_match_name = 'UpdateBarcodesByProductCode'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'productId'}.issubset(provided_names) and provided_names.issubset({'productId'}):
            candidates.append((1, -1, 'UpdateBarcodes'))
        if {'productCode'}.issubset(provided_names) and provided_names.issubset({'productCode'}):
            candidates.append((1, -1, 'UpdateBarcodesByProductCode'))
        if not candidates:
            raise TypeError("UpdateBarcodes(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("UpdateBarcodes(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'UpdateBarcodes':
        params, data = _prepare_UpdateBarcodes(productId=productId)
        return invoke_operation(api, OP_UpdateBarcodes if validate else OP_UpdateBarcodes_RAW, params=params, data=data)
    if selected == 'UpdateBarcodesByProductCode':
        params, data = _prepare_UpdateBarcodesByProductCode(productCode=productCode)
        return invoke_operation(api, OP_UpdateBarcodesByProductCode if validate else OP_UpdateBarcodesByProductCode_RAW, params=params, data=data)
    raise TypeError("UpdateBarcodes(): internal overload dispatch failure")

@overload
def FilterSql(api: SyncInvokerProtocol, criteriaFilter: "ProductCriteriaFilter", *, validate: bool = True) -> ResponseEnvelope[List[ProductListElement]]: ...
@overload
def FilterSql(api: SyncRequestProtocol, criteriaFilter: "ProductCriteriaFilter", *, validate: bool = True) -> ResponseEnvelope[List[ProductListElement]]: ...
def FilterSql(api: object, criteriaFilter: "ProductCriteriaFilter", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_FilterSql(validate=validate, criteriaFilter=criteriaFilter)
    return invoke_operation(api, OP_FilterSql if validate else OP_FilterSql_RAW, params=params, data=data)

@overload
def GetPagedDocument(api: SyncInvokerProtocol, page: int, size: int, orderBy: "enumOrderByType", *, validate: bool = True) -> ResponseEnvelope[Page]: ...
@overload
def GetPagedDocument(api: SyncRequestProtocol, page: int, size: int, orderBy: "enumOrderByType", *, validate: bool = True) -> ResponseEnvelope[Page]: ...
def GetPagedDocument(api: object, page: int, size: int, orderBy: "enumOrderByType", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetPagedDocument(page=page, size=size, orderBy=orderBy)
    return invoke_operation(api, OP_GetPagedDocument if validate else OP_GetPagedDocument_RAW, params=params, data=data)

@overload
def GetPageWithSalePrices(api: SyncInvokerProtocol, page: int, size: int, orderBy: "enumOrderByType", *, validate: bool = True) -> ResponseEnvelope[Page]: ...
@overload
def GetPageWithSalePrices(api: SyncRequestProtocol, page: int, size: int, orderBy: "enumOrderByType", *, validate: bool = True) -> ResponseEnvelope[Page]: ...
def GetPageWithSalePrices(api: object, page: int, size: int, orderBy: "enumOrderByType", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetPageWithSalePrices(page=page, size=size, orderBy=orderBy)
    return invoke_operation(api, OP_GetPageWithSalePrices if validate else OP_GetPageWithSalePrices_RAW, params=params, data=data)

@overload
def GetPageWithDimensions(api: SyncInvokerProtocol, page: int, size: int, orderBy: "enumOrderByType", *, validate: bool = True) -> ResponseEnvelope[Page]: ...
@overload
def GetPageWithDimensions(api: SyncRequestProtocol, page: int, size: int, orderBy: "enumOrderByType", *, validate: bool = True) -> ResponseEnvelope[Page]: ...
def GetPageWithDimensions(api: object, page: int, size: int, orderBy: "enumOrderByType", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_GetPageWithDimensions(page=page, size=size, orderBy=orderBy)
    return invoke_operation(api, OP_GetPageWithDimensions if validate else OP_GetPageWithDimensions_RAW, params=params, data=data)

@overload
def FilterSqlWthSalePrices(api: SyncInvokerProtocol, criteriaFilter: "ProductCriteriaFilter", *, validate: bool = True) -> ResponseEnvelope[List[ProductListElementWithSalePrices]]: ...
@overload
def FilterSqlWthSalePrices(api: SyncRequestProtocol, criteriaFilter: "ProductCriteriaFilter", *, validate: bool = True) -> ResponseEnvelope[List[ProductListElementWithSalePrices]]: ...
def FilterSqlWthSalePrices(api: object, criteriaFilter: "ProductCriteriaFilter", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_FilterSqlWthSalePrices(validate=validate, criteriaFilter=criteriaFilter)
    return invoke_operation(api, OP_FilterSqlWthSalePrices if validate else OP_FilterSqlWthSalePrices_RAW, params=params, data=data)

@overload
def FilterSqlWthDimensions(api: SyncInvokerProtocol, criteriaFilter: "ProductCriteriaFilter", *, validate: bool = True) -> ResponseEnvelope[List[ProductListElementWithDimensions]]: ...
@overload
def FilterSqlWthDimensions(api: SyncRequestProtocol, criteriaFilter: "ProductCriteriaFilter", *, validate: bool = True) -> ResponseEnvelope[List[ProductListElementWithDimensions]]: ...
def FilterSqlWthDimensions(api: object, criteriaFilter: "ProductCriteriaFilter", *, validate: bool = True) -> ResponseEnvelope[Any]:
    params, data = _prepare_FilterSqlWthDimensions(validate=validate, criteriaFilter=criteriaFilter)
    return invoke_operation(api, OP_FilterSqlWthDimensions if validate else OP_FilterSqlWthDimensions_RAW, params=params, data=data)

@overload
def GetLogisticFields(api: SyncInvokerProtocol, productId: int, *, validate: bool = True) -> ResponseEnvelope[List[ProductLogisticField]]: ...
@overload
def GetLogisticFields(api: SyncRequestProtocol, productId: int, *, validate: bool = True) -> ResponseEnvelope[List[ProductLogisticField]]: ...
@overload
def GetLogisticFields(api: SyncInvokerProtocol, productCode: str, *, validate: bool = True) -> ResponseEnvelope[List[ProductLogisticField]]: ...
@overload
def GetLogisticFields(api: SyncRequestProtocol, productCode: str, *, validate: bool = True) -> ResponseEnvelope[List[ProductLogisticField]]: ...
def GetLogisticFields(api: object, productId: object = _UNSET, productCode: object = _UNSET, *, validate: bool = True) -> ResponseEnvelope[Any]:
    provided_names = {
        'productId' if productId is not _UNSET else None,
        'productCode' if productCode is not _UNSET else None,
    }
    provided_names.discard(None)
    exact_match = None
    exact_match_name = None
    if provided_names == {'productId'}:
        if exact_match_name is not None:
            raise TypeError("GetLogisticFields(): ambiguous overload for provided arguments")
        exact_match = 'GetLogisticFields'
        exact_match_name = 'GetLogisticFields'
    if provided_names == {'productCode'}:
        if exact_match_name is not None:
            raise TypeError("GetLogisticFields(): ambiguous overload for provided arguments")
        exact_match = 'GetLogisticFieldsByProductCode'
        exact_match_name = 'GetLogisticFieldsByProductCode'
    if exact_match_name is not None:
        selected = exact_match_name
    else:
        candidates: list[tuple[int, int, str]] = []
        if {'productId'}.issubset(provided_names) and provided_names.issubset({'productId'}):
            candidates.append((1, -1, 'GetLogisticFields'))
        if {'productCode'}.issubset(provided_names) and provided_names.issubset({'productCode'}):
            candidates.append((1, -1, 'GetLogisticFieldsByProductCode'))
        if not candidates:
            raise TypeError("GetLogisticFields(): no matching overload for provided arguments")
        candidates.sort(reverse=True)
        best_score = candidates[0][:2]
        best = [name for score_req, score_all, name in candidates if (score_req, score_all) == best_score]
        if len(best) != 1:
            raise TypeError("GetLogisticFields(): ambiguous overload for provided arguments")
        selected = best[0]
    if selected == 'GetLogisticFields':
        params, data = _prepare_GetLogisticFields(productId=productId)
        return invoke_operation(api, OP_GetLogisticFields if validate else OP_GetLogisticFields_RAW, params=params, data=data)
    if selected == 'GetLogisticFieldsByProductCode':
        params, data = _prepare_GetLogisticFieldsByProductCode(productCode=productCode)
        return invoke_operation(api, OP_GetLogisticFieldsByProductCode if validate else OP_GetLogisticFieldsByProductCode_RAW, params=params, data=data)
    raise TypeError("GetLogisticFields(): internal overload dispatch failure")

__all__ = ["Get", "GetWithSalePrices", "GetWithDimensions", "Filter", "FilterWithSalePrices", "FilterWithDimensions", "AddNew", "Update", "GetMarkers", "GetKinds", "GetCatalogs", "IncrementalSync", "GetBarcodes", "UpdateBarcodes", "FilterSql", "GetPagedDocument", "GetPageWithSalePrices", "GetPageWithDimensions", "FilterSqlWthSalePrices", "FilterSqlWthDimensions", "GetLogisticFields"]
