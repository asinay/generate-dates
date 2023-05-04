# generate-dates
## Generate Dates Utility (not a dating app!)
This utility generates a CSV file containing dates between 1990-01-01 and 2030-12-31, along with some relevant information about each date.

## Usage
To use the utility, simply run the generate_dates.py script. The generated CSV file will be saved in the data subfolder. If the subfolder does not exist, it will be created.

## Generated CSV
The CSV file contains the following columns:

- Day: The date in YYYY-MM-DD format
- Year: The year of the date
- Month: The month of the date as an integer
- MonthName: The name of the month
- Weekday: The day of the week as an integer (0 = Monday, 1 = Tuesday, etc.)
- WeekdayName: The name of the day of the week
- IsWeekend: True if the day is a Saturday or Sunday, False otherwise
- IsHoliday: True if the day is a US federal holiday, False otherwise
- Holiday: The name of the holiday (empty string if not a holiday)

## Dependencies

This utility requires the following Python packages:
• csv
• datetime
• holidays
• os

These packages can be installed using pip:
```bash
pip install csv datetime holidays os
```

## License
This project is licensed under the MIT License - see the LICENSE file for details.

