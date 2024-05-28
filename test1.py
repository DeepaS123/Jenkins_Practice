#update value
def update_status(dictionary):
 for key, value in dictionary.items():
     if isinstance(value, dict):
         update_status(value)
     elif isinstance(value, list):
         for item in value:
             if isinstance(item, dict):
                 update_status(item)
     if key == 'status' and value == 'NA':
         dictionary[key] = 'Not processed'

dict1 = {'item1': {'name': 'apple', 'quantity': 100, 'status': 'NA', 'variety': [{'name': 'Green Apple', 'quantity': 10, 'status': 'NA'}, {'name': 'Red Apple', 'quantity': 70, 'status': 'NA'}, {'name': 'yellow Apple', 'quantity': 30, 'status': 'Processed'}]}, 'item2': {'name': 'Mango', 'quantity': 50, 'status': 'NA', 'variety': {'name': 'Parrot Mango', 'quantity': 50, 'status': 'NA'}}, 'item3': {'name': 'Goose Berry', 'quantity': 5, 'status': 'Processed', 'variety': {}}}

update_status(dict1)
print(dict1)