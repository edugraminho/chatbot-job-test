from llm import llm
from langchain_core.prompts import ChatPromptTemplate

true_indicators = [
    "verdadeira",
    "é correta",
    "está correta",
    "faz sentido",
    "é válida",
]


false_indicators = [
    "falsa",
    "não é verdadeira",
    "não faz sentido",
    "não é correta",
    "errada",
    "começado a conversa",
    "começou a conversa",
]


def verify_statement(statement):
    verification_prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "Você é um assistente que verifica a veracidade das informações.",
            ),
            ("human", f"A afirmação a seguir é verdadeira ou falsa? {statement}"),
        ]
    )

    formatted_prompt = verification_prompt.format()
    response = llm.invoke(formatted_prompt).content.lower()

    print(f"LLM verifier response: {response}", flush=True)

    if any(indicator in response for indicator in true_indicators):
        return True
    elif any(indicator in response for indicator in false_indicators):
        return False
    else:
        print("It was not possible to determine the veracity.", flush=True)
        return False
