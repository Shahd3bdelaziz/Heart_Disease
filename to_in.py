


decoders=[
    {1: 'Male', 0: 'Female'},
    {1: 'Typical angina', 2: 'Atypical angina', 3: 'Non-anginal pain', 4: 'Asymptomatic'},
    {1: 'Over 120', 0: 'Under 120'},
    {0: 'Normal', 1: 'ST-T wave abnormality', 2: 'Left ventricular hypertrophy'},
    {1: 'Yes', 0: 'No'},
    {1: 'Up sloping', 2: 'Flat', 3: 'Down sloping'},
    {0: '0', 1: '1', 2: '2', 3: '3'},
    {3: 'Normal', 6: 'Fixed', 7: 'Reversable'}
]
inputs=[]
for i in range(12):
    inputs.append(float(input()))

idx=[1,2,5,6,7,9,10,11]
j=0
encoder = {"Age": 'unk',"Sex": 'unk',"Chest pain type":'unk',"BP":'unk',"Cholesterol": 'unk',"FBS":'unk',"EKG results": 'unk',"Exercise angina": 'unk',"ST depression":'unk',"Slope of ST":'unk',"Number of vessels":'unk',"Thallium":"unk"}
for i in range(len(inputs)):

    if i in idx:
        decoder=decoders[j]
        encoder[list(encoder.keys())[i]]=(decoder[int(inputs[i])])
        j+=1
    else:
        encoder[list(encoder.keys())[i]]=inputs[i]

print(20*"#","After Encode",20*"#")
for k,v in encoder.items():
    print(f"{k} : {v}")

