import pandas as pd
import numpy as np
from scipy.stats import norm


chat_id = 307311223 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    
    p1 = x_success/x_cnt
    p2 = y_success/y_cnt
    p = (x_success + y_success)/ (x_cnt + y_cnt)
    
    z = (p2-p1)/((p*(1-p)*(1/x_success + 1/y_success))**0.5)
    
    print(z)
    
    alpha = 0.01
    
    p_value = norm.cdf(z)
    
    print(p_value)
    
    if p_value < alpha: return True
    else: return False
