import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def generate_uk_claims(num_records=500):
    # Data definitions
    claim_types = ['Motor', 'Property', 'Health', 'Travel', 'Liability']
    uk_cities = ['London', 'Manchester', 'Birmingham', 'Glasgow', 'Liverpool', 'Leeds', 'Edinburgh', 'Bristol']
    status_options = ['Open', 'Closed', 'Under Investigation', 'Pending']

    # Generating synthetic data
    data = {
        'Claim_ID': [f'UKC-{1000 + i}' for i in range(num_records)],
        'Claim_Date': [(datetime(2026, 1, 1) + timedelta(days=random.randint(0, 120))).strftime('%Y-%m-%d') for i in range(num_records)],
        'Policy_Holder_City': [random.choice(uk_cities) for _ in range(num_records)],
        'Claim_Type': [random.choice(claim_types) for _ in range(num_records)],
        'Claim_Amount_GBP': np.round(np.random.uniform(500, 15000, size=num_records), 2),
        'Status': [random.choice(status_options) for _ in range(num_records)],
        'Processing_Time_Days': [random.randint(1, 60) for _ in range(num_records)]
    }
    
    # Create DataFrame and Save
    df = pd.DataFrame(data)
    df.to_csv('claims_demo.csv', index=False)
    print(f"Success: claims_demo.csv with {num_records} records generated.")

if __name__ == "__main__":
    generate_uk_claims(500)
