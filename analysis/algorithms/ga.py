def optimize_valve_placement(wn, max_pressure=30):
    # Dummy example of selecting key pipes
    critical_pipes = [link for link in wn.pipe_name_list if "P" in link][:5]
    return critical_pipes
