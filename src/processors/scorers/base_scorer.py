from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
import numpy as np
from src.logger.logger import logger

class BaseScorer(ABC):
    def __init__(self, name: str, weight: float = 1.0):
        self.name = name
        self.weight = weight
        self.logger = logger
        
    @abstractmethod
    def calculate_score(self, data: Dict[str, Any]) -> float:
        pass
    
    @abstractmethod
    def get_components(self, data: Dict[str, Any]) -> Dict[str, float]:
        pass
    
    def normalize_score(self, score: float, min_val: float = 0.0, max_val: float = 1.0) -> float:
        if max_val == min_val:
            return 0.5
        
        normalized = (score - min_val) / (max_val - min_val)
        return max(0.0, min(1.0, normalized))
    
    def calculate_weighted_score(self, data: Dict[str, Any]) -> float:
        score = self.calculate_score(data)
        return score * self.weight
    
    def get_performance_level(self, score: float) -> str:
        if score < 0.3:
            return "low"
        elif score < 0.6:
            return "medium"
        else:
            return "high"
    
    def __str__(self) -> str:
        return f"{self.name} (weight: {self.weight})"
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}', weight={self.weight})"