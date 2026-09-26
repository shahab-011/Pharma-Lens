from typing import List, Optional

from pydantic import BaseModel, Field, field_validator


class PharmaDocument(BaseModel):

    # ============================================================
    # DOCUMENT INFORMATION
    # ============================================================

    document_title: Optional[str] = None
    document_type: Optional[str] = None
    company: Optional[str] = None
    report_date: Optional[str] = None
    study_name: Optional[str] = None
    study_id: Optional[str] = None


    # ============================================================
    # DRUG INFORMATION
    # ============================================================

    drug_name: Optional[str] = None
    generic_name: Optional[str] = None
    drug_code: Optional[str] = None
    active_ingredient: Optional[str] = None
    drug_class: Optional[str] = None
    route_of_administration: Optional[str] = None
    dosage: Optional[str] = None
    dosing_frequency: Optional[str] = None
    treatment_duration: Optional[str] = None
    therapeutic_area: Optional[str] = None
    indication: Optional[str] = None


    # ============================================================
    # CLINICAL TRIAL INFORMATION
    # ============================================================

    clinical_phase: Optional[str] = None
    study_design: Optional[str] = None

    number_enrolled: Optional[int] = None
    number_screened: Optional[int] = None
    number_randomized: Optional[int] = None
    number_treated: Optional[int] = None

    number_efficacy_analysis: Optional[int] = None
    number_safety_analysis: Optional[int] = None

    number_of_sites: Optional[int] = None

    countries: List[str] = Field(
        default_factory=list
    )

    study_start_date: Optional[str] = None
    expected_completion_date: Optional[str] = None
    expected_results_date: Optional[str] = None

    principal_investigator: Optional[str] = None


    # ============================================================
    # EFFICACY / OUTCOMES
    # ============================================================

    primary_endpoint: Optional[str] = None

    secondary_endpoints: List[str] = Field(
        default_factory=list
    )

    treatment_results: Optional[str] = None
    comparator_results: Optional[str] = None
    placebo_results: Optional[str] = None
    response_rates: Optional[str] = None

    other_outcomes: List[str] = Field(
        default_factory=list
    )


    # ============================================================
    # SAFETY
    # ============================================================

    adverse_events: List[str] = Field(
        default_factory=list
    )

    serious_adverse_events: List[str] = Field(
        default_factory=list
    )

    treatment_discontinuations: Optional[str] = None

    treatment_related_events: List[str] = Field(
        default_factory=list
    )

    severity_grade: Optional[str] = None


    # ============================================================
    # REGULATORY INFORMATION
    # ============================================================

    regulatory_status: Optional[str] = None
    regulatory_agency: Optional[str] = None
    approval_status: Optional[str] = None
    submission_status: Optional[str] = None


    # ============================================================
    # OTHER INFORMATION
    # ============================================================

    resistance_monitoring: Optional[str] = None
    biomarkers: Optional[str] = None
    manufacturing_information: Optional[str] = None
    market_estimates: Optional[str] = None

    company_statements: List[str] = Field(
        default_factory=list
    )

    limitations: List[str] = Field(
        default_factory=list
    )


    # ============================================================
    # DATA QUALITY
    # ============================================================

    missing_information: List[str] = Field(
        default_factory=list
    )

    contradictions: List[str] = Field(
        default_factory=list
    )

    ambiguous_statements: List[str] = Field(
        default_factory=list
    )

    data_quality_issues: List[str] = Field(
        default_factory=list
    )

    # ============================================================
    # ROBUST LLM OUTPUT VALIDATION
    # ============================================================

    @field_validator(
        "countries",
        "secondary_endpoints",
        "other_outcomes",
        "adverse_events",
        "serious_adverse_events",
        "treatment_related_events",
        "company_statements",
        "limitations",
        "missing_information",
        "contradictions",
        "ambiguous_statements",
        "data_quality_issues",
        mode="before"
    )
    @classmethod
    def coerce_none_to_list(cls, v):
        if v is None:
            return []
        if isinstance(v, str):
            return [v] if v.strip() else []
        return v