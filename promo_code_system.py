import uuid

class PromoCodeSystem:
    def __init__(self):
        self.promo_codes = {}

    def generate_promo_code(self, discount, uses):
        promo_code = str(uuid.uuid4())[:8].upper()
        self.promo_codes[promo_code] = {"discount": discount, "uses": uses}
        return promo_code
    
    def apply_promo_code(self, promo_code):
        if promo_code not in self.promo_codes:
            return "Invalid promo code"
        elif self.promo_codes[promo_code]["uses"] <= 0:
            return "Expired promo code"
        else:
            self.promo_codes[promo_code]["uses"] -= 1
            return f"Discount applied: {self.promo_codes[promo_code]['discount']}%"
    
    def get_promo_codes(self, promo_code):
        return self.promo_codes.get(promo_code, None)
    

promo_system = PromoCodeSystem()

discount = 60
uses = 5
promo_code = promo_system.generate_promo_code(discount, uses)
print(f"Generated Promo code: {promo_code}")

# Test by applying the promo code multiple times
for i in range(10):
    if i == 3:
        result = promo_system.apply_promo_code("promo_code")
    else:
        result = promo_system.apply_promo_code(promo_code)
    print(result)
