
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TextClassificationPipeline

def load_model():
    model_adi = "poseidon07x/bert-spam-model"
    model = AutoModelForSequenceClassification.from_pretrained(model_adi)
    tokenizer = AutoTokenizer.from_pretrained(model_adi)
    pipeline = TextClassificationPipeline(model=model, tokenizer=tokenizer)
    return pipeline
