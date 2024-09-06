import pandas as pd
pd.set_option('display.max_columns',None)
#pd.set_option('display.max_rows',None)


#TASK 1: Load the data using Python:using Pandas
print("TASK 1: Load the data using Python:using Pandas")
print("---------------------------------------------------")
# Reading the Csv File
employee_file = pd.read_csv("C:\\Users\\rajsi\\PycharmProjects\\pythonProject\\Employee_data.csv")
# print(employee_file)
# making it as Dataframe
employee_df = pd.DataFrame(employee_file)
employee_df.index=range(1,10001)
print(employee_df)
#------------------------------------------------------------------------------------------------------------------
print("-----------------------------------------------------------------------------------------------------------------------------------------")
print("Cleansing Process/Tansformation Process")
print("-------------------------------------------------")

# After Extraction , Transformation process happens.
# As it is a Machine Generated Data sets We cant find much of Errors in the Data sets.
# Checking Data types is neccessary if we need to load to any of the databases.

employee_df['DOB']=pd.to_datetime(employee_df['DOB'],format="%d/%m/%Y")
print("Data Types:")
print(employee_df.dtypes) # DOB has to be changed to Date time format
print("Sum of Duplicates:",sum(employee_df.duplicated()))
print("Sum of NAN values",employee_df.isna().sum())
#----------------------------------------------------------------------------------------------------------------

print("-----------------------------------------------------------------------------------------------------------------------------------------")


# TASK 2: Filter the top 500 experienced and store it in another variable.
print("TASK 2: Filter the top 500 experienced and store it in another variable.")
print("-------------------------------------------------------------------------------")
sorting_data =employee_df.sort_values(by='Experience',ascending=False).reset_index(drop=True)
print(sorting_data)
experienced_top500_employee =sorting_data.head(500)
experienced_top500_employee.index=range(1,501)
print(experienced_top500_employee)
print("-------------------------------------------------------------------------------------------------------------------------------------------------------------")
#----------------------------------------------------------------------------------------------------------------------------------------

# TASK 3: Then Count their skills and store them in the new column.
print("TASK 3: Then Count their skills and store them in the new column.")
print("-----------------------------------------------------------------------")
experienced_top500_employee['Skill_count'] = experienced_top500_employee['Skills'].apply(lambda x: len(x.split(',')))
print(experienced_top500_employee)
print("---------------------------------------------------------------------------------------------------------------------------------------------------")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Task 4: Then segregate their skill sets in separate columns.
print("Task 4: Then segregate their skill sets in separate columns.")
print("--------------------------------------------------------------------")
# Splitting the Skills column and creating new columns
employee_skills = experienced_top500_employee['Skills'].str.split(',', expand=True)
# print(employee_skills)
employee_skills.columns = [f'Skill_{i+1}' for i in range(len(employee_skills.columns))]
# print(employee_skills)
experienced_top500_employee=pd.concat([experienced_top500_employee,employee_skills],axis=1)
experienced_top500_employee.index=range(1,501)
print(experienced_top500_employee)
print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")
#-----------------------------------------------------------------------------------------------------------------------------------------------------

# Task 5: Finally filter who has having top  50 unique skill set of those 500.

# checking the  50 unique skill which has more presence in 500 experienced employee

print("Task 5: Finally filter who has having top  50 unique skill set of those 500.")
print("--------------------------------------------------------------------------------")

#taking top 50 unique skills into list
top50_unique_skills = experienced_top500_employee['Skills'].str.split(',').explode().value_counts().head(50).index.tolist()

#  top 50 unique skills dataframe
top_50_unique_skills_df = experienced_top500_employee[experienced_top500_employee['Skills'].str.split(',').explode().isin(top50_unique_skills)]

print("Top_50_unique_skills_DataFrame:")
print(top_50_unique_skills_df)
print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")