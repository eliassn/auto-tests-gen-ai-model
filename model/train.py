import os
import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel, TextDataset, DataCollatorForLanguageModeling, Trainer, TrainingArguments

DATA_PATH = "./data/raw/cypress_tests.txt" 
MODEL_OUTPUT_DIR = "./model/gpt2-cypress"

def load_dataset(file_path, tokenizer, block_size=128):
    return TextDataset(
        tokenizer=tokenizer,
        file_path=file_path,
        block_size=block_size,
    )

def main():
    # Load tokenizer and model (pretrained GPT-2)
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    model = GPT2LMHeadModel.from_pretrained("gpt2")
    
    # Ensure padding token is defined
    tokenizer.pad_token = tokenizer.eos_token
    model.resize_token_embeddings(len(tokenizer))

    # Prepare dataset and data collator
    dataset = load_dataset(DATA_PATH, tokenizer, block_size=128)
    data_collator = DataCollatorForLanguageModeling(
        tokenizer=tokenizer, mlm=False,
    )

    # Define training arguments
    training_args = TrainingArguments(
        output_dir=MODEL_OUTPUT_DIR,
        overwrite_output_dir=True,
        num_train_epochs=3,
        per_device_train_batch_size=2,
        save_steps=500,
        save_total_limit=2,
        prediction_loss_only=True,
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        data_collator=data_collator,
        train_dataset=dataset,
    )

    # Start training
    trainer.train()
    
    # Save the final model
    trainer.save_model(MODEL_OUTPUT_DIR)
    tokenizer.save_pretrained(MODEL_OUTPUT_DIR)
    print("Training completed and model saved.")

if __name__ == "__main__":
    main()
