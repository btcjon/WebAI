turbo_capabilities = {
    'max_tokens': 4096,
    'cost': 'low',
    'exact_cost': 0.10,
    'internet_ability': False,
    'text_generation': True,
    'text_classification': True,
    'sentiment_analysis': True,
    'translation': True,
    'summarization': True,
}

turbo_16k_capabilities = {
    'max_tokens': 16384,
    'cost': 'medium',
    'exact_cost': 0.40,
    'internet_ability': False,
    'text_generation': True,
    'text_classification': True,
    'sentiment_analysis': True,
    'translation': True,
    'summarization': True,
}

gpt_4_capabilities = {
    'max_tokens': 8192,
    'cost': 'high',
    'exact_cost': 0.20,
    'internet_ability': True,
    'text_generation': True,
    'text_classification': True,
    'sentiment_analysis': True,
    'translation': True,
    'summarization': True,
}

bing_capabilities = {
    'max_tokens': 4096,
    'cost': 'free',
    'exact_cost': 0.00,
    'internet_ability': True,
    'text_generation': True,
    'text_classification': False,
    'sentiment_analysis': False,
    'translation': False,
    'summarization': False,
}

bard_capabilities = {
    'max_tokens': 4096,
    'cost': 'free',
    'exact_cost': 0.00,
    'internet_ability': True,
    'text_generation': True,
    'text_classification': False,
    'sentiment_analysis': False,
    'translation': False,
    'summarization': False,
}
