
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TextClassificationPipeline

def load_model():
    model_adi = "poseidon07x/bert-base-multilingual-cased-spam-mail-detection"
    model = AutoModelForSequenceClassification.from_pretrained(model_adi)
    tokenizer = AutoTokenizer.from_pretrained(model_adi)
    pipeline = TextClassificationPipeline(model=model, tokenizer=tokenizer)
    return pipeline
