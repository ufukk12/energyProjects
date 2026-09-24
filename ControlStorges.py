class ControlStorges:

    def __init__(self):
        self.default_metanol = 67.7
        self.default_water = 37.3


    def control_fuels(self , current_metanol , current_water , current_soc , is_ref_active):

        try:
            current_metanol = float(current_metanol)
        except ValueError:
            return 301 , 0, 0

        try:
            current_water = float(current_water)
        except ValueError:
            return 302 , 0 , 0

        if is_ref_active == True:
            #50kWh için 20 den 85 e kadar kaplanan enerji miktarı 32.5kWh ve bunun için temel olarak gereken metanol miktarı 18,51L ve su miktarı 10,19L
            # Önce depolarda bulunan metanol miktarı ile su miktarının oranlarına bakalım. eğer 0,551 in üzerinde ise suyun tümünü harcayacak şekilde tam tersi durum için de tüm metanolü harcayacak şekilde ilerleyelim
            necessary_soc = 85 - current_soc
            if necessary_soc <= 0:
                return current_soc, current_metanol, current_water
            necessary_kWh = (32.5/65) * necessary_soc
            necessary_metanol = (18.51 / 32.5) * necessary_kWh
            necessary_water = (10.19 / 32.5) * necessary_kWh

            if current_metanol < necessary_metanol or current_water < necessary_water:
                #sistem zaten 32.5 tan az üretim yapacağı için aynen kalsın(gemini için not kısmıdır silinecek)

                if current_metanol == 0:
                    return 3010 , current_metanol , current_water

                if current_water == 0:
                    return 3020, current_metanol , current_water

                rate = current_metanol / current_water

                if rate > 0.551:

                    water_to_be_used = current_water
                    metanol_to_be_used = current_water / 0.551  # DÜZELTME: Metanolü bulmak için böldük

                    # DÜZELTME: Doğru orantı (10.19L su 32.5kWh üretiyorsa...)
                    produced_kWh = (water_to_be_used * 32.5) / 10.19

                    new_soc = current_soc + ((produced_kWh / 50) * 100)
                    current_metanol -= metanol_to_be_used
                    current_water -= water_to_be_used

                    return new_soc, current_metanol, current_water
                else:
                    metanol_to_be_used = current_metanol
                    water_to_be_used = current_metanol * 0.551


                    produced_kWh = (metanol_to_be_used * 32.5) / 18.51

                    new_soc = current_soc + ((produced_kWh / 50) * 100)
                    current_metanol -= metanol_to_be_used
                    current_water -= water_to_be_used

                    return new_soc, current_metanol, current_water


            else:_
                metanol_to_be_used = necessary_metanol
                water_to_be_used = necessary_water

                new_soc = 85.0
                current_metanol -= metanol_to_be_used
                current_water -= water_to_be_used

                return new_soc, current_metanol, current_water

