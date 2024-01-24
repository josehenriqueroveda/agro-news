import pandas as pd
from transformers import BertForSequenceClassification
from transformers import BertTokenizer
from transformers import Trainer
from transformers import TrainingArguments

PRE_TRAINED_MODEL_NAME = "neuralmind/bert-base-portuguese-cased"

model = BertForSequenceClassification.from_pretrained(
    PRE_TRAINED_MODEL_NAME, num_labels=2
)
tokenizer = BertTokenizer.from_pretrained(PRE_TRAINED_MODEL_NAME, do_lower_case=False)


training_args = TrainingArguments(
    output_dir="/ml_models",
    num_train_epochs=3,
    per_device_train_batch_size=4,
    evaluation_strategy="epoch",
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=pd.DataFrame(),  # Substitua pelo conjunto de dados
    eval_dataset=pd.DataFrame(),  # Substitua pelo conjunto de dados
)

trainer.train()

trainer.evaluate()
