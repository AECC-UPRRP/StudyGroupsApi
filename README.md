# StudyGroupsApi
API for University Study Groups

To create a new study group entry make a POST request to /groups with the following JSON format:

```json
{
    "title": "some_data", 
    "starting_date": "some_data", 
    "end_date": "some_data", 
    "place": "some_data", 
    "course_description": "some_data", 
    "cordinator_name":"some_data", 
    "cordinator_phone": "some_data", 
    "cordinator_email": "some_data", 
    "comments": "some_data"
}
```