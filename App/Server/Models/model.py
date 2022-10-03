from pydantic import BaseModel, Field, EmailStr

# [TODO] -> Add any other needed schema here
"""
--
SCHEMAS
--
"""

MOODS = ["angry", "happy", "calm"]

# [TODO] tonal data
class Tone(BaseModel):
    persons_tone: str = Field(default=MOODS[-1])
    text: str = Field(default=None)

    class Config:

        the_schema = {
            "tone_demo" : {
                "mood" : MOODS,
                "text" : "some_text_data",
            }
        }

# allowed data set
dataset_type = ["csv", "json", "pdf", "txt", "xlsx", "docx"]

# [TODO] dataset type
class Source(BaseModel):
    data_source: str = Field(default=MOODS[-1])
    type_of_dataset: str = Field(default=None)
    dataset: str = Field(default=None)

    class Config:

        the_schema = {
            "tone_demo" : {
                "mood" : MOODS[0],
                "type_of_dataset" : dataset_type,
                "text" : "some_text_data",
            }
        }


#  [TODO] -> dataset for model training
class Model_extract_dataset(BaseModel):
    type_of_dataset: str = Field(default=None)
    dataset = Field(default=None) # this will be the data file its self [ URL_LINK ]

    class Config:

        the_schema = {
            "tone_demo" : {
                "type_of_dataset" : "pickle_file",
                "data" : "the_pickle_file",
            }
        }