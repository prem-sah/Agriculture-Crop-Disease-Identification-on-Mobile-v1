import tensorflow as tf

model = tf.keras.models.load_model(r"/Users/pawansah/Documents/prem_assignment/plant_disease_model.keras")

print("Model loaded successfully")
model.summary()

# Accuracy 
loss, acc = model.evaluate(val_data)
print("Validation Accuracy:", acc)
print("Validation Loss:", loss)