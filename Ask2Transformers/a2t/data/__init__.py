"""The module `data` implements different dataloaders or `Dataset`s for predefined tasks.
"""
from .tacred import TACREDRelationClassificationDataset
from .babeldomains import BabelDomainsTopicClassificationDataset
from .sentiment import SentimentTopicClassificationDataset
from .base import Dataset

PREDEFINED_DATASETS = {"tacred": TACREDRelationClassificationDataset, "babeldomains": BabelDomainsTopicClassificationDataset ,"sentiment": SentimentTopicClassificationDataset}

__all__ = ["Dataset", "TACREDRelationClassificationDataset", "BabelDomainsTopicClassificationDataset","SentimentTopicClassificationDataset"]
