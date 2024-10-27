import enum
import json
import os


@enum.unique
class DataTypes(enum.StrEnum):
    INVALID_EMAIL = "INVALID_EMAIL"
    INVALID_PASSWORD = "INVALID_PASSWORD"


@enum.unique
class PlanTypes(enum.StrEnum):
    BUSINESS_PLAN = "BUSINESS"
    SCHOOL_PLAN = "SCHOOL"
    WEDDING_PLAN = "WEDDING"
    TRAVEL_PLAN = "TRAVEL"
    HOME_PLAN = "HOME"
    KIDS_PLAN = "KIDS"
    RENT_PLAN = "RENT"


def get_credential_data(data_type: DataTypes):
    """
    Filter the test data by data type
    """
    with open("data\\credentials.json", "r") as cred_file:
        credentials = json.loads(cred_file.read())

    return list(filter(lambda x: x["type"] == data_type, credentials))


def get_plan_data(plan_type: PlanTypes):
    """
    Filter the test data by plan type
    """
    with open("data\\plans.json", "r") as plan_file:
        plans = json.loads(plan_file.read())

    return list(filter(lambda x: x["type"] == plan_type, plans)) if plan_type else plans


def calculate_plan_stats(plan_data: dict) -> float:
    """
    Calculate the estimated interest rate, recurring investment,
    returns amount and maturity amount

    Params
    ------
    plan_data: dict
        Contains the plan data for test purposes
    """
    from datetime import date
    from dateutil.relativedelta import relativedelta

    currency_rate = float(os.getenv("CURRENCY_RATE"))
    interest_rate = float(os.getenv("INTEREST_RATE"))

    maturity_date = date.today() + relativedelta(months=plan_data["period"])
    plan_data["maturity_date"] = maturity_date.strftime("%d-%m-%Y")

    plan_data["investment_amount"] = plan_data["amount"] / currency_rate
    plan_data["est_interest_rate"] = interest_rate * plan_data["period"]
    plan_data["est_recurring_amount"] = plan_data["investment_amount"] / \
        plan_data["period"]
    plan_data["returns_amount"] = (plan_data["est_interest_rate"] *
                                   plan_data["investment_amount"]) / 100
    plan_data["maturity_amount"] = plan_data["returns_amount"] + \
        plan_data["investment_amount"]
