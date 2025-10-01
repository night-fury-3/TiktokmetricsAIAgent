"""
Base scorer class for all KPI scorers
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
import numpy as np
from src.logger.logger import logger


class BaseScorer(ABC):
    """
    Abstract base class for all KPI scorers
    """
    
    def __init__(self, name: str, weight: float = 1.0):
        """
        Initialize base scorer
        
        Args:
            name: Scorer name
            weight: Scorer weight for overall score calculation
        """
        self.name = name
        self.weight = weight
        self.logger = logger
        
    @abstractmethod
    def calculate_score(self, data: Dict[str, Any]) -> float:
        """
        Calculate the KPI score based on input data
        
        Args:
            data: Input data dictionary containing metrics
            
        Returns:
            Normalized score between 0 and 1
        """
        pass
    
    @abstractmethod
    def get_components(self, data: Dict[str, Any]) -> Dict[str, float]:
        """
        Get component scores for detailed analysis
        
        Args:
            data: Input data dictionary containing metrics
            
        Returns:
            Dictionary of component scores
        """
        pass
    
    def normalize_score(self, score: float, min_val: float = 0.0, max_val: float = 1.0) -> float:
        """
        Normalize score to 0-1 range
        
        Args:
            score: Raw score
            min_val: Minimum possible value
            max_val: Maximum possible value
            
        Returns:
            Normalized score between 0 and 1
        """
        if max_val == min_val:
            return 0.5
        
        normalized = (score - min_val) / (max_val - min_val)
        return max(0.0, min(1.0, normalized))
    
    def calculate_weighted_score(self, data: Dict[str, Any]) -> float:
        """
        Calculate weighted score
        
        Args:
            data: Input data dictionary
            
        Returns:
            Weighted score
        """
        score = self.calculate_score(data)
        return score * self.weight
    
    def get_performance_level(self, score: float) -> str:
        """
        Get performance level based on score
        
        Args:
            score: Normalized score (0-1)
            
        Returns:
            Performance level: 'low', 'medium', or 'high'
        """
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
