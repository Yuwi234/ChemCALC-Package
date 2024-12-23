#!/usr/bin/env python
# coding: utf-8

# ### Energy Balance Calculator

# Computes energy requirements or releases for heating, cooling, and phase changes

# In[3]:


class EnergyBalanceCalculator:
    """
    A class for energy balance calculations.
    """
    @staticmethod
    def calculate(known_energy, equations):
        """
        Calculates energy balance for a system.

        Parameters:
            known_energy (dict): Known energy values (e.g., energy in, work done).
            equations (list): Energy balance equations.

        Returns:
            dict: Energy balance results.
        """
        energy = known_energy.copy()
        for eq in equations:
            lhs, rhs = eq.split("=")
            lhs = lhs.strip()
            rhs = rhs.strip()

            if lhs in energy:
                energy[rhs] = energy[lhs]
            elif rhs in energy:
                energy[lhs] = energy[rhs]
            else:
                lhs_value = eval(lhs, {}, energy)
                rhs_value = eval(rhs, {}, energy)
                if isinstance(lhs_value, (int, float)) and isinstance(rhs_value, str):
                    energy[rhs_value] = lhs_value
                else:
                    energy[lhs_value] = lhs_value + 1
        return energy