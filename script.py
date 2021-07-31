medical_data = \
"""Marina Allison   ,27   ,   31.1 , 
#7010.0   ;Markus Valdez   ,   30, 
22.4,   #4050.0 ;Connie Ballard ,43 
,   25.3 , #12060.0 ;Darnell Weber   
,   35   , 20.6   , #7500.0;
Sylvie Charles   ,22, 22.1 
,#3022.0   ;   Vinay Padilla,24,   
26.9 ,#4620.0 ;Meredith Santiago, 51   , 
29.3 ,#16330.0;   Andre Mccarty, 
19,22.7 , #2900.0 ; 
Lorena Hodson ,65, 33.1 , #19370.0; 
Isaac Vu ,34, 24.8,   #7045.0"""

# Add your code here
# Working with Strings
print("\n" + "\t\t" + "Working with Strings" + "\n")

# Display medical_data
print(medical_data)

# Replace # with $ in medical_data and store the result in updated_medical_data
updated_medical_data = medical_data.replace('#', '$')

# Display updated_medical_data
print("\n" + updated_medical_data)

# Create a variable called num_records and initialize it at 0
num_records = 0

# Iterate through updated_medical_data
for i in range(0, len(updated_medical_data)):
  if updated_medical_data[i] == "$":
    num_records += 1

# Display num_records on a new line
print("\nThere are {} medical records in the data.".format(num_records))

# Split updated_medical_data and store the result in a variable called medical_data_split
medical_data_split = updated_medical_data.split(';')

# Display a new line
print("\n")

# Display medical_data_split
print(medical_data_split)

# Define an empty list called medical_records
medical_records = []

# Iterate through medical_data_split
for record in medical_data_split:
  medical_records.append(record.split(','))

# Display a new line 
print("\n")

# Display medical_records
print(medical_records)

# Cleaning Data
print("\n" + "\t\t" + "Cleaning Data")

# Create an  empty list called medical_records_clean
medical_records_clean = []

# Iterate through medical records
for record in medical_records:
# record_clean to store cleaned medical_records
  record_clean = []
# A nested loop to iterate through record in medical_records
  for item in record:
# Cleaning the whitespace for each record using item.strip()
    record_clean.append(item.strip())
# Append record_clean to medical_records_clean
  medical_records_clean.append(record_clean)

# Display a new line
print("\n")

# Display medical_records_clean
print(medical_records_clean)

# Analyzing Data
print("\n" + "\t\t" + "Analyzing Data")

# Display a new line
print("\n")

# Display the names of each of the ten individuals
for record in medical_records_clean:
  record[0] = record[0].upper()
  print(record[0])


# Create four empty lists
names = []
ages = []
bmis = []
insurance_costs = []

# Iterate through medical_records_clean
for record in medical_records_clean:
  # Append the name to names
  names.append(record[0])
  # Append the age to ages
  ages.append(record[1])
  # Append the BMI to bmis
  bmis.append(record[2])
  # Append the insurance cost to insurance_costs
  insurance_costs.append(record[3])

# Display a new line
print("\n")

# Display names, ages, bmis, and insurance_costs
print("Names: {}".format(names))
print("\nAges: {}".format(ages))
print("\nBMI: {}".format(bmis))
print("\nInsurance Costs: {}".format(insurance_costs))

# Create a variable called total_bmi and set it equal to 0
total_bmi = 0

# Iterate through bmis
for bmi in bmis:
  # Calculate the total bmi values
  total_bmi += float(bmi)

# Create a variable called average_bmi that stores the total_bmi divided by the length of the bmis list and the result is rounded to two decimal places
average_bmi = total_bmi/len(bmis)

# Display average_bmi
print("\nAverage BMI: {:.2f}".format(average_bmi))

# Create an empty list called insurance_costs_strip
insurance_costs_strip = []

# Iterate through the insurance_costs
for cost in insurance_costs:
  # Append each cost to insurance_costs_strip without the $ sign
  insurance_costs_strip.append(cost.strip('$'))

# Display insurance_costs_strip
print("\n {}".format(insurance_costs_strip))

# Create a variable called total_insurance_costs and set it equal to 0
total_insurance_costs = 0

# Iterate through insurance_costs_strip
for cost in insurance_costs_strip:
  # Calculate the total insurance costs
  total_insurance_costs += float(cost)

# Create a variable called average_insurance_cost that stores the total_insurance_costs divided by the length of the insurance_costs_strip list
average_insurance_cost = total_insurance_costs/len(insurance_costs_strip)

# Display average_insurance_cost
print("\nAverage Insurance Cost: ${:.2f}".format(average_insurance_cost))

# Iterate through the range(0, 10) to output a data for each individual
for i in range(0, len(names)):
  print("\n{} is {} years old with a BMI of {} and an insurance cost of {}".format(names[i], ages[i], bmis[i],  insurance_costs[i]))