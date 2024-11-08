import os
from weaviate import Client
from verify_statement import verify_statement

weaviate_url = os.getenv("WEAVIATE_URL")

client = Client(weaviate_url)


def setup_weaviate_schema():
    class_names = [cls["class"] for cls in client.schema.get()["classes"]]

    if "VerifiedResponse" not in class_names:
        schema = {
            "class": "VerifiedResponse",
            "description": "Stores inputs and responses verified by the model.",
            "properties": [
                {
                    "name": "user_input",
                    "dataType": ["text"],
                    "description": "Original user input, which was evaluated by the model.",
                },
                {
                    "name": "response",
                    "dataType": ["text"],
                    "description": "Response generated by the chatbot, stored if the statement is true.",
                },
            ],
        }
        client.schema.create_class(schema)
        print("'VerifiedResponse' class successfully created in Weaviate.", flush=True)
    else:
        print("Class 'VerifiedResponse' already exists in Weaviate", flush=True)


def store_response(user_input, response):
    if verify_statement(user_input):

        client.data_object.create(
            {"user_input": user_input, "response": response}, "VerifiedResponse"
        )
        print("Response stored successfully", flush=True)

    else:
        print(
            "The statement is not considered true and will not be stored.",
            flush=True,
        )
