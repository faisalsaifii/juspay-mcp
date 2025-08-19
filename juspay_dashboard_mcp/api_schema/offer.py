# Copyright 2025 Juspay
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at https://www.apache.org/licenses/LICENSE-2.0.txt

from typing import Optional, List, Dict, Any, Literal
from pydantic import BaseModel, Field

from juspay_dashboard_mcp.api_schema.headers import WithHeaders

class JuspayGetOfferDetailsPayload(WithHeaders):
    offer_ids: List[str] = Field(
        ...,
        description="List of unique identifiers of the offers to retrieve details for."
    )
    offer_codes: List[str] = Field(
        ...,
        description="List of unique identifiers of the offer codes to retrieve details for."
    )

class CreatedAtRange(BaseModel):
    lte: str = Field(..., description="Less than or equal to timestamp (ISO format).")
    gte: str = Field(..., description="Greater than or equal to timestamp (ISO format).")

class SortWith(BaseModel):
    order: Literal["ASCENDING", "DESCENDING"] = Field(..., description="Sort order.")
    field: Literal["GROUP_ID", "STATUS", "OFFER_CODE", "PRIORITY", "CREATED_AT"] = Field(
        ...,
        description="Field to sort by."
    )

class JuspayListOffersPayload(WithHeaders):
    merchant_id: str = Field(
        ...,
        description="Merchant identifier for which to list offers."
    )
    start_time: str = Field(
        ...,
        description="Start time for filtering offers (ISO format)."
    )
    end_time: str = Field(
        ...,
        description="End time for filtering offers (ISO format)."
    )
    sort_offers: SortWith = Field(
        ...,
        description="Sorting options for offers with order and field."
    )
    created_at: CreatedAtRange = Field(
        ...,
        description="Created at range for filtering offers with gte and lte timestamps."
    )
    auto_apply: Optional[Literal["TRUE", "FALSE"]] = Field(
        default=None,
        description="Auto apply setting for offers."
    )
    batch_id: Optional[List[str]] = Field(
        default=None,
        description="List of batch IDs to filter offers."
    )
    benefit_type: Optional[List[Literal["CASHBACK", "DISCOUNT", "MERCHANT_DISCOUNT", "EMI_DISCOUNT", "EMI_CASHBACK"]]] = Field(
        default=None,
        description="List of benefit types to filter offers."
    )
    currency: Optional[List[str]] = Field(
        default=None,
        description="List of currencies to filter offers."
    )
    fetch_all_offers: Optional[Literal["TRUE", "FALSE"]] = Field(
        default=None,
        description="Flag to fetch all offers."
    )
    group_id: Optional[List[str]] = Field(
        default=None,
        description="List of group IDs to filter offers."
    )
    limit: Optional[int] = Field(
        default=None,
        description="Limit for number of offers to fetch."
    )
    offer_code: Optional[List[str]] = Field(
        default=None,
        description="List of offer codes to filter offers."
    )
    offer_id: Optional[List[str]] = Field(
        default=None,
        description="List of offer IDs to filter offers."
    )
    offset: Optional[int] = Field(
        default=None,
        description="Offset for pagination."
    )
    payment_method_type: Optional[List[Literal["CARD", "UPI", "WALLET", "REWARD", "CONSUMER_FINANCE", "MERCHANT_CONTAINER", "CASH", "RTP", "OTC"]]] = Field(
        default=None,
        description="List of payment method types to filter offers."
    )
    status: Optional[List[Literal["NEW", "ACTIVE", "PAUSED", "EXPIRED"]]] = Field(
        default=None,
        description="List of offer statuses to filter offers."
    )
