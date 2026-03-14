def classify_price_band(price_band: float) -> str:
    if price_band <= 60:
        return "LOW"
    if price_band <= 150:
        return "MEDIUM"
    if price_band <= 300:
        return "HIGH"
    return "EXTREME"


def generate_recommendation(gen_volume: float, load_volume: float, price_band: float) -> dict:
    if gen_volume == 0 and load_volume == 0:
        classification = "IDLE"
        net_direction = "NONE"
        reason = "Both generation and load volumes are zero"
    elif gen_volume > load_volume:
        classification = "GEN_FAVOURED"
        net_direction = "GEN"
        reason = "Generation volume exceeds load volume"
    elif load_volume > gen_volume:
        classification = "LOAD_FAVOURED"
        net_direction = "LOAD"
        reason = "Load volume exceeds generation volume"
    else:
        classification = "BALANCED"
        net_direction = "NEUTRAL"
        reason = "Generation and load volumes are equal"

    price_band_category = classify_price_band(price_band)
    risk_flag = price_band > 300

    return {
        "net_direction": net_direction,
        "classification": classification,
        "price_band_category": price_band_category,
        "risk_flag": risk_flag,
        "reason": reason,
    }