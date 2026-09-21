from pydantic import BaseModel, Field

from llm_llamacpp import llm_model


text = '''
The Dodge Challenger SRT Demon 170 feels less like a conventional performance car and more like a machine built to overwhelm you. Its supercharged 6.2-liter HEMI V8 produces up to 1,025 hp on E85, giving it brutal acceleration and a claimed 0–60 mph time of just 1.66 seconds. The experience is dominated by the engine’s enormous power, aggressive exhaust note, and the sheer violence of its launches. It is not particularly subtle, nor is it designed to be a refined corner-carving sports car. Instead, the Demon 170 focuses almost entirely on straight-line performance, and it does that exceptionally well. The specialized drag-racing hardware, weight reduction, and reinforced drivetrain make the car feel purpose-built for the quarter mile. As a final evolution of the Challenger, the Demon 170 is excessive in almost every respect, but that excess is exactly what gives it its character.'''


class CarStructuredOutput(BaseModel):
    car_model: str | None = Field(description='Exact car model')
    car_type: str | None = Field(description='Car type, such as Muscle, Sports, Sedan etc')
    highlights: str | None = Field(description='Standout features of the car')


structured_model = llm_model.with_structured_output(
    CarStructuredOutput
)
structured_result = structured_model.invoke(text)

print('Car model: ', structured_result.car_model) # type: ignore
print('Car Type: ', structured_result.car_type) # type: ignore
print("Car highlights: ", structured_result.highlights) # type: ignore