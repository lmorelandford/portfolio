#!/usr/bin/env python
# coding: utf-8

# # U.S. Medical Insurance Costs
# 
# In this project a **CSV** file with medical insurance costs will be investigated using Python Fundamentals.  The goal with this project will be to analyze various attributes within **insurance.csv** to learn more about the patient information in the file and gain insight into potential use cases for the dataset.

# In[1]:


# import csv library
import csv


# Before importing the csv library that we are investigating: the **insurance.csv** data, we must creat lists for each type of data in the library. The types of data in this library are:
#  * Patient Age
#  * Patient Sex
#  * Patient BMI
#  * Patient Number of Children
#  * Patient Smoking Status
#  * Patient U.S. Geographical Region
#  * Patient Yearly Medical Insurance Cost

# In[2]:


#create empty lists for each attribute in insurance.csv
ages = []
sexes = []
bmis = []
num_children = []
smoker_statuses = []
regions = []
insurance_charges = []


# Below is a helper function that was created to make loading data into the lists as efficient as possible. Without this function, one would have to open **insurance.csv** and rewrite the for loop seven times; however, with this function, one can simply call `load_list_data()` each time as shown below.

# In[3]:


#helper function to load csv data
def load_list_data(lst, csv_file, column_name):
    with open(csv_file) as csv_info:
        #read the data from the file
        csv_dict = csv.DictReader(csv_info)
        #loop through data in each row of csv
        for row in csv_dict:
            #add data from each row to list
            lst.append(row[column_name])
        return lst


# Now we will call on the helper function to add the data to each of our lists.

# In[5]:


# look at the data in insurance_csv_dict
load_list_data(ages, 'insurance.csv', 'age')
load_list_data(sexes, 'insurance.csv', 'sex')
load_list_data(bmis, 'insurance.csv', 'bmi')
load_list_data(num_children, 'insurance.csv', 'children')
load_list_data(smoker_statuses, 'insurance.csv', 'smoker')
load_list_data(regions, 'insurance.csv', 'region')
load_list_data(insurance_charges, 'insurance.csv', 'charges')


# Now that all the data from **insurance.csv** neatly organized into labeled lists, the analysis can be started. This is where one must plan out what to investigate and how to perform the analysis. There are many aspects of the data that could be looked into. The following operations will be implemented:
# * find average age of the patients
# * find where a majority of the patients are from
# * return the average yearly medical charges of the patients
# * compare average cost differences between smokers and non-smokers
# * creating a dictionary that contains all patient information
# 
# To perform these inspections, a class called `PatientsInfo` has been built out which contains fives methods:
# * `analyze_ages()`
# * `analyze_regions()`
# * `average_charges()`
# * `analyze_smoking_charges()`
# * `create_dictionary()`
# 
# The class has been built out below. 

# In[116]:


class PatientsInfo:
    #method that initializes each parameter category
    def __init__(self, patient_ages, patient_sexes, patient_bmis, patient_num_children, patient_smoker_statuses, patient_regions, patient_insurance_charges):
        self.patient_ages = patient_ages
        self.patient_sexes = patient_sexes
        self.patient_bmis = patient_bmis
        self.patient_num_children = patient_num_children
        self.patient_smoker_statuses = patient_smoker_statuses
        self.patient_regions = patient_regions
        self.patient_insurance_charges = patient_insurance_charges
    
    def analyze_ages(self):
        #finds the average age of patients
        total_age = 0
        for age in self.patient_ages:
            total_age += int(age)
        average_age = round(total_age/len(self.patient_ages), 2)
        print('Average Age of Patients: ' + str(average_age) + ' years.')
    
    
    def analyze_regions(self):
        #finds the most commonly occuring region, and how many patients are from that region
        count = 0
        most_common_region = ''
        for region in self.patient_regions:
            if self.patient_regions.count(region) > count:
                count = self.patient_regions.count(region)
                most_common_region = str(region)
        print('Most Common U.S. Region of Patients: ' + str(most_common_region))
        print('Number of Patients From Region: ' + str(count))
    
    def average_charges(self):
        #returns average insurance charges of patients
        total_charge = 0
        for charge in self.patient_insurance_charges:
            total_charge += float(charge)
        average_charge = round(total_charge/len(self.patient_insurance_charges), 2)
        print('Average Yearly Insurance Charge of Patients: ' + str(average_charge) + (' dollars.'))

    def analyze_smoking_charges(self):
        #finds the daverage charge for smokers and non-smokers and compares the difference.
        total_smoking_charge = 0
        num_smokers = 0
        total_non_smoking_charge = 0
        num_non_smokers = 0
        for i in range(len(self.patient_smoker_statuses)):
            if self.patient_smoker_statuses[i] == 'yes':
                num_smokers += 1
                total_smoking_charge += float(self.patient_insurance_charges[i])
            elif self.patient_smoker_statuses[i] == 'no':
                num_non_smokers += 1
                total_non_smoking_charge += float(self.patient_insurance_charges[i])
        average_smoking_charge = round(total_smoking_charge/num_smokers, 2)
        print('Average Yearly Insurance Charge of Smokers: ' + str(average_smoking_charge) + ' dollars.')
        average_non_smoking_charge = round(total_non_smoking_charge/num_non_smokers, 2)
        print('Average Yearly Insurance Charge of Non-Smokers: ' + str(average_non_smoking_charge) + ' dollars.')
        smoking_charge_difference = average_smoking_charge - average_non_smoking_charge
        print("On average, insurance charges smokers " + str(smoking_charge_difference) + ' dollars more than non-smokers, per year.')
        
    def create_dictionary(self):
        #creates a dictionary of all the patient info following the format of 'parameter of data': list of data.  For example: 'age': list of patient ages
        self.patient_dict = {}
        self.patient_dict["age"] = [int(age) for age in self.patient_ages]
        self.patient_dict["sex"] = self.patient_sexes
        self.patient_dict["bmi"] = self.patient_bmis
        self.patient_dict["number of children"] = self.patient_num_children
        self.patient_dict["smoker status"] = self.patient_smoker_statuses
        self.patient_dict["U.S. region"] = self.patient_regions
        self.patient_dict["insurance charges"] = self.patient_insurance_charges
        return self.patient_dict
        


# First we created an instance in the class `PatientsInfo` called `patient_info` that contains all of the data from our **insurance.csv** library.

# In[117]:


patient_info = PatientsInfo(ages, sexes, bmis, num_children, smoker_statuses, regions, insurance_charges)


# Then we used our `analyze_ages()` method to find the average age of patients from the library.

# In[118]:


patient_info.analyze_ages()


# Then we used our `analyze_regions()` method on our library to identify what U.S. region a majority of patients were from, and how many patients were from that region.

# In[119]:


patient_info.analyze_regions()


# Then we used our `average_charges()` method on our library to find the average yearly insurance charge of patients.

# In[120]:


patient_info.average_charges()


# Then we used our `analyze_smoking_charges()` method on our library to find the average yearly insurance charge of smokers and then average yearly insurance charge of non-smokers, and compared the difference in charges.

# In[121]:


patient_info.analyze_smoking_charges()


# Then using our `create_dictionary()` method, we created a dictionary containing all of the patient information from the library.  In this dictionary, the title of info are the keys, and the list of all of that type of info are the values.

# In[122]:


patient_info.create_dictionary()

