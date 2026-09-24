class BatteryHealth:
    def __init__(self, capacity_kwh , default_soc):
        self.capacity_kwh = capacity_kwh #50kWh
        self.default_soc = default_soc #85%

        self.soh = 100
        self.is_ref_active = False
        self.cycle_count = 0


    def ref_karar_mekanizması(self , current_soc , nearest_charge_stat_km , metanol_rate , current_speed, is_fc_healthy):

        try:
            metanol_rate = float(metanol_rate)
        except ValueError:
            return 301

        try:
            is_fc_healthy = bool(is_fc_healthy)
        except ValueError:
            return 401

        try:
            nearest_charge_stat_km = float(nearest_charge_stat_km)
        except ValueError:
            nearest_charge_stat_km = 50.0 # Gps sensörlerinin bozuk olma ihtimali vardır. Bu durumda kötü senaryoyu düşünerek mesageyi 45 km nin üstünde tuttum


        if metanol_rate == 0:
            return 300
        if is_fc_healthy == False:
            return 400

        if current_soc < 25:
            if current_speed > 125:
                if nearest_charge_stat_km > 30:
                    self.cycle_count += 1
                    return 200
                else:
                    return 201 # Seçim sunulacak
            else:
                if nearest_charge_stat_km > 45:
                    self.cycle_count += 1
                    return 200
                else:
                    return 201 # Seçim sunulacak























