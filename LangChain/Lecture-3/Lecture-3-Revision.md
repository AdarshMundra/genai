# Lecture 3 Revision

## Overview
This lecture covers **Structured Output** from LLMs. It explores different ways to enforce a specific schema on the model's response using `JSON Schema`, `Pydantic`, and `TypedDict`.

## 1. JSON Schema (`jsonSchema`)

### `with_structured_output_json.py`
- **Method**: Using a raw python dictionary representing a JSON Schema.
- **Key Function**: `model.with_structured_output(json_schema)`
- **Functionality**:
    - Defines a schema with fields like `key_themes`, `summary`, `sentiment`, `pros`, `cons`.
    - Ensures the model returns data strictly matching this JSON structure.

## 2. Pydantic Classes (`pydantic_class`)

### `01_pydantic_demo.py`
- **Description**: Introduction to Pydantic.
- **Functionality**:
    - Defines a `Student` model with type validation (`str`, `int`, `EmailStr`, `float`).
    - Demonstrates data validation and serialization to JSON.

### `02_with_structured_output_pydantic.py`
- **Method**: Using Pydantic classes.
- **Key Function**: `model.with_structured_output(PydanticModel)`
- **Functionality**:
    - Defines a `Review` class inheriting from `BaseModel`.
    - Uses `Field` to provide descriptions for the LLM.
    - The LLM returns an instance of the `Review` class.

## 3. TypedDict (`typedict`)

### `01_typing_dict_demo.py`
- **Description**: Introduction to Python's `TypedDict`.
- **Functionality**: Shows how to define a dictionary with fixed keys and types.

### `02_with_structured_output_typeddict.py`
- **Method**: Using `TypedDict`.
- **Functionality**:
    - Defines a simple schema using `TypedDict`.
    - Gets structured output from the model.

### `03_detailed_with_structured_output_typeddict.py`
- **Method**: `TypedDict` with `Annotated`.
- **Functionality**:
    - Uses `Annotated[Type, "Description"]` to provide context to the LLM about what each field means (similar to `Field` in Pydantic).

## Root Files

### `dont_support_strucutre_output.py`
- **Description**: Testing structured output on models that may have limited support.
- **Functionality**:
    - Uses `HuggingFaceEndpoint` (`TinyLlama`) wrapped in `ChatHuggingFace`.
    - Attempts to use `with_structured_output` with a Pydantic model.
