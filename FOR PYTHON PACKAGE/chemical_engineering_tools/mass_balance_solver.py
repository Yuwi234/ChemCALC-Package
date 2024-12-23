#!/usr/bin/env python
# coding: utf-8

# ### Mass Balance Solver 

# In[8]:


class MassBalanceSolver:
    """
    A class to solve mass balance equations.
    """
    @staticmethod
    def solve(known_streams, equations):
        """
        Solves mass balance equations for steady-state systems.

        Parameters:
            known_streams (dict): Known streams with flow rates and compositions.
            equations (list): Mass balance equations in string form.

        Returns:
            dict: Solved streams.
        """
        streams = known_streams.copy()
        for eq in equations:
            lhs, rhs = eq.split("=")
            lhs = lhs.strip()
            rhs = rhs.strip()

            if lhs in streams:
                streams[rhs] = streams[lhs]
            elif rhs in streams:
                streams[lhs] = streams[rhs]
            else:
                lhs_value = eval(lhs, {}, streams)
                rhs_value = eval(rhs, {}, streams)
                if isinstance(lhs_value, (int, float)) and isinstance(rhs_value, str):
                    streams[rhs_value] = lhs_value
                else:
                    streams[lhs_value] = lhs_value + 1
        return streams