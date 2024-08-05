import uuid

class PromoCodeSystem:
    def __init__(self):
        self.promo_codes = {}

    def generate_promo_code(self, discount, uses):
        promo_code = str(uuid.uuid4())[:8].upper()
        self.promo_codes[promo_code] = {"discount": discount, "uses": uses}
        return promo_code
    
    def apply_promo_code(self, promo_code):
        if promo_code in self.promo_codes:
            if self.promo_codes[promo_code]["uses"] > 0:
                self.promo_codes[promo_code]["uses"] -= 1
                return self.promo_codes[promo_code]["discount"]
            else:
                return 0
        else:
            return 0
        
    def get_promo_codes(self, promo_code):
        return self.promo_codes.get(promo_code, None)
    

promo_system = PromoCodeSystem()

discount = 60
uses = 5
promo_code = promo_system.generate_promo_code(discount, uses)
print(f"Generated Promo code: {promo_code}")


#Test by applying the promo code multiple times
for i in range(10):
    discount_applied = promo_system.apply_promo_code(promo_code)
    print(f"Discount applied: {discount_applied}")