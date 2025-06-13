import numpy as np

def run_mpc_control(wn):
    # Dummy MPC: Simulate simple demand forecast
    demand_forecast = np.random.normal(10, 2, 24)  # 24-hour simulation
    control_actions = [round(d * 0.8, 2) for d in demand_forecast]
    return {
        "forecast": demand_forecast.tolist(),
        "control": control_actions
    }
