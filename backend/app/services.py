def calculate_risk(amount: float, country: str, channel: str) -> float:
    score = 10.0
    if amount >= 100000:
        score += 35
    elif amount >= 50000:
        score += 20
    if country not in {"Ethiopia", "Kenya", "Uganda"}:
        score += 25
    if channel.lower() in {"card", "international", "crypto"}:
        score += 10
    return min(score, 100.0)
