from __future__ import annotations

from pydantic import BaseModel

from SymfWebAPI.WebAPI.Interface.Enums import enumFilterSqlCriteriaMode

class FKF_Common_ViewModels_CriteriaFilter_IntCriteriaFilter(BaseModel):
    Value_From: int
    Value_To: int
    Mode: "enumFilterSqlCriteriaMode"
IntCriteriaFilter = FKF_Common_ViewModels_CriteriaFilter_IntCriteriaFilter

class FKF_Common_ViewModels_CriteriaFilter_StringCriteriaFilter(BaseModel):
    Value: str
    Mode: "enumFilterSqlCriteriaMode"
StringCriteriaFilter = FKF_Common_ViewModels_CriteriaFilter_StringCriteriaFilter
