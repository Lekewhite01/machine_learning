import json
import warnings
import pandas as pd
import numpy as np
import uvicorn
from fastapi import FastAPI
from mangum import Mangum
from pydantic import BaseModel
warnings.filterwarnings('ignore')

# Create FastAPI application
app = FastAPI()

class SendIn(BaseModel):
    msisdn: str

class SendOut(SendIn):
    success: bool
    message: str

# Load the DataFrame once
df = pd.read_csv("amount_recommend_demo.csv")
    
@app.post("/", status_code=200, response_model=SendOut)
async def predict_amount(request: SendIn):

    """Query scored dataframe, return amount.

    Parameters
    ----------
        request : SendIn

    Returns
    ------
    dict
        Must conform to `SendOut` class
    """
    # Create `response` dictionary from `request`
    response = request.dict()

    # Create try block to handle exceptions
    try:
        # df = pd.read_csv("amount_recommend_demo.csv")
        recommended_amount = df[df["MSISDN"] == request.msisdn]["RECOMMENDED_AMOUNT"].values[0]
        # Add `"success"` key to `response`
        response["success"] = True

        # Add `"message"` key to `response` with recommended amount
        response["message"] = f"The recommended loan amount for customer {request.msisdn} is {recommended_amount}"

    # Create except block
    except Exception as e:
        # Add `"success"` key to `response`
        response["success"] = False

        # Add `"message"` key to `response` with error message
        response["message"] = str(e)

    # Return response
    return response

# handler = Mangum(app)

