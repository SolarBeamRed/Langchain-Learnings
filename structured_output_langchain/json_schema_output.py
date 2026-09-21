import json

from llm_llamacpp import llm_model

text = '''
The Dodge Challenger SRT Demon 170 feels less like a conventional performance car and more like a machine built to overwhelm you. Its supercharged 6.2-liter HEMI V8 produces up to 1,025 hp on E85, giving it brutal acceleration and a claimed 0–60 mph time of just 1.66 seconds. The experience is dominated by the engine’s enormous power, aggressive exhaust note, and the sheer violence of its launches. It is not particularly subtle, nor is it designed to be a refined corner-carving sports car. Instead, the Demon 170 focuses almost entirely on straight-line performance, and it does that exceptionally well. The specialized drag-racing hardware, weight reduction, and reinforced drivetrain make the car feel purpose-built for the quarter mile. As a final evolution of the Challenger, the Demon 170 is excessive in almost every respect, but that excess is exactly what gives it its character.'''

with open('json_schema.json', 'r') as f:
    json_schema = json.load(f)

structured_model = llm_model.with_structured_output(json_schema)
structured_result = structured_model.invoke(text)

print('Car Model: ', structured_result['car_model'])
print('Car type: ', structured_result['car_type'])
print('Highlights: ', structured_result['highlights'])